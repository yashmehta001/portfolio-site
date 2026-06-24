# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

Personal portfolio site for Yash Mehta, a full-stack engineer. It is a static site — plain HTML + CSS, no build tools, no frameworks. The design originates from a Claude Design project (`Portfolio.dc.html`) and was compiled into static markup.

Live at **https://itsyashmehta.com**. Hosted on GitHub Pages with Cloudflare DNS.

## Files

- `index.html` — the entire site (nav, hero, about, services, skills, experience, patent, contact, footer). A projects section exists but is commented out.
- `styles.css` — all styles, organized by section. Uses `clamp()` for responsive sizing and CSS classes for hover/transition effects.
- `assets/Yash-Mehta-Resume.pdf` — downloadable resume linked from nav, hero, and footer.
- `assets/og-image.png` — Open Graph image for social link previews (1200x630).
- `CNAME` — GitHub Pages custom domain file (auto-generated, do not edit).

## Local Preview

No build step. Serve with any static file server:

```sh
python3 -m http.server 8080
# or
npx serve .
```

Then open `http://localhost:8080`.

## Making Changes

HTML and CSS are hand-authored and directly editable. Content changes go in `index.html`, styling in `styles.css`. Key conventions:

- **Fonts:** Space Grotesk (headings), IBM Plex Sans (body), IBM Plex Mono (labels/code) — loaded from Google Fonts.
- **Colors:** Blue `#2E5AE6`, green `#12A05F`, dark `#1A1C20`, body text `#52565D`, muted `#7A7E85`/`#9A9EA4`.
- **Section pattern:** Each section uses `.section-border` for the top border, `.container .section-inner` for padding, `.section-header` with `.section-number` + `.section-title`.
- **Hover effects:** All interactive hover styles are CSS classes (`.btn-primary:hover`, `.service-card:hover`, etc.) — no inline `style-hover` or JavaScript.
- **Accessibility:** Social icon links use `aria-label`, decorative icons use `aria-hidden="true"`, external links use `rel="noopener noreferrer"`.

## Deployment

Push to `main` — GitHub Pages deploys automatically. DNS is managed through Cloudflare (A records + CNAME pointing to `yashmehta001.github.io`).

## Design Origin

The design was imported from Claude Design project `2f8bb664-8ab5-4368-a006-8e655aac280e`, file `Portfolio.dc.html`. The DC component template (with `<sc-for>`, `<sc-if>`, `style-hover` directives) was compiled into static HTML with all data inlined and directives resolved.
