# Contributing

Keep contributions portable, attributable, and small enough to review.

1. Discuss material scope or license changes before adding assets or dependencies.
2. Preserve both templates' shared 16-layout and public runtime contracts, or update every inventory document and `scripts/check_repo.py` together. Update the Briefing manifest digest only after explicit Briefing review.
3. Do not add personal paths, agent identifiers, credentials, private tooling assumptions, unsupported facts, or unclear third-party visual assets.
4. Run `python3 scripts/check_repo.py` and `sh -n scripts/new-project.sh`.
5. Test default, explicit Briefing, and Showcase generation through both CLI entry points in disposable project directories; confirm each output matches its selected source.

By contributing, you agree that your contribution may be distributed under the MIT license, subject to `TRADEMARKS.md`.
