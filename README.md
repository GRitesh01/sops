# StrategicOps Global Consulting: Agentic AI website

Static, multi-page corporate website (HTML5, CSS3, Bootstrap 5 grid via CDN, vanilla JavaScript).
Same business model and 20-page architecture as the SYMMENTIS build, with a different identity:
light "operations atlas" look (cobalt, paper, ink, sun), floating pill navigation, bordered tiles with
offset shadows, and a cursor-driven interaction layer.

## Run
```bash
python3 -m http.server 8080     # then open http://localhost:8080
```
Deploy the folder as-is to any static host.

## Structure
```
index.html, pages/*.html      20 pages (home, about, services + 6 service pages, solutions, industries,
                              technology, process, case studies, insights, contact, consultation, 3 legal)
css/style.css                 Tokens, layout, components, cursor layers
css/responsive.css            Breakpoints, full-screen mobile menu, touch rules
css/animations.css            Motion (neutralised under prefers-reduced-motion)
js/config.js                  >>> Launch configuration: formEndpoint, calendarUrl, turnstileSiteKey <<<
js/cursor.js                  Custom cursor: dot, lagging ring, label bubbles, comet trail, click ripples
js/animations.js              Scroll progress, word reveals, 3D tilt, magnetic buttons, spotlight text,
                              floats, marquee scroll-velocity
js/agent-visualization.js     Hero dot-field, agent loop, draggable mission-control board
js/navigation.js              Pill header (hide/show on scroll, sliding hover blob), dropdowns, mobile menu
js/main.js, forms.js, components.js
build/                        Python generator (optional): python3 build/build.py
```

## Cursor and motion layer
- **Custom cursor** (fine pointers only): dot + lagging ring that inverts over any background, fills on links,
  shrinks on headings, turns into a labelled bubble ("Open", "Drag", "Read"...) via `data-cursor="Label"`.
- **Comet trail** and **click ripples** across the page.
- **Hero field**: dot grid bends around the cursor; agent chips lean toward it; click sends signals from the orchestrator.
- **Magnetic buttons** (`data-magnetic`), **3D tilt cards** (`data-tilt`), **spotlight text** (`data-spotlight`), cursor-reactive floats.
- Touch devices and `prefers-reduced-motion` users get the native cursor, static visuals and no pointer effects.

## Interactive diagrams
- **Agent loop**: 7 stages, token travels the loop, play button for a sample task.
- **Mission-control board**: drag nodes (arrow keys also nudge), select for details, dispatch a request.
  Below 720px it becomes a stacked list.

## Before launch
1. Replace bracketed placeholders (`[BUSINESS EMAIL]`, phone, address, company story, leadership, article dates, legal text).
2. Set `SITE["base_url"]` in `build/common.py` (currently `https://www.strategicops.example`) and rebuild.
3. Add real social URLs to `SITE["social"]` (empty ones show as "URL pending").
4. Set `formEndpoint` in `js/config.js`. Until set, forms validate but state plainly that nothing was sent (no fake success).
5. Set `calendarUrl` for the booking embed; optionally `turnstileSiteKey` (verify the token server-side).
6. Legal pages are draft templates: have counsel review. Replace the generated `og-image.png` with branded art.

## Integrity and accessibility
No invented clients, metrics, awards or testimonials; case studies are labelled demonstration projects; benefits are
phrased as potential outcomes. Skip link, landmarks, ordered headings, visible focus, ARIA tabs/accordion, labelled
forms with alert errors, keyboard-operable dropdowns and board, and reduced-motion support.
