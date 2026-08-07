#!/usr/bin/env python3
"""Dependency-free integrity, portability, and privacy checks for OneChartLab Slides."""

from __future__ import annotations

from pathlib import Path
import contextlib
import hashlib
import io
import json
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
    "templates/showcase.html",
    "templates/briefing.manifest.json",
    "index.html",
    "index.en.html",
    "PRODUCT.md",
    "DESIGN.md",
    "themes/zxchart/design.md",
    "themes/showcase/design.md",
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
    "themes/showcase/design.md",
    "docs/layouts.md",
]

PUBLIC_RUNTIME_MARKERS = [
    "URLSearchParams",
    'classList.add("embed")',
    'slide.setAttribute("aria-hidden", String(!isActive))',
    "slide.inert = !isActive",
    "width: 44px;",
    "height: 44px;",
    "touchStartedInScroller",
    'event.target.closest(".compare-scroll")',
    "touchcancel",
    "prefers-reduced-motion",
    "focusConfigs",
    "pointerover",
    "pointerleave",
    "aria-selected",
    "aria-pressed",
    "compare-scroll",
    "min-width: 720px",
    "overflow: auto",
    "overscroll-behavior: contain",
]

BRIEFING_ACCEPTED_SHA256 = "4f52815430045d38038f72ab062ddf6ef025d492aed8fb7dc766cb9a9d26e44c"

