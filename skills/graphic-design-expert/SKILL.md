---
name: graphic-design-expert
description: Use when helping a non-programmer design plugin GUI mockups, album covers, logos, merch prints, gig posters, social images, Squarespace visuals or 16-bit pixel art with free Linux tools on Bazzite.
---

# Graphic design for a music producer on Bazzite (free tools)

Labels: VERIFIED (source) = read on a fetched page. COMMUNITY = widely repeated, third-party. UNVERIFIED = not read on a fetched page; check before relying on it.
Rules: say which tool and which menu. Assume the reader is not a programmer. Plain words first, then one exact step. One change at a time, ask the reader to test, then continue.
Hand off, do not duplicate: colour choice and palettes go to color-palette-expert. Screens, buttons, plugin panel usability go to ux-ui-designer. Colour grading, filters, retouching go to photo-editing-color-grading. Figma, Affinity, Adobe, website builders go to design-software-guide. Tablet setup goes to drawing-tablets. Squarespace specifics: squarespace-expert. Plugin mockups: vst-maker.

## Workflow for any job (follow in order)

1. Ask the goal, the audience, where it will be seen (phone, print, shirt, plugin window) and the final size.
2. Gather references (mood board, see below). Pick 2 fonts and the palette (color-palette-expert) before drawing.
3. Make 3 rough thumbnails in greyscale. Choose one.
4. Build in vector (Inkscape) or layers (GIMP/Krita) at final size, with bleed if it is for print.
5. Run the critique checklist. Fix. Export per the file spec for the destination.
6. Keep the editable source file and the exported file. Name them clearly (project-item-size-v1).

## Core principles (what makes a design work)

- Hierarchy: order elements so the eye reads them in order of importance. Tools: scale, colour and contrast, grouping. Max three sizes recommended. VERIFIED (NN/g visual hierarchy article).
- Squint test: blur or squint, see what still stands out. If the wrong thing stands out, fix hierarchy. VERIFIED (NN/g, Canva).
- Contrast: difference between elements (dark/light, thick/thin, large/small); improves legibility and draws the eye to key items. VERIFIED (Canva design elements and principles).
- Balance: distribute visual weight; symmetrical mirrors elements, asymmetrical offsets with size and placement. VERIFIED (Canva).
- Repetition: reuse logos, colours, typefaces, margins, patterns to unify. VERIFIED (Canva).
- Negative space (whitespace): empty area around elements; it separates groups and lets the eye rest. VERIFIED (Canva, NN/g).
- Grid: rows and columns that elements align to; this is the main alignment tool. VERIFIED (Canva).
- Proximity: items near each other read as related; items apart read as separate. Use space to group and separate. VERIFIED (NN/g Gestalt proximity).
- Alignment as its own rule (align edges, avoid near-misses): the grid link is VERIFIED; the "avoid near-misses" advice is UNVERIFIED general practice.
- Rule of thirds, rule of odds, leading lines for composition. VERIFIED (Canva visual hierarchy).
- Reading patterns: F pattern for text-heavy, Z pattern for sparse layouts. VERIFIED (Canva visual hierarchy).

### Gestalt, composition, storytelling (theory)

- Only proximity was read on a fetched page (VERIFIED, NN/g). The rest are UNVERIFIED here but standard teaching: similarity (alike items group), continuity (eye follows a line), closure (mind completes shapes), figure/ground (subject vs background), common region (a box groups items). NN/g also says borders or backgrounds can reinforce groups when spacing is not enough. VERIFIED.
- Focal point: one dominant thing per piece. A poster has one. If everything shouts, nothing does. UNVERIFIED general practice.
- Visual storytelling for covers and posters: one clear subject, one mood, one idea the viewer gets in two seconds. UNVERIFIED general practice.
- Brand idea: a repeatable motif (for example an animal silhouette, a paw, eyes) used big, small and as pattern gives repetition and recognition. UNVERIFIED suggestion.

## Typography

