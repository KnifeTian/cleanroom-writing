# Cleanroom Writing

将多轮写作讨论整理为一致定稿的 Agent 技能。

已经否定的思路，AI 却总在定稿中重新提起？Cleanroom Writing 依据最新确认的内容起草，并检查旧措辞、废弃方案和内部修改理由是否残留。

可在 Codex 或 Claude Code 中安装，也可将独立提示词用于日常 LLM 对话。

[English](README.md)

## 一个小例子

**讨论记录：** 曾考虑周报和月报，最后决定每月第一个工作日交付月报。目标读者只需要知道交付安排。

**携带讨论历史的写法：** “不再采用周报，而是改为月报，以避免此前的汇报负担。”

**最终写法：** “报告于每月第一个工作日交付。”

这是说明性示例，并非基准测试结果。[完整示例](examples/writing.md)还展示必要比较、未决事项，以及中文讨论后交付英文稿件的情况。

## 工作方式

多轮写作会积累备选方案、审阅意见、旧措辞和修改理由。本技能在讨论过程与最终交付物之间建立明确边界：

1. 恢复当前权威状态，区分已确认内容、已确认修改、排除历史和未决事项。
2. 从只包含当前有效内容的纯净清单起草或修订。
3. 独立检查旧决定残留、通过否定句重新出现的废案、内部理由，以及摘要、表格和图示中的不一致。

否定句和对比句只是检查信号。必要的限制、安全条件、法律边界以及服务目标读者的比较应当保留。

## 选择适合你的使用方式

核心流程由写作指令和审计规则组成，没有调用 Codex 专属工具。可以根据使用环境选择入口：

