<div align="center">
  <h1 align="center">
    <img src="icons/icon.png" width="200" alt="Monster logo"/>
    <br/>
    Monster
  </h1>

  <p>
    一个基于图像识别的鸣潮自动化程序，支持后台运行，基于 <a href="https://ok-script.com">Mon-script</a> 开发。
    <br />
    An image-recognition-based automation tool for Wuthering Waves, with background mode support, developed with <a href="https://ok-script.com">Mon-script</a>.
  </p>

  <p><i>通过 Windows 接口模拟用户进行操作，无内存读取、无文件修改</i></p>
</div>

<!-- Badges -->
<div align="center">

![平台](https://img.shields.io/badge/platform-Windows-blue)
[![Discord](https://img.shields.io/discord/296598043787132928?color=5865f2&label=%20Discord)](https://discord.gg/vVyCatEBgA)

</div>

<p align="center"><strong>官方网站：</strong> <a href="https://ok-script.com/ok-ww">https://ok-script.com/ok-ww</a></p>

### [English](docs/en/index.md) | 中文说明 | [繁體中文](docs/zh-TW/index.md) | [日本語](docs/ja/index.md)

**演示与教程:** [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://youtu.be/h6P1KWjdnB4)

---

## ⚠️ 免责声明

本软件为外部辅助工具，旨在自动化《鸣潮》的部分游戏流程。它完全通过模拟常规用户界面与游戏交互，遵循相关法律法规。本项目旨在简化用户的重复性操作，不会破坏游戏平衡或提供不公平优势，也绝不会修改任何游戏文件或数据。

本软件开源、免费，仅供个人学习与交流使用，请勿用于任何商业或营利性目的。开发者团队拥有本项目的最终解释权。因使用本软件而产生的任何问题，均与本项目及开发者无关。

请注意，根据库洛官方的《鸣潮》公平运营声明：
> 严禁利用任何第三方工具破坏游戏体验。
> 我们将严厉打击使用外挂、加速器、作弊软件、宏脚本等违规工具的行为，这些行为包括但不限于自动挂机、技能加速、无敌模式、瞬移、修改游戏数据等操作。
> 一经查证，我们将视违规情况和次数，采取包括但不限于扣除违规收益、冻结或永久封禁游戏账号等措施。

**使用本软件即表示您已阅读、理解并同意以上声明，并自愿承担一切潜在风险。**

## ✨ 主要功能
<img width="1774" height="1182" alt="QQ_1762960844719" src="https://github.com/user-attachments/assets/c5eb0145-0d45-44f9-85b3-184de0ef20bf" />

*   **高分辨率支持**: 流畅运行于 4K 及以下所有 16:9 分辨率（最低 1280x720）。部分功能兼容 21:9 等超宽屏。
*   **后台模式**: 支持游戏窗口最小化或被遮挡时在后台运行，不影响您使用电脑。
*   **智能识别**: 全角色自动识别，无需手动配置技能序列，一键启动。
*   **自动静音**: 在后台运行时，可自动将游戏静音。

## 🔧 疑难解答 (Troubleshooting)

如果遇到问题，请在提问前按以下步骤逐一排查：

1.  **杀毒软件**：将软件的安装目录添加到您的杀毒软件（包括 Windows Defender）的**信任区或白名单**中，以防文件被误删或拦截。
2.  **显示设置**：
    *   一般可以开启游戏内滤镜。
    *   可以开启 Windows HDR，但必须关闭 Auto HDR（自动 HDR）。
    *   建议关闭显卡滤镜，例如 RTX HDR、RTX 动态亮丽（RTX Dynamic Vibrance）、AMD 锐化等。
    *   使用游戏默认的亮度设置。
    *   关闭任何在游戏画面上显示信息的叠加层（如 MSI Afterburner、Fraps 等显示的帧率）。
3.  **自定义按键**：如果您修改了游戏内的默认按键，请务必在 `ok-ww` 的设置中进行同步配置。仅支持设置中列出的按键。
4.  **软件版本**：检查并确保您使用的是最新版本的 `ok-ww`。
5.  **游戏性能**：请确保游戏能稳定在 **60 FPS** 运行。如果帧率不稳定，请尝试降低游戏画质或分辨率。
6.  **游戏断线**：在 `ok-ww` 设置中开启“启动后关闭启动器”，确保启动器进程未在运行；或者使用源码运行。
7.  **OpenVINO 报错**：如果遇到 `0x000005` 报错，并且使用的是带 NPU 的 Intel CPU，请更新至 Intel 最新的 NPU 驱动。
8.  **寻求帮助**：如果以上步骤都无法解决您的问题，请通过 Discord 提交详细的错误报告。
9.  **关闭自动奔跑**：游戏设置里关闭自动奔跑。
10. **为所有角色装备主声骸**：队伍中的每个角色都必须装备主声骸（画面右下角应显示声骸技能图标）。任何一个角色未装备主声骸时，自动战斗将无法正常运行，并可能反复锁定敌人而不攻击。

---

## 📦 发行包与更新（Monster Portable Release）

本 fork 的发行包由手动触发的 `Monster Portable Release` 工作流构建，只产出**便携压缩包**：没有安装程序，也没有在线安装包。GitHub Actions → 该工作流 → Run workflow 即可触发。

解压后目录结构：

```
Monster/
├── Monster.exe                    # 启动器
├── Monster.cmd                    # 命令行 / 离线启动入口
└── data/apps/Monster/
    ├── python/                    # 内置 Python 3.12 与全部依赖
    ├── app.json                   # 版本、profile、更新源
    ├── repo/                      # 精简过的 git 仓库（只保留版本 tag）
    └── working/                   # 程序源码；configs/、logs/ 由程序自己创建
```

### 两种启动器模式

触发工作流时可通过 `launcher` 选择：

| 模式 | `Monster.exe` | 更新方式 | 配置 |
| --- | --- | --- | --- |
| `updater`（默认） | PyAppify 官方启动器，也就是原项目那个「启动 + 更新」程序 | 启动时从更新源 fetch 新版本 tag 的**差异对象**，只下载变化的源码 | 保留 |
| `cmd-only` | 带图标和管理员权限清单的轻量包装器，只调用 `Monster.cmd` | 无更新 / 无联网逻辑 | 需手动迁移 |

`updater` 模式解决了旧便携包的两个问题：

1. **不用再重下 2 GiB**：Python 环境、pip 依赖、`ok_templates/` 模板等都不在更新源仓库里，更新时启动器只把新 tag 中变化的文件 checkout 到 `data/apps/Monster/working`，并复用已有的 `data/apps/Monster/python/`。首次解压仍然需要完整包，之后每次更新通常只有几 MB 到几十 MB。
2. **配置不再失效**：`configs/`、`logs/` 等由程序运行时生成且被 `.gitignore` 排除，`checkout` 只覆盖受版本控制的文件，不会删除用户数据。恢复的队伍配置页（`src/gui/CharacterCodeTab.py`）也已纳入版本控制，更新后依然可用。

> `Monster.cmd` 设置了 `PYAPPIFY_UPGRADEABLE=0`，适合带命令行参数启动或完全离线使用；它不会触发更新。要更新请双击 `Monster.exe`。
>
> `updater` 模式的启动器界面依赖系统 WebView2 Runtime（Windows 11 与多数已更新的 Windows 10 自带）。若双击 `Monster.exe` 无界面，安装微软的 [WebView2 Runtime](https://developer.microsoft.com/microsoft-edge/webview2/) 常青版即可；`Monster.cmd` 不依赖它。

### 更新源指向自己发布的版本

更新源由 `pyappify.yml` 的 `profiles[].git_url` 决定，当前指向**本 fork 自己发布的仓库**：

```yaml
git_url: "https://github.com/3055909481/ok-wuthering-waves.git"
```

工作流每次运行都会在这个仓库上创建并推送一个新的版本 tag，启动器检查更新时拉取的正是这些自己发布的 tag，不会再去原作者的更新仓库。想换成另一个由你发布的仓库，把上面这行改成那个仓库地址并提交即可；该仓库需要有同名的版本 tag，且其中的 `pyappify.yml` 也要把 `git_url` 指回自己（工作流也提供 `update_repo` 输入用于构建时临时覆盖，但必须配合手动指定的 `version` 使用）。

> 压缩包约 2.2 GiB，超过 GitHub 单个 Release 资产 2 GiB 上限，因此 Release 里是 `.7z.001` / `.7z.002` 分卷：下载全部放到同一目录，用 7-Zip 打开第一个即可解压。完整单文件包也可在对应 Actions 运行的 artifact 中下载。

---

## 🔗 依赖：Mon-script（ok-script 的 fork）

本项目不再使用 PyPI 上的官方 `ok-script`，改为自建 fork **[Mon-script](https://github.com/3055909481/Mon-script)**，以隔离命名空间、避免与官方包冲突：

| 项目 | 值 |
| --- | --- |
| 分发名 | `Mon-script` |
| Python 顶层模块 | `Mon`（源码中 `from ok import ...` 已全部改为 `from Mon import ...`） |
| 安装来源 | `Mon-script[ocr,qt] @ https://github.com/3055909481/Mon-script/archive/refs/tags/v3.0.5b7-mon1.tar.gz` |
| 上游 | [ok-oldking/ok-script](https://github.com/ok-oldking/ok-script)，版本基线 `v3.0.5b7` |

修改依赖时需同时更新 `pyproject.toml` 和 `requirements.txt`（后者是锁文件，PyAppify 打包时用 `--no-deps` 按它安装）。升级方法：在 Mon-script 仓库提交改动并打新 tag，再把这两个文件里的 tag 换成新值；fork 未发布到 PyPI，所以必须保留 tag 归档 URL 的形式。

> **为什么不用 `git+https://...@tag`**：PyAppify v1.2.7 的 `clear_python_envs()` 会把 pip 子进程的 `PATH` 重置为仅 `C:\Windows\System32` 等系统目录，其中没有 `git.exe`。实测 git URL 在打包阶段报 `ERROR: Cannot find command 'git'` 并导致 setup 失败；GitHub 的 tag 归档包只需 HTTPS 下载，无需 git，且仍精确锁定同一个 tag。

> **刻意保留的旧名**：gettext 翻译域仍是 `ok`（`i18n/*/LC_MESSAGES/ok.po` / `ok.mo`）、运行时对象属性仍是 `og.ok`、issue 日志解析脚本仍认 `logs/ok-script.log`。这些不是 Python 模块名，改动会破坏现有翻译文件和上游日志附件的解析。
>
> 依据原项目 [LICENSE.txt](LICENSE.txt) 第 4 条，衍生版本必须保留对 **ok-script** 的提及与链接；本项目同时保留上游官网 `https://ok-script.com` 的链接作为致谢。

---

## 💻 开发者专区

### 从源码运行

开发环境、源码运行和贡献说明请参阅[贡献指南](docs/development/contributing.md)。

### AI 技能

在支持项目技能的编码代理中打开本仓库，即可通过技能名称或自然语言提出相关请求。有关具体用法、准备工作和执行流程，请询问编码代理；技能的详细说明也可通过下面的链接查看。

使用队伍评估或改进技能前，请先选好队伍，并进入游戏中的「深境再临」或「终焉矩阵」。

| 技能 | 简介 |
| --- | --- |
| [evaluate-team](.agents/skills/evaluate-team/SKILL.md) | 通过多次战斗评估当前队伍的自动战斗循环并提出建议。 |
| [improve-team](.agents/skills/improve-team/SKILL.md) | 根据队伍评估结果提出并验证角色自动战斗改进。 |
| [ok-script-develop](.agents/skills/ok-script-develop/SKILL.md) | 使用 Mon-script 开发和验证游戏自动化功能。 |
| [ok-script-tasks](.agents/skills/ok-script-tasks/SKILL.md) | 创建、修改或审查自动化任务。 |
| [ok-ww-characters](.agents/skills/ok-ww-characters/SKILL.md) | 开发、审查和测试角色自动战斗逻辑。 |
| [ok-script-i18n](.agents/skills/ok-script-i18n/SKILL.md) | 添加、同步和编译任务界面翻译。 |
| [pr-review](.agents/skills/pr-review/SKILL.md) | 审查或合并本项目的 GitHub PR。 |
| [deploy](.agents/skills/deploy/SKILL.md) | 提交已完成的修改，创建版本标签并发布。 |
| [use-local-venv](.agents/skills/use-local-venv/SKILL.md) | 运行 Python 命令时优先使用仓库的本地虚拟环境。 |

### 命令行参数

您可以通过命令行参数实现自动化启动。

```powershell
# 示例：启动后自动执行第一个任务（一条龙），并在任务完成后退出程序
.\.venv\Scripts\python.exe main.py -t 1 -e
```

*   `-t` 或 `--task`: 启动后自动执行第 N 个任务。`1` 代表任务列表中的第一个。
*   `-e` 或 `--exit`: 任务执行完毕后自动退出程序。

## 💬 加入我们

*   **Discord**: [点击加入](https://discord.gg/vVyCatEBgA)

本项目基于 [Mon-script](https://ok-script.com) 框架开发，简单易维护。欢迎有兴趣的开发者使用 [Mon-script](https://ok-script.com) 开发您自己的自动化项目。

## ❤️ 赞助与致谢

### 赞助商 (Sponsors)
*   **EXE 签名**: Free code signing provided by [SignPath.io](https://signpath.io/), certificate by [SignPath Foundation](https://signpath.org/).

### 致谢
*   [lazydog28/mc_auto_boss](https://github.com/lazydog28/mc_auto_boss)
*   [ok-oldking/OnnxOCR](https://github.com/ok-oldking/OnnxOCR)
*   [zhiyiYo/PyQt-Fluent-Widgets](https://github.com/zhiyiYo/PyQt-Fluent-Widgets)
*   [Toufool/AutoSplit](https://github.com/Toufool/AutoSplit)
