# Agent SOP

## Boundary

Work only in the repository-relative `projects/` directory or in a path supplied by the user. Treat `template.html` as the default ZXcharT Briefing source and `templates/showcase.html` as the optional ZXcharT Showcase source. Never edit either source while producing an individual deck. Do not assume a local machine path, a fixed agent identity, a private service, or a platform-specific application.

## Layout inventory

`layout-cover`, `layout-agenda`, `layout-metrics`, `layout-dashboard`, `layout-split`, `layout-bars`, `layout-quote`, `layout-timeline`, `layout-detail`, `layout-stack`, `layout-compare`, `layout-timeline-3col`, `layout-hook`, `layout-statement`, `layout-outro`, `layout-closing`.

## SOP

1. **Align requirements**: audience, purpose, medium, page range, source material, brand constraints, accessibility needs, and template preference. Use Briefing when no preference is given.
2. **Choose the template**: Briefing for research/strategy/data/decisions; Showcase for launches/proposals/keynotes/narrative stage work. Do not call them old/new or V1/V2.
3. **Plan content**: make a page list and map each page to one of the 16 classes listed in `docs/layouts.md`. Flag unsupported claims and missing assets.
4. **Confirm the outline**: obtain confirmation for meaningful structural choices before producing a polished deck.
5. **Generate**: run the generator with the selected template or copy its source into the selected output folder. Delete unused sample slides and replace all placeholders.
6. **Preview**: test arrows, space, Home/End, buttons, focus lock, touch, Compare scrolling, viewport resizing, and reduced-motion settings.
7. **Iterate**: follow the selected template's design document and edit `:root` tokens before component CSS; maintain source attribution and contrast.
8. **Review independently**: separate the execution role from a verification role. The verifier checks template choice, slide count, facts, source links, accessibility, and the agreed brief.
9. **Close out**: report template name, output path, inputs used, validations performed, and unresolved risks.

## Data → Skill → Agent

Treat data as attributable inputs, a skill as a declared transformation method, and an agent as an executor with a review trail. Each layer should be replaceable without requiring a particular vendor or personal environment.
