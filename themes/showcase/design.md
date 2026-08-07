# ZXcharT Showcase design system

## Purpose

ZXcharT Showcase is the presentation-led companion to the default ZXcharT Briefing template. Use it for launches, proposals, keynotes, narrative product stories, and other situations where pacing and stage presence matter alongside content clarity.

It is not the legacy template. It keeps the more cinematic visual direction while using the current OneChartLab Slides runtime, accessibility, adaptive, and interaction contracts.

## Visual language

- Base field: deep blue-gray `#171824` with warm gold `#f0b93c`.
- Typography: Space Grotesk for display and data, Inter for body, Noto Sans SC fallback.
- Card surfaces are allowed for Agenda, Metrics, Dashboard, Detail, and Stack because Showcase uses staged modules rather than Briefing's flat editorial rails.
- Gradient text and blurred light fields are allowed only on Cover, Hook, Statement, Outro, and Closing. Data and evidence pages must remain flat and readable.
- Decorative short rules, ambiguous em-dash metric placeholders, unsourced images, logos, screenshots, and quotations are prohibited.
- No effect may obscure the primary message, create required meaning, or reduce text contrast below WCAG AA.

## Hierarchy

- Every slide has one dominant statement or metric.
- Cards do not imply equal importance by default; a presenter may preview one item and lock one item to make hierarchy explicit.
- Gold is used for the focal title, metric, sequence, or active state—not for body copy.
- Source, period, unit, limitation, and ownership remain visible when factual content is inserted.

## Motion and interaction

- Pointer preview changes only the current item; peers remain unchanged until click/keyboard lock.
- Click, Enter, or Space locks one item and dims peers. Escape, blank click, second activation, or slide navigation clears it.
- Cover light fields, data drift, timeline flow, bar reveal, statement cursor, and closing rings may animate slowly. They are decorative, bounded, and removed by `prefers-reduced-motion`.
- Routine feedback uses shared motion tokens; no bounce, elastic motion, continuous proximity opacity, or hover-driven peer flicker.

## Adaptive and overflow rules

- Desktop slides may use the 2×3 Agenda, three-card Metrics, six-cell Dashboard, and two-column Detail structures.
- At `max-width: 780px`, major grids reflow to one column and the slide becomes a controlled vertical reading surface.
- Body content must never be silently clipped. Slide-local scrolling is allowed when content exceeds the viewport.
- Compare preserves a readable `720px` table and exposes a labelled horizontal scroll region on narrow screens; swiping that region must not change slides.
- Navigation controls retain a 44×44 CSS-pixel target.

## Layout minimums

| Layout | Showcase requirement |
|---|---|
| `layout-cover` | Dominant title, scope, metadata; bounded cinematic field |
| `layout-agenda` | Six staged modules with visible sequence |
| `layout-metrics` | Three labelled measures with unit/source placeholders |
| `layout-dashboard` | Six compact status cells with readable context |
| `layout-split` | Evidence and synthesis remain visually distinct |
| `layout-bars` | Labels, values, unit, and source remain explicit |
| `layout-quote` | Verified attribution or an explicit quotation placeholder |
| `layout-timeline` | Four ordered steps; line is structural |
| `layout-detail` | Four independently reviewable blocks |
| `layout-stack` | Four layered dependencies with keyboard focus |
| `layout-compare` | Four criteria columns in a controlled horizontal region |
| `layout-timeline-3col` | State, step, and action stay aligned |
| `layout-hook` | One concrete question; decorative field remains subordinate |
| `layout-statement` | One concise thesis; cursor is decorative |
| `layout-outro` | One conclusion plus optional presenter focus state |
| `layout-closing` | Clear end state without hidden required content |

## Runtime contract

Showcase must retain the same 16 layout classes and the shared URL, embed, navigation, hidden-slide, keyboard, touch, Compare isolation, stable pointer preview, click lock, Escape clear, and reduced-motion semantics as Briefing. Visual differences do not permit runtime or accessibility regressions.
