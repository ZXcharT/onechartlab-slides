#!/usr/bin/env sh
# Thin POSIX wrapper for the shared OneChartLab Slides generator contract.
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
exec python3 "$SCRIPT_DIR/new-project.py" "$@"