- Hierarchy in text: three levels, a primary element, secondary section labels, readable body text. VERIFIED (Canva visual hierarchy).
- Families: serif, sans-serif, script, display (bold, italic styles) set mood and emphasis. VERIFIED that category choice supports mood (Canva); the classification list itself is UNVERIFIED general practice.
- Pairing rules of thumb: use two typefaces, one display for headlines and one plain for body; contrast them, do not pair two similar ones. Canva font-pairing page failed to load. UNVERIFIED.
- Size scale: pick a ratio (for example each step about 1.25 to 1.5 times the last) and stay with it. UNVERIFIED general practice.
- Line height about 1.4 to 1.6 for body text; tighten for big headlines. Kerning: adjust letter pairs by eye in logos and big titles, then flip the design upside down to check. UNVERIFIED general practice.
- Never use more than 2 or 3 fonts in a piece. UNVERIFIED general practice.
- Text size for screens: WCAG treats 18 pt (about 24 px) or 14 pt bold (about 18.5 px) as "large text". VERIFIED (W3C contrast-minimum).
- Convert text to outlines/paths in logos and print files so the font is not needed later (Inkscape: Path, Object to Path). Inkscape menu name UNVERIFIED.

### Free fonts and licensing

- Google Fonts is open, with a stylesheet link method for websites. VERIFIED (Google Fonts getting started). That page does not state licences or file download; check fonts.google.com/faq. Its FAQ text did not load. UNVERIFIED.
- SIL Open Font License (OFL) per its FAQ: usable for any design work including logos, posters, business cards and merchandise without an extra licence (1.1); your artwork stays yours (1.1.1); no acknowledgement needed (1.1.2). VERIFIED (openfontlicense.org FAQ).
- OFL: you may not sell the font by itself (1.6); you may sell software that includes it (1.4); embedding in documents is allowed (1.12). Modified versions cannot use a declared Reserved Font Name (3.1, 5.3). VERIFIED (same).
- Always keep a note of font name and licence for each project. Not all fonts on the web are free for commercial use; check each one. UNVERIFIED general advice.
- Linux install of a font (UNVERIFIED, standard practice): copy .ttf/.otf files to ~/.local/share/fonts, then run `fc-cache -f`, restart the app. Flatpak apps may need a restart; sandboxed apps read host fonts through a Flatpak setting that UNVERIFIED on Bazzite. KDE System Settings has a Fonts install page. UNVERIFIED.

## Vector, raster, resolution, formats

- Raster (pixels): photos, textures, pixel art; blurs when scaled up. Vector (maths): logos, icons, type; scales to any size. SVG "stays small by storing mathematical values". VERIFIED (Krita file formats overview).
- Lossy: JPG and WebP. Lossless: PNG, GIF, BMP. VERIFIED (Krita overview).
- PSD is largely closed; SVG can be opened in any text editor; formats can store an ICC colour profile in metadata. VERIFIED (Krita overview).
- Keep layered working files (XCF in GIMP, KRA in Krita, SVG in Inkscape) and export copies. Native format names: KRA VERIFIED (Krita); XCF and Inkscape SVG UNVERIFIED here.
- Rules of thumb (UNVERIFIED general practice): logos in SVG plus a PNG; photos JPG; screenshots, transparency and pixel art PNG; PDF for print and multi-page; TIFF for print masters; EPS only when a printer asks for it. Never upscale pixel art with smoothing; scale by whole numbers with nearest-neighbour.
- DPI only matters for print: pixels needed = inches x DPI. Screens use pixel size. UNVERIFIED general practice.

## Colour modes and print-ready basics (palette choice: color-palette-expert)

- RGB for screens, CMYK for offset print. Printful says use sRGB (IEC61966-2.1), its CMYK process is tuned for RGB files, though its FAQ suggests CMYK PDF/TIFF for offset printing (a conflict inside the page). VERIFIED (Printful print file blog).
- Printify: save in sRGB; wide-gamut colours can print dull or shifted. VERIFIED (Printify knowledge hub).
- Scribus supports CMYK, spot colour, EPS import/export and colour separations, and produces PDF and PostScript output. VERIFIED (Flathub listing).
- GIMP and Krita are mainly RGB tools; for a CMYK print shop PDF use Scribus, or ask the shop whether sRGB is accepted. UNVERIFIED.
- Bleed: typical 0.125 in (1/8 in) on each edge, 0.25 in for prints 24 in and up. Safe zone typically 0.125 in inside the trim line. Example: 8x10 in print with bleed is 8.25x10.25 in at 300 DPI CMYK. VERIFIED (Printkeg guide, third-party tool site, so COMMUNITY strength). Always use the shop's own template.
- Printful: fill the whole bleed area to avoid white borders or blank fabric. VERIFIED (Printful blog).
- Pantone (spot) vs process (CMYK): spot is a pre-mixed ink for exact brand colour, process mixes 4 inks. UNVERIFIED general practice. Print-on-demand shops here use RGB files, so Pantone matters only for screen print or offset jobs.
- ICC profile: embed one (sRGB) when exporting so colours are read the same. Formats can carry it. VERIFIED that formats can store ICC (Krita overview); the advice to embed sRGB is COMMUNITY.

