---
name: color-palette-expert
description: Use when choosing, building, checking or exporting colours for dark plugin UIs, pixel-art palettes, websites, merch and flyers, incl. contrast, colour blindness, OKLCH, tokens and print vs screen.
---

# Colour and palette expert for non-programmer producers and builders

Labels: VERIFIED (source) means read on a fetched page. COMMUNITY means widely repeated craft advice, not sourced. UNVERIFIED means not read; check before relying on it.
Contrast numbers in section 12 were computed with a Python script using the WCAG formula, not estimated.
Related skills, do not duplicate them: photo-editing-color-grading (deep photo grading, filters), graphic-design-expert, ux-ui-designer, design-software-guide, drawing-tablets, vst-maker, squarespace-expert.

## Rules of engagement

1. Ask first: where will it be used (plugin UI, game, site, print), dark or light, how many colours, any brand colour already chosen. Never assume a palette (the vst-maker skill also says to ask first).
2. Give hex codes that can be pasted, plus a plain name for each role ("background", "button").
3. One decision at a time: brand colour, then neutrals, then accent, then status colours, then check contrast.
4. Always report measured contrast ratios. Never say "looks fine" without a number.
5. The approved mockup is the product. Do not shift approved colours without asking.
6. Colour is never the only signal. Add text, icon, shape or position.

## 1. Colour models (what to use for what)

- RGB: light mixed on a screen. Hex like #FFB454 is RGB written in base 16. COMMUNITY.
- HSL and HSV: reshuffled RGB with a hue angle. HSL is cylindrical, so equal lightness values look different per hue. VERIFIED (Evil Martians: "The main problem with HSL is that it has a cylindrical color space").
- Oklab: designed to predict perceived lightness, chroma and hue; L, C, h should act as independent controls. VERIFIED (bottosson.github.io/posts/oklab).
- OKLCH: the polar form of Oklab. Lightness, Chroma, Hue. VERIFIED (CSS Color 4: "specifies an Oklab color by Oklab Lightness, Chroma, and hue").
- CIELAB: older, weak at hue, especially blue. VERIFIED (Ottosson: "Largest issue is their inability to predict hue. In particular blue hues are predicted badly"). Blends in CIELAB, CIELUV and HSV shift toward purple; Oklab avoids that. VERIFIED.
- CMYK: subtractive ink model. Each model has a distinct gamut, so colours visible in one may not be reproducible in the other. No fixed formula converts RGB to CMYK, ICC profiles are needed. VERIFIED (Wikipedia, CMYK colour model).

### Why OKLCH for palettes

- L is perceived lightness, so a ramp that steps L evenly looks even. VERIFIED (Evil Martians).
- L runs 0 to 1. Hue 0 to 360 (red about 20, yellow 90, green 140). Chroma has no fixed max but stays below about 0.37 in sRGB and P3. VERIFIED (Evil Martians).
- Same L across different hues gives similar contrast against a background, which HSL does not. VERIFIED in spirit (Evil Martians cites the blue vs purple 10% example); the exact claim is theirs.
- Syntax: `oklch(0.82 0.14 70)`, also with alpha `oklch(0.82 0.14 70 / 0.5)`. VERIFIED (CSS Color 4 grammar lists oklch()).
- Browser support: article says all latest browsers support oklch() (MDN, September 2025). VERIFIED as the article's claim. Squarespace custom CSS support: UNVERIFIED, test in preview.
- JUCE and plugin code do not read oklch(). Convert to hex first (section 12 script, or oklch.com). UNVERIFIED for JUCE specifics; hex is the safe route.
- Out-of-gamut colours get gamut mapped to a lower-chroma lookalike. VERIFIED (CSS Color 4). Chrome and Safari use fast clipping, so check by eye. VERIFIED (Evil Martians).
- Tools: oklch.com picker, Huetone, Color.js, culori. VERIFIED as named in the article.

## 2. Value, saturation, temperature

