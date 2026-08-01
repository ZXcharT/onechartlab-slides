#!/usr/bin/env python3
"""Create a local OneChartLab Slides deck without third-party dependencies."""
from pathlib import Path
import shutil
import sys

def main() -> int:
    if len(sys.argv) != 2 or not sys.argv[1]:
        print('Usage: scripts/new-project.py "project-name"', file=sys.stderr)
        return 64
    name = sys.argv[1]
    if name in {'.', '..'} or Path(name).name != name:
        print('Project name must be a simple directory name.', file=sys.stderr)
        return 64
    root = Path(__file__).resolve().parent.parent
    template = root / 'template.html'
    destination = root / 'projects' / name
    if not template.is_file():
        print('Seed template is missing.', file=sys.stderr)
        return 66
    if destination.exists():
        print(f'Destination already exists: {destination}', file=sys.stderr)
        return 73
    destination.mkdir(parents=True)
    shutil.copy2(template, destination / 'index.html')
    print(f'Created {destination / "index.html"}')
    print('Open index.html with any modern browser, then replace the placeholders.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
