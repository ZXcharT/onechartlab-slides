# HanaAgent installation and use

OneChartLab Slides can be installed directly from its public GitHub repository because `SKILL.md` is located at the repository root and all required resources are bundled with it.

## Recommended installation

Ask HanaAgent to install the complete repository as a Skill:

```text
请安装这个 Skill：https://github.com/ZXcharT/onechartlab-slides
```

You can also select the repository or a correctly structured ZIP through the platform's Skill installer. Keep the complete `onechartlab-slides/` folder intact; installing only `SKILL.md` will omit the template and design references.

## Manual local installation

If a manual local installation is preferred, place the complete folder at:

```text
$HOME/.hanako/skills/onechartlab-slides/
```

The resulting path must contain:

```text
$HOME/.hanako/skills/onechartlab-slides/SKILL.md
```

## First use

Start a new task and ask for the desired outcome in natural language:

```text
请使用 OneChartLab Slides，把这份材料制作成一份 HTML 演示文稿。
先给我页面大纲，确认后再生成文件。
```

When the Skill triggers, the Agent should follow `SKILL.md`, then load `AGENTS.md`, `themes/zxchart/design.md`, and the relevant layout documentation before generating the deck.
