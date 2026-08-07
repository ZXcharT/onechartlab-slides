# Customization

## Tokens

A copied deck exposes its visual system in `:root`: `--bg`, `--bg-surface`, `--bg-elevated`, `--accent`, `--accent-rgb`, `--accent-light`, `--accent-soft`, `--accent-subtle`, `--accent-border`, `--red`, `--text`, `--text-secondary`, `--text-muted`, `--border`, `--border-strong`, and `--positive`. Change tokens rather than scattering inline colors.

## Type and evidence

The seed remotely references Space Grotesk, Inter, and Noto Sans SC through Google Fonts. The deck remains usable when offline because its font stacks include system fallbacks. This repository distributes no font files.

Give each page one primary message. Use the fine `evidence-rail` only when it identifies sequence, unit, source, or interpretive context. Do not use it as decoration. Use plain type emphasis rather than gradient text, and avoid large gradients because they can band in recordings.

## Motion and interaction

Slides retain short transitions and bar reveals; none carry required meaning. The `prefers-reduced-motion: reduce` media query removes animation and scaling. Non-current slides are made `aria-hidden` and inert by the navigation script. Keep controls as real buttons or links, with visible keyboard focus.

## Content rules

Replace every placeholder, retain only selected slides, and cite non-obvious facts. Do not add images, logos, screenshots, or quotations unless their source and redistribution status are known. On narrow screens, reflow or permit controlled vertical reading; never silently crop body copy.
