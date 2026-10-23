# rAIght design system

The app must look like our final pitch deck ([`Scrumsterz_rAIght_Pitch.pptx`](../presentations/Scrumsterz_rAIght_Pitch.pptx)). Slide 3, *"Prototype 2 · Lena's dashboard"*, is the **reference screen** for the dashboard: match it closely.

Values below are extracted from the deck's theme ("Scrumsterz rAIght") and slides. Use the tokens; **never hard-code hex values in components**.

## 1. Character

Calm, factual, enterprise. Dark forest green and a single lime accent. Lots of white space, flat surfaces, thin borders, no gradients, no glow, no playful illustration. The message is "lean, not more": the UI should feel restrained.

## 2. Logo (wordmark)

The logo is **text, not an image**: `rAIght` in **Arial Bold**, where only **"AI"** is lime.

| Background | `r` + `ght` | `AI` |
|---|---|---|
| Dark (`--color-surface-inverse`) | white | lime `--color-accent` |
| Light (white / mist) | ink `--color-text` | lime `--color-accent` |

```html
<span class="logo">r<span class="logo-ai">AI</span>ght</span>
```
```css
.logo     { font-family: var(--font-heading); font-weight: 700; letter-spacing: -0.01em; }
.logo-ai  { color: var(--color-accent); }
```

- Use it in the app header (on the dark bar, like the dashboard header on slide 3) and wherever the product name appears in running text, e.g. "Why r**AI**ght".
- **Tagline:** "Not more AI, but r**AI**ght." – tagline in white or ink, the trailing word as the logo, the full stop in the base colour.
- Don't recolour, outline, add a shadow, or swap the font. Don't use lime for any other word in the same line.
- Lime "AI" on white has low contrast (1.5 : 1). That's accepted **only for the logo at ≥ 20 px bold**. Never set other lime text on light backgrounds.

## 3. Colour tokens

### Brand (theme colours of the deck)

| Token | Hex | Deck role | Use in the app |
|---|---|---|---|
| `--color-forest-900` | `#0B2B26` | Title slide / dark panels (dk2) | Header bar, dark hero panels, sidebar |
| `--color-forest-700` | `#11604F` | Primary (accent1) | Primary buttons, links, section labels, icons, "good" values |
| `--color-ink` | `#1C2B28` | Text (dk1) | Body text and headings on light |
| `--color-lime-400` | `#B8E04A` | Signature accent (accent2) | Logo "AI", highlighted ladder steps (Rule/Workflow), check marks, accents **on dark** |
| `--color-orange-400` | `#F7A54E` | accent3 | Token usage bars (data, not a warning) |
| `--color-green-300` | `#8FD18A` | accent4 | Secondary data series |
| `--color-yellow-300` | `#FCE27A` | accent5 | Sticky notes / user-story cards |
| `--color-red-500` | `#E5484D` | accent6 | Problems: blind spot, "Agent" triage outcome, high same-path share |

### Neutrals (from the slides)

| Token | Hex | Use |
|---|---|---|
| `--color-white` | `#FFFFFF` | Page background, cards |
| `--color-mist-50` | `#F4F7F5` | Card fill on white (Goals/Pains boxes) |
| `--color-mint-50` | `#EAF4EF` | Tinted fill: secondary buttons, triage outcomes, highlight panels (lt2) |
| `--color-line-100` | `#E3EAE6` | Bar track (empty part of a bar), row dividers |
| `--color-line-200` | `#C9D6D0` | Borders, table lines, connectors |
| `--color-sage-400` | `#9FB8AF` | Muted text on dark, arrows |
| `--color-slate-500` | `#5E6E6A` | Secondary text on light, captions, footers |
| `--color-forest-800` | `#153A33` | Raised elements on dark (ladder steps on the title slide) |
| `--color-red-50` | `#FDECEC` | Problem tint (Blind spot box, "Agent" outcome) |

### Semantic tokens (use these in components)