- Value (lightness) carries structure; hue carries mood. Squint test: if the design works in greyscale, the values are right. COMMUNITY.
- Saturation: keep most of the UI low chroma, spend high chroma on one thing. COMMUNITY.
- Temperature: warm colours advance, cool colours recede. COMMUNITY. Warm displays drew more attention but cool ones were rated more favourably in one cited study. VERIFIED (Wikipedia, Colour psychology), treat as context only.
- Apple notes colours look darker and muted in bright surroundings and brighter and more saturated in dark ones. VERIFIED (Apple HIG Color). A studio is dim, so test the UI at night.

## 3. Colour wheel harmonies

- Monochromatic: one hue, many lightness steps. Safest for plugins.
- Analogous: neighbouring hues (about 30 degrees apart). Calm.
- Complementary: opposite hues. Strong, use one as the accent.
- Split-complementary, triadic, tetradic: more colours, harder to balance. COMMUNITY.
- Realtime Colors offers monochromatic, analogous and triadic schemes. VERIFIED (realtimecolors.com).
- Note: the RYB wheel vs the RGB/OKLCH wheel disagree on complements. For screens, pick by OKLCH hue angle. COMMUNITY.
- Adobe Color harmony page could not be fetched. Adobe's exact rule names: UNVERIFIED.

## 4. 60-30-10

- 60% dominant (background and large surfaces), 30% secondary (panels, cards), 10% accent (buttons, active knobs, links). COMMUNITY.
- Plugin version: 60 dark bg, 30 surfaces and text, 10 one accent. A plugin suite can give each plugin its own accent on a shared neutral base. Ask before changing approved designs.

## 5. Neutrals and tinted greys

- Pure grey looks dead next to coloured accents. Tint neutrals toward the brand hue with tiny chroma (about 0.01 to 0.04 in OKLCH). COMMUNITY. The example palettes below use this (measured chroma 0.016 to 0.045).
- Keep the same tint hue across the whole neutral ramp so greys feel related. COMMUNITY.
- Warm tint for site paper backgrounds, cool or purple tint for night UIs. COMMUNITY.

## 6. Dark mode rules

- Do not use pure black #000000 as the main background. Pure white on pure black is 21:1 (computed), which glares. Prefer a dark tinted grey, text at about 12:1 to 16:1. COMMUNITY advice; the glare claim is UNVERIFIED. (Material's dark theme page needs JavaScript and could not be read, so its exact hex and 15.8:1 figure are UNVERIFIED.)
- Elevated surfaces get lighter: bg, then surface, then raised, each a few L steps up. COMMUNITY. Plugin panels: the front-most control is the lightest.
- Desaturate accents slightly and raise their lightness so they glow without vibrating on dark. COMMUNITY.
- Text: off-white tinted, not #FFFFFF. Secondary text must still reach 4.5:1. VERIFIED threshold (WCAG 1.4.3).
- Apple: custom colours need light and dark variants and an increased-contrast option. VERIFIED (HIG Color). Even single-appearance apps should supply both. VERIFIED.
- Borders in dark UIs often fail 3:1. Check them (section 12 shows 1.88:1 for a decorative divider and 3.87:1 for a real control edge).

## 7. Semantic colours

- Success green, warning amber, error red, info blue. COMMUNITY convention.
- Never use the same colour for two meanings; a brand colour used for both "interactive" and plain text confuses. VERIFIED (Apple HIG: "Avoid using the same color to mean different things").
- Red means danger in some cultures and good luck in others; stocks are red-up in Chinese-language Stocks app. VERIFIED (Apple HIG).
- Pair every status colour with an icon or word (VERIFIED, WCAG 1.4.1, section 8).
- Keep status colours distinct from the brand accent (an amber accent clashes with an amber warning; example A keeps them 15 hue degrees apart, so add an icon too).
- Red/green only is a trap for colour blind users. Use blue/orange or add shapes. COMMUNITY plus section 9.

## 8. WCAG 2.2 contrast (exact numbers)

