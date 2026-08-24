#!/usr/bin/env bash
# Fallback installer: copy skills into a Claude skills directory.
# Usage:
#   ./install.sh --list
#   ./install.sh --plugin advisor-client --target ~/.claude/skills
#   ./install.sh --plugin all --target ~/.claude/skills
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
PLUGIN="" TARGET=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --list) ls "$ROOT/plugins"; exit 0 ;;
    --plugin) PLUGIN="$2"; shift 2 ;;
    --target) TARGET="$2"; shift 2 ;;
    *) echo "unknown arg: $1" >&2; exit 1 ;;
  esac
done

[[ -n "$PLUGIN" && -n "$TARGET" ]] || { echo "usage: ./install.sh --plugin <name|all> --target <dir>" >&2; exit 1; }
mkdir -p "$TARGET"

install_one() {
  local p="$1"
  [[ -d "$ROOT/plugins/$p/skills" ]] || { echo "no such plugin: $p" >&2; exit 1; }
  cp -R "$ROOT/plugins/$p/skills/"* "$TARGET/"
  echo "installed $p"
}

# advisor-core is a hard dependency of every workflow plugin
if [[ "$PLUGIN" == "all" ]]; then
  for p in "$ROOT"/plugins/*/; do install_one "$(basename "$p")"; done
else
  install_one advisor-core
  [[ "$PLUGIN" != "advisor-core" ]] && install_one "$PLUGIN"
fi
echo "done → $TARGET"
