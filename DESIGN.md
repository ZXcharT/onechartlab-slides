# V2 Phase 1 design facts

## Visual world

- The deck uses an ink-like blue-black field (`#11131b`), warm paper-white text (`#f3f0e8`), and muted brass (`#d9a441`) for a matte research-briefing character.
- Gold is a signal, not a coating: section indexes and primary data may use it; tags, body copy, and broad surfaces do not.
- Large-area gradients, glow, blurred orbs, decorative rings, and gradient text are absent. Cover ornament is suppressed so typography and metadata carry the identity.
- Quality comes from explicit type roles, restrained contrast, aligned data, and a conclusion → evidence → source reading order. Short decorative rules are not a motif; lines are reserved for full structural divisions such as rows, columns, and tables.
- Informational muted text uses `#9695a0`, preserving at least WCAG AA contrast on base, surface, and elevated backgrounds.

## Stage and alignment

- Every core layout uses the same responsive stage insets: `--stage-inline`, `--stage-top`, and `--stage-bottom`.
- Core content spans the available stage width instead of stopping at unrelated 980–1120px caps.
- Titles, evidence rails, and primary content share common left and right anchors; wide-screen empty space must be intentional and assigned to a secondary evidence or metadata column.
- Core content bodies use viewport-relative minimum height on landscape screens and release that height on compact or narrow screens.

## Core layout rules

- Cover uses a two-column composition so title and metadata occupy the full stage instead of leaving an accidental empty right half.
- Agenda is a weighted narrative list, not a card grid.
- Metrics and Dashboard establish one primary signal before supporting evidence.
- Split, Detail, and Compare expose reasoning through rails, annotations, and flat structures rather than equal rounded-card piles.
- On narrow screens, Compare preserves readable column widths in a labelled horizontal region instead of crushing cells into unreadable columns.

## Adaptive rules

- Wide slides preserve a presentation composition.
- Narrow layouts reflow major grids and allow slide-local vertical reading rather than silently clipping body content.
- Dense comparison tables use a keyboard-focusable horizontal region with an explicit narrow-screen hint.
- Navigation controls retain a 44×44 CSS-pixel touch target.

## Typography roles

- Space Grotesk is explicit for headings and real numeric roles; Inter carries body, labels, and metadata; Noto Sans SC remains the multilingual fallback.
- Heading weights are declared rather than inherited from browser defaults.
- Primary metrics use 700; sequence numbers, percentages, times, and folios use 600 with lining tabular numerals.
- Header tags are visually quieter than gold section indexes. Evidence and source metadata use a protected 500 weight without becoming body copy.

## Motion and interaction

- Motion uses shared `--motion-*` and `--ease-*` tokens and is evaluated individually, not cleared wholesale.
- Bars retain a measured entry transition. Stack retains keyboard-accessible click focus; Timeline and Stack retain restrained proximity on fine pointers only; Outro retains its optional focus shift.
- Decorative cover pulses, blurred orbs, gradient timeline flow, and closing rings are suppressed.
- Escape clears temporary focus effects. No information depends on hover, focus animation, or motion.
- `prefers-reduced-motion` keeps the complete static presentation.

## Accessibility facts

- Non-current slides are `aria-hidden` and inert.
- Stack and Outro focus interactions expose button roles, keyboard activation, and `aria-pressed` state.
- Focus rings, selection, scrollbars, informational contrast, and touch targets use the theme system.
