"""Make PyAppify's updater launcher request administrator rights.

PyAppify v1.2.7 builds its Tauri launcher with UAC disabled
(src-tauri/build.rs: "const UAC: bool = false"). Its embedded manifest only
declares the Common-Controls dependency, i.e. asInvoker. Double-clicking that
Monster.exe runs the launcher AND the pythonw.exe it spawns at MEDIUM integrity,
while Wuthering Waves runs at HIGH integrity (anti-cheat). Windows UIPI then
blocks win32gui.PostMessage with Win32 error 5 "Access is denied":

    PostMessage error <hwnd>: (5, 'PostMessage', 'Access is denied.')

Monster.cmd self-elevates via fltmc + RunAs, which is why cmd-only packages
never hit this. This script replaces the RT_MANIFEST / ID 1 / lang 1033 resource
in-place with the Win32 resource-update APIs (no compiler needed) and verifies
the result by parsing the PE resource directory.
"""

import ctypes
import struct
import sys
from ctypes import wintypes
from pathlib import Path

RT_MANIFEST = 24
CREATEPROCESS_MANIFEST_RESOURCE_ID = 1
LANG_EN_US = 1033

_kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
_kernel32.BeginUpdateResourceW.argtypes = [wintypes.LPCWSTR, wintypes.BOOL]
_kernel32.BeginUpdateResourceW.restype = wintypes.HANDLE
_kernel32.UpdateResourceW.argtypes = [
    wintypes.HANDLE, ctypes.c_void_p, ctypes.c_void_p,
    wintypes.WORD, ctypes.c_void_p, wintypes.DWORD,
]
_kernel32.UpdateResourceW.restype = wintypes.BOOL
_kernel32.EndUpdateResourceW.argtypes = [wintypes.HANDLE, wintypes.BOOL]
_kernel32.EndUpdateResourceW.restype = wintypes.BOOL


def apply_manifest(exe: Path, data: bytes) -> None:
    handle = _kernel32.BeginUpdateResourceW(str(exe), False)
    if not handle:
        raise ctypes.WinError(ctypes.get_last_error())

    buffer = (ctypes.c_ubyte * len(data)).from_buffer_copy(data)
    ok = _kernel32.UpdateResourceW(
        handle,
        ctypes.c_void_p(RT_MANIFEST),
        ctypes.c_void_p(CREATEPROCESS_MANIFEST_RESOURCE_ID),
        LANG_EN_US,
        buffer,
        len(data),
    )
    if not ok:
        error = ctypes.get_last_error()
        _kernel32.EndUpdateResourceW(handle, True)
        raise ctypes.WinError(error)
    if not _kernel32.EndUpdateResourceW(handle, False):
        raise ctypes.WinError(ctypes.get_last_error())


def read_embedded_manifests(path: Path):
    """Minimal PE resource parser, used only to verify the patch landed."""
    blob = path.read_bytes()
    pe = struct.unpack_from("<I", blob, 0x3C)[0] + 4
    section_count = struct.unpack_from("<H", blob, pe + 2)[0]
    optional_size = struct.unpack_from("<H", blob, pe + 16)[0]
    optional = pe + 20
    magic = struct.unpack_from("<H", blob, optional)[0]
    directories = optional + (112 if magic == 0x20B else 96)
    rsrc_rva, _ = struct.unpack_from("<II", blob, directories + 16)

    sections = []
    for i in range(section_count):
        offset = optional + optional_size + i * 40
        virtual_size, virtual_addr, raw_size, raw_ptr = struct.unpack_from(
            "<IIII", blob, offset + 8
        )
        sections.append((virtual_addr, max(virtual_size, raw_size), raw_ptr))

    def rva_to_offset(rva):
        for virtual_addr, span, raw_ptr in sections:
            if virtual_addr <= rva < virtual_addr + span:
                return raw_ptr + (rva - virtual_addr)
        return None

    base = rva_to_offset(rsrc_rva)
    if base is None:
        return []

    def entries(offset):
        named, by_id = struct.unpack_from("<HH", blob, offset + 12)
        return [
            struct.unpack_from("<II", blob, offset + 16 + i * 8)
            for i in range(named + by_id)
        ]

    found = []
    for name, directory in entries(base):
        if name != RT_MANIFEST or not (directory & 0x80000000):
            continue
        for resource_id, level3 in entries(base + (directory & 0x7FFFFFFF)):
            if not (level3 & 0x80000000):
                continue
            for language, data_entry in entries(base + (level3 & 0x7FFFFFFF)):
                entry = base + (data_entry & 0x7FFFFFFF)
                data_rva, size, _, _ = struct.unpack_from("<IIII", blob, entry)
                start = rva_to_offset(data_rva)
                if start is None:
                    continue
                found.append((resource_id, language, blob[start:start + size]))
    return found


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: patch_launcher_manifest.py <exe> <manifest.xml>", file=sys.stderr)
        return 2

    exe = Path(sys.argv[1]).resolve()
    manifest_path = Path(sys.argv[2]).resolve()
    if not exe.is_file():
        print(f"ERROR: executable not found: {exe}", file=sys.stderr)
        return 1
    if not manifest_path.is_file():
        print(f"ERROR: manifest not found: {manifest_path}", file=sys.stderr)
        return 1

    data = manifest_path.read_bytes()
    if data.startswith(b"\xef\xbb\xbf"):
        data = data[3:]
    if b'level="requireAdministrator"' not in data:
        print("ERROR: manifest does not declare requireAdministrator", file=sys.stderr)
        return 1

    apply_manifest(exe, data)

    patched = [
        raw for resource_id, language, raw in read_embedded_manifests(exe)
        if resource_id == CREATEPROCESS_MANIFEST_RESOURCE_ID and language == LANG_EN_US
    ]
    if not patched or b'level="requireAdministrator"' not in patched[0]:
        print("ERROR: verification failed - patched manifest not found in PE resources",
              file=sys.stderr)
        return 1

    print(f"requireAdministrator manifest applied and verified ({len(data)} bytes).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
