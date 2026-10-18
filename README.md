# claude-skills

A collection of Claude skills. One folder per skill under `skills/`.

## Skills

| Skill | What it does |
|---|---|
| [korg-logue-sdk-expert](skills/korg-logue-sdk-expert/SKILL.md) | Write, port, debug, build and load custom oscillators, synths and effects with the KORG logue SDK (minilogue xd, prologue, NTS-1 mkI/mkII, NTS-3, drumlogue, microKORG2). Per-platform APIs, manifest and header rules, memory limits, `logue-cli`, realtime DSP checklist. |

## Install a skill in Claude

Works on Pro, Max, Team and Enterprise plans with code execution enabled.

1. Download this repo (Code > Download ZIP) and unzip it.
2. Zip the one skill folder you want, for example `korg-logue-sdk-expert`. The folder name must match the skill name, and it must contain `SKILL.md`.
3. In Claude go to Settings > Capabilities > Skills > Upload skill and pick the ZIP.

Custom skills are private to the account that uploads them.

## Add a new skill

Create `skills/<skill-name>/SKILL.md` with this frontmatter, then the instructions:

```
---
name: <skill-name>
description: <when Claude should use this skill>
---
```

Add a row to the table above.

## Notes

- These are unofficial community skills. They are provided as-is, with no warranty.
- The logue SDK skill is not made or endorsed by KORG. It is based on the official BSD-3-Clause logue-sdk repo: https://github.com/korginc/logue-sdk
- `logue-cli` is not included and is not covered by this repo's license. It has its own EULA from KORG.

## License

MIT, see [LICENSE](LICENSE).
