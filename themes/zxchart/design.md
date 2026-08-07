# ZXcharT design system

## Intent

The ZXcharT theme uses an ink-like blue-black field, warm paper-white typography, and muted brass emphasis. Its character is a matte research briefing: precise, editorial, and quiet enough for evidence to remain primary. It is the default visual theme of OneChartLab Slides, an independent project in the OneChartLab ecosystem, and does not require any platform or personal workflow.

## Tokens

```css
--bg: #11131b;
--bg-surface: #181b25;
--bg-elevated: #202430;
--accent: #d9a441;
--accent-rgb: 217,164,65;
--accent-light: #edc974;
--accent-soft: rgba(217,164,65,.12);
--accent-subtle: rgba(217,164,65,.055);
--accent-border: rgba(217,164,65,.28);
--red: #e66b60;
--text: #f3f0e8;
--text-secondary: #b7b5b9;
--text-muted: #9695a0;
--border: rgba(243,240,232,.09);
--border-strong: rgba(243,240,232,.17);
--control-border: rgba(243,240,232,.35);
--positive: #3cc59e;
--motion-fast: 160ms;
--motion-base: 360ms;
--motion-slow: 720ms;
--ease-out: cubic-bezier(.22,1,.36,1);
--ease-soft: cubic-bezier(.2,.8,.2,1);
```

Use `--accent` for emphasis and meaningful sequence marks—not body copy, broad surfaces, or isolated decorative rules. Reserve `--red` and `--positive` for semantic negative and positive states. Preserve readable contrast after customization.

## Typography, spacing, and surfaces

- Headings and real numeric roles: Space Grotesk with Inter and Noto Sans SC fallback; body, labels, and metadata: Inter with Noto Sans SC fallback.
- Heading weights are explicit. Primary metrics use weight 700; sequence numbers, percentages, times, and folios use weight 600 with lining tabular numerals.
- Gold section indexes outrank quiet neutral tags. Metadata uses weight 500 to survive projection and compression without competing with body copy.
- The remote font reference is optional at runtime; system fallbacks remain usable offline.
- All core layouts share responsive stage insets through `--stage-inline`, `--stage-top`, and `--stage-bottom`; compact heights reduce them without hiding content.
- Core bodies use the full available stage width rather than unrelated fixed content caps. Titles, evidence rails, and content share common anchors.
- Body text uses responsive sizing. A page has one primary message, then evidence, then source or limitation.
- Do not use large-area gradients, gradient text, decorative glass, all-equal card arrays, or isolated short rules. Lines are reserved for structural divisions; evidence labels should communicate through text and alignment.

## Interaction and accessibility

Keyboard, touch, and visible controls navigate slides. Non-current slides are `aria-hidden` and inert, so hidden content cannot receive focus. Focus-visible rings, selection, scrollbars, and control borders follow the theme. Motion uses shared duration and easing tokens. In evidence groups, pointer preview is held as explicit state across internal gaps, so movement never flashes the whole group; click/Enter/Space locks one item, and Escape, blank click, or slide navigation clears it. Preview and lock use a 220ms matte color/opacity transition without a tight content border. Only one locked focus exists at a time. Rows may shift horizontally by at most 6px and cards vertically by at most 3px. Stack and Outro retain their authored click states, while Timeline and Stack keep restrained pointer proximity. Decorative pulses, glow, gradient flow, and rings remain suppressed. None carries required meaning; `prefers-reduced-motion: reduce` preserves color and opacity feedback while removing displacement and animation.

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