BRIEFING_VISUAL_PRIMITIVES = [
    "--stage-inline",
    "evidence-rail",
    "text-gradient { color: var(--accent); }",
    "--motion-base",
    "font-variant-numeric: lining-nums tabular-nums",
    "statement-cursor",
    "prefers-reduced-motion",
    "max-height: 720px",
    "nav-btn:disabled",
    "touchstart",
    "aria-hidden",
    "slide.inert",
    "expandedBlock",
    "focus-sub",
    "pointerover",
    "has-preview-focus",
    "is-previewed",
    "aria-pressed",
    "focusConfigs",
    "has-locked-focus",
    "Enter lock focus",
    "aria-selected",
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

    template_paths = {
        "briefing": ROOT / "template.html",
        "showcase": ROOT / "templates/showcase.html",
    }
    templates = {
        name: path.read_text(encoding="utf-8")
        for name, path in template_paths.items()
    }
    template = templates["briefing"]
    showcase = templates["showcase"]

    for name, source in templates.items():
        slide_layouts = re.findall(r'<section\s+class="slide\s+(layout-[a-z0-9-]+)', source)
        if slide_layouts != LAYOUTS:
            errors.append(f"{name} slide order mismatch: {slide_layouts}")
        if len(slide_layouts) != len(set(slide_layouts)):
            errors.append(f"{name} contains duplicate slide layouts")
        for marker in PUBLIC_RUNTIME_MARKERS:
            if marker not in source:
                errors.append(f"{name} missing public runtime marker: {marker}")

    manifest = json.loads((ROOT / "templates/briefing.manifest.json").read_text(encoding="utf-8"))
    briefing_digest = hashlib.sha256((ROOT / "template.html").read_bytes()).hexdigest()
    if manifest.get("entry") != "../template.html" or manifest.get("default") is not True:
        errors.append("Briefing manifest must lock template.html as the default entry")
    if manifest.get("sha256") != BRIEFING_ACCEPTED_SHA256:
        errors.append("Briefing manifest does not match the explicitly accepted digest")
    if briefing_digest != BRIEFING_ACCEPTED_SHA256:
        errors.append(
            f"Briefing bytes changed without explicit acceptance: {briefing_digest}"
        )

    gallery_paths = {
        "zh-CN": ROOT / "index.html",
        "en": ROOT / "index.en.html",
    }
    locale_markers = {
        "zh-CN": [
            '<html lang="zh-CN">',
            'href="index.en.html" lang="en"',
            "Briefing 为默认模板",
            "每套模板各 3 个实时预览",
        ],
        "en": [
            '<html lang="en">',
            'href="index.html" lang="zh-CN"',
            "Briefing is the default",
            "Three live previews from each template",
        ],
    }
    gallery_preview_sets: dict[str, tuple[list[int], list[int]]] = {}
    gallery_sources: dict[str, str] = {}
    for locale, path in gallery_paths.items():
        gallery = path.read_text(encoding="utf-8")
        gallery_sources[locale] = gallery
        gallery_cards = gallery.count('class="gallery-card"')
        briefing_previews = [
            int(value)
            for value in re.findall(r'<iframe src="template\.html\?slide=(\d+)&amp;embed=1"', gallery)
        ]
        showcase_previews = [
            int(value)
            for value in re.findall(r'<iframe src="templates/showcase\.html\?slide=(\d+)&amp;embed=1"', gallery)
        ]
        gallery_previews = briefing_previews + showcase_previews
        gallery_preview_sets[locale] = (briefing_previews, showcase_previews)
        if not 4 <= gallery_cards <= 8:
            errors.append(f"{locale} gallery must stay curated at 4-8 cards, found {gallery_cards}")
        if len(gallery_previews) != gallery_cards:
            errors.append(f"{locale} gallery live previews are missing: {gallery_previews}")
        if len(briefing_previews) != 3 or len(showcase_previews) != 3:
            errors.append(
                f"{locale} gallery must show three Briefing and three Showcase previews: "
                f"{briefing_previews} / {showcase_previews}"
            )
        if len(briefing_previews) != len(set(briefing_previews)) or len(showcase_previews) != len(set(showcase_previews)):
            errors.append(f"{locale} gallery must not duplicate a preview within one template")
        if any(value < 1 or value > len(LAYOUTS) for value in gallery_previews):
            errors.append(f"{locale} gallery references an invalid slide number: {gallery_previews}")
        for marker in [
            "ZXcharT Briefing",
            "ZXcharT Showcase",
            'href="template.html"',
            'href="templates/showcase.html"',
            *locale_markers[locale],
        ]:
            if marker not in gallery:
                errors.append(f"{locale} dual-template gallery marker missing: {marker}")
    if gallery_preview_sets["zh-CN"] != gallery_preview_sets["en"]:
        errors.append("Chinese and English galleries must preview the same slides")
    gallery_style_matches = {
        locale: re.search(r"<style>(.*?)</style>", source, re.S)
        for locale, source in gallery_sources.items()
    }
    if any(match is None for match in gallery_style_matches.values()):
        errors.append("Chinese and English galleries must each contain an inline style block")
    else:
        gallery_styles = {
            locale: match.group(1)
            for locale, match in gallery_style_matches.items()
        }
        if gallery_styles["zh-CN"] != gallery_styles["en"]:
            errors.append("Chinese and English galleries must share identical layout and visual CSS")
    if ".text-gradient { color: var(--accent); }" not in template:
        errors.append("core layouts must not use gradient text")
    if ".text-gradient {\n      background:" in template:
        errors.append("core layouts must not use a gradient text treatment")
    if ".evidence-rail::before" in template or "accent-line" in template:
        errors.append("core layouts must not use isolated short-line decoration")
    if re.search(r'<div class="metric-value"[^>]*>—</div>', template):
        errors.append("metric placeholders must not render as ambiguous short bars")
    if "--text-muted: #9695a0" not in template:
        errors.append("informational muted text must retain the audited contrast token")
    if "--accent: #d9a441" not in template or "--bg: #11131b" not in template:
        errors.append("template must retain the audited matte briefing palette")
    if "filter: blur" in template or "linear-gradient" in template or "radial-gradient" in template:
        errors.append("template must not reintroduce glow or gradient effects")
    if "h4 { font-weight: 700; }" not in template:
        errors.append("heading weights must be explicit rather than UA-dependent")
    if ".tag {" not in template or "color: var(--text-secondary);" not in template:
        errors.append("header tags must remain quieter than gold section indexes")
    if 'font-feature-settings: "lnum" 1, "tnum" 1;' not in template:
        errors.append("real numeric roles must retain lining tabular numerals")
    focus_config = re.search(r"const focusConfigs = \[(.*?)\];", template, re.S)
    if not focus_config or focus_config.group(1).count('["') < 9:
        errors.append("shared presentation focus must cover the audited evidence groups")
    if 'if (["Enter", " "].includes(event.key))' not in template:
        errors.append("presentation focus items must support Enter and Space")
    if ".focus-item.is-previewed" not in template or ".focus-item.is-focused" not in template:
        errors.append("presentation focus must expose stable preview and locked states")
    if ':has(.focus-item:hover)' in template or 'addEventListener("mousemove"' in template:
        errors.append("presentation focus must not reintroduce gap-flicker or proximity opacity loops")
    preview_peer_dimming = re.search(r"has-preview-focus[^}]*opacity", template, re.S)
    if preview_peer_dimming:
        errors.append("pointer preview must remain local and must not animate peer opacity")
    focused_rule = re.search(r"\.focus-item\.is-focused\s*\{([^}]*)\}", template)
    if not focused_rule or "box-shadow" in focused_rule.group(1) or "border" in focused_rule.group(1):
        errors.append("locked focus must not place a tight border around content")
    if "--motion-focus: 220ms" not in template:
        errors.append("presentation focus must retain the audited smooth transition duration")

    showcase_design = (ROOT / "themes/showcase/design.md").read_text(encoding="utf-8")
    showcase_markers = [
        "ZXcharT Showcase · Layout Gallery",
        "--bg: #171824",
        "--accent: #f0b93c",
        "--text-muted: #9695a0",
        "--red: #e66b60",
        "cover-orb",
        "text-gradient",
        "hookOrbBreathe",
        "statement-cursor",
        "closing-ring-outer",
        "compare-scroll",
        "min-width: 720px",
        "overflow: auto",
        "overflow-wrap: anywhere",
        ".slide-content { flex: 0 0 auto; justify-content: flex-start; min-height: 0; }",
        "width: 44px;",
        "height: 44px;",
    ]
    for marker in showcase_markers:
        if marker not in showcase:
            errors.append(f"Showcase visual/runtime marker missing: {marker}")
    if "accent-line" in showcase:
        errors.append("Showcase must not restore isolated decorative short rules")
    if re.search(r'<div class="metric-value"[^>]*>—</div>', showcase):
        errors.append("Showcase metric placeholders must be explicit numeric forms")
    for marker in [
        "Gradient text and blurred light fields are allowed only",
        "Pointer preview changes only the current item",
        "Body content must never be silently clipped",
        "Layout minimums",
        "Runtime contract",
    ]:
        if marker not in showcase_design:
            errors.append(f"Showcase design contract missing: {marker}")

    for name, source in templates.items():
        focus_config = re.search(r"const focusConfigs = \[(.*?)\];", source, re.S)
        if not focus_config or focus_config.group(1).count('["') < 9:
            errors.append(f"{name} focus coverage is incomplete")
        if 'if (["Enter", " "].includes(event.key))' not in source:
            errors.append(f"{name} focus items must support Enter and Space")

    interaction_contract = {
        "single global locked focus": [
            "let lockedFocus = null;",
            "const wasFocused = lockedFocus === item;",
            "lockedFocus = item;",
        ],
        "mutually exclusive focus modes": [
            "clearExpandedBlock();\n      clearOutroFocus();\n      clearLockedFocus();",
            "clearLockedFocus();\n      clearOutroFocus();\n      clearExpandedBlock();",
            "clearLockedFocus();\n        clearExpandedBlock();\n        clearOutroFocus();",
        ],
        "unified clear paths": [
            'if (event.key === "Escape") { clearFocusEffects(); return; }',
            "function updateSlide() {\n      clearFocusEffects();",
            'if (!event.target.closest(".stack-tier, #outroSub, .focus-item")) clearFocusEffects();',
        ],
        "compare touch isolation": [
            'touchStartedInScroller = Boolean(event.target.closest(".compare-scroll"));',
            "if (!touchStartedInScroller &&",
        ],
        "table row semantics": [
            'const tableRow = item.matches("tr");',
            'tableRow ? "aria-selected" : "aria-pressed"',
            "item.tabIndex = 0;",
        ],
        "keyboard activation": [
            'if (["Enter", " "].includes(event.key))',
            "toggleLockedFocus(item);",
        ],
        "stable pointer preview": [
            'document.querySelectorAll(".focus-group, .stack-body")',
            'group.addEventListener("pointerover"',
            'group.addEventListener("pointerleave"',
            "clearPreviewFocus(group);",
        ],
        "reduced motion focus guard": [
            ".focus-item.is-previewed,\n      .focus-item.is-focused,",
            "transform: none !important;",
        ],
    }
    for name, source in templates.items():
        for contract, markers in interaction_contract.items():
            missing = [marker for marker in markers if marker not in source]
            if missing:
                errors.append(f"{name} interaction contract missing {contract}: {missing}")
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

    for marker in BRIEFING_VISUAL_PRIMITIVES:
        if marker not in template:
            errors.append(f"Briefing missing visual or interaction primitive: {marker}")

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
    customization = (ROOT / "docs/customization.md").read_text(encoding="utf-8")
    for marker in [
        "Briefing suppresses decorative cover pulses",
        "Showcase permits only the bounded narrative-page effects",
        "Showcase may use its documented gradient text",
    ]:
        if marker not in customization:
            errors.append(f"customization guide missing template-specific visual boundary: {marker}")

    for name, source in templates.items():
        if len(source.splitlines()) < 400:
            errors.append(f"{name} is unexpectedly compressed; keep public source formatted and reviewable")
        if "“" in source or "”" in source:
            errors.append(f"{name} contains a displayed typographic quotation; use an explicit placeholder or sourced quote")

    shell = (ROOT / "scripts/new-project.sh").read_text(encoding="utf-8")
    python_script = (ROOT / "scripts/new-project.py").read_text(encoding="utf-8")
    readme_zh = (ROOT / "README.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.en.md").read_text(encoding="utf-8")
    pages = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    trademarks = (ROOT / "TRADEMARKS.md").read_text(encoding="utf-8")

    if 'exec python3 "$SCRIPT_DIR/new-project.py" "$@"' not in shell:
        errors.append("shell generator must remain a thin Python wrapper")
    if "Path(__file__).resolve()" not in python_script or "third-party" not in python_script:
        errors.append("Python generator portability marker missing")
    for marker in [
        '"briefing": ("template.html", "ZXcharT Briefing")',
        '"showcase": ("templates/showcase.html", "ZXcharT Showcase")',
        'Usage: scripts/new-project.py [--template briefing|showcase]',
        "return 64",
        "return 66",
        "return 73",
    ]:
        if marker not in python_script:
            errors.append(f"Python generator contract marker missing: {marker}")

    generator_namespace: dict[str, object] = {"__name__": "checker_import"}
    with contextlib.redirect_stderr(io.StringIO()):
        exec(compile(python_script, "scripts/new-project.py", "exec"), generator_namespace)
        parse_args = generator_namespace["parse_args"]
        cli_cases = {
            ("demo",): ("briefing", "demo"),
            ("--template", "briefing", "demo"): ("briefing", "demo"),
            ("--template", "showcase", "demo"): ("showcase", "demo"),
            ("--template", "unknown", "demo"): None,
            ("--template",): None,
        }
        for args, expected in cli_cases.items():
            actual = parse_args(list(args))
            if actual != expected:
                errors.append(f"generator CLI parse mismatch for {args}: {actual}")
    if 'sh scripts/new-project.sh "my-deck"' not in readme:
        errors.append("README must invoke the POSIX generator through sh")
    for marker in [
        "ZXcharT Briefing",
        "ZXcharT Showcase",
        'sh scripts/new-project.sh --template showcase "my-showcase"',
        'py scripts/new-project.py --template showcase "my-showcase"',
    ]:
        if marker not in readme or marker not in readme_zh:
            errors.append(f"bilingual README missing dual-template marker: {marker}")
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
        "themes/showcase/design.md",
        "docs/layouts.md",
        "docs/customization.md",
        "template.html",
        "templates/showcase.html",
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
        f"{len(REQUIRED)} required files, 2 templates × {len(LAYOUTS)} ordered layouts, "
        f"{len(PUBLIC_RUNTIME_MARKERS)} public runtime markers, "
        f"{len(BRIEFING_VISUAL_PRIMITIVES)} Briefing visual/interaction primitives, "
        "full-repository privacy scan, portable generators, manual-only Pages, and license boundaries passed."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
