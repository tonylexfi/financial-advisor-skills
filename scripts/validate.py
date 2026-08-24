#!/usr/bin/env python3
"""Validate repository structure and SKILL.md frontmatter.

Checks:
- every plugin has .claude-plugin/plugin.json with name/version/description
- every skills/*/ dir has SKILL.md
- SKILL.md frontmatter: name matches directory, description present,
  starts with 'Use when', <= 1024 chars total frontmatter fields
- workflow skills reference the three core skills
- marketplace.json plugin sources exist
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORE_REFS = ["lexfi-mcp-playbook", "evidence-discipline", "advisor-communication"]
errors = []

def fm(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    out = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out

mk = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
for p in mk["plugins"]:
    src = ROOT / p["source"]
    if not src.is_dir():
        errors.append(f"marketplace source missing: {p['source']}")

for plugin in sorted((ROOT / "plugins").iterdir()):
    if not plugin.is_dir():
        continue
    pj = plugin / ".claude-plugin/plugin.json"
    if not pj.exists():
        errors.append(f"{plugin.name}: missing plugin.json"); continue
    meta = json.loads(pj.read_text())
    for field in ("name", "version", "description"):
        if not meta.get(field):
            errors.append(f"{plugin.name}: plugin.json missing '{field}'")
    for skill in sorted((plugin / "skills").iterdir()):
        if not skill.is_dir():
            continue
        sm = skill / "SKILL.md"
        if not sm.exists():
            errors.append(f"{skill}: missing SKILL.md"); continue
        text = sm.read_text()
        meta = fm(text)
        if meta is None:
            errors.append(f"{sm}: no YAML frontmatter"); continue
        if meta.get("name") != skill.name:
            errors.append(f"{sm}: frontmatter name '{meta.get('name')}' != dir '{skill.name}'")
        desc = meta.get("description", "")
        if not desc:
            errors.append(f"{sm}: missing description")
        elif not desc.startswith("Use when"):
            errors.append(f"{sm}: description must start with 'Use when'")
        if len(desc) > 1024:
            errors.append(f"{sm}: description exceeds 1024 chars")
        if plugin.name != "advisor-core":
            missing = [c for c in CORE_REFS if c not in text]
            if missing:
                errors.append(f"{sm}: missing core references: {missing}")

if errors:
    print("FAIL")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print(f"OK — validated {len(list((ROOT/'plugins').glob('*/skills/*/SKILL.md')))} skills")
