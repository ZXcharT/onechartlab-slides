# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

People and AI agents creating browser-ready slide decks for research, reporting, explanation, product communication, and other presentation work. Viewers may open the result on different screen shapes and playback platforms.

## Product Purpose

OneChartLab Slides is an HTML presentation / slide-deck Agent Skill. Its first duty is to present content clearly, make the most important point unmistakable, and support that point with legible evidence while conveying visual quality.

## Positioning

It combines portable single-file HTML decks, reusable presentation layouts, and an Agent workflow that keeps content hierarchy, source attribution, and visual consistency explicit.

## Template Families

- **ZXcharT Briefing** is the default template at `template.html`. It serves research, strategy, data analysis, reporting, and decision communication through matte editorial hierarchy and restrained presenter focus.
- **ZXcharT Showcase** is the optional template at `templates/showcase.html`. It serves launches, proposals, keynotes, and narrative stage work through cinematic pacing, modular cards, and bounded decorative motion.

Both templates expose the same 16 layout classes and the same URL, embed, navigation, accessibility, touch, Compare, focus, overflow, and reduced-motion contracts. The choice is a communication decision, not a quality tier or version number.

## Operating Context

Decks are generated or adapted from source material, previewed in a modern browser, and presented or reviewed on varied screen sizes. Screen recording is one possible use, not the product's defining workflow.

## Capabilities and Constraints

- Playback is not restricted to one platform; layouts should adapt across common screen shapes.
- A deck must not become cluttered, unfocused, or more decorative than informative.
- Motion must never be required to understand the content; reduced-motion rendering remains complete.
- The output remains a browser-ready, portable HTML presentation with no local build or runtime dependency; remote fonts fall back to system fonts when offline.
- If no template is requested, use ZXcharT Briefing.

## Brand Commitments

- Preserve the OneChartLab Slides and ZXcharT names and the established deep blue-gray field with restrained gold emphasis.
- Briefing avoids large-area gradients and glow; Showcase permits bounded gradients and light fields only on statement-led slides.
- Review and improve existing motion: keep useful, restrained details; remove effects that distract, create recording defects, or have no practical purpose.

## Evidence on Hand

- Existing 16-layout HTML template and live gallery in this repository.
- A synthetic pressure deck used only to verify long Chinese copy, dense comparisons, long numbers, dates, source notes, and adaptive behavior. It must not be presented as real business evidence.

## Product Principles

1. Content hierarchy before decoration.
2. One unmistakable primary message per slide, with supporting evidence clearly subordinate.
3. Adaptive presentation without silently clipping body content.
4. Visual quality through typography, proportion, spacing, alignment, and deliberate motion.
5. Attributable claims and explicit limits.

## Accessibility & Inclusion

Keyboard, touch, visible controls, readable contrast, semantic hidden-slide state, and reduced-motion support are durable requirements.
