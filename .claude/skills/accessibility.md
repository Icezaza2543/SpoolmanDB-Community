# SpoolmanDB Accessibility (A11y) Reference

Guidelines for ensuring high accessibility compliance across all components.

## 1. Table Accessibility
- **Headers:** Define `<th scope="col">` and `<th scope="row">` structures to enable screen reader navigability.
- **Sort Indicators:** Use appropriate `aria-sort` attributes when columns are interactive.
- **Descriptions:** Use `aria-describedby` or captions describing the grid purpose to screen readers.

## 2. Keyboard Navigation & Focus
- **Filter controls:** Ensure all search and select components are accessible via standard tab loops.
- **Outline focus:** Preserve custom outlines (`outline: 2px solid var(--accent-gold)`) on interactive button hover states.
- **Active state focus:** Reset focus back to the target container when operations (like URL copying) complete successfully.

## 3. Screen Reader Alerts & Alternative Texts
- **Filtering:** Declare `aria-live="polite"` on results status logs to announce active count updates automatically.
- **Color Swatches:** Never rely solely on visual swatches. Always supply alternate text representing the specific color name alongside color circles to satisfy contrast requirements.
