#!/usr/bin/env python3
"""Dependency-free integrity, portability, and privacy checks for OneChartLab Slides."""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent

REQUIRED = [
    "README.md",
    "README.en.md",
    "LICENSE",
    "THIRD_PARTY_NOTICES.md",
    "TRADEMARKS.md",
    "SOURCES.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "SKILL.md",
    "AGENTS.md",
    "template.html",
    "index.html",
    "themes/zxchart/design.md",
    "docs/layouts.md",
    "docs/customization.md",
    "docs/platforms/hanaagent.md",
    "examples/agent-workflow/index.html",
    "scripts/new-project.sh",
    "scripts/new-project.py",
    ".gitignore",
    ".github/workflows/pages.yml",
]

LAYOUTS = [
    "layout-cover",
    "layout-agenda",
    "layout-metrics",
    "layout-dashboard",
    "layout-split",
    "layout-bars",
    "layout-quote",
    "layout-timeline",
    "layout-detail",
    "layout-stack",
    "layout-compare",
    "layout-timeline-3col",
    "layout-hook",
    "layout-statement",
    "layout-outro",
    "layout-closing",
]

# Assemble sensitive terms so this checker does not trigger on its own source.
BANNED_PATTERNS = {
    "fixed private agent id": r"hua" + r"zhu",
    "private agent display name": "花花的" + "小助手",
    "macOS user path": r"/Us" + r"ers/",
    "private workspace name": "OH-" + "WorkSpace",
    "private username": "kangk" + "ang",
    "hard-coded agent selector": r"agent\s*=\s*[\"']hua" + r"zhu[\"']",
    "hard-coded agent type": r"agentType\s*=\s*[\"']hua" + r"zhu[\"']",
    "private-key marker": "PRIVATE " + "KEY",
    "authorization header credential": r"Bear" + r"er\s+[A-Za-z0-9._-]{8,}",
    "OpenAI-style secret": r"sk" + r"-[A-Za-z0-9]{16,}",
    "password assignment": r"pass" + r"word\s*[:=]\s*[\"'][^\"']{4,}[\"']",
    "token assignment": r"to" + r"ken\s*[:=]\s*[\"'][A-Za-z0-9._-]{8,}[\"']",
    "API key assignment": r"api[_ -]?" + r"key\s*[:=]\s*[\"'][^\"']{8,}[\"']",
}

TEXT_SUFFIXES = {
    "",
    ".md",
    ".html",
    ".css",
    ".js",
    ".py",
    ".sh",
    ".yml",
    ".yaml",
    ".json",
    ".txt",
    ".toml",
}

LAYOUT_DOCS = [
    "README.md",
    "README.en.md",
    "SKILL.md",
    "AGENTS.md",
    "themes/zxchart/design.md",
    "docs/layouts.md",
]

VISUAL_PRIMITIVES = [
    "--stage-inline",
    "evidence-rail",
    "cover-datastream",
    "text-gradient { color: var(--accent); }",
    "closing-ring-outer",
    "statement-cursor",
    "prefers-reduced-motion",
    "max-height: 720px",
    "nav-btn:disabled",
    "touchstart",
    "aria-hidden",
    "slide.inert",
    "expandedBlock",
    "focus-sub",
    "mousemove",
    "aria-pressed",
    "compare-scroll",
]


def read_text_files() -> list[tuple[Path, str]]:
    files: list[tuple[Path, str]] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            files.append((path, path.read_text(encoding="utf-8")))
        except UnicodeDecodeError:
            continue
    return files


