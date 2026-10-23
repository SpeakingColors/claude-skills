#!/usr/bin/env bash
# Remove skills installed by install.sh. Usage: ./uninstall.sh reaper ardour   (or --all)
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
dest="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
if [ "$#" -eq 0 ]; then echo "Usage: ./uninstall.sh <skill> [<skill>...] | --all" >&2; exit 1; fi
if [ "$1" = "--all" ]; then set -- $(ls -1 "$here/skills"); fi
for n in "$@"; do
  case "$n" in */*|..|.) echo "Skip bad name: $n" >&2; continue;; esac
  if [ -d "$dest/$n" ]; then rm -r "$dest/$n"; echo "Removed $n"; else echo "Not installed: $n"; fi
done
