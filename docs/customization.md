# Customization

## Tokens

A copied deck exposes its visual system in `:root`: `--bg`, `--bg-surface`, `--bg-elevated`, `--accent`, `--accent-rgb`, `--accent-light`, `--accent-soft`, `--accent-subtle`, `--accent-border`, `--red`, `--text`, `--text-secondary`, `--text-muted`, `--border`, `--border-strong`, `--control-border`, `--positive`, `--motion-*`, and `--ease-*`. Change tokens rather than scattering inline colors or timing values.

## Type and evidence

The seed remotely references Space Grotesk, Inter, and Noto Sans SC through Google Fonts. The deck remains usable when offline because its font stacks include system fallbacks. This repository distributes no font files.

Give each page one primary message. Keep the shared stage insets and alignment anchors unless a layout has a deliberate full-bleed reason; do not add arbitrary per-layout max-width caps that leave unused wide-screen space. Use `evidence-rail` as a text label only when it identifies sequence, unit, source, or interpretive context. Do not add a short line or other symbol merely to decorate it. Use plain type emphasis rather than gradient text, and avoid large gradients because they can band in recordings.

## Motion and interaction

Motion is reviewed effect by effect rather than removed as a category. The seed provides a shared presentation-focus contract: pointer preview changes only the current item and leaves peers untouched; click, Enter, or Space locks an item and may then dim peers; Escape, blank click, or slide navigation clears it. Do not replace the state-driven preview with group `:has(:hover)` dimming, hover-driven peer opacity, or continuous `mousemove` opacity updates. Only one locked focus exists at a time, and no content is hidden. Bars retain entry feedback, Stack retains an authored click state, Timeline/Stack retain restrained pointer proximity, and Outro retains an optional focus shift. Decorative cover pulses, blurred orbs, gradient flow, and rings are suppressed. `prefers-reduced-motion: reduce` preserves color/opacity acknowledgement while removing displacement and animation. Non-current slides are made `aria-hidden` and inert by the navigation script. Keep focusable presentation items keyboard-operable with visible focus.

## Content rules

Replace every placeholder, retain only selected slides, and cite non-obvious facts. Do not add images, logos, screenshots, or quotations unless their source and redistribution status are known. On narrow screens, reflow or permit controlled vertical reading; never silently crop body copy.
