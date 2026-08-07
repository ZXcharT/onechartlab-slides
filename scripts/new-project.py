#!/usr/bin/env python3
"""Create a local OneChartLab Slides deck without third-party dependencies."""
from pathlib import Path
import shutil
import sys

TEMPLATES = {
    "briefing": ("template.html", "ZXcharT Briefing"),
    "showcase": ("templates/showcase.html", "ZXcharT Showcase"),
}


def usage() -> str:
    return 'Usage: scripts/new-project.py [--template briefing|showcase] "project-name"'


def parse_args(args: list[str]) -> tuple[str, str] | None:
    if len(args) == 1 and args[0] and not args[0].startswith("-"):
        return "briefing", args[0]
    if len(args) == 3 and args[0] == "--template" and args[1] and args[2]:
        if args[1] not in TEMPLATES:
            print(f'Unknown template: {args[1]}. Choose briefing or showcase.', file=sys.stderr)
            return None
        return args[1], args[2]
    print(usage(), file=sys.stderr)
    return None


def main() -> int:
    parsed = parse_args(sys.argv[1:])
    if parsed is None:
        return 64
    template_id, name = parsed
    if name in {".", ".."} or Path(name).name != name or name.startswith("-"):
        print("Project name must be a simple directory name.", file=sys.stderr)
        return 64

    root = Path(__file__).resolve().parent.parent
    relative_template, display_name = TEMPLATES[template_id]
    template = root / relative_template
    destination = root / "projects" / name

    if not template.is_file():
        print(f"Seed template is missing: {relative_template}", file=sys.stderr)
        return 66
    if destination.exists():
        print(f"Destination already exists: {destination}", file=sys.stderr)
        return 73

    destination.mkdir(parents=True)
    shutil.copy2(template, destination / "index.html")
    print(f'Created {destination / "index.html"} with {display_name}.')
    print("Open index.html with any modern browser, then replace the placeholders.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
