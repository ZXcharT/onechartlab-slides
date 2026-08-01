# HanaAgent adaptation

OneChartLab Slides can be used from HanaAgent as an optional platform adaptation; it has no HanaAgent runtime dependency.

1. Put the repository in a user-selected workspace or attach it to the task.
2. Ask the agent to read `SKILL.md`, `AGENTS.md`, `docs/layouts.md`, and `themes/zxchart/design.md` before drafting.
3. Provide an output folder, brief, and source material. The agent should make a layout plan, seek confirmation where appropriate, then create a copy of `template.html`.
4. Ask a separate verification pass to test the deck and check claims against the supplied sources.

If installing as a local skill is desired, a portable optional location is `$HOME/.hanako/skills/onechartlab-slides/`. Installation is not required to use the repository. Use the platform UI or your normal file workflow to preview the generated HTML in a browser.
