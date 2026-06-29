# Frontend Design Skill Reference

Guidelines for layout, component structure, typography, spacing, and modern UI patterns for SpoolmanDB Community.

## 1. Typography & Hierarchy
*   **Headings:** Use `Outfit` (sans-serif) for all headers (`h1`, `h2`, `h3`). Apply letter-spacing of `-0.02em` or `-0.03em` for clean, professional modern headers.
*   **Body Copy:** Use `Inter` (sans-serif) for all body text, lists, and tables. Set line-height to `1.5` or `1.6` for optimal readability.
*   **Monospace:** Use a solid mono font (e.g. `Cascadia Mono`, `SFMono-Regular`, `Consolas`) for technical specs, codes, and URLs.

## 2. Spacing & Grid System
*   **Layout Spacing:** Maintain a max-width container of `1180px` for consistent desktop wrapping.
*   **Grid:** Utilize `display: grid` with `gap` properties instead of ad-hoc margins to prevent layout shifts.
*   **Paddings:** Align card inner padding to `24px` or `34px` for breathing space.

## 3. Dark Theme & Aesthetics
*   **Background:** Use ultra-dark slate (`#0A0A0F`) to make content cards stand out.
*   **Surfaces:** Cards and floating headers should use a lighter shade of dark gray (`#18181B` or `#27272A`) to establish a clear visual hierarchy.
*   **Visual Enhancements:** Implement glassmorphism using `backdrop-filter: blur(10px)`. Add subtle gold shadows (`rgba(245, 158, 11, 0.08)`) on hover to produce high-end developer-tool vibes.
