# OneChartLab Slides

**English** | [简体中文](README.zh-CN.md)

OneChartLab Slides is an Agent Skill for creating browser-ready HTML presentations. It includes 16 reusable layouts and the dark ZXcharT visual theme for research reports, project updates, product introductions, data presentations, and video storyboards.

After installation, give the Agent a topic, source material, audience, and production requirements. The Agent will produce an editable presentation that runs in a modern browser.

## Features

- Plan a presentation from articles, reports, data, or an outline
- Present a page-by-page outline for approval before generation
- Select layouts for openings, agendas, data, comparisons, timelines, arguments, and closing pages
- Generate an HTML presentation with built-in styling and interactions
- Support keyboard, touch, and button navigation
- Support focused cards, animated bars, and reduced-motion settings
- Check overflow, readability, source links, and content completeness
- Manage colors, typography, and spacing through CSS variables

## Install the Skill

Install the complete `onechartlab-slides` folder. The template, design rules, layout reference, and scripts are all part of the Skill.

For ZIP uploaders, the archive should contain one top-level folder:

```text
onechartlab-slides/
└── SKILL.md
```

### HanaAgent

Ask HanaAgent to install the GitHub repository, or select the repository/ZIP in its Skill installer:

```text
Install this Skill: https://github.com/ZXcharT/onechartlab-slides
```

See [docs/platforms/hanaagent.md](docs/platforms/hanaagent.md) for manual installation.

### Claude

1. Enable **Code execution and file creation**.
2. Open **Customize → Skills**.
3. Select **Add/Create skill → Upload a skill**.
4. Upload a ZIP whose top-level folder is `onechartlab-slides/`.

### OpenAI Codex

Ask `$skill-installer` to install the GitHub repository, or place the complete folder at:

```text
~/.agents/skills/onechartlab-slides/
```

For a project-only installation, use:

```text
PROJECT_ROOT/.agents/skills/onechartlab-slides/
```

Restart Codex if the new Skill does not appear.

## Quick start

After installation, describe the task to the Agent:

```text
Use OneChartLab Slides to turn this quarterly business review into a
10-slide presentation for the management team. Focus on key metrics,
problems, and next steps. Show me the page-by-page outline before
creating the HTML.
```

Standard workflow:

1. The Agent confirms the topic, audience, slide count, sources, and output location.
2. The Agent creates a page-by-page outline and selects layouts.
3. The user approves the outline.
4. The Agent creates the HTML presentation and writes the content.
5. The Agent previews the result and checks layout, navigation, and interactions.
6. The Agent applies feedback and reports the output path.

Default output location:

```text
projects/project-name/index.html
```

## Requirements

- An AI Agent with local file read/write access
- Browser preview capability is recommended
- A current version of Chrome, Edge, Firefox, or Safari for playback
- Python 3 only when using the optional Python generator

## Layout system

- **Open and close:** `layout-cover`, `layout-outro`, `layout-closing`
- **Agenda and content structure:** `layout-agenda`, `layout-split`, `layout-detail`, `layout-stack`
- **Data and comparison:** `layout-metrics`, `layout-dashboard`, `layout-bars`, `layout-compare`
- **Narrative and argument:** `layout-quote`, `layout-timeline`, `layout-timeline-3col`, `layout-hook`, `layout-statement`

See [docs/layouts.md](docs/layouts.md) for detailed guidance.

## Key files

```text
.
├── SKILL.md                       Skill entrypoint and execution requirements
├── AGENTS.md                      production and review workflow
├── template.html                  presentation seed
├── index.html                     preview of the 16 layouts
├── themes/zxchart/design.md       visual rules and layout inventory
├── docs/                          layout, customization, and platform notes
├── examples/agent-workflow/       generic Agent workflow example
├── scripts/                       optional generators and repository checker
├── projects/                      default output directory
└── assets/                        project images and other media
```

## Optional: create a project from the command line

### macOS / Linux

```sh
sh scripts/new-project.sh "my-deck"
```

### Windows

```powershell
py scripts/new-project.py "my-deck"
```

Both commands create:

```text
projects/my-deck/index.html
```

## Credits

The template basis is [beautiful-html-templates](https://github.com/zarazhangrui/beautiful-html-templates) by Zara Zhang, under MIT. [frontend-slides](https://github.com/zarazhangrui/frontend-slides) and [html-presentation](https://github.com/juanjuanjie/html-presentation) informed workflow and presentation methods. Details are in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and [SOURCES.md](SOURCES.md).

## License and trademarks

Code, documentation, and generic demos are [MIT licensed](LICENSE). The OneChartLab, OneChartLab Slides, and ZXcharT names and logos are reserved; see [TRADEMARKS.md](TRADEMARKS.md).
