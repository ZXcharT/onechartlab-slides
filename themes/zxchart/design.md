# ZXcharT design system

## Intent

The ZXcharT theme uses a dark blue-gray base and restrained gold emphasis. It is the default visual theme of OneChartLab Slides, an independent project in the OneChartLab ecosystem, and does not require any platform or personal workflow.

## Tokens

```css
--bg: #171824;
--bg-surface: #1e2030;
--bg-elevated: #252838;
--accent: #f0b93c;
--accent-rgb: 240,185,60;
--accent-light: #f5cd6e;
--accent-soft: rgba(240,185,60,.14);
--accent-subtle: rgba(240,185,60,.06);
--accent-border: rgba(240,185,60,.22);
--red: #e3392a;
--text: #ededf5;
--text-secondary: #9898a8;
--text-muted: #88889c;
--border: rgba(255,255,255,.07);
--border-strong: rgba(255,255,255,.12);
--positive: #00b894;
```

Use `--accent` for emphasis, sequence marks, and fine evidence rails—not body copy or broad surfaces. Reserve `--red` and `--positive` for semantic negative and positive states. Preserve readable contrast after customization.

## Typography, spacing, and surfaces

- Headings and numeric emphasis: Space Grotesk with Noto Sans SC fallback; body: Inter with Noto Sans SC fallback.
- The remote font reference is optional at runtime; system fallbacks remain usable offline.
- All core layouts share responsive stage insets through `--stage-inline`, `--stage-top`, and `--stage-bottom`; compact heights reduce them without hiding content.
- Core bodies use the full available stage width rather than unrelated fixed content caps. Titles, evidence rails, and content share common anchors.
- Body text uses responsive sizing. A page has one primary message, then evidence, then source or limitation.
- Do not use large-area gradients, gradient text, decorative glass, or all-equal card arrays. Fine rules and annotation rails should encode a source, sequence, unit, or interpretation.

## Interaction and accessibility

Keyboard, touch, and visible controls navigate slides. Non-current slides are `aria-hidden` and inert, so hidden content cannot receive focus. Focus-visible rings, selection, and scrollbars follow the theme. Motion is reviewed effect by effect: the cover keeps a small local data pulse, bars reveal on entry, Stack retains keyboard-accessible focus, Timeline and Stack retain restrained pointer proximity, and Outro retains an optional focus shift. None carries required meaning; `prefers-reduced-motion: reduce` removes the motion.

## Audited layout inventory (16)

| Class | Purpose |
|---|---|
| `layout-cover` | Content-first cover |
| `layout-agenda` | Weighted narrative agenda |
| `layout-metrics` | Primary metric with supporting measures |
| `layout-dashboard` | Primary status with evidence |
| `layout-split` | Asymmetric evidence and conclusion |
| `layout-bars` | Bar ranking |
| `layout-quote` | Attributable quote |
| `layout-timeline` | Four-step timeline |
| `layout-detail` | Annotation rail |
| `layout-stack` | Layered model |
| `layout-compare` | Flat comparison table |
| `layout-timeline-3col` | Three-column sequence |
| `layout-hook` | Framing prompt |
| `layout-statement` | Thesis statement |
| `layout-outro` | Conclusion |
| `layout-closing` | Closing slide |

The class count is deliberately tied to `template.html`; update this document, `README.md`, `SKILL.md`, `AGENTS.md`, `docs/layouts.md`, and the checker together if the inventory changes.
