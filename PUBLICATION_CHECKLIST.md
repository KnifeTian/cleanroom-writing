# Publication checklist

Local package prepared on 2026-10-08. Confirmed repository name: `cleanroom-writing`.

GitHub repository Description (copy when creating the repository):

> Writing skill for Codex and Claude Code. Keep rejected ideas out of final drafts. 面向论文与技术文档的多轮 AI 写作定稿与审计，防止废案回流；附独立提示词。

Suggested GitHub Topics (11): `agent-skills`, `codex`, `claude-code`, `llm`, `ai-writing`, `writing-assistant`, `prompt-engineering`, `document-editing`, `academic-writing`, `research-writing`, `thesis-writing`.

## Owner decisions before publication

- [x] GitHub owner: KnifeTian.
- [x] Repository name: cleanroom-writing; visibility: public.
- [x] Displayed author: KnifeTian; no contact email supplied.
- [x] MIT selected by the owner; LICENSE added with Copyright (c) 2026 KnifeTian.
- [x] Author, planned repository URL, and license added to plugin metadata. The remote repository has not yet been created.
- [ ] Review the final package and authorize repository creation/push.
- [ ] Decide whether to publish `v0.1.0` and a first release.

## Package review

- [ ] Review both READMEs and bilingual companion documents.
- [x] Package validator passed, including local links and confirmed author/license metadata.
- [x] Official Skill Creator validator passed with project-local PyYAML.
- [x] plugin.json passed the published Agent Plugins 1.0.0 JSON Schema; UI and workflow YAML parsed.
- [ ] Review `tests/activation-cases.md`; record any actual model evaluation separately.
- [x] PowerShell copy and existing-directory refusal tested for both host layouts in an isolated directory outside the package. Personal directories were not modified.
- [ ] Test macOS/Linux commands and live host discovery; not verified on this Windows machine.
- [ ] If distributing through a plugin marketplace, test that installation path separately.
- [x] Reviewed candidate files for private content; original skill hashes unchanged, Chinese source copies identical.

## Public-package changes from the local skill

- The existing local skill entrypoint was already English.
- Added one rule for output language: explicit user choice, then existing source language, then request language for a new draft.
- Shortened the UI description to the documented length range.
- Preserved automatic invocation (`allow_implicit_invocation: true`) and the core drafting/audit workflow.
- Chinese companion documents were copied from source; English companion documents are edited translations using the same workflow principles.
- Original skill files were not edited. Source hashes are recorded in the sibling local review file, outside this publishable folder.

## After authorized publication

- [ ] Verify rendered READMEs, file list, repository visibility, and license.
- [ ] Test installation from the published contents.
- [ ] If approved, tag and release the tested version.
- [ ] Keep future changes scoped and record observed compatibility and selection issues.