## Album and music platform specs

- Apple Music Curator cover art page: minimum 3000x3000 px, 72 dpi minimum, PNG with no transparency, RGB. VERIFIED (help.apple.com Music curator best practices). That page is for curators, not the release itself; for releases the distributor's delivery spec rules. UNVERIFIED.
- Spotify artist images (support.spotify.com): avatar at least 750x750, header at least 2660x1140, gallery at least 690x500, JPEG/PNG/GIF, max 20 MB. VERIFIED (Spotify artist image guidelines).
- Spotify release cover size: not on a fetched official page. Industry norm is a square 3000x3000 JPG or PNG in RGB (RouteNote says "3000x3000 or larger" as its own advice). COMMUNITY. Check the distributor's current minimum before upload. VERIFIED that RouteNote says to check the distributor.
- Design rules for covers (UNVERIFIED general practice): must still read at 100x100 px thumbnail; big simple type; no tiny text; keep key art inside the centre 80 percent; check in both light and dark app themes.
- Do the thumbnail check yourself: export a 150 px version and look at it on a phone.

## T-shirt and merch print files (print on demand)

- Printful accepts JPEG, PNG, SVG; recommended 300 DPI for JPEG/PNG; large format 120 to 150 DPI; max 100 MB for JPEG/PNG and 20 MB for SVG. VERIFIED (support.printful.com file types page).
- Printful blog (different page): 150 to 300 DPI ideal, 150 the sweet spot; 300 for small detailed items; T-shirt print area up to 12x16 in, select DTG up to 15x18 in; uploads up to 200 MB. The two Printful pages differ on file size limits, so trust the Design Maker for the product. VERIFIED, with conflict noted.
- Printful dimensions are per product; use the File guidelines tab template. VERIFIED.
- Printful DTG transparency: fully transparent areas vanish; semi-transparent areas can show the white underbase as speckles on dark garments. A black background on a black shirt prints as a grey rectangle, so remove backgrounds. VERIFIED (Printful blog).
- Printify: 300 DPI at physical scale, standard canvas 4500x5400 px (15x18 in), sRGB, PNG with 100 percent transparent background (8-bit alpha), zero semi-transparent pixels. VERIFIED (Printify PNG setup page). Printify upload size limit not on that page. UNVERIFIED.
- Practical recipe: make the design in Inkscape, export PNG at 4500x5400 with transparent background; in GIMP use Layer, Transparency, Threshold Alpha to remove soft edges. Menu names UNVERIFIED.
- Dark shirt vs light shirt: check the design on both; have a one-colour version. UNVERIFIED.
- Embroidery: Printful requires PNG for embroidery. VERIFIED.
- Hang tags, neck labels, packaging: ask the shop for templates. UNVERIFIED.

## Posters, flyers, social images, web

- Common poster sizes (UNVERIFIED general knowledge): A3 297x420 mm, A2 420x594 mm, A4 210x297 mm, 18x24 in and 24x36 in in the US. Add bleed (see above), keep text in the safe zone, 300 DPI at final size.
- Gig poster structure (UNVERIFIED general practice): artist name biggest, date and venue second, support acts and ticket info third, URL or QR last. Legible from 2 m away.
- Social image sizes: not read on any official platform page this session. UNVERIFIED for Instagram, YouTube, Facebook and others. Ask the person you help to confirm current sizes on the platform, or fetch the platform help page first. RouteNote lists 1080x1920 (9:16) and 1920x1080 (16:9) for video and social posts, not covering stills; COMMUNITY.
- Squarespace images (squarespace-expert covers the rest): the seospace.co third-party article says upload 1500 to 2500 px wide, display images under 250 KB, banners under 500 KB, JPG/GIF/PNG accepted, SVG and PDF not accepted as images, RGB, 60 MP limit. COMMUNITY, third party, not Squarespace itself. Verify on Squarespace support.
- Use alt text on web images: write alt text when the image conveys information or function, empty alt when decorative or when it repeats nearby text. VERIFIED (W3C alt decision tree).

