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
--text-muted: #646478;
--border: rgba(255,255,255,.07);
--border-strong: rgba(255,255,255,.12);
--positive: #00b894;
```

Use `--accent` for emphasis, not for body copy. Reserve `--red` and `--positive` for semantic negative and positive states. Preserve readable contrast after customization.

## Typography and spacing

- Headings and numeric emphasis: Space Grotesk with Noto Sans SC fallback.
- Body: Inter with Noto Sans SC fallback.
- The remote font reference is optional at runtime; system fallbacks remain usable offline.
- Slide padding: `5.5vw 7vw 8vh`; cover left padding: `16vw` on wide screens.
- Body text uses responsive sizing and a 1.75 line height.

## Interaction and accessibility

Keyboard, touch, and visible controls navigate slides. Cards can be focused by click. The cover includes animated light orbs and a data stream; bars reveal on entry; timeline and stack items respond to pointer proximity; the outro supports a focused closing line; and the closing page retains decorative rings. Motion is optional: the seed honors `prefers-reduced-motion: reduce` by removing animation and scaling. Do not encode essential information solely in color, hover, or motion.

## Audited layout inventory (16)

| Class | Purpose |
|---|---|
| `layout-cover` | Cover |
| `layout-agenda` | Agenda grid |
| `layout-metrics` | Three metric cards |
| `layout-dashboard` | Six-cell dashboard |
| `layout-split` | Two-column argument |
| `layout-bars` | Bar ranking |
| `layout-quote` | Attributable quote |
| `layout-timeline` | Four-step timeline |
| `layout-detail` | Detail cards |
| `layout-stack` | Layered model |
| `layout-compare` | Comparison table |
| `layout-timeline-3col` | Three-column sequence |
| `layout-hook` | Framing prompt |
| `layout-statement` | Thesis statement |
| `layout-outro` | Conclusion |
| `layout-closing` | Closing slide |

The class count is deliberately tied to `template.html`; update this document, `README.md`, `SKILL.md`, `AGENTS.md`, `docs/layouts.md`, and the checker together if the inventory changes.
