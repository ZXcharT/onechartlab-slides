# V2 Phase 1 design facts

## Visual world

- The deck retains a deep blue-gray field with restrained gold for emphasis, sequence markers, and evidence rails.
- Large-area gradients and gradient text are absent from the seven Phase 1 layouts. The cover uses a fine vertical evidence line and a small local data pulse instead of light-orb decoration.
- Quality comes from typography, asymmetry, spacing, fine rules, aligned data, and a conclusion → evidence → source reading order.
- Informational muted text uses `#88889c`, which remains readable on both the base and surface backgrounds.

## Core layout rules

- Cover establishes title, scope, and authorship as a three-level reading order.
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
