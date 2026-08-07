# V2 Phase 1 design facts

## Visual world

- The deck retains a deep blue-gray field with restrained gold for emphasis, sequence markers, and evidence rails.
- Large-area gradients and gradient text are absent from the seven Phase 1 layouts. The cover uses a fine vertical evidence line and a small local data pulse instead of light-orb decoration.
- Quality comes from typography, asymmetry, spacing, aligned data, and a conclusion → evidence → source reading order. Short decorative rules are not a motif; lines are reserved for full structural divisions such as rows, columns, and tables.
- Informational muted text uses `#88889c`, which remains readable on both the base and surface backgrounds.

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

## Motion and interaction

- Motion is evaluated individually, not cleared wholesale.
- The cover keeps a small local data pulse; bars retain entry animation.
- Stack retains keyboard-accessible click focus. Timeline and Stack retain restrained proximity on fine pointers only. Outro retains its optional focus shift.
- Escape clears temporary focus effects. No information depends on hover, focus animation, or motion.
- `prefers-reduced-motion` keeps the complete static presentation.

## Accessibility facts

- Non-current slides are `aria-hidden` and inert.
- Stack and Outro focus interactions expose button roles, keyboard activation, and `aria-pressed` state.
- Focus rings, selection, scrollbars, informational contrast, and touch targets use the theme system.
