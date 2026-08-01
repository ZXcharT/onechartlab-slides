# OneChartLab Slides

OneChartLab Slides v0.1.0 is an agent-friendly HTML presentation system and an independent project in the OneChartLab open-source ecosystem by ZXcharT. It provides a portable, single-file slide seed with the ZXcharT visual theme; it is not the OneChartLab brand hub or website source tree.

## Features

- 16 audited layout classes in one editable HTML file
- Dark ZXcharT theme with gold emphasis and responsive layouts
- Keyboard, touch, and button navigation
- Click-to-focus cards and animated bars, with `prefers-reduced-motion` support
- POSIX shell and Python 3 standard-library project generators
- Generic agent workflow example and a platform adaptation guide

## Layouts

`layout-cover`, `layout-agenda`, `layout-metrics`, `layout-dashboard`, `layout-split`, `layout-bars`, `layout-quote`, `layout-timeline`, `layout-detail`, `layout-stack`, `layout-compare`, `layout-timeline-3col`, `layout-hook`, `layout-statement`, `layout-outro`, and `layout-closing`.

See [docs/layouts.md](docs/layouts.md) for intended use and constraints.

## Quick start

### macOS / Linux

```sh
sh scripts/new-project.sh "my-deck"
# Then open projects/my-deck/index.html in a modern browser.
```

### Windows

```powershell
py scripts/new-project.py "my-deck"
# Then open projects\my-deck\index.html in any modern browser.
```

Python is optional on macOS/Linux when using the shell script. Both generators locate the repository from their own path and create output beneath `projects/` by default.

## AI agent use

Give an agent the repository root (or a user-selected output directory), a brief, source material, and the needed slide sequence. Ask it to:

1. align on audience, objective, and constraints;
2. plan content against the 16 layouts;
3. obtain confirmation for the outline when appropriate;
4. generate a copy of `template.html`;
5. preview and verify claims, links, and readability;
6. iterate and record unresolved questions.

Read [AGENTS.md](AGENTS.md) and [SKILL.md](SKILL.md) for the portable SOP. The agent workflow example deliberately separates an execution role from an independent verification role.

## Online demo / GitHub Pages

`index.html` is a lightweight gallery entrypoint that embeds the neutral seed. A manual-only Pages workflow is included at `.github/workflows/pages.yml`. It runs only when the repository owner explicitly selects **Run workflow**; cloning or pushing the repository does not deploy anything automatically. The intended project URL is `https://zxchart.github.io/onechartlab-slides/`; this repository does not claim `onechart.top` or `onechartlab.com`.

## Theme customization

Change CSS custom properties in `:root` inside a copied deck. Keep semantic colors as variables, retain adequate contrast, and test with motion reduced. [docs/customization.md](docs/customization.md) describes the token surface and font behavior.

## Target browsers

The design targets current Chrome, Edge, Firefox, and Safari, but v0.1.0 has not yet completed a formal four-browser compatibility matrix. JavaScript enables navigation and optional interactions; the slide markup remains inspectable without it. Google Fonts are network references only, with system fallbacks when they are unavailable.

## Directory structure

```text
.
├── template.html                 neutral seed and layout source of truth
├── index.html                    gallery entrypoint
├── themes/zxchart/design.md      design tokens and layout inventory
├── docs/                         layouts, customization, platform notes
├── examples/agent-workflow/      generic workflow example
├── scripts/                      portable generators and repository checker
├── projects/.gitkeep             local generated-output placeholder
└── assets/.gitkeep               intentionally empty preview-assets area
```

## Credits

The template basis is [beautiful-html-templates](https://github.com/zarazhangrui/beautiful-html-templates) by Zara Zhang, under MIT. [frontend-slides](https://github.com/zarazhangrui/frontend-slides) and [html-presentation](https://github.com/juanjuanjie/html-presentation) informed workflow and presentation methods. Details are in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and [SOURCES.md](SOURCES.md).

## License and trademarks

Code, documentation, and generic demos are [MIT licensed](LICENSE). The OneChartLab, OneChartLab Slides, and ZXcharT names and logos are reserved; see [TRADEMARKS.md](TRADEMARKS.md).
