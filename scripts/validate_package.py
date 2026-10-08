#!/usr/bin/env python3
"""Validate this package's deliberately minimal metadata and local links.

Standard library only. This is not a general YAML or Agent Plugins schema
validator, and does not evaluate model selection or writing behavior.
"""
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


def validate():
    errors = []

    def check(condition, message):
        if not condition:
            errors.append(message)

    required = [
        'plugin.json', 'LICENSE', 'README.md', 'README.zh-CN.md', 'CONTRIBUTING.md',
        'PUBLICATION_CHECKLIST.md', 'examples/writing.md',
        'tests/activation-cases.md', '.github/workflows/validate.yml',
        'skills/cleanroom-writing/SKILL.md',
        'skills/cleanroom-writing/agents/openai.yaml',
        'docs/en/background.md', 'docs/en/before-writing.md',
        'docs/en/inspect-and-repair.md',
        'docs/zh-CN/cleanroom-writing技能开发背景与应用说明.md',
        'docs/zh-CN/LLM写作开始前约定与检查.md',
        'docs/zh-CN/LLM文稿废案回流检查与修复.md',
    ]
    for name in required:
        check((ROOT / name).is_file(), 'Missing file: ' + name)
    if errors:
        return errors

    manifest = json.loads((ROOT / 'plugin.json').read_text(encoding='utf-8'))
    check(manifest.get('$schema') ==
          'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json',
          'Unexpected portable manifest schema')
    check(manifest.get('name') == 'cleanroom-writing', 'Unexpected plugin name')
    check(manifest.get('license') == 'MIT', 'Unexpected license')
    check(manifest.get('author', {}).get('name') == 'KnifeTian',
          'Unexpected author')
    check(bool(re.fullmatch(r'\d+\.\d+\.\d+', manifest.get('version', ''))),
          'Invalid version')
    check(isinstance(manifest.get('description'), str) and
          bool(manifest['description'].strip()), 'Missing description')

    skill_dir = ROOT / 'skills' / 'cleanroom-writing'
    skill = (skill_dir / 'SKILL.md').read_text(encoding='utf-8')
    frontmatter = re.match(r'\A---\n(.*?)\n---\n', skill, re.S)
    check(frontmatter is not None, 'Missing YAML frontmatter')
    if frontmatter:
        # This skill uses only two plain single-line scalar fields.
        fields = {}
        for line in frontmatter.group(1).splitlines():
            match = re.fullmatch(r'(name|description): (.+)', line)
            check(match is not None, 'Unsupported minimal frontmatter: ' + line)
            if match:
                check(match[1] not in fields, 'Duplicate field: ' + match[1])
                fields[match[1]] = match[2]
        check(fields.get('name') == skill_dir.name, 'Skill name/folder mismatch')
        check(0 < len(fields.get('description', '')) <= 1024,
              'Missing or oversized skill description')

    ui = (skill_dir / 'agents' / 'openai.yaml').read_text(encoding='utf-8')
    ui_fields = {}
    section = None
    sections = []
    for line in ui.splitlines():
        if not line.strip():
            continue
        if line in ('interface:', 'policy:'):
            section = line[:-1]
            sections.append(section)
            continue
        match = re.fullmatch(r'  ([a-z_]+): (.+)', line)
        check(match is not None and section is not None,
              'Unsupported minimal UI metadata: ' + line)
        if not match or section is None:
            continue
        key = section + '.' + match[1]
        check(key not in ui_fields, 'Duplicate UI field: ' + key)
        ui_fields[key] = match[2]
    check(sections == ['interface', 'policy'], 'Unexpected UI sections')
    for key in ('display_name', 'short_description', 'default_prompt'):
        raw = ui_fields.get('interface.' + key, '')
        check(raw.startswith('"') and raw.endswith('"'), 'Unquoted UI ' + key)
        if raw.startswith('"'):
            try:
                ui_fields['interface.' + key] = json.loads(raw)
            except json.JSONDecodeError:
                check(False, 'Invalid quoted UI value: ' + key)
    check(25 <= len(ui_fields.get('interface.short_description', '')) <= 64,
          'UI description outside 25–64 characters')
    check('$cleanroom-writing' in ui_fields.get('interface.default_prompt', ''),
          'Default prompt must invoke skill')
    check(ui_fields.get('policy.allow_implicit_invocation') == 'true',
          'Automatic invocation unexpectedly changed')

    for path in ROOT.rglob('*.md'):
        content = path.read_text(encoding='utf-8')
        # Remove fenced examples so illustrative template text is not a link.
        prose = re.sub(r'^```.*?^```[^\n]*', '', content, flags=re.M | re.S)
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', prose):
            target = target.strip('<>')
            parts = urlsplit(target)
            if parts.scheme or target.startswith('#'):
                continue
            resolved = (path.parent / unquote(parts.path)).resolve()
            check(ROOT == resolved or ROOT in resolved.parents,
                  'Link escapes package: ' + target)
            check(resolved.exists(),
                  f'Broken link in {path.relative_to(ROOT)}: {target}')
        for private_marker in ('C:\\Users\\', 'sk-proj-', 'github_pat_'):
            check(private_marker not in content,
                  f'Private-content marker in {path.relative_to(ROOT)}')
    return errors


if __name__ == '__main__':
    findings = validate()
    for finding in findings:
        print('FAIL:', finding)
    if findings:
        raise SystemExit(1)
    print('PASS: structure, minimal metadata, local links, and private-marker checks')
    print('Not evaluated: full remote schema, installation, model activation/behavior')
