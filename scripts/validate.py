#!/usr/bin/env python3
"""Validate every skills/<name>/SKILL.md. Exit 1 on any error."""
import re, sys, pathlib

root = pathlib.Path(__file__).resolve().parent.parent / "skills"
errors, warnings = [], []
for d in sorted(p for p in root.iterdir() if p.is_dir()):
    f = d / "SKILL.md"
    if not f.exists():
        errors.append(f"{d.name}: SKILL.md missing")
        continue
    text = f.read_text(encoding="utf-8")
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        errors.append(f"{d.name}: file must start with ---")
        continue
    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        errors.append(f"{d.name}: frontmatter not closed")
        continue
    fm = {}
    for l in lines[1:end]:
        m = re.match(r"^([A-Za-z_-]+):\s*(.*)$", l)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip('"')
    name, desc = fm.get("name", ""), fm.get("description", "")
    if name != d.name:
        errors.append(f"{d.name}: name '{name}' must equal folder name")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
        errors.append(f"{d.name}: name must be lowercase letters, digits, hyphens, max 64")
    if not desc:
        errors.append(f"{d.name}: description missing")
    if len(desc) > 1024:
        errors.append(f"{d.name}: description over 1024 characters ({len(desc)})")
    elif len(desc) > 200:
        warnings.append(f"{d.name}: description is {len(desc)} characters; claude.ai upload limit is 200")
    if re.search("[–—]", text):
        errors.append(f"{d.name}: contains an em or en dash")
    if len(lines) > 700:
        warnings.append(f"{d.name}: {len(lines)} lines is long")
for w in warnings:
    print("WARN ", w)
for e in errors:
    print("ERROR", e)
print(f"{len(list(root.iterdir()))} skills checked, {len(errors)} errors, {len(warnings)} warnings")
sys.exit(1 if errors else 0)
