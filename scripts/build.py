#!/usr/bin/env python3
"""Build release files into dist/:
  <name>.zip      one per skill, skill folder at the zip root (for claude.ai upload)
  all-skills.zip  every skill folder + install.sh + uninstall.sh + INSTALL.txt (for Claude Code)
  SHA256SUMS      checksums of everything above
"""
import hashlib, pathlib, zipfile

repo = pathlib.Path(__file__).resolve().parent.parent
skills = repo / "skills"
dist = repo / "dist"
dist.mkdir(exist_ok=True)
for old in dist.glob("*"):
    old.unlink()

FIXED = (2026, 1, 1, 0, 0, 0)  # reproducible zips

def add(z, path, arc):
    info = zipfile.ZipInfo(arc, FIXED)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = (0o755 if arc.endswith(".sh") else 0o644) << 16
    z.writestr(info, path.read_bytes())

names = sorted(p.name for p in skills.iterdir() if (p / "SKILL.md").exists())
for n in names:
    with zipfile.ZipFile(dist / f"{n}.zip", "w") as z:
        for f in sorted((skills / n).rglob("*")):
            if f.is_file():
                add(z, f, f"{n}/{f.relative_to(skills / n).as_posix()}")

with zipfile.ZipFile(dist / "all-skills.zip", "w") as z:
    for n in names:
        for f in sorted((skills / n).rglob("*")):
            if f.is_file():
                add(z, f, f"skills/{n}/{f.relative_to(skills / n).as_posix()}")
    for extra in ("install.sh", "uninstall.sh", "INSTALL.txt"):
        add(z, repo / extra, extra)

sums = []
for f in sorted(dist.glob("*.zip")):
    sums.append(f"{hashlib.sha256(f.read_bytes()).hexdigest()}  {f.name}")
(dist / "SHA256SUMS").write_text("\n".join(sums) + "\n")
print(f"built {len(names)} skill zips + all-skills.zip")