## Logo design, branding and identity systems

- Brand identity has visual parts (logo, colours, typography, imagery style) and verbal parts (name, tone, story, tagline). VERIFIED (Canva brand identity).
- Brand guidelines: a style guide, shared templates, consistency across touchpoints ("arguably the most important factor"), scalability rules, a refresh policy. VERIFIED (Canva).
- Logo should be "simple, unique, and memorable". VERIFIED (Canva brand identity).
- Logo checklist (UNVERIFIED general practice): works at 16 px favicon and on a billboard; has a one-colour version in black and in white; has a horizontal and a stacked version; clear space around it equal to a chosen unit (for example the height of one letter of the name); minimum size stated; no gradients or tiny details that fail in embroidery or screen print; supply SVG and PNG.
- Identity system for a studio or artist brand: mark, wordmark, 2 fonts, palette (color-palette-expert), motif (for example a mascot or a paw), pattern, photo/illustration style, voice. One page style sheet saved in the project docs.
- Mood board: 10 to 20 images, colours, textures and type samples saved in one folder or Penpot/Krita canvas; pick 3 words for the mood and test every draft against them. Process is UNVERIFIED general practice.

## Licensing and legal (not legal advice)

- OFL fonts: see typography section. VERIFIED.
- AI images: the US Copyright Office Part 2 report concludes purely AI-generated material is not protected, prompts alone are not enough, repeated prompting or picking among outputs is not authorship, but human-authored expression, creative selection/arrangement and creative modifications can be protected. VERIFIED (copyright.gov report PDF). So for a logo or cover you want to own, draw or heavily modify it by hand. Other countries and each AI tool's terms: UNVERIFIED, read the tool's terms before commercial use.
- Trademark vs copyright: the USPTO page was blocked, so definitions here are UNVERIFIED. General practice: search for similar names and logos in your market before launching a brand; do not copy another brand's logo. Consider a lawyer for registration.
- Stock images and photos: read each licence (commercial use, merch use, resale as part of a template). UNVERIFIED. For merch, many stock licences forbid use as the main item sold. UNVERIFIED.
- Do not use copyrighted characters, band logos or sample art in merch. UNVERIFIED general advice.
- AI sprite and image generators: store the tool name and terms with the asset. PixelLab terms are linked from its MCP server (pixellab.ai/termsofservice). VERIFIED (tool description).

## Accessibility

- Text contrast AA: 4.5:1 normal text, 3:1 large text. Not rounded (4.499 fails). VERIFIED (W3C contrast-minimum).
- UI components and graphics needed to understand content: 3:1. VERIFIED (W3C non-text contrast). Applies to plugin knobs, buttons and chart lines on a website; see ux-ui-designer.
- Do not use colour as the only way to show meaning; add text, icon or shape. VERIFIED (W3C use of colour).
- Pointer targets at least 24x24 CSS px (WCAG 2.2), with exceptions. VERIFIED (W3C target size minimum).
- Alt text rules: see social/web section. VERIFIED.
- Nielsen's heuristic "Aesthetic and Minimalist Design" supports removing clutter. VERIFIED (NN/g ten heuristics list).

## Linux tool guide (Bazzite: Flatpak first, as in bazzite-kde-linux)

Install route: Bazaar or Discover store, or `flatpak install flathub <id>`. App IDs below were read on Flathub pages unless stated. Flathub states several are community packages, not verified by the developers.

