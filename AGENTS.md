# Agent SOP

## Boundary

Work only in the repository-relative `projects/` directory or in a path supplied by the user. Keep `template.html` as the layout source of truth. Do not assume a local machine path, a fixed agent identity, a private service, or a platform-specific application.

## Layout inventory

`layout-cover`, `layout-agenda`, `layout-metrics`, `layout-dashboard`, `layout-split`, `layout-bars`, `layout-quote`, `layout-timeline`, `layout-detail`, `layout-stack`, `layout-compare`, `layout-timeline-3col`, `layout-hook`, `layout-statement`, `layout-outro`, `layout-closing`.

## SOP

1. **Align requirements**: audience, purpose, medium, page range, source material, brand constraints, and accessibility needs.
2. **Plan content**: make a page list and map each page to one of the 16 classes listed in `docs/layouts.md`. Flag unsupported claims and missing assets.
3. **Confirm the outline**: obtain confirmation for meaningful structural choices before producing a polished deck.
4. **Generate**: run a generator or copy `template.html` into the selected output folder. Delete unused sample slides and replace all placeholders.
5. **Preview**: test arrows, space, Home/End, buttons, touch, viewport resizing, and reduced-motion settings.
6. **Iterate**: edit `:root` CSS variables for theme changes; maintain source attribution and visual contrast.
7. **Review independently**: separate the execution role from a verification role. The verifier checks slide count, facts, source links, accessibility, and that the output meets the agreed brief.
8. **Close out**: report output path, inputs used, validations performed, and unresolved risks.

## Data → Skill → Agent

Treat data as attributable inputs, a skill as a declared transformation method, and an agent as an executor with a review trail. Each layer should be replaceable without requiring a particular vendor or personal environment.