| 使用环境 | 使用方式 |
| --- | --- |
| Codex | 按[在 Codex 中安装](#在-codex-中安装)操作。 |
| Claude Code | 按[在 Claude Code 中安装](#在-claude-code-中安装)操作，通过 `/cleanroom-writing` 调用。 |
| 支持 `SKILL.md` 的其他 Agent | 按该工具的安装与调用要求使用 `skills/cleanroom-writing/`，具体宿主的兼容性尚未逐一验证。 |
| 支持自定义指令或工作流规则的 Agent | 将 `SKILL.md` 中的指令适配为该工具支持的格式。 |
| 普通 LLM 聊天环境 | 直接复制[独立指南](#无法安装技能时)中的提示词。 |

Codex 和 Claude Code 使用包内同一份 `SKILL.md`，安装目录与调用方式有所不同。`agents/openai.yaml` 提供 Codex 专用的界面和自动选择设置。本项目不声称兼容所有 Agent。

## 在 Codex 中安装

下载或克隆仓库后，在仓库根目录打开终端。只复制技能文件夹。以下命令遇到同名目录会停止复制，更新前请先审阅已安装的版本。

**Windows PowerShell**

```powershell
$skillDestination = Join-Path $HOME '.agents/skills/cleanroom-writing'
if (Test-Path -LiteralPath $skillDestination) { throw 'Skill already exists; review it before replacing.' }
New-Item -ItemType Directory -Force -Path (Split-Path $skillDestination) | Out-Null
Copy-Item -LiteralPath './skills/cleanroom-writing' -Destination $skillDestination -Recurse
```

**macOS / Linux shell**

```sh
skill_destination="$HOME/.agents/skills/cleanroom-writing"
if [ -e "$skill_destination" ]; then
  printf '%s\n' 'Skill already exists; review it before replacing.'
else
  mkdir -p "$HOME/.agents/skills" && cp -R ./skills/cleanroom-writing "$skill_destination"
fi
```

仅供单个项目使用时，复制到 `<项目>/.agents/skills/cleanroom-writing`。这些位置依据[官方本地技能文档](https://learn.chatgpt.com/docs/build-skills)。请避免在当前生效的多个范围中安装同名副本。

本项目目前通过复制技能文件夹安装，可按本文说明用于 Codex 和 Claude Code。根目录的 `plugin.json` 为后续插件形式分发预留，普通安装无需使用。

## 在 Claude Code 中安装

Claude Code 支持 `SKILL.md` 技能格式。个人使用时，将同一个 `skills/cleanroom-writing` 文件夹复制到 `~/.claude/skills/cleanroom-writing`；仅供单个项目使用时，放到 `<项目>/.claude/skills/cleanroom-writing`。无需另外编写技能正文。目录及 `/技能名` 调用方式依据 [Claude Code 官方技能文档](https://code.claude.com/docs/en/skills)。

在本仓库根目录打开终端，按操作系统选择以下命令完成个人安装。已有同名技能时不会覆盖。

**Windows PowerShell**

```powershell
$skillDestination = Join-Path $HOME '.claude/skills/cleanroom-writing'
if (Test-Path -LiteralPath $skillDestination) { throw 'Skill already exists; review it before replacing.' }
New-Item -ItemType Directory -Force -Path (Split-Path $skillDestination) | Out-Null
Copy-Item -LiteralPath './skills/cleanroom-writing' -Destination $skillDestination -Recurse
```

**macOS / Linux shell**

```sh
skill_destination="$HOME/.claude/skills/cleanroom-writing"
if [ -e "$skill_destination" ]; then
  printf '%s\n' 'Skill already exists; review it before replacing.'
else
  mkdir -p "$HOME/.claude/skills" && cp -R ./skills/cleanroom-writing "$skill_destination"
fi
```

这是直接复制技能目录的安装方式，不依赖根目录的 `plugin.json` 或 `agents/openai.yaml`。Claude Code 默认依据技能描述自动选择；Codex 的 `allow_implicit_invocation` 设置不控制 Claude Code。本包尚未在实际 Claude Code 会话中验证安装与写作效果。

## 使用

**Codex**

```text
请用 $cleanroom-writing 根据已经确认的修改统一修订正文、摘要和表格，交付中文定稿。
```

```text
Use $cleanroom-writing to draft the final report from our approved decisions.
Keep the summary, body, and tables consistent with the latest decisions.
```

**Claude Code**

```text
/cleanroom-writing 根据已经确认的修改统一修订正文、摘要和表格，交付中文定稿。
```

```text
/cleanroom-writing Draft the final report from our approved decisions. Keep the summary, body, and tables consistent.
```

Codex 配置保留 `allow_implicit_invocation: true`，允许根据描述自动选择技能，范围是多轮讨论后的最终起草或修订。实际选择取决于宿主与模型；需要明确调用时可使用对应工具的调用方式。

技能指令使用英文。交付语言优先遵循用户要求；没有指定时，修订保留原稿语言，新写采用请求语言。

## 适用范围

- 多轮讨论后生成正式文稿。
- 根据已确认的修改计划统一修订文件。
- 整合作者意见、审阅意见与旧稿。
- 清理反复修改后的概念残留。

头脑风暴、决策记录、评审回复和明确要求的方案比较可以合理保留决策历史。本技能的纯净成稿边界只用于需要它的最终交付物。影响结果的未决事项需要先澄清。

## 无法安装技能时

可把独立指南中的提示词发送给通常使用的 LLM：

| 用途 | 简体中文 | English |
| --- | --- | --- |
| 理解背景与设计 | [开发背景与应用说明](docs/zh-CN/cleanroom-writing技能开发背景与应用说明.md) | [Background](docs/en/background.md) |
| 写作前预防 | [写作开始前约定与检查](docs/zh-CN/LLM写作开始前约定与检查.md) | [Before writing](docs/en/before-writing.md) |
| 现有文稿诊断与修复 | [文稿废案回流检查与修复](docs/zh-CN/LLM文稿废案回流检查与修复.md) | [Inspect and repair](docs/en/inspect-and-repair.md) |

修复指南中的提示词明确采用“先检查、确认后修改”的审阅模式。它不构成每次使用技能都必须增加的审批步骤。

## 能力边界

写作部分只有指令和文档，无运行依赖。技能无法恢复上下文中没有提供的决定，也不能保证发现所有回流问题。它不验证已确认主张的事实正确性。其他 Agent 可能可以采用这些指令，其发现机制和界面元数据支持需要另外验证。本包不声称经过跨模型可靠性测量。

## 目录与维护

```text
plugin.json                         便携插件元数据
skills/cleanroom-writing/            可安装技能与 Codex 界面配置
docs/en/                            英文背景与独立指南
docs/zh-CN/                         中文背景与独立指南
examples/writing.md                 双语说明性示例
tests/activation-cases.md           人工选择与行为检查案例
scripts/validate_package.py         无第三方依赖的包检查
.github/workflows/validate.yml      CI 包检查
```

Python 3.9 或更新版本可运行 `python scripts/validate_package.py`，检查目录、最小元数据格式与本地 Markdown 链接。[人工检查案例](tests/activation-cases.md)记录触发边界与预期行为，尚未作为独立模型评估执行。

贡献方式见 [CONTRIBUTING.md](CONTRIBUTING.md)。报告问题时请使用合成示例，删除私人文稿材料。

## 作者与许可证

作者：[KnifeTian](https://github.com/KnifeTian)。本项目采用 [MIT 许可证](LICENSE)。
