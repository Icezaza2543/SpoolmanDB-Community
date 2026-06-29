# Accessibility Skill Reference

Accessibility (A11y) standards and implementation patterns for SpoolmanDB Community.

## 1. Keyboard Navigability
*   **Active Elements:** Ensure all interactive elements (`a`, `button`, `input`, `select`) are focusable.
*   **Focus Outline:** Never suppress outlines completely. Implement customized `:focus-visible` styles using amber or orange glow borders to preserve visual indicator positioning:
    ```css
    button:focus-visible {
        outline: 2px solid var(--orange);
        outline-offset: 2px;
    }
    ```

## 2. Screen Reader Compatibility (ARIA)
*   **Navigation:** Define clear `aria-label` or `aria-labelledby` roles on primary landmarks (e.g. `<header>`, `<nav>`, `<main>`, `<section>`).
*   **Status updates:** Declare `aria-live="polite"` on message elements (like loading alerts or filter status readouts) to notify assistive technologies upon text changes.

## 3. Contrast Ratios
*   Ensure a contrast ratio of at least 4.5:1 for body copy and 3:1 for large headers in both light and dark mode versions.
*   Validate swatches and badges with explicit fallback text representation, rather than relying strictly on color visualization alone.