| Job | Tool | Flatpak ID | Notes |
|---|---|---|---|
| Photo/raster edit, T-shirt PNG, covers | GIMP | org.gimp.GIMP | VERIFIED ID. gimp.org lists stable 3.2.6 (2026-09-10), Flatpak for x86_64 and ARM64, `flatpak install --user https://flathub.org/repo/appstream/org.gimp.GIMP.flatpakref`, run with `flatpak run org.gimp.GIMP//stable` |
| Logos, posters, vector merch | Inkscape | org.inkscape.Inkscape | VERIFIED ID. Native format SVG: UNVERIFIED (README did not load) |
| Painting, illustration, texture | Krita | org.kde.krita | VERIFIED. Docs: Flatpak is on Flathub but not maintained or tested by core developers, may have bugs |
| Print layout, CMYK, PDF | Scribus | net.scribus.Scribus | VERIFIED. Community-provided package. Docs site blocked, so bleed and PDF/X menu steps UNVERIFIED |
| Interface mockups, plugin GUI, web | Penpot | web app, self-host option | VERIFIED open source, SVG/CSS/HTML/JSON standards, self-host page exists. License name and export steps UNVERIFIED. Docs: help.penpot.app |
| Photo develop (raw) | Darktable | org.darktable.Darktable | VERIFIED. Grading: photo-editing-color-grading |
| 3D logos, mockup renders | Blender | org.blender.Blender | VERIFIED. Basics below |
| Pixel art, animation | Pixelorama | com.orama_interactive.Pixelorama | VERIFIED ID. MIT license; exports PNG, animated PNG, spritesheets, GIF, video; indexed mode, tilemap layers, palettes, onion skin (GitHub page) |
| Pixel art, Aseprite-like | LibreSprite | com.github.libresprite.LibreSprite | VERIFIED ID (the org.libresprite ID page failed). GPLv2 fork of the last GPL Aseprite commit, independent now. Development pace UNVERIFIED |
| Pixel art (paid) | Aseprite | Steam or build from source | Source and official binaries under the Aseprite EULA, not open source. Whether binaries are free of charge: UNVERIFIED. Build steps in INSTALL.md in the repo. |

Basic recipes (all menu names UNVERIFIED, from general practice, check in the app):
- Inkscape logo: draw at 1000x1000 px page, use Boolean Path operations, convert text to paths, save plain SVG, export PNG at needed size.
- GIMP cover: new image 3000x3000 px, work in layers, Export As JPG/PNG. For a plugin mockup background, 1:1 pixel size of the real window.
- Krita: new document with transparent background, 300 DPI for print, export PNG.
- Scribus poster: set page size plus bleed in New Document, import SVG/PNG, Export as PDF.
- Blender: free 3D; use for a rendered logo object or product mockup, render a transparent PNG (Film, Transparent). UNVERIFIED.
- Pixel art workflow for a game: work at native size (for example 16x16 or 32x32 tiles), limited palette (color-palette-expert), no anti-aliasing blur, no rotation after drawing, export PNG, scale by integers. UNVERIFIED general practice; follow pixel-art-sprite-master for style.
- Plugin GUI mockup: use Penpot or Inkscape at exact plugin window pixels; export PNG; see vst-maker.

## Troubleshooting (ask these in order)

1. Print looks blurry: is pixel size at least inches x 150? If not, redo at a larger canvas. If it is a logo, redo as vector. Upscaling by AI is a last resort, check result by eye. UNVERIFIED.
2. Colours look dull in print: was the file wide-gamut or CMYK-converted? Re-export as sRGB; check the shop preview. VERIFIED for sRGB advice (Printify, Printful).
3. White speckles or halo on a dark shirt: semi-transparent pixels. Threshold the alpha or avoid soft glows. VERIFIED (Printful, Printify).
4. Grey box behind the print: remove the background layer, export PNG. VERIFIED (Printful).
5. Font missing on another PC or print shop: convert text to paths or embed fonts in the PDF. UNVERIFIED.
6. Fonts not showing in a Flatpak app: restart the app, check ~/.local/share/fonts. UNVERIFIED.
7. Flatpak app cannot see a folder: use Flatseal or the file dialog portal. UNVERIFIED.
8. Design feels flat or messy: run the critique checklist; usually hierarchy, spacing or too many fonts.
9. Upload rejected: compare with the destination spec above; check file size and colour mode first.

## Design critique checklist (score each yes/no)

