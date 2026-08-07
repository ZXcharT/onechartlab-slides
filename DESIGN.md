# V2 Phase 1 design facts

## Visual world

- The deck retains a deep blue-gray field with restrained gold only for emphasis, sequence markers, and evidence rails.
- Large-area gradients and gradient text are absent. The cover uses a fine vertical evidence line and three small static data points instead of light-orb decoration.
- Quality comes from typography, asymmetry, spacing, fine rules, aligned data, and a conclusion → evidence → source reading order.

## Core layout rules

- Cover establishes title, scope, and authorship as a three-level reading order.
- Agenda is a weighted narrative list, not a card grid.
- Metrics and Dashboard establish one primary signal before supporting evidence.
- Split, Detail, and Compare expose reasoning through rails, annotations, and flat tables rather than rounded card piles.

## Adaptive and interaction facts

- Wide slides preserve a presentation composition; narrow slides reduce grids to a readable vertical flow and allow slide-local scrolling rather than clipping content.
- Non-current slides are `aria-hidden` and inert. Existing button, keyboard, and touch navigation remains available; buttons have visible focus.
- Motion remains optional: bar entry can animate, while `prefers-reduced-motion` disables animation and transitions. No information depends on motion.
