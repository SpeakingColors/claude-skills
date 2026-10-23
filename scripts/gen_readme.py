#!/usr/bin/env python3
"""Regenerate README.md (skills tables) from each SKILL.md frontmatter."""
import pathlib, re

repo = pathlib.Path(__file__).resolve().parent.parent
skills = repo / "skills"

GROUPS = [
 ("DAWs and hub", ["daw-hub","bitwig-studio","reaper","ardour","waveform","ableton-live","fl-studio","cubase","studio-one-fender-studio-pro","logic-pro","pro-tools"]),
 ("Audio editors, Max for Live and Push", ["wavelab","sound-forge","audacity","max-for-live-expert","ableton-push-expert"]),
 ("Making plugins and hardware tools", ["vst-maker","juce-expert","mockup-is-the-plugin","korg-logue-sdk-expert","hardware-protocol-capture","github-for-beginners"]),
 ("Studio, audio on Linux and sound", ["linux-audio-production","audio-driver-stacks","audio-interface-digital-io","wine-proton-bottles","sound-engineer-acoustics","electronic-music-producer","hard-dance-production","av-receiver-specialist"]),
 ("DJ", ["dj-specialist","dj-gig-guide","denon-prime-sc5000-x1800"]),
 ("Linux and devices", ["bazzite-kde-linux","linux-expert","linux-terminal-expert","man-page-expert","linux-security-hardening","couch-pc-cec-gaming-mode","rog-ally-x-bazzite","knulli-handhelds-m8","arduino-electronics-soldering","grapheneos"]),
 ("Home server and network", ["unraid-specialist","nextcloud-specialist","pihole-raspberry-pi","home-network-specialist"]),
 ("Design and images", ["color-palette-expert","graphic-design-expert","ux-ui-designer","design-software-guide","photo-editing-color-grading","drawing-tablets","squarespace-expert"]),
]


def desc(name):
    for line in (skills / name / "SKILL.md").read_text(encoding="utf-8").split("\n")[:8]:
        if line.startswith("description:"):
            d = line[len("description:"):].strip().strip('"')
            d = re.sub(r"^Use (when|for|first for)\s+", "", d)
            return d[0].upper() + d[1:]
    return ""


present = {p.name for p in skills.iterdir() if (p / "SKILL.md").exists()}
listed = {n for _, ns in GROUPS for n in ns}
extra = sorted(present - listed)
out = []
for title, names in GROUPS + ([("Other", extra)] if extra else []):
    names = [n for n in names if n in present]
    if not names:
        continue
    out.append(f"### {title}\n\n| Skill | What it does |\n|---|---|")
    for n in names:
        out.append(f"| [{n}](skills/{n}/SKILL.md) | {desc(n)} |")
    out.append("")
table = "\n".join(out)

readme = f"""# claude-skills

Free Claude skills for music makers, DJs and Linux users. One folder per skill under `skills/`.
{len(present)} skills. Every skill labels its claims: **VERIFIED** (read on a source page), **COMMUNITY** (forum or project report) or **UNVERIFIED** (not checked, test first). Prices and versions change, so check the vendor page before paying or installing.

## Skills

{table}
## Install

Download from the Releases page. Check files with `sha256sum -c SHA256SUMS`.

**Claude (claude.ai or the desktop app), one skill at a time**

1. Download the zip for one skill, for example `reaper.zip`.
2. In Claude open Customize > Skills (claude.ai/customize/skills) and upload the zip. Code execution must be on.
3. Switch the skill on.

The zip has the skill folder at its root and the folder name matches the skill name, as Claude's help article asks.

**Claude Code (terminal), all skills or a few**

1. Download and unzip `all-skills.zip`.
2. Run `./install.sh` for everything, or `./install.sh reaper ardour` for some. `./install.sh --list` shows names.
3. Start a new Claude Code session. Skills are copied to `~/.claude/skills/<name>/`. Old copies are moved to `<name>.bak-<date>`, never deleted.
4. Remove with `./uninstall.sh <name>` or `./uninstall.sh --all`.

## Build the release files yourself

```
python3 scripts/validate.py   # checks names, descriptions, dashes
python3 scripts/build.py      # writes dist/*.zip and dist/SHA256SUMS
```

Releases are created by the Release workflow (Actions > Release > Run workflow, give a tag such as v1.0.0).

## Add a new skill

Create `skills/<skill-name>/SKILL.md` with this frontmatter, then the instructions. The folder name must equal `name`, and the description should stay under 200 characters (the limit for uploading to Claude).

```
---
name: <skill-name>
description: <when Claude should use this skill>
---
```

Then run `python3 scripts/gen_readme.py` to refresh the table above.

## Notes

- These are unofficial community skills, provided as-is with no warranty. Product and company names belong to their owners; this project is not affiliated with them.
- The logue SDK skill is not made or endorsed by KORG. It is based on the official BSD-3-Clause logue-sdk repo: https://github.com/korginc/logue-sdk
- `logue-cli` is not included and is not covered by this repo's license. It has its own EULA from KORG.
- Skills that run Windows software on Linux (Wine, Bottles) describe community methods. They are not supported by the software makers. Keep a supported system for paid work.
- Legal and contract notes are general information, not legal advice. Laws differ by country.

## License

MIT, see [LICENSE](LICENSE).
"""
(repo / "README.md").write_text(readme, encoding="utf-8")
print("README written,", len(present), "skills")
