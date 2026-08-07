---
name: onechartlab-slides
description: >-
  Create, adapt, and review browser-ready HTML slide decks with the OneChartLab Slides layout system and the ZXcharT Briefing or ZXcharT Showcase template. Use when a user asks for HTML slides, a browser presentation, a deck, report-to-slides conversion, video storyboard, 演示文稿, 幻灯片, PPT, 视频分镜, HTML Slides, or a ZXcharT presentation and accepts HTML output. If the user explicitly requires a .pptx file, clarify that this skill produces HTML presentations.
license: MIT. See LICENSE.
compatibility: Requires an AI agent with local file read/write access. Browser preview is recommended. Python 3 is optional.
---

# OneChartLab Slides

Use this skill to turn source material and a production brief into a coherent HTML presentation. The user works through natural-language instructions; HTML is the delivery format.

## Load the bundled guidance

Before planning or generating a deck:

1. Read `AGENTS.md` for the production and review workflow.
2. Read `themes/zxchart/design.md` for the default ZXcharT Briefing rules and `themes/showcase/design.md` for the optional ZXcharT Showcase rules.
3. Read `docs/layouts.md` while choosing a template and mapping content to layouts.
4. Read `docs/customization.md` only when changing theme tokens, fonts, or component styling.
5. Treat `template.html` as the read-only source template. Copy it into the output project before editing.

Do not rely on the README as execution instructions. The files above are the Skill's operational source of truth.

## Collect the brief

Establish these inputs before generation:

- topic and purpose;
- audience and delivery medium;
- approximate slide count;
- source material and citation expectations;
- language, tone, and brand constraints;
- template preference: Briefing for research/strategy/data/decisions, Showcase for launches/proposals/keynotes/narrative stage work; default to Briefing;
- user-selected output directory, if any.

Ask related clarification questions together. Do not make the user learn layout identifiers or HTML.

## Workflow

1. **Align** — confirm the brief, evidence boundary, and desired output.
2. **Choose** — select ZXcharT Briefing unless the brief clearly calls for Showcase or the user chooses it.
3. **Plan** — create a page-by-page outline and map each page to a layout from `docs/layouts.md`.
4. **Confirm** — obtain approval before implementing a substantive outline.
5. **Generate** — copy the selected source (`template.html` for Briefing or `templates/showcase.html` for Showcase), remove unused sample slides, and replace every placeholder.
6. **Preview** — open the generated HTML and test navigation, focus interaction, overflow, responsive sizing, Compare scrolling, contrast, citations, and reduced-motion behavior.
7. **Iterate** — revise content and layout; follow the selected design document and change theme tokens before component CSS.
8. **Review** — verify template choice, slide count, claims, source links, layout fit, and unresolved gaps.
9. **Deliver** — report the selected template, output path, inputs used, checks performed, and any remaining limitations.

## Output rules

- Write only inside the user-selected output directory or the repository-relative `projects/` directory.
- Never modify `template.html` or `templates/showcase.html` while producing an individual deck.
- Produce a browser-ready `index.html` unless the user requests another HTML filename.
- Preserve keyboard, touch, and button navigation.
- Keep factual claims attributable. Include source, period, unit, and method where relevant.
- Do not invent statistics, quotations, images, testimonials, or source links.
- Do not assume a private agent identity, personal filesystem path, private service, or platform-specific tool.
- If the requested output must be `.pptx`, explain the format mismatch before proceeding or route to an appropriate PowerPoint workflow.

## Optional project generators

An agent may create a clean project copy with either command. Briefing is the default:

```sh
sh scripts/new-project.sh "my-deck"
sh scripts/new-project.sh --template showcase "my-showcase"
```

```powershell
py scripts/new-project.py "my-deck"
py scripts/new-project.py --template showcase "my-showcase"
```

The only supported explicit values are `briefing` and `showcase`. Every command creates `projects/<name>/index.html`. The generator does not upload files, contact an AI service, or modify either source template.

## Layout inventory

`layout-cover`, `layout-agenda`, `layout-metrics`, `layout-dashboard`, `layout-split`, `layout-bars`, `layout-quote`, `layout-timeline`, `layout-detail`, `layout-stack`, `layout-compare`, `layout-timeline-3col`, `layout-hook`, `layout-statement`, `layout-outro`, `layout-closing`.
