# Project Policy

Effective date: 2026-06-29

This policy explains how SpoolmanDB Community handles data quality, privacy expectations, public contributions, and correction requests. It applies to the public repository, compiled JSON files, and GitHub Pages site.

## 1. Data scope

SpoolmanDB Community is intended to store public filament and material reference data, including manufacturer names, product names, material types, densities, temperatures, diameters, weights, spool types, color names, color hex values, SKU/EAN identifiers, and public SDS/TDS links.

The project is not intended to store personal data, private customer information, confidential manufacturer files, private pricing agreements, authentication tokens, or non-public business records.

## 2. Source and quality policy

Preferred sources include manufacturer product pages, product labels, datasheets, safety data sheets, technical data sheets, marketplace pages, and direct community verification.

Maintainers may ask contributors for source evidence when a change adds a new manufacturer, changes material properties, changes safety-relevant fields, or updates identifiers such as SKUs and EANs.

The project favors reviewable source files in `filaments/` and `materials.json`. Generated files should be produced by the compiler and should not be hand-edited unless maintainers explicitly request it.

## 3. Privacy policy

The static GitHub Pages site does not intentionally set project-owned cookies, require accounts, collect form submissions, or run project-owned analytics.

GitHub may process technical information for repository hosting, Pages delivery, Actions, issues, pull requests, security, and abuse prevention. GitHub-hosted interactions are governed by GitHub's own privacy statement and platform terms:

- [GitHub General Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement)
- [GitHub Terms of Service](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service)

If you open an issue, submit a pull request, comment, review, or commit, the information you provide is public on GitHub and may include your GitHub username, profile link, commit metadata, message text, and any files or screenshots you upload.

## 4. Contribution moderation

Maintainers may close, edit, request changes to, or remove contributions that:

- fail schema validation;
- lack reasonable source evidence for important changes;
- include personal, confidential, or unsafe information;
- introduce unrelated formatting churn;
- duplicate existing entries without a clear reason;
- contain abusive, misleading, spammy, or off-topic content.

Repeated disruptive behavior may result in blocked participation through GitHub moderation tools.

## 5. Correction and removal requests

If you believe data is inaccurate, outdated, improperly sourced, trademark-sensitive, or should be removed, open an issue with:

- the affected manufacturer, product, material, color, or file path;
- the current value;
- the requested correction or removal;
- supporting source links or evidence when available.

Maintainers will review requests in good faith, but the project may retain public factual references when they are useful, source-backed, and lawful.

## 6. Safety and technical data

Temperatures, densities, material classifications, SDS/TDS links, color values, and spool metadata are best-effort reference data. They are not safety instructions, compliance documents, or manufacturer warranties.

Always follow manufacturer documentation, product labels, printer vendor guidance, and local safety requirements when handling, storing, printing, or disposing of filament.

## 7. Policy updates

This policy may be updated as the project changes. Material updates should be committed to the repository so contributors can review the history.
