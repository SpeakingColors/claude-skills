#!/usr/bin/env bash
# Install skills for Claude Code into ~/.claude/skills (or $CLAUDE_SKILLS_DIR).
# Usage:
#   ./install.sh                 install every skill
#   ./install.sh reaper ardour   install only these
#   ./install.sh --list          list available skills
# An existing skill folder is moved to <name>.bak-<date>, never deleted.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
src="$here/skills"
dest="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
[ -d "$src" ] || { echo "No skills/ folder next to install.sh" >&2; exit 1; }
if [ "${1:-}" = "--list" ]; then ls -1 "$src"; exit 0; fi
if [ "$#" -eq 0 ]; then set -- $(ls -1 "$src"); fi
mkdir -p "$dest"
stamp="$(date +%Y%m%d-%H%M%S)"
for n in "$@"; do
  [ -f "$src/$n/SKILL.md" ] || { echo "Skip: no skill named '$n'" >&2; continue; }
  if [ -e "$dest/$n" ]; then mv "$dest/$n" "$dest/$n.bak-$stamp"; echo "Backed up old $n"; fi
  cp -r "$src/$n" "$dest/$n"
  echo "Installed $n"
done
echo "Done. Restart Claude Code (or start a new session) to load them. Folder: $dest"
