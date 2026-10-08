# Cleanroom Writing

An agent skill for turning multi-round writing discussions into consistent final drafts.

Already rejected an idea, but your AI keeps bringing it back? Cleanroom Writing drafts from the latest approved content and checks for outdated wording, discarded alternatives, and internal revision explanations.

Use the skill with Codex or Claude Code, or copy the standalone prompts into your usual LLM chat.

多轮 AI 写作定稿与审计，防止废案回流。可用于 Codex 和 Claude Code，并提供其他 LLM 可直接使用的独立提示词。

[简体中文](README.zh-CN.md)

## A small example

**Discussion:** We considered weekly and monthly reports. The final decision is monthly reports, delivered on the first business day. The audience only needs the reporting schedule.

**History leaking into the draft:** “Instead of weekly reports, we now provide monthly reports to avoid the previous reporting burden.”

**Clean final wording:** “Reports are delivered monthly on the first business day.”

This is an illustrative example, not a benchmark result. See [worked examples](examples/writing.md) for necessary comparisons, unresolved decisions, and Chinese discussion with English output.

## What it does

Long writing conversations accumulate alternatives, reviewer comments, superseded wording, and reasons for changing course. Cleanroom Writing establishes an explicit boundary between that discussion and the final deliverable:

1. Recover the current authoritative state: approved content, approved changes, excluded history, and unresolved matters.
2. Draft or revise from a clean brief containing the current effective content.
3. Audit for superseded decisions, rejected concepts reintroduced through denials, internal rationale, and inconsistencies across summaries, tables, and figures.

Negative or comparative language is a review signal. Necessary limitations, safety conditions, legal boundaries, and audience-relevant comparisons remain part of the deliverable.

## Use with your agent

The core workflow consists of writing instructions and audit rules, with no Codex-specific tool calls. Choose an entry point for your environment:

| Environment | How to use |
| --- | --- |
| Codex | Follow [Install in Codex](#install-in-codex). |
| Claude Code | Follow [Install in Claude Code](#install-in-claude-code); invoke with `/cleanroom-writing`. |
| Another agent that supports `SKILL.md` | Use `skills/cleanroom-writing/` according to that agent's installation and invocation conventions. Compatibility has not been verified for individual hosts. |
| An agent with custom instructions or workflow rules | Adapt the instructions in `SKILL.md` to its supported format. |
| An ordinary LLM chat | Copy the prompts from the [standalone guides](#use-without-custom-skills). |

Codex and Claude Code use the same `SKILL.md` in this package, with different installation paths and invocation syntax. `agents/openai.yaml` supplies Codex-specific UI and selection settings. This package does not claim universal agent compatibility.

## Install in Codex

Download or clone this repository, then open a terminal in its root. Copy **the skill folder**, rather than the whole repository, into your personal skill directory. The commands stop if a folder with that name already exists; review the installed version before replacing it.

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

For a project-specific installation, copy the same folder to `<project>/.agents/skills/cleanroom-writing`. These locations follow the [official local skill documentation](https://learn.chatgpt.com/docs/build-skills). Avoid installing duplicate copies with the same skill name across your active scopes.

Install this project by copying the skill folder, following the instructions here for Codex or Claude Code. The root `plugin.json` is reserved for future plugin distribution and is not needed for this installation method.

## Install in Claude Code

Claude Code supports `SKILL.md` skills. Copy the same `skills/cleanroom-writing` folder to `~/.claude/skills/cleanroom-writing` for personal use, or `<project>/.claude/skills/cleanroom-writing` for one project. No separate skill body is needed. These paths and the `/skill-name` invocation follow the [Claude Code skill documentation](https://code.claude.com/docs/en/skills).

From this repository's root, use one of the following commands for a personal installation. Existing installations are preserved.

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

This is a direct skill-folder installation. The root `plugin.json` and `agents/openai.yaml` are not required for it. Claude Code uses the skill description for automatic selection by default; the Codex `allow_implicit_invocation` setting does not configure Claude Code. Installation and writing behavior have not been tested in a live Claude Code session.

## Use it

**Codex**

```text
Use $cleanroom-writing to draft the final report from our approved decisions.
Keep the summary, body, and tables consistent with the latest decisions.
```

```text
请用 $cleanroom-writing 根据已经确认的修改统一修订正文、摘要和表格，交付中文定稿。
```

**Claude Code**

```text
/cleanroom-writing Draft the final report from our approved decisions. Keep the summary, body, and tables consistent.
```

```text
/cleanroom-writing 根据已经确认的修改统一修订正文、摘要和表格，交付中文定稿。
```

For Codex, automatic selection remains enabled through `allow_implicit_invocation: true`. The skill description targets final drafting or revision after iterative discussion. Selection depends on the host and model; explicit invocation is useful when you want to request the workflow directly.

The instructions are English. Output follows the user's requested language; otherwise revisions preserve the source language and new drafts follow the request language.

## When to use it

- Final drafting after multiple alternatives or revisions.
- Applying an approved modification plan across a document.
- Consolidating author comments, reviewer feedback, and older drafts.
- Cleaning residual concepts from a repeatedly edited artifact.

Brainstorming, decision logs, review responses, and requested comparisons can legitimately include decision history. This skill's clean drafting boundary applies only to the final artifact that calls for it. Materially unresolved decisions require clarification.

## Use without custom skills

Copy the prompt blocks from these standalone guides into your usual LLM conversation:

| Purpose | English | 简体中文 |
| --- | --- | --- |
| Background and design | [Background](docs/en/background.md) | [开发背景与应用说明](docs/zh-CN/cleanroom-writing技能开发背景与应用说明.md) |
| Prevent leakage before writing | [Before writing](docs/en/before-writing.md) | [写作开始前约定与检查](docs/zh-CN/LLM写作开始前约定与检查.md) |
| Diagnose and repair an existing draft | [Inspect and repair](docs/en/inspect-and-repair.md) | [文稿废案回流检查与修复](docs/zh-CN/LLM文稿废案回流检查与修复.md) |

The repair guide deliberately requests inspection and confirmation before editing. That is a user-selected review mode in its prompt, rather than a mandatory approval step for every use of the skill.

## Scope and limitations

This package contains instructions and documentation, with no runtime dependencies for writing. It cannot recover decisions absent from the provided context or guarantee that every leakage instance will be found. It does not establish whether approved claims are factually correct. Other agents may be able to use the instructions, but their discovery and UI metadata support need separate verification. No cross-model reliability measurement is claimed.

## Development

```text
plugin.json                         Portable plugin metadata
skills/cleanroom-writing/            Installable skill and Codex UI metadata
docs/en/                            English background and standalone guides
docs/zh-CN/                         Chinese background and standalone guides
examples/writing.md                 Bilingual illustrative cases
tests/activation-cases.md           Manual selection and behavior cases
scripts/validate_package.py         Dependency-free package checks
.github/workflows/validate.yml      Package validation in CI
```

Run `python scripts/validate_package.py` with Python 3.9 or newer. It checks package structure, the minimal metadata format, and local Markdown links. [Manual cases](tests/activation-cases.md) cover selection boundaries and expected observable behavior; they have not been executed as independent model evaluations.

See [CONTRIBUTING.md](CONTRIBUTING.md). Please use synthetic examples when reporting failures and remove private manuscript material.

## Author and license

Created by [KnifeTian](https://github.com/KnifeTian). Licensed under the [MIT License](LICENSE).
