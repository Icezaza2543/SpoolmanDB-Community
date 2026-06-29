# Design Systems Skill Reference

Guidelines for maintaining design systems, tokens, components, and variables inside SpoolmanDB Community.

## 1. CSS Design Tokens
All core variables are centralized in `:root`:
*   `--bg`: Background colors (e.g. `#0A0A0F` dark mode).
*   `--ink`: Primary text color (`#FAFAFA` white).
*   `--muted`: Muted text descriptions (`#A1A1AA` grey).
*   `--line`: Border color with subtle alpha opacity (`rgba(255, 255, 255, 0.08)`).
*   `--soft`: Dark surface backgrounds (`#18181B`).
*   `--orange`: Primary accent gold / amber (`#F59E0B`).
*   `--orange-dark`: Secondary accent orange (`#F97316`).

## 2. Dynamic Components
*   **Buttons:** Apply transitions `all 0.25s cubic-bezier(0.4, 0, 0.2, 1)`. Dark / default buttons should shift background/borders seamlessly.
*   **Cards:** Hover actions on cards must lift them `translateY(-2px)` and apply responsive drop-shadows rather than scaling child text.
*   **Form Controls:** Selects and search inputs must have identical height (`min-height: 44px`), borders, and focus glows to ensure absolute consistency.