1. Squint test: does the main thing stand out first, second thing second? VERIFIED method.
2. One focal point, three or fewer text sizes? VERIFIED (NN/g size limit).
3. Are related items close and unrelated items apart (proximity)? VERIFIED.
4. Is everything aligned to a grid or shared edges? VERIFIED (grid) / UNVERIFIED (near-misses).
5. Enough whitespace; nothing touching the edge inside the safe zone?
6. Max 2 fonts, licences recorded? (UNVERIFIED rule, OFL VERIFIED)
7. Text contrast 4.5:1 (3:1 large)? Graphics 3:1? Meaning not by colour alone? VERIFIED.
8. Readable at thumbnail size and at full size?
9. Matches the brand system: palette, fonts, motif repeated? VERIFIED (consistency).
10. Works in one colour / on dark and light backgrounds?
11. Correct size, bleed, colour mode, format for the destination?
12. Rights cleared: fonts, images, AI output, trademarks?
Give feedback as: what works, top 3 fixes in priority order, then one example change. Ask the person you help one question at a time.

## Brief template (for a human designer or an AI image tool)

```
Goal: (what it is for, one sentence)
Audience: (who sees it, where: phone, shirt, poster wall)
Deliverable: (item, final size in px or mm, format, bleed, colour mode)
Mood: 3 words. References: 3 to 5 links or files, and what to take from each
Must include: (name, text exact spelling, logo file, date, URL)
Style: (flat vector / pixel art 32x32 / grunge / 16-bit), motif details
Palette: (hex values from color-palette-expert) Fonts: (names)
Avoid: (clichés, copyrighted things, tiny text)
Variations: (1-colour, dark and light)
Rights: who owns it, AI allowed or not
```
For AI image tools: write the subject first, then style, then composition ("centered, flat background, empty space at top for the title"), then what to avoid. Generate many, pick the best, then redraw or edit by hand. UNVERIFIED practice. Never let the AI draw the final text; add type yourself in Inkscape or GIMP.

## Not verified (could not read, or not sourced)

- Social platform image sizes (Instagram, Facebook, YouTube, TikTok), Spotify release cover size on an official page, Printify upload size limit and product-specific print areas.
- Google Fonts FAQ licence text, Google Fonts download steps, Canva font pairing and logo tips, USPTO trademark page, Adobe bleed/CMYK guides.
- Gestalt principles other than proximity; font pairing, size scale, line height, kerning values; poster size lists; logo clear-space rules.
- Inkscape, GIMP, Scribus, Krita official docs menu names and recipes; Scribus bleed/PDF settings; Penpot export and license; Aseprite price; LibreSprite maintenance status.
- Linux font install path details, Flatpak permissions for fonts and folders on Bazzite.
- Reddit r/graphic_design, r/gimp, r/inkscape: blocked by the proxy, not read.
- Stock image and trademark licensing rules by country.

## Sources (fetched)

- W3C WCAG 2.2: Understanding contrast-minimum, non-text-contrast, use-of-color, target-size-minimum; W3C WAI images decision tree.
- Nielsen Norman Group: ten usability heuristics; visual hierarchy; Gestalt proximity.
- Canva Learn: design elements and principles; visual hierarchy; brand identity.
- SIL OFL FAQ (openfontlicense.org/ofl-faq); Google Fonts getting started (developers.google.com/fonts/docs/getting_started).
- Printful: support.printful.com/hc/en-us/articles/41396495537553; printful.com/blog/how-to-create-perfect-printfile; printful.com/blog/everything-you-need-to-know-to-prepare-the-perfect-printfile.
- Printify knowledge hub: printify.com/knowledge-hub/png-file-setup-for-tshirts.
- Apple Music curator best practices (help.apple.com/itc/musiccuratorbestpractices); Spotify artist image guidelines (support.spotify.com/artists/article/artist-image-guidelines); RouteNote artwork sizes article.
- US Copyright Office: Copyright and AI Part 2 report (copyright.gov PDF).
- Printkeg bleed and safe zone guide; SEOSpace Squarespace image size article (third party).
- Flathub: GIMP, Inkscape, Scribus, Darktable, Blender, Pixelorama, LibreSprite; gimp.org downloads; Krita manual (installation, file formats); Penpot home and user guide index; GitHub: Pixelorama, LibreSprite, Aseprite.
