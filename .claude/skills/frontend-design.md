# SpoolmanDB Frontend Design Reference

Guidelines for Layouts, Components, Grid Systems, and Visual Elements.

## 1. Hero Section Layout
- **Structure:** Split layout or two-column responsive grid (`1.2fr` and `0.8fr`).
- **Visuals:** Gold radial glowing accents in the background, a code-dash terminal box for the Copy URL Widget, and clean call-to-action buttons.
- **Copy Box:** A distinct monospaced code container with dashed gold borders, clear copy states, and an dynamic check mark hover state.

## 2. Stats Grid
- **Responsiveness:** Use CSS grid `grid-template-columns: repeat(auto-fit, minmax(200px, 1fr))` to scale nicely on desktop and tablets, down to 1 column on mobile.
- **Card Elements:** Lighter elevated card background (`var(--bg-elevated)`), large glowing stats numbers with gold/orange accents, and descriptions below.

## 3. Database Explorer Layout
- **Filter Bar:** Flex or grid container displaying search field, select dropdown filters, and reset button.
- **Table Structure:** Headers with standard `#111113` background, cells wrapping gracefully on small viewports, and round color swatches with scale transformations on hover.
- **Hover effects:** Enhance active row selection by drawing a left gold border:
  `border-l-2 border-[--accent-gold]`

## 4. Glass Card Component
- Apply `backdrop-filter: blur(10px)` with background color using transparent white opacity `rgba(255,255,255,0.03)` and line border `rgba(255,255,255,0.06)`.