```css
:root {
  /* brand */
  --color-forest-900: #0B2B26;
  --color-forest-800: #153A33;
  --color-forest-700: #11604F;
  --color-ink:        #1C2B28;
  --color-lime-400:   #B8E04A;
  --color-orange-400: #F7A54E;
  --color-green-300:  #8FD18A;
  --color-yellow-300: #FCE27A;
  --color-red-500:    #E5484D;
  --color-red-600:    #C83A3F; /* text-safe red on white (5.1 : 1) */
  /* neutrals */
  --color-white:      #FFFFFF;
  --color-mist-50:    #F4F7F5;
  --color-mint-50:    #EAF4EF;
  --color-line-100:   #E3EAE6;
  --color-line-200:   #C9D6D0;
  --color-sage-400:   #9FB8AF;
  --color-slate-500:  #5E6E6A;
  --color-red-50:     #FDECEC;

  /* semantic */
  --color-bg:               var(--color-white);
  --color-surface:          var(--color-mist-50);
  --color-surface-tint:     var(--color-mint-50);
  --color-surface-inverse:  var(--color-forest-900);
  --color-text:             var(--color-ink);
  --color-text-muted:       var(--color-slate-500);
  --color-text-inverse:     var(--color-white);
  --color-text-inverse-muted: var(--color-sage-400);
  --color-primary:          var(--color-forest-700);
  --color-on-primary:       var(--color-white);
  --color-accent:           var(--color-lime-400);   /* logo + accents on dark only */
  --color-on-accent:        var(--color-ink);
  --color-border:           var(--color-line-200);
  --color-track:            var(--color-line-100);
  --color-data-tokens:      var(--color-orange-400);
  --color-danger:           var(--color-red-500);    /* large/bold text, icons, fills */
  --color-danger-text:      var(--color-red-600);    /* small text */
  --color-danger-surface:   var(--color-red-50);
  --color-good:             var(--color-forest-700);

  /* type */
  --font-heading: Arial, "Helvetica Neue", Helvetica, sans-serif;
  --font-body: Calibri, Carlito, "Segoe UI", system-ui, sans-serif;

  /* shape */
  --radius-sm: 2px;    /* cards, panels, boxes – almost square */
  --radius-pill: 999px;/* buttons, suggestion chips */
  --border-width: 1px;
  --shadow-card: 0 1px 3px rgba(11, 43, 38, 0.12); /* only for the "floating" dashboard card */
}
```

**Contrast (checked, WCAG):** white on forest-900 15 : 1 · lime on forest-900 9.9 : 1 · forest-700 on white 7.5 : 1 · ink on lime 9.7 : 1 · slate-500 on white 5.4 : 1 · red-500 on white 3.9 : 1 (→ large/bold only; use `--color-danger-text` for small text) · lime on white 1.5 : 1 (→ logo only).

**Dark mode:** not needed for the demo. The deck's "dark" is used for emphasis panels, not as a theme.

## 4. Typography

| Role | Font | Size (web) | Weight | Colour | Example in deck |
|---|---|---|---|---|---|
| Hero wordmark | Arial | 64–88 px | Bold | white + lime | Title slide |
| Page title | Arial | 32–36 px | Bold | ink | "Meet Lena: she builds her own automations" |
| Section heading | Arial | 20–24 px | Bold | ink | Card titles "Learn", "Lena, 38" |
| **Eyebrow / overline** | Arial | 12–13 px | Bold, **UPPERCASE, letter-spacing 0.2em** | forest-700 (lime on dark, red for problems) | "① DESIRABILITY · PERSONA & POINT OF VIEW", "GOALS", "PAINS" |
| Body | Calibri (web: Carlito) | 15–16 px | Regular | ink | Card text |
| Small / caption | Calibri | 12–13 px | Regular or *italic* | slate-500 | "Illustrative values", footers |
| Numbers in tables | Calibri | 18–20 px | Bold | red (problem) / forest-700 (fine) | "94 %", "52 %" |

- **Calibri isn't a web font.** Load **Carlito** (metric-compatible, open licence) as the web fallback; Arial is a system font everywhere.
- Headings in **sentence case**, as statements ("The CIO office gets autonomy without footprint growth"). Only eyebrows are uppercase.
- Eyebrows separate parts with a middle dot `·` and may start with a circled number (① ② ③).
- Italic is used for quotes, notes and captions only.

## 5. Layout & spacing

