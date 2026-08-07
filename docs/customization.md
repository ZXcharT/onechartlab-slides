# Customization

## Choose the template before customizing

ZXcharT Briefing is the default at `template.html`; ZXcharT Showcase is available at `templates/showcase.html`. Choose by communication job before editing tokens. Briefing rules live in `themes/zxchart/design.md`; Showcase rules live in `themes/showcase/design.md`. Do not blend both visual systems inside one deck unless the user explicitly asks for a new art direction.

## Tokens

A copied deck exposes its visual system in `:root`: `--bg`, `--bg-surface`, `--bg-elevated`, `--accent`, `--accent-rgb`, `--accent-light`, `--accent-soft`, `--accent-subtle`, `--accent-border`, `--red`, `--text`, `--text-secondary`, `--text-muted`, `--border`, `--border-strong`, `--control-border`, `--positive`, `--motion-*`, and `--ease-*`. Change tokens rather than scattering inline colors or timing values.

## Type and evidence

The seed remotely references Space Grotesk, Inter, and Noto Sans SC through Google Fonts. The deck remains usable when offline because its font stacks include system fallbacks. This repository distributes no font files.

Give each page one primary message. Keep the shared stage insets and alignment anchors unless a layout has a deliberate full-bleed reason; do not add arbitrary per-layout max-width caps that leave unused wide-screen space. In Briefing, use `evidence-rail` as a text label only when it identifies sequence, unit, source, or interpretive context; do not add a short line or symbol merely to decorate it, and use plain type emphasis rather than gradient text. Showcase may use its documented gradient text and blurred light fields only on Cover, Hook, Statement, Outro, and Closing; keep them bounded and subordinate to readable content. See the selected template's design document for the exact boundary.

## Motion and interaction

Both templates share the same focus, keyboard, touch, overflow, and reduced-motion contract. Motion is reviewed effect by effect rather than removed as a category. The seed provides a shared presentation-focus contract: pointer preview changes only the current item and leaves peers untouched; click, Enter, or Space locks an item and may then dim peers; Escape, blank click, or slide navigation clears it. Do not replace the state-driven preview with group `:has(:hover)` dimming, hover-driven peer opacity, or continuous `mousemove` opacity updates. Only one locked focus exists at a time, and no content is hidden. Bars retain entry feedback, Stack retains an authored click state, Timeline/Stack retain restrained pointer proximity, and Outro retains an optional focus shift. Briefing suppresses decorative cover pulses, blurred orbs, gradient flow, and rings. Showcase permits only the bounded narrative-page effects listed in `themes/showcase/design.md`; they remain decorative, `aria-hidden`, and subordinate to content. In both templates, `prefers-reduced-motion: reduce` preserves color/opacity acknowledgement while removing displacement and animation. Non-current slides are made `aria-hidden` and inert by the navigation script. Keep focusable presentation items keyboard-operable with visible focus.

## Content rules

Replace every placeholder, retain only selected slides, and cite non-obvious facts. Do not add images, logos, screenshots, or quotations unless their source and redistribution status are known. On narrow screens, reflow or permit controlled vertical reading; never silently crop body copy.
