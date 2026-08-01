# Customization

## Tokens

A copied deck exposes its visual system in `:root`: `--bg`, `--bg-surface`, `--bg-elevated`, `--accent`, `--accent-rgb`, `--accent-light`, `--accent-soft`, `--accent-subtle`, `--accent-border`, `--red`, `--text`, `--text-secondary`, `--text-muted`, `--border`, `--border-strong`, and `--positive`. Change tokens rather than scattering inline colors.

## Type

The seed remotely references Space Grotesk, Inter, and Noto Sans SC through Google Fonts. The deck remains usable when offline because its font stacks include system fallbacks. This repository distributes no font files.

## Motion and interaction

Slides use a short transition, click-to-focus cards, bar reveals, cover light orbs and data streams, proximity effects, an outro focus state, and closing rings. The `prefers-reduced-motion: reduce` media query removes animation and scaling. Do not make essential meaning depend on motion or hover.

## Content rules

Replace every placeholder, retain only selected slides, and cite non-obvious facts. Do not add images, logos, screenshots, or quotations unless their source and redistribution status are known.