- Generous margins (the deck uses ~5 % side margins), left-aligned content, clear grid.
- Spacing scale: 4, 8, 12, 16, 24, 32, 48, 64 px.
- **Page pattern:** eyebrow → page title → content in cards → a quiet footer (`Scrumsterz · rAIght`, slate-500, small).
- Max content width about 1200 px for the dashboard.

## 6. Components

| Component | Look (from the deck) |
|---|---|
| **App header** | Full-width bar in forest-900; logo left (white `r`/`ght`, lime `AI`), then `· Lena's automations` in white, semibold |
| **Card** | mist-50 fill **or** white with 1 px line-200 border; radius ≤ 2 px; padding 16–24 px; eyebrow label at the top |
| **Dark emphasis panel** | forest-900 fill, white text, lime headline or quote ("Why it pays", the persona card) |
| **Problem card** | red-50 fill, eyebrow in red ("BLIND SPOT") |
| **Primary button** | Pill, forest-700 fill, white bold text, trailing `›` ("Convert to workflow ›") |
| **Secondary button / chip** | Pill, mint-50 fill, forest-700 bold text, no border ("Keep for complex panels") |
| **Table (dashboard)** | No vertical lines; header row as eyebrow style (uppercase, spaced, slate/forest); rows separated by 1 px line-100; generous row height |
| **Bar (tokens/month)** | Flat horizontal bar, orange-400 fill on line-100 track, no rounded ends, no labels inside |
| **Same-path share** | Large bold percentage: **red** when the agent is flagged *uniform*, **forest-700** otherwise. Colour must come from the metric threshold, never hard-coded per agent |
| **Ladder (1 Rule … 6 Multi-agent)** | Stacked staircase of rectangles; lower steps lime with ink bold text = recommended; higher steps forest-800 with thin border and white text |
| **Triage step** | White box, 1.5 px forest-700 border, bold question; "yes" arrow → outcome box in mint-50 (forest text) or red-50 (red text for *Agent*) |
| **Process step (Learn → Build → Monitor → Convert)** | mist-50 card, white circle with forest-700 icon on the left, bold title, slate description, grey arrow between cards |
| **Check list** | Lime circle with dark check mark, bold line + slate sub-line (product box) |
| **Numbered marker** | Forest-700 filled circle with white number |
| **Sticky / story card** | yellow-300 fill, ink small text (user story map) |

## 7. Icons

Solid, rounded, single-colour glyphs in forest-700, the style of **Font Awesome 6 Free Solid** (graduation-cap, sitemap, chart-simple, shuffle are used in the deck). Use one icon set consistently; no outline/solid mix, no multicolour icons. Typical placement: inside a white circle on a mist card.

## 8. Data & charts

- Data colours: tokens → orange-400; good/neutral → forest-700 / green-300; problem → red-500. Lime is reserved for brand accents, not data.
- Keep charts flat: no 3D, no gradients, light gridlines (line-100) or none.
- Always show the unit or the explanation in a small italic caption below (as on slide 3: *"Tokens straight from the run logs · 'Same path' = share of runs with identical steps · no extra AI checks the AI"*).
- Mark simulated values: a small italic "Illustrative values" / "Demo data" label top right, as in the deck ([ADR 0006](../decisions/0006-pure-clickable-demo.md)).

## 9. Voice in the UI

Short, plain English, sentence case, verbs first on buttons ("Convert to workflow", "Retire agent"). Use glossary terms ([09-glossary.md](../concept/09-glossary.md)). Talk to Lena as the owner ("your automations"), never as someone being checked.

## 10. Don'ts

- **No Disney characters or other copyrighted figures.** The deck's Lena avatar is a placeholder from the pitch and must not appear in the software. Use initials in a forest-700 circle ("L") or a neutral illustration instead.
- No logos of SAP, Microsoft, OpenAI or n8n, and no SAP Fiori branding: providers and systems appear **by name only** ([ADR 0005](../decisions/0005-scope-external-agents.md)).
- No gradients, glows, drop shadows on everything, or rounded "bubbly" cards.
- No lime text on white except the logo; no more than one lime element per component.
- No new colours outside this file. If you need one, propose it (structural change).
