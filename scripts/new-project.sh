#!/usr/bin/env sh
# Create a local OneChartLab Slides deck from the repository seed.
set -eu

if [ "$#" -ne 1 ] || [ -z "$1" ]; then
  printf '%s\n' 'Usage: scripts/new-project.sh "project-name"' >&2
  exit 64
fi
SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT_DIR=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
TEMPLATE="$ROOT_DIR/template.html"
DEST="$ROOT_DIR/projects/$1"

case "$1" in */*|*'\'*|'.'|'..') printf '%s\n' 'Project name must be a simple directory name.' >&2; exit 64;; esac
[ -f "$TEMPLATE" ] || { printf '%s\n' 'Seed template is missing.' >&2; exit 66; }
[ ! -e "$DEST" ] || { printf '%s\n' "Destination already exists: $DEST" >&2; exit 73; }
mkdir -p "$DEST"
cp "$TEMPLATE" "$DEST/index.html"
printf '%s\n' "Created $DEST/index.html"
printf '%s\n' 'Open index.html with any modern browser, then replace the placeholders.'