Sources: w3.org Understanding 1.4.3, 1.4.6, 1.4.11, 1.4.1. All VERIFIED.
- AA normal text: at least 4.5:1.
- AA large text: at least 3:1. Large is 18 pt, or 14 pt bold (about 24 px and 18.5 px).
- AAA normal text: at least 7:1. AAA large text: at least 4.5:1.
- UI components and graphical objects: at least 3:1 against adjacent colours (1.4.11, AA). Covers visual info needed to identify controls and states, and focus indicators.
- Exempt from 3:1: inactive components, and browser-default appearance the author did not change. Author-added hover effects are not required to meet it.
- Text exceptions: inactive UI text, pure decoration, logos and brand names (no requirement). Low contrast chosen by taste is not exempt for graphics.
- Ratios are never rounded: 4.499:1 fails 4.5:1; 2.999:1 fails 3:1.
- Ratio range is 1:1 to 21:1. Formula: (L1 + 0.05) / (L2 + 0.05), L1 the lighter. Relative luminance: linearise each channel (c/255; if c <= 0.04045 then c/12.92 else ((c+0.055)/1.055)^2.4), then L = 0.2126 R + 0.7152 G + 0.0722 B. The threshold was 0.03928 before May 2021. VERIFIED (Understanding 1.4.3).
- 1.4.1 Use of Colour (Level A): colour cannot be the only visual means. A lightness difference of at least 3:1 can count as the extra cue. VERIFIED.
- Plugins are not websites, but use the same numbers as the target. COMMUNITY.

## 9. APCA and WCAG 3 status

- APCA: a newer perceptual contrast method giving an Lc value. Its own page says "APCA W3 is in public beta" and gives rough replacements Lc 90, 75, 60 for 7:1, 4.5:1, 3:1. VERIFIED (apcacontrast.com), the mapping is theirs.
- WCAG 3.0 working draft (10 September 2026 per the page): contrast algorithm "yet to be determined", APCA not mentioned. VERIFIED (w3.org/TR/wcag-3.0).
- So: WCAG 2.2 ratios are the standard to cite today. Use APCA only as a second opinion. Anything legal or client-facing: WCAG 2.2.

## 10. Colour blindness

- Red-green deficiency affects up to 1 in 12 males (8%) and 1 in 200 females (0.5%). Protan (L cone) about 2% of males and makes reds look dimmer; deutan (M cone) about 6% of males. VERIFIED (Wikipedia, Color blindness; its own table is slightly inconsistent for protan).
- Monochromacy exists and is much rarer. VERIFIED.
- Tritan (blue-yellow) type: UNVERIFIED, the fetched page did not cover it. NEI page could not be fetched.
- Safe habits (COMMUNITY): differ in lightness, not only hue; avoid red vs green and green vs brown pairs; use shapes, labels and patterns; blue plus orange is a reliable pair.
- Test: Coolors lists "Color Blind Friendly" sections and a variations menu option, free status unclear. VERIFIED (coolors.co). Other simulators (Color Oracle, Firefox/Chrome devtools emulation): UNVERIFIED.
- Meter and spectrum colours: use lightness steps (dark to light) instead of a rainbow. COMMUNITY.

## 11. Colour psychology (be honest about it)

- Two kinds of effect: embodied (red raises arousal and attention) and learned (brown suggests cola). VERIFIED (Wikipedia, Colour psychology).
- Cultural variation is real: Poles linked purple with anger, Germans linked jealousy with yellow. VERIFIED (same page).
- Warnings from the same page: "no specific color attracts all audiences"; chromotherapy is called pseudoscience by many; several famous effects failed to replicate. VERIFIED.
- Preference survey (one US study): blue 35%, green 16%, purple 10%, red 9%. VERIFIED, single study.
- Use colour meaning as a starting hypothesis, then test on real listeners/viewers. Say so when advising.

## 12. Building a palette, step by step

Step 1. Pick the brand colour (the one already in use or liked). Write it in hex.
Step 2. Convert to OKLCH (oklch.com). Note L, C, H.
Step 3. Neutral ramp: same hue as brand (or a cooler/warmer neighbour), chroma 0.01 to 0.04, 9 to 11 steps from near-black to near-white. Even L steps. COMMUNITY.
Step 4. Brand ramp: hold H, vary L in even steps, reduce C near the extremes (dark and light ends cannot hold high chroma). COMMUNITY. Material uses tonal palettes with fixed tones, 0 to 100. UNVERIFIED (page needs JavaScript).
Step 5. Pick one accent from the harmony rules (section 3). Keep it for the 10%.
Step 6. Add status colours (section 7). Match their L to the accent so none shouts.
Step 7. Assign roles (tokens), then test every text/background pair and every control edge.
Step 8. Simulate colour blindness and greyscale. Fix anything that merges.
Step 9. Export (CSS variables, GPL/ASE palette, Lospec hex list) and save in the project docs.

