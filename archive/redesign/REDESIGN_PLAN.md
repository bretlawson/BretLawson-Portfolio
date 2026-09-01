# Portfolio Redesign — v2 (light/refined direction)

**This replaces the first (dark/bulky) attempt, which was rejected.** Open **`index-mock.html`** to review.

> Non-destructive: nothing in the live site (`index.html`, `styles.css`, `analysis/`) is changed. Everything here is a proposal.

## What changed, and why

The first mock was dark, gradient-heavy, salesy, and recycled the old projects. Exemplar research (Chip Huyen, Lee Robinson, Vicki Boykis, Nadieh Bremer, Brittany Chiang) was unanimous: portfolios that read **senior** are **light, text-forward, and restrained** — credibility lives in plain prose and the sharpness of the work, never in stat-bands, gradient buttons, or a "Fortune 500" label in the headline.

**The new direction — "analyst's notebook":**
- **Light, warm paper-white canvas** (`#FAFAF7`), near-black ink, **one** restrained accent (deep ink-blue `#1F3A5F`). No dark bands, no gradients, no grid texture, no glow, no emoji.
- **Fraunces (serif display) + Inter (body)** on a strict 3-level type scale; structure comes from whitespace and hairline rules, not boxes.
- **Personal voice, not a sales pitch.** Headline is just *Bret Lawson · Senior Analytics Leader* with one Fraunces line — "I turn the questions that take weeks into answers that hold up the same day." Candidate CTAs only (email, LinkedIn, résumé).
- **Compact thumbnail grid** of 6 small tiles with small text — not big magazine cards. Each tile: line-art thumbnail · title · one Fraunces callout (the answer) · tiny meta row. The whole tile is the link.
- **One page, ~2–3 tight scrolls:** Hero → Selected work → About → Experience (lean one-line-per-role list) → Tooling (brief) → Contact.

## Project selection — your best *last-6-months* work (freshly mined, not recycled)

| Tile | Executive question → callout | Skill shown |
|---|---|---|
| **Interactive sample dashboard** | Live ecommerce KPI view, re-aggregates as you slice fiscal Y/Q/P/W | BI / engineering |
| **Quarterly CPC forecast engine** | Beat the legacy curve by 2.5 pts; called Q3 at −11% vs −16% raw | Forecasting / elasticity |
| **"Is organic search dying?"** | Organic −27%, but PDPs −68% to AI Overviews, offset by a +170% content play | Decomposition / SEO |
| **Channel elasticity & spillover** | 224 channel-pairs: 71.5% organic base vs 28.5% spend-driven; saturates past $7.5M/wk | Causal / MMM |
| **Omni purchase propensity** | 34 deploy-ready signals at 92–99% AUC; caught 90%-leakage feature | Predictive ML |
| **Margin-dollar YoY waterfall** | Margin held within $9K on $4.1M less discount — only $73K was real pricing | Margin / pricing |

*(Repeat-buyer identity-graph cohorts, AOV/UPT decomposition, and the site-performance revenue model are noted as "available on request" rather than crowding the grid.)* All figures illustrative/anonymized; methods real. The dashboard is presented as **one ordinary tile** — the "command center" narrative is gone.

## Decisions for you
1. **Accent color** — using deep ink-blue `#1F3A5F`. Prefer the slightly more editorial **oxblood** `#7A1E2B`?
2. **Headline line** — using "I turn the questions that take weeks into answers that hold up the same day." (3 alternates exist if you want a different one.)
3. **Which 6 tiles** — happy to swap in the repeat-buyer identity-graph or AOV decomposition for any of the six.
4. **Thumbnails** — currently clean inline SVG line-art. Keep, or render real mini-charts from each analysis?

## v5 direction (Sep 2026) — real-work case studies replace the draft tiles

The table above is superseded. Featured work is now a **triptych mined from the real work repo**, each its own case-study page (situation → hero visual → what I did → the turn → what happened after → collapsible technical notes; figures indexed/perturbed, one "shapes real, scales disguised" line):

1. **Organic decline decomposition** — written case study. **Built: `organic-decline.html`** ("Everyone blamed rankings. Rankings were one percent of it."). This is the format exemplar.
2. **Ecom mart** — the "I model the data" story. **Built: `ecomm-mart.html`** ("The source of truth was a 40-tab spreadsheet.") with inline-SVG lineage hero.
3. **Dashboard & reporting suite** — delivery/adoption story. **Built: `dashboard-suite.html`** ("The BI stack is a folder of HTML files.") + **`paid-funnel-decomp.html`**, a working sanitized replica of the flagship (8-effect LMDI, client-side recompute, house-standard Primary/Comparison controls, synthetic data) with `funnel-decomp-preview.png` embedded in the case page.

**Index rewired (v5):** work section = 3 case cards (finding-as-title, mini-SVG thumbs, links to pages) + "Also in the portfolio" secondary row, all three linked: forecast explorer · SKU decomposition · **`propensity-signals.html`** (short-form write-up, "The best-performing feature was 90% data leakage."). Modal machinery removed.

## If approved
Rebuild the live `index.html`/`styles.css` to this system; accessibility + performance pass; update `resume.html` and SEO/meta to match; retire `command-center.html`.