def main() -> int:
    errors: list[str] = []

    for item in REQUIRED:
        if not (ROOT / item).is_file():
            errors.append(f"missing required file: {item}")

    if errors:
        print("\n".join(f"FAIL: {error}" for error in errors))
        return 1

    template = (ROOT / "template.html").read_text(encoding="utf-8")
    slide_layouts = re.findall(r'<section\s+class="slide\s+(layout-[a-z0-9-]+)', template)
    if slide_layouts != LAYOUTS:
        errors.append(f"template slide order mismatch: {slide_layouts}")
    if len(slide_layouts) != len(set(slide_layouts)):
        errors.append("template contains duplicate slide layouts")

    gallery = (ROOT / "index.html").read_text(encoding="utf-8")
    gallery_cards = gallery.count('class="gallery-card"')
    gallery_previews = [
        int(value)
        for value in re.findall(r"template\.html\?slide=(\d+)&amp;embed=1", gallery)
    ]
    if not 4 <= gallery_cards <= 8:
        errors.append(f"gallery must stay curated at 4-8 cards, found {gallery_cards}")
    if len(gallery_previews) != gallery_cards or len(gallery_previews) != len(set(gallery_previews)):
        errors.append(f"gallery live previews are missing or duplicated: {gallery_previews}")
    if any(value < 1 or value > len(LAYOUTS) for value in gallery_previews):
        errors.append(f"gallery references an invalid slide number: {gallery_previews}")
    if "Selected Gallery" not in gallery or "Live HTML previews" not in gallery:
        errors.append("gallery title or live-preview description is missing")
    if "URLSearchParams" not in template or 'classList.add("embed")' not in template:
        errors.append("template must support direct slide links and embedded gallery previews")
    if 'slide.setAttribute("aria-hidden", String(!isActive))' not in template or "slide.inert = !isActive" not in template:
        errors.append("non-current slides must be aria-hidden and inert")
    if ".text-gradient { color: var(--accent); }" not in template:
        errors.append("core layouts must not use gradient text")
    if ".text-gradient {\n      background:" in template:
        errors.append("core layouts must not use a gradient text treatment")
    if ".evidence-rail::before" in template or "accent-line" in template:
        errors.append("core layouts must not use isolated short-line decoration")
    if re.search(r'<div class="metric-value"[^>]*>—</div>', template):
        errors.append("metric placeholders must not render as ambiguous short bars")
    if "--text-muted: #88889c" not in template:
        errors.append("informational muted text must retain readable contrast")
    if "width: 44px;\n      height: 44px;" not in template:
        errors.append("navigation controls must retain a 44px touch target")
    pressure = ROOT / "projects/v2-pressure-test/index.html"
    if not pressure.is_file():
        errors.append("missing V2 Phase 1 pressure test")
    else:
        pressure_text = pressure.read_text(encoding="utf-8")
        pressure_slides = {
            "layout-cover": 1,
            "layout-agenda": 2,
            "layout-metrics": 3,
            "layout-dashboard": 4,
            "layout-split": 5,
            "layout-detail": 9,
            "layout-compare": 11,
        }
        for layout, slide_no in pressure_slides.items():
            case_id = layout.removeprefix("layout-")
            if f'id="case-{case_id}"' not in pressure_text:
                errors.append(f"pressure test missing content for {layout}")
            if f"../../template.html?slide={slide_no}&amp;embed=1" not in pressure_text:
                errors.append(f"pressure test must render {layout} through template.html")
        if "applyCase(this" not in pressure_text or "frame.contentDocument" not in pressure_text:
            errors.append("pressure test must inject content into the real template runtime")
        if "合成演示" not in pressure_text:
            errors.append("pressure test must identify synthetic/demo content")

    for doc in LAYOUT_DOCS:
        text = (ROOT / doc).read_text(encoding="utf-8")
        missing = [layout for layout in LAYOUTS if layout not in text]
        if missing:
            errors.append(f"{doc} missing layouts: {', '.join(missing)}")

    for marker in VISUAL_PRIMITIVES:
        if marker not in template:
            errors.append(f"template missing visual or interaction primitive: {marker}")

    documented_tokens = [
        "--bg-surface",
        "--bg-elevated",
        "--accent-border",
        "--text-secondary",
        "--text-muted",
        "--border-strong",
    ]
    for doc in ["themes/zxchart/design.md", "docs/customization.md"]:
        text = (ROOT / doc).read_text(encoding="utf-8")
        for token in documented_tokens:
            if token not in text:
                errors.append(f"{doc} missing current theme token: {token}")

    if len(template.splitlines()) < 400:
        errors.append("template is unexpectedly compressed; keep public source formatted and reviewable")
    if "“" in template or "”" in template:
        errors.append("template contains a displayed typographic quotation; use an explicit placeholder or sourced quote")

    shell = (ROOT / "scripts/new-project.sh").read_text(encoding="utf-8")
    python_script = (ROOT / "scripts/new-project.py").read_text(encoding="utf-8")
    readme_zh = (ROOT / "README.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.en.md").read_text(encoding="utf-8")
    pages = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    trademarks = (ROOT / "TRADEMARKS.md").read_text(encoding="utf-8")

    if "ROOT_DIR" not in shell or "template.html" not in shell:
        errors.append("shell generator is not self-locating")
    if "Path(__file__).resolve()" not in python_script or "third-party" not in python_script:
        errors.append("Python generator portability marker missing")
    if 'sh scripts/new-project.sh "my-deck"' not in readme:
        errors.append("README must invoke the POSIX generator through sh")
    if "# OneChartLab Slides" not in readme or "OneChartLab Slides is an Agent Skill" not in readme:
        errors.append("README product description is missing or inconsistent")
    if "[简体中文](README.md)" not in readme:
        errors.append("English README is missing the Simplified Chinese language link")
    if "## Install the Skill" not in readme or "~/.agents/skills/onechartlab-slides/" not in readme:
        errors.append("English README is missing concrete Skill installation instructions")
    if (
        "[English](README.en.md)" not in readme_zh
        or "OneChartLab Slides 是一个用于制作 HTML 演示文稿的 Agent Skill" not in readme_zh
        or "## 安装 Skill" not in readme_zh
        or "## 快速开始" not in readme_zh
        or "## 使用要求" not in readme_zh
    ):
        errors.append("Simplified Chinese README is incomplete or missing user instructions")
    if readme.index("## Quick start") > readme.index("## Optional: create a project from the command line"):
        errors.append("English README must present normal use before optional command-line use")
    if readme_zh.index("## 快速开始") > readme_zh.index("## 可选：使用命令行创建项目"):
        errors.append("Simplified Chinese README must present normal use before optional command-line use")
    skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    skill_frontmatter = skill_text.split("---", 2)[1] if skill_text.startswith("---") else ""
    if "name: onechartlab-slides" not in skill_frontmatter:
        errors.append("SKILL.md must use the onechartlab-slides identifier")
    if "license: MIT. See LICENSE." not in skill_frontmatter or "compatibility:" not in skill_frontmatter:
        errors.append("SKILL.md is missing its public license or compatibility declaration")
    for trigger in ["PPT", "视频分镜", "HTML Slides"]:
        if trigger not in skill_frontmatter:
            errors.append(f"SKILL.md description missing trigger context: {trigger}")
    for reference in [
        "AGENTS.md",
        "themes/zxchart/design.md",
        "docs/layouts.md",
        "docs/customization.md",
        "template.html",
    ]:
        if f"`{reference}`" not in skill_text:
            errors.append(f"SKILL.md missing operational resource link: {reference}")
    if "./scripts/new-project.sh" in readme:
        errors.append("README contains an executable-bit-dependent shell command")
    if "workflow_dispatch:" not in pages:
        errors.append("Pages workflow must remain manually triggered")
    if re.search(r"if:\s*\$\{\{\s*false\s*\}\}", pages):
        errors.append("Pages workflow is permanently disabled")
    if "push:" in pages or "schedule:" in pages:
        errors.append("Pages workflow must not deploy automatically in v0.1.0")
    if "Copyright (c) 2026 Zara Zhang" not in license_text:
        errors.append("upstream MIT copyright notice is missing")
    if "Copyright (c) 2026 ZXcharT (modifications)" not in license_text:
        errors.append("ZXcharT modification copyright notice is missing")
    if "does not grant trademark rights" not in trademarks:
        errors.append("trademark boundary is missing")

    for path, text in read_text_files():
        relative = path.relative_to(ROOT)
        for label, pattern in BANNED_PATTERNS.items():
            if re.search(pattern, text, flags=re.IGNORECASE):
                errors.append(f"{label} found in {relative}")

    if errors:
        print("\n".join(f"FAIL: {error}" for error in errors))
        return 1

    print(
        "OK: "
        f"{len(REQUIRED)} required files, {len(LAYOUTS)} ordered layouts, "
        f"{len(VISUAL_PRIMITIVES)} visual/interaction primitives, full-repository privacy scan, "
        "portable generators, manual-only Pages, and license boundaries passed."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