Ramp size: 9 to 11 steps is COMMUNITY practice (e.g. 50, 100 ... 900, 950). Naming is a convention, not a standard.

Contrast checker script (stdlib only, run with `python3 -I`). VERIFIED formula (WCAG):
```
def lin(c):
    c/=255
    return c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4
def L(h):
    h=h.lstrip('#'); r,g,b=[int(h[i:i+2],16) for i in (0,2,4)]
    return 0.2126*lin(r)+0.7152*lin(g)+0.0722*lin(b)
def ratio(a,b):
    x,y=sorted((L(a),L(b)),reverse=True); return (x+.05)/(y+.05)
```
OKLCH conversion needs the Oklab matrices from bottosson.github.io; the numbers below came from that method. Do not hand-wave L, C, H: compute.

## 13. Design tokens and CSS

- Name by role, not by colour: `--bg`, `--surface`, `--raised`, `--text`, `--text-muted`, `--accent`, `--border`, `--ok`, `--warn`, `--err`. Never `--purple`. COMMUNITY. Apple does the same: colours are "semantically defined by its purpose, rather than its appearance". VERIFIED (HIG Color).
- Two layers: raw ramp (`--grey-900`) then role tokens (`--bg: var(--grey-900)`). COMMUNITY.
- Light/dark switching: define light tokens on `:root`, redefine under `@media (prefers-color-scheme: dark)`. COMMUNITY standard CSS; the `light-dark()` function was not in the CSS Color 4 page read, so UNVERIFIED.
- Wide gamut: sRGB hex by default, P3 value inside `@media (color-gamut: p3)`. VERIFIED (Evil Martians recommendation). Apple: use Display P3 for wide colour, supply sRGB variants when similar P3 colours merge or gradients clip. VERIFIED (HIG).
- Squarespace: where colour tokens go in the 7.1 style editor and custom CSS is in the squarespace-expert skill. Do not guess here. UNVERIFIED.
- Plugin code (JUCE): keep one colours header or struct with the same role names, so the mockup, installer and website match. COMMUNITY.

## 14. Pixel-art palettes for 16-bit style games

Rules (COMMUNITY unless marked):
- Small palettes force consistency. 16 to 32 colours for a whole game is normal; 4 to 8 per sprite.
- Build ramps of 3 to 5 colours per material. Dark end shifts toward cool/purple/blue, light end toward warm/yellow. This is called hue shifting.
- Avoid pure black outlines everywhere; use a very dark tinted colour (selective outlining).
- Share ramps between sprites and tiles so the scene feels unified.
- Contrast between character and background: value first. Test in greyscale.
- Limit pure white and pure saturated colours to highlights and UI.
- Dithering approximates missing colours by mixing available ones, and matters most with 16 colours. VERIFIED (Wikipedia, Dither).
- Ordered dithering (Bayer) is stable between frames, good for animation, but poor with arbitrary palettes. Error diffusion (Floyd-Steinberg) adapts to custom palettes better. VERIFIED (same page). Pixel artists often hand-dither; that claim is COMMUNITY.
- Lock the palette before sprites exist; extra colours creep in. Lock the palette in your pixel-art tool (for example a colour-reduce function).

