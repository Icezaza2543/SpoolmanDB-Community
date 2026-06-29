# SpoolmanDB Design System

## 1. Color Tokens (Spoolman Dark Theme)

```css
:root {
  /* Background */
  --bg: #0A0A0F;
  --bg-elevated: #18181B;
  --bg-hover: #27272A;

  /* Text */
  --text-primary: #FAFAFA;
  --text-secondary: #A1A1AA;
  --text-muted: #71717A;

  /* Accent */
  --accent-gold: #F59E0B;
  --accent-orange: #F97316;
  --accent-gold-hover: #D97706;

  /* Border & Glass */
  --border: rgba(255, 255, 255, 0.06);
  --glass-bg: rgba(255, 255, 255, 0.03);

  /* Status */
  --success: #22C55E;
  --warning: #F59E0B;
  --danger: #EF4444;
}
```

## 2. Spacing Scale (ใช้สม่ำเสมอ)

```css
--space-xs: 4px;
--space-sm: 8px;
--space-md: 16px;
--space-lg: 24px;
--space-xl: 32px;
--space-2xl: 48px;
```

## 3. Component Tokens

### Button
- Primary: `bg-[--accent-orange] text-white`
- Secondary: `border border-[--border] hover:bg-[--bg-hover]`
- Ghost: `hover:bg-[--bg-hover]`

### Card
- `bg-[--bg-elevated] border border-[--border] rounded-2xl`
- Hover: `hover:border-[--accent-gold] transition-all`

### Table
- Header: `bg-[#111113] text-[--text-secondary]`
- Row Hover: `hover:bg-[#1F1F23]`
- Left accent bar on hover: `border-l-2 border-[--accent-gold]`

## 4. Typography

- Heading: `font-family: 'Outfit', sans-serif; letter-spacing: -0.02em;`
- Body: `font-family: 'Inter', system-ui, sans-serif;`
- Data / Code: `font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;`
