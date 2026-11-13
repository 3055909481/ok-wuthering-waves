// Thin Win32 launcher for the Monster portable package.
//
// It intentionally contains NO update, git, profile or Python-environment
// logic. All of that belongs to PyAppify's generated Monster.cmd, which this
// exe simply invokes with a hidden console. The exe exists only to give the
// portable build an icon, a taskbar identity and a UAC manifest; it never
// contacts the network and needs no runtime beyond the .NET Framework 4.x
// that ships with Windows.
//
// Built by portable-release.yml with:
//   csc.exe /nologo /target:winexe /optimize+ /out:Monster.exe
//           /win32icon:icons/launcher.ico
//           /win32manifest:.github/scripts/MonsterLauncher.manifest.xml
//           .github/scripts/MonsterLauncher.cs

using System;
using System.Diagnostics;
using System.IO;
using System.Reflection;
using System.Runtime.InteropServices;

[assembly: AssemblyTitle("Monster")]
[assembly: AssemblyDescription("Monster portable launcher")]
[assembly: AssemblyCompany("Monster")]
[assembly: AssemblyProduct("Monster")]
[assembly: AssemblyVersion("1.0.0.0")]
[assembly: AssemblyFileVersion("1.0.0.0")]

internal static class MonsterLauncher
{
    [DllImport("user32.dll", CharSet = CharSet.Unicode)]
    private static extern int MessageBoxW(IntPtr owner, string text, string caption, uint flags);

    [STAThread]
    private static int Main(string[] args)
    {
        string folder = AppDomain.CurrentDomain.BaseDirectory;
        string entry = Path.Combine(folder, "Monster.cmd");

        if (!File.Exists(entry))
        {
            ShowError("Monster.cmd was not found next to Monster.exe." + Environment.NewLine + folder);
            return 1;
        }

        // cmd.exe /d /c ""<entry>" <args>" : cmd strips the outer quotes,
        // leaving a correctly quoted path plus the forwarded arguments.
        string command = "\"" + entry + "\"";
        foreach (string arg in args)
        {
            command += " \"" + arg.Replace("\"", "") + "\"";
        }

        ProcessStartInfo start = new ProcessStartInfo();
        start.FileName = Environment.GetEnvironmentVariable("ComSpec");
        if (string.IsNullOrEmpty(start.FileName))
        {
            start.FileName = "cmd.exe";
        }
        start.Arguments = "/d /c \"" + command + "\"";
        start.WorkingDirectory = folder;
        start.UseShellExecute = false;
        start.CreateNoWindow = true;   // no console flash; Monster.cmd detaches pythonw.exe
        start.WindowStyle = ProcessWindowStyle.Hidden;

        try
        {
            Process child = Process.Start(start);
            if (child != null)
            {
                child.Dispose();
            }
            return 0;
        }
        catch (Exception error)
        {
            ShowError("Failed to start Monster.cmd:" + Environment.NewLine + error.Message);
            return 1;
        }
    }

    private static void ShowError(string message)
    {
        // MB_ICONERROR; avoids a System.Windows.Forms reference so the build
        // only needs the framework assemblies csc references by default.
        MessageBoxW(IntPtr.Zero, message, "Monster", 0x00000010u);
    }
}