Known palettes (hex read from lospec.com pages):
- PICO-8, 16 colours (Lexaloffle's console; the Lospec page names no palette author): #000000 #1D2B53 #7E2553 #008751 #AB5236 #5F574F #C2C3C7 #FFF1E8 #FF004D #FFA300 #FFEC27 #00E436 #29ADFF #83769C #FF77A8 #FFCCAA. VERIFIED. Also usable in TIC-80 per a commenter (COMMUNITY).
- Sweetie 16, by GrafxKid, 16 colours: #1a1c2c #5d275d #b13e53 #ef7d57 #ffcd75 #a7f070 #38b764 #257179 #29366f #3b5dc9 #41a6f6 #73eff7 #f4f4f4 #94b0c2 #566c86 #333c57. VERIFIED.
- ENDESGA 32, by ENDESGA, 32 colours (hexes on lospec.com/palette-list/endesga-32). VERIFIED count and author.
- Resurrect 64, by Kerrie Lake, 64 colours. VERIFIED. Apollo, by AdamCYounis, 46 colours. VERIFIED.
- Lospec downloads: PNG, PAL, ASE, TXT, GPL, HEX. VERIFIED (PICO-8 page). Other popular names (DB16, DB32, AAP-64): UNVERIFIED, page failed or unread.
- Lospec "popular" list ranking: UNVERIFIED (page failed to fetch).

## 15. Print vs screen, merch, flyers

- Screens emit light (RGB). Ink absorbs light (CMYK). Gamuts differ both ways. VERIFIED (Wikipedia).
- sRGB gives accurate colour on most displays; P3 is richer on wide-colour screens. VERIFIED (Apple HIG).
- Neon, glowing cyan, hot pink, bright green often cannot print in CMYK. COMMUNITY. Show the proof and say it will look duller.
- Always ask the printer: colour profile they want, bleed, whether they print spot colours or white ink. UNVERIFIED, varies per printer.
- Rich black (CMY plus K) gives deeper black than K alone. VERIFIED (Wikipedia). Exact ink limits: ask the printer.
- Order a physical proof (one shirt, one flyer) before bulk merch. COMMUNITY.
- Keep merch art to few flat colours (screen printing costs by colour). COMMUNITY.
- Software for conversion (Inkscape, GIMP, Krita) and exact menu steps: see design-software-guide; UNVERIFIED here.

## 16. Genre colour associations (all UNVERIFIED opinion)

- Hardstyle: black with neon red, orange, electric blue; strong contrast; metallic and fire.
- Trance: deep blue, cyan, violet, white light; gradients, space, horizon glow.
- UK/happy hardcore, rave: saturated multi-colour, pink, yellow, green, cartoon energy.
- Hard dance flyers often use black backgrounds with one or two glowing accents; high contrast works for readability. 
- Treat these as a starting palette to react to, not as fact. Colour psychology evidence is mixed (section 11).

## 17. Brand palettes

- A brand palette is small: 1 primary, 1 accent, 3 to 5 neutrals, 4 status colours. COMMUNITY.
- Keep a light and a dark version (VERIFIED principle, Apple). Name and document tokens once, reuse on site, plugins, merch, flyers.
- Trademarked brand colours exist (Tiffany Blue example); do not copy famous brand colours. VERIFIED (Wikipedia, Colour psychology).
- Logos have no contrast requirement under WCAG, but still test legibility on dark and light. VERIFIED exemption.
- Write palette docs as: swatch, hex, OKLCH, role, allowed on which backgrounds, measured contrast.

## 18. Extracting and generating palettes

- Palette extraction treats colours as clusters in 3D space and averages each cluster. Methods: median cut (Heckbert, 1982, most popular), k-means, octree. VERIFIED (Wikipedia, Colour quantisation).
- Extraction is often paired with dithering to hide banding. VERIFIED.
- For a photo, flyer or reference game screenshot: extract 6 to 8 colours, then hand-fix ramps and contrast. Never ship an extracted palette unchecked. COMMUNITY.
- Coolors: spacebar generator, contrast checker, exports (URL, PDF, image, CSS, ASE, SVG, code, Tailwind). Free: up to 5 colours per palette, 10 saved palettes; palette contrast check, image colour picking and more than 5 colours are Pro. VERIFIED (coolors.co).
- Realtime Colors: five colours (text, background, primary, secondary, accent) shown on a live site, AA/AAA indicators, exports CSS, SCSS, Tailwind. Free. VERIFIED. Best for the Squarespace look.
- Leonardo (Adobe, open source): give target contrast ratios, it generates swatches that meet them. VERIFIED. Best for ramps that must pass.
- Lospec: palette list with downloads (section 14). VERIFIED. Adobe Color wheel: page not fetched, UNVERIFIED.
- Contrast Analyser (TPGi), WebAIM checker, "Accessible Colors": existence UNVERIFIED, not fetched.
- Palette files: GPL (GIMP, Inkscape, Krita read GPL) and ASE are offered by Lospec. Which app reads which format: UNVERIFIED, check in the app's palette docker.
- Linux pickers: KColorChooser (KDE), gpick, Inkscape/GIMP colour picker tool, KDE screen colour picker widget. All UNVERIFIED; install via Bazaar/Flatpak and check availability first.

## 19. Colour grading overview (images and video)

Deep photo grading and filters: photo-editing-color-grading skill. Here only the basics.
- Grading is post-production that alters image appearance for different presentation environments. Usually done in a dim suite. VERIFIED (Wikipedia, Color grading).
- Primary grading: whole frame, per-channel density curves. Secondary: isolates a range of hue, saturation or brightness via masks, shapes, keys. VERIFIED.
- Correction (fix exposure, white balance) comes before grading (creative look). The page says they are often used synonymously. VERIFIED; the order of work is COMMUNITY.
- Lift, gamma, gain: shadows, midtones, highlights controls. The fetched page did not cover them, so details are UNVERIFIED.
- A 3D LUT is a lattice of output RGB values indexed by input RGB; values between points are interpolated, usually trilinear. Used for grading and for mapping between colour spaces. 33x33x33 cubes are common. VERIFIED (Wikipedia, 3D lookup table). .cube file format: UNVERIFIED.
- Looks for music visuals (COMMUNITY): teal and orange for cinematic; crushed blacks plus magenta highlights for club; keep skin and logo colours readable.
- Grade on a calibrated monitor in a dim room if colour matters. Calibration tools on Linux: UNVERIFIED.

## 20. Worked example palettes (contrast measured by script)

A. Plugin night UI (dark, purple-tinted, amber accent). Format: role hex (OKLCH L C H).
- --bg #14121A (0.188 0.016 296), --surface #1D1A26 (0.227 0.023 296), --raised #272333 (0.268 0.030 296)
- --text #ECE8F4 (0.938 0.017 301), --text-muted #A9A2BC (0.727 0.038 298)
- --divider #4A4560 (0.407 0.045 293), --control-edge #7A7494 (0.576 0.049 293)
- --accent #FFB454 (0.824 0.141 70), --accent-2 #5FD3C8 (0.797 0.106 187)
- --ok #6FD08C, --warn #F2C14E, --err #FF7A7A
Measured: text on bg 15.40, on surface 14.18, on raised 12.67. Muted on bg 7.59, surface 6.99, raised 6.24. Accent on bg 10.53, on surface 9.70. Accent-2 on surface 9.48. Dark text #14121A on accent 10.53, on accent-2 10.29. ok on surface 9.02, warn 10.19, err 6.77. Control edge on bg 4.20, surface 3.87, raised 3.46 (passes 3:1). Divider on surface 1.88 (decorative only, fails 3:1 so never use it as a control edge). All text AAA. Surface vs bg is 1.09:1 so panels are separated by tone and edge, not contrast.

B. Squarespace site (light paper, deep orange accent, violet links).
- --bg #FBF8F3 (0.980 0.007 81), --surface #FFFFFF, --text #1E1B24 (0.230 0.018 300), --text-muted #5A5566 (0.461 0.028 299)
- --border #8C8579 (0.619 0.020 81), --accent #B4430B (0.533 0.158 41), --link #6A32B8 (0.468 0.197 297)
Measured: text on bg 16.02. Muted on bg 6.77, on white 7.18. Border on bg 3.45, on white 3.65 (passes 3:1). White on accent button 5.60 (AA). Accent as text on bg 5.29. Link on bg 7.18, on white 7.61. Dark-mode twin: reuse Palette A roles. Applying it in Squarespace: squarespace-expert skill.

C. Pixel palette, 12 of the 16 verified Sweetie 16 colours (GrafxKid), organised as ramps.
- Blue-grey ramp (dark to light): #1A1C2C (0.232 0.031 278), #333C57, #566C86, #94B0C2, #F4F4F4
- Warm accent ramp: #5D275D, #B13E53, #EF7D57, #FFCD75. Green ramp: #257179, #38B764, #A7F070
Measured on #1A1C2C: #F4F4F4 15.32, #94B0C2 7.42, #566C86 3.12, #FFCD75 11.43, #EF7D57 6.21, #38B764 6.52, #A7F070 12.31, #B13E53 2.96 (fails 3:1, use only on lighter ground). #94B0C2 on #333C57 4.80. #F4F4F4 on #5D275D 9.98. Dark #1A1C2C text on #FFCD75 11.43. Note the hue shift: ramp darks sit at hue 278 to 253 and lights at 236 to 90, measured. Use these hexes only as an example; check the project palette first.

## 21. Troubleshooting trees

Problem: "it looks muddy".
1. Squint or greyscale: are values too close? Move L apart by at least 0.1 OKLCH. 
2. Too many mid-chroma hues? Cut to one accent. 
3. Greys pure? Tint them (section 5).
Problem: "text hard to read".
1. Measure ratio. Below 4.5:1 for body text, fix the lighter or darker side by L, not hue.
2. Small text on accent? Use dark text on light accents (example A), white on deep accents (example B).
Problem: "colours look different on phone/print/site".
1. Same hex, different screens: check display profile and brightness. VERIFIED principle (Apple: test devices, P3 vs sRGB).
2. Print: CMYK gamut loss (section 15). Ask for a proof.
3. Squarespace colours off: confirm the hex in custom CSS vs style editor; mixed tokens cause drift. UNVERIFIED.
Problem: "status colours indistinguishable".
1. Add icon and label. 2. Vary lightness. 3. Test in a colour blindness simulator.
Problem: "pixel sprite has too many colours".
1. Reduce to the locked palette (your pixel-art tool). 2. Merge near-duplicate ramp steps. 3. Check by dithering sample at 1x.

## Not verified

- Material Design colour roles and dark theme exact numbers (pages need JavaScript).
- Adobe Color harmony names, NEI colour-blindness page (fetch failed), tritan prevalence.
- Lift/gamma/gain definition, .cube format, Lospec popularity ranking, DB16, AAP-64.
- Genre colour associations, GIMP/Inkscape/Krita palette format support, Linux colour pickers (KColorChooser, gpick), calibration tools.
- light-dark() CSS function, JUCE hex handling, Squarespace OKLCH support, printer ink limits.
- Hue-shift and 60-30-10 craft advice are COMMUNITY, not from a fetched page. Reddit r/PixelArt and r/UI_Design not fetched.
- WCAG: Understanding docs read, not the full TR/WCAG22 glossary (formula taken from Understanding 1.4.3).

## Sources (fetched)

- https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- https://www.w3.org/WAI/WCAG22/Understanding/contrast-enhanced.html
- https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
- https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html
- https://www.w3.org/WAI/perspective-videos/contrast/
- https://www.w3.org/TR/css-color-4/
- https://www.w3.org/TR/wcag-3.0/
- https://apcacontrast.com/
- https://evilmartians.com/chronicles/oklch-in-css-why-quit-rgb-hsl
- https://bottosson.github.io/posts/oklab/
- https://developer.apple.com/design/human-interface-guidelines/color.md
- https://lospec.com/palette-list/pico-8
- https://lospec.com/palette-list/sweetie-16
- https://lospec.com/palette-list/endesga-32
- https://lospec.com/palette-list/resurrect-64
- https://lospec.com/palette-list/apollo
- https://coolors.co/
- https://www.realtimecolors.com/
- https://leonardocolor.io/
- https://en.wikipedia.org/wiki/Color_blindness
- https://en.wikipedia.org/wiki/CMYK_color_model
- https://en.wikipedia.org/wiki/Color_psychology
- https://en.wikipedia.org/wiki/Color_grading
- https://en.wikipedia.org/wiki/3D_lookup_table
- https://en.wikipedia.org/wiki/Color_quantization
- https://en.wikipedia.org/wiki/Dither
