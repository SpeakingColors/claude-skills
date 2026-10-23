---
name: design-software-guide
description: Use when choosing or using design software (Figma, Penpot, Affinity, Adobe, Canva, GIMP, Inkscape, Krita, Scribus, Webflow) on Bazzite, Windows or macOS for plugin mockups, websites, posters, merch.
---

# Design Software Guide (Bazzite first, Windows and macOS too)

## 0. How to work with the reader
- Assume the reader is not a programmer. Plain words first, then one exact step. One change at a time, ask the reader to test, then continue.
- Give the exact click path for each step.
- Labels: VERIFIED (source), COMMUNITY (forum, news or user report), UNVERIFIED (not read on a fetched page, say so, never guess).
- Date of this guide: 2026-10-23. Prices and plans change. Always tell the reader to check the live pricing page before paying.
- Research limit: my web fetch tool hit its hourly limit during research. Most vendor pages were NOT read. Where a fact comes from my own background knowledge, it is marked UNVERIFIED. Re-verify before relying on it.
- Parallel skills, use them instead of repeating their content:
  - graphic-design-expert: layout, type, logo and poster craft.
  - color-palette-expert: palettes, contrast, brand colours.
  - ux-ui-designer: wireframes, flows, usability, responsive thinking.
  - photo-editing-color-grading: photo retouch and grade.
  - drawing-tablets: Wacom, Huion, XP-Pen setup on Linux.
  - squarespace-expert: generic Squarespace 7.1 guide.
  - vst-maker: plugin GUI mockups and plugin building.
  - wine-proton-bottles: the full Bottles and Wine method.
- Note: some parallel skills may not be installed yet. If a name is missing, say so and carry on.

## 1. Questions to ask the reader first (so advice fits)
- Is there an existing website, on which builder and plan (Squarespace 7.1: see squarespace-expert)?
- Is there a plugin suite or app GUI? Rule: the approved mockup is the product. The real editor must match it.
- Is merch or print involved (Printful or Printify mockups through Squarespace, logos and posters)?

## 2. Quick answer: which tool for which job on Bazzite
| Job | First choice | Why | Backup |
|---|---|---|---|
| Plugin GUI mockup | Figma in browser or Penpot | Vector, components, export SVG and PNG | Inkscape |
| Plugin knob filmstrips, textures | Krita or GIMP | Raster painting, layers | Blender render |
| Website wireframe | Penpot or Figma | Frames, auto layout | Excalidraw |
| Website high fidelity | Figma or Penpot | Breakpoints, handoff | Framer, Webflow |
| Squarespace page | Squarespace editor itself | Fluid Engine | Canva for images |
| Logo | Inkscape | SVG, true vector, free | Affinity under Wine, Figma |
| Poster, print | Inkscape plus Scribus, or Canva | CMYK PDF with bleed (Scribus) | Affinity, Adobe |
| Photo edit | GIMP 3 | Layers, masks, curves | Photopea, Krita |
| Pixel art | Aseprite, LibreSprite or Pixelorama | Animation tools | Krita |
| Open a PSD someone sent | Photopea, then GIMP or Krita | No install | none |

## 3. Install methods on Bazzite (pick in this order)
1. Flathub Flatpak via Discover or terminal: `flatpak install flathub <app id>`. Safe on immutable systems.
2. Web app or PWA: open the site in Chromium or Firefox. In Chromium choose Install (adds a launcher). Works for Figma, Penpot, Canva, Photopea, Excalidraw, Framer, Webflow.
3. Bottles (Wine) for Windows only apps. See section 18 and the wine-proton-bottles skill.
- Flatpak IDs I trust from memory (UNVERIFIED unless noted): GIMP org.gimp.GIMP (VERIFIED, flathub.org page), Inkscape org.inkscape.Inkscape, Krita org.kde.krita, Scribus net.scribus.Scribus, Blender org.blender.Blender, Pixelorama com.orama_interactive.Pixelorama.
- Check any ID first: `flatpak search <name>`.

## 4. Figma
- For: UI design, plugin GUI layouts, website mockups, prototypes, handoff.
- Price, plans (partly VERIFIED for Penpot only; Figma NOT read): Figma has a free Starter plan and paid Professional, Organization and Enterprise plans (UNVERIFIED). Seats are split into Full, Dev and Collab (UNVERIFIED). A web search showed an official Figma help article titled "Updates to Figma's pricing, seats, and billing experience" (COMMUNITY, search title only). Tell the reader to open figma.com/pricing and read the Starter column.
- Dev Mode: paid feature, inspect panel, code snippets, variables, Ready for dev status (UNVERIFIED on price and tier today). Free plan can view but limits are UNVERIFIED.
- Figma Make and AI credits exist (COMMUNITY, search result titles mention Make and credits). Details UNVERIFIED.
- OS: web app in any browser (UNVERIFIED but long standing). Desktop app is Windows and macOS only (UNVERIFIED). No official Linux app.
- Bazzite: use Chromium or Firefox web app. Install as PWA for its own window. Unofficial Flatpak or AppImage wrappers exist (UNVERIFIED, avoid for account sign in).
- Beginner flow:
  1. New design file. Press F for Frame (a screen or a plugin window).
  2. Draw shapes (R rectangle, O ellipse, L line, T text).
  3. Select items, press Ctrl+Alt+G (Cmd+Opt+G) for Frame selection.
  4. Make a repeated item a Component: Ctrl+Alt+K (Cmd+Opt+K).
  5. Use Auto layout: Shift+A, so spacing stays tidy.
  6. Name layers clearly (knob_cutoff, label_title).
  7. Prototype tab links frames for click tests.
- Shortcuts (UNVERIFIED, standard): V move, F frame, R rect, O ellipse, T text, P pen, K scale, Shift+A auto layout, Ctrl+D duplicate, Ctrl+G group, Ctrl+Shift+E export, Ctrl+/ quick actions, Shift+1 zoom to fit.
- Formats: native .fig (proprietary). Imports SVG, PNG, JPG. Exports PNG, JPG, SVG, PDF. Figma cannot be saved as a local file for editing offline in browser (UNVERIFIED).
- Export settings: PNG at 1x and 2x for web, 2x and 3x for retina previews. SVG for icons, tick "Include id attribute" only if needed. Outline text before SVG export if the font will be missing.
- Limits: cloud only, account needed, paid dev features, no Linux app, file lock in to .fig.

## 5. Penpot
- For: free open source Figma alternative. Good for mockups and handoff.
- Features (VERIFIED, same page): unlimited teams, CSS Grid and Flex layouts, design tokens, libraries, templates, developer handoff, Penpot MCP server.
- Price (VERIFIED, penpot.app/pricing): Professional $0 per user, "free and fully featured, with no limits on tools". Unlimited $7 per editor per month, capped at $175 per month. Enterprise $25 per member. Private Server $50k per year. Non profit, education and open source discounts exist.
- Self hosting is possible (VERIFIED, same page). Requirements not listed there (UNVERIFIED). Typically Docker (UNVERIFIED).
- OS: web app in any browser (UNVERIFIED but implied by cloud plans). Works on Bazzite in Chromium or Firefox.
- Beginner flow: same ideas as Figma. Board (frame), rectangles, text, components, flex layout, then Inspect tab for handoff.
- Formats: .penpot file export. SVG, PNG, JPG, PDF export (UNVERIFIED). SVG import good.
- Recommendation: start plugin and web mockups here if zero cost and no account lock in matter.

## 6. Affinity (Photo, Designer, Publisher, now unified)
- WARNING: status changed in late 2025. Re-verify at affinity.studio and affinity.serif.com.
- Search result titles (COMMUNITY): "Affinity by Canva Is a Free Photo, Design and Layout Bundle" (etcentric.org), "Affinity Goes Completely Free with Unified Mac App" (igeeksblog.com), "Affinity's new design platform combines everything into one app" (The Verge). Page bodies were NOT read.
- Canva pricing page (VERIFIED, canva.com/pricing): Free plan lists "Access to Affinity". Pro, Business and Enterprise list "Access to Affinity with AI". So Affinity is free, and AI features sit in paid Canva plans.
- What I believe (UNVERIFIED): one unified app with Photo, Vector and Layout "studios" replaced the three separate Affinity 2 apps. Free with a Canva account. Windows and macOS. iPad later. Old Affinity 2 one time purchases may still run.
- Linux: no official build (UNVERIFIED). Search titles (COMMUNITY): "Unofficial AppImage Lets You Run Canva's Affinity on Ubuntu" (OMG! Ubuntu via linux.org) and "I Ran the Famed Affinity Designer on Linux. Here's How It Went". Contents NOT read.
- Bazzite plan, in order (UNVERIFIED, test one at a time):
  1. Check the official site first for a Linux or web version.
  2. Bottles with a recent Wine or Proton runner and the community Affinity patches. Read the wine-proton-bottles skill. Expect GPU and UI glitches.
  3. Use Windows or macOS for Affinity jobs.
- Formats: .afphoto .afdesign .afpub (old), new unified format unknown (UNVERIFIED). Imports PSD, AI (PDF compatible), SVG, PDF. Exports PDF, SVG, PNG, JPG, TIFF, EPS.
- Limits: no Linux, AI features paid, Canva account tie.

## 7. Adobe Photoshop, Illustrator, InDesign, Express
- Price: Creative Cloud is subscription only. I did not read adobe.com. Search results (COMMUNITY titles only) show 2026 articles, including "When should you upgrade to Adobe Creative Cloud Pro?" (TechRadar). Pro is the name of the all apps plan (COMMUNITY). Prices UNVERIFIED. Tell the reader to read adobe.com/creativecloud/plans.html.
- OS: Photoshop, Illustrator, InDesign run on Windows and macOS only. No Linux (UNVERIFIED but long standing). Express runs in the browser.
- Bazzite: not recommended.
  - Adobe CC through Wine/Bottles: unreliable (UNVERIFIED, WineHQ AppDB not read). Old versions (CS6, CC 2015 to 2021) sometimes work, new ones need the Creative Cloud installer and often fail (UNVERIFIED).
  - Better: use Photopea for PSD and AI files, Krita or GIMP for raster work, Inkscape for vector, Scribus for print layout.
- Formats: PSD, AI, INDD, all proprietary. AI is PDF based so Inkscape and Affinity open most. INDD only opens in InDesign. IDML is the exchange format (UNVERIFIED).
- Limits: subscription, no Linux, heavy.

## 8. Canva
- For: fast posters, social posts, simple merch art, brand templates.
- Price (VERIFIED, canva.com/pricing, yearly figures in US$): Free $0, Pro $144 per year for one person, Business $250 per year per person, Enterprise contact sales. Save from 16 percent on yearly billing. The page text did not show monthly prices.
- Plan details (VERIFIED, same page): Brand Kits 1 (3 colours only) on Free, 5 on Pro, 100 on Business, 1,000 on Enterprise. Cloud storage 5GB, 100GB, 500GB, 1TB. Pro lists AI tools including resize and background removal.
- Export list on the page: PDF, JPG, PNG and print ready CMYK export. Which plan gets which was NOT visible (UNVERIFIED). Transparent PNG and background remover are usually paid (UNVERIFIED).
- OS: web app, any browser. Desktop apps for Windows and macOS (UNVERIFIED).
- Bazzite: web. Install as PWA in Chromium.
- Beginner flow: pick a size, pick a template, upload brand fonts and colours, edit, Share > Download.
- Export: PNG for web, PDF Print for print (tick Crop marks and bleed), SVG is paid (UNVERIFIED).
- Limits: not true vector control, brand risk from stock templates, plan gating, cloud only. Check licence terms before putting Canva stock on merch (UNVERIFIED).

## 9. GIMP 3.x
- For: photo edits, textures, raster mockup parts, converting formats.
- Price: free software (VERIFIED, flathub.org page says "Free Software", licence text not shown there). GPL (UNVERIFIED).
- Version (VERIFIED, Flathub page fetched today): 3.2.6, described as a bugfix release of GIMP 3.2, released about a month ago.
- OS: Windows, macOS, Linux (UNVERIFIED but standard).
- Install on Bazzite: Flathub org.gimp.GIMP (VERIFIED ID). Often preinstalled or one click in Discover.
- Beginner flow:
  1. File > Open. Image > Scale Image for size.
  2. Layers dock: new layer, add Layer Mask for non destructive edits.
  3. Use Colors > Curves for tone. Use Filters for blur and sharpen.
  4. File > Export As (not Save). Save keeps XCF.
- Shortcuts (UNVERIFIED): Ctrl+Z undo, Ctrl+Shift+N new layer, Ctrl+Shift+E export as, Ctrl+E export again, Shift+Ctrl+J fit image in window, X swap colours, D default colours, Q quick mask.
- Formats: XCF native. Opens PSD (layers kept, mostly), PNG, JPG, WebP, TIFF, SVG as raster, PDF as raster. Exports PNG, JPG, WebP, TIFF, PDF, ORA.
- CMYK: GIMP 3 works mainly in RGB. Real CMYK print work is limited (UNVERIFIED). Use Scribus or Inkscape plus a printer profile for CMYK PDFs.
- Limits: weaker text and vector tools, steeper UI, no real CMYK workflow.

## 10. Inkscape
- For: logos, icons, posters, merch vector art, plugin knob and panel art, SVG export.
- Price: free, open source (UNVERIFIED on page, gimp.org and inkscape.org not read). GPL (UNVERIFIED).
- Version: 1.4.x line known to me (UNVERIFIED). Check About.
- OS: Windows, macOS, Linux (UNVERIFIED).
- Install: Flathub org.inkscape.Inkscape (UNVERIFIED ID, check with flatpak search).
- Beginner flow for a logo:
  1. File > Document Properties. Set size in px or mm.
  2. Draw with shapes. Combine with Path > Union / Difference.
  3. Type text. Choose font. Then Path > Object to Path before sending anywhere.
  4. Use Path > Simplify for traced shapes. Use Path > Trace Bitmap to vectorise a sketch.
  5. Save as Inkscape SVG. Export PNG with File > Export (Ctrl+Shift+E).
- Shortcuts (UNVERIFIED): S select, N node tool, B pen, R rect, E ellipse, T text, Ctrl+D duplicate, Ctrl+G group, Ctrl+Shift+C object to path, Ctrl++ union, Ctrl+- difference, 5 fit page, 3 fit drawing.
- Formats: SVG native. Imports AI (older ones), PDF, EPS, PNG. Exports SVG (plain), PDF, EPS, PNG, DXF.
- Export for web: Plain SVG, text converted to paths. PNG at 96 dpi for 1x. For print: PDF with fonts embedded or converted.
- CMYK: Inkscape is RGB. CMYK output is limited (UNVERIFIED). For CMYK, make the final PDF in Scribus, or ask the printer if RGB is fine.
- Limits: slow on huge files, UI has many dialogs, weak CMYK.

## 11. Krita
- For: painting, textures, knob art, texture sheets, concept art, sprite sketches, mascot art.
- Price: free, open source (UNVERIFIED, krita.org not read). GPL (UNVERIFIED).
- OS: Windows, macOS, Linux (UNVERIFIED).
- Install: Flathub org.kde.krita (UNVERIFIED ID). KDE app, fits Bazzite KDE.
- Beginner flow: New file at final size and 300 dpi for print, 72 for web. Use layers, a Brush preset, a Layer mask. Save .kra. Export PNG.
- Formats: KRA native. Opens PSD with layers, exports PSD, PNG, JPG, ORA, TIFF, SVG import as vector layers.
- Limits: not for page layout or logos.

## 12. Scribus
- For: print layout, posters, flyers, PDF/X for printers, CMYK, bleed, crop marks.
- Price: free, open source, GPL (UNVERIFIED).
- OS: Windows, macOS, Linux (UNVERIFIED).
- Install: Flathub net.scribus.Scribus (UNVERIFIED ID).
- Beginner flow:
  1. New document: choose size (A3, A2, 18x24 in), set bleed 3 mm (about 0.125 in) per printer.
  2. Place images (Insert Image Frame), text frames, shapes.
  3. Colours: Edit > Colors and Fills. Use CMYK when the printer wants it.
  4. File > Export > Save as PDF. Choose PDF/X-3 or the printer's preset. Tick bleed and crop marks if asked.
- Formats: SLA native. Imports SVG, EPS, PDF (partial), PNG, JPG. Exports PDF, PNG, EPS, SVG.
- Limits: dated look, steep learning, no vector drawing depth (use Inkscape for art).

## 13. Blender (basics)
- For: 3D renders of plugin knobs, logos, merch product shots, bevelled text.
- Price: free, open source (UNVERIFIED, blender.org not read).
- OS: Windows, macOS, Linux. Flathub org.blender.Blender (UNVERIFIED ID).
- Beginner flow for a 3D knob: delete default cube, add Cylinder, add Bevel modifier, add material, add Area light, Render > Render Image (F12), Image > Save As PNG with transparent background (Film > Transparent).
- Formats: .blend native. Imports SVG (to curves), OBJ, FBX, glTF. Exports PNG, EXR, glTF.

## 14. Photopea
- For: opening and quick editing PSD, AI, SKETCH, XCF files in a browser.
- Price: free with ads, paid tier removes ads (UNVERIFIED, photopea.com not read).
- OS: any browser. No install. Files stay in the browser (vendor claim, UNVERIFIED).
- Beginner flow: File > Open, edit layers, File > Export As > PNG or SVG, or Save as PSD.
- Formats: reads PSD, AI, XCF, SKETCH, FIG, SVG (UNVERIFIED breadth); writes PSD, PNG, JPG, SVG, PDF.
- Limits: not a replacement for a daily pro app, RAM heavy, privacy care for client files.

## 15. Sketch, Lunacy, Excalidraw
- Excalidraw: free open source web whiteboard, hand drawn style diagrams (UNVERIFIED). Use at excalidraw.com. Good for quick wireframes and signal flow sketches. Saves .excalidraw, exports PNG and SVG.
- Sketch is macOS only and paid; Lunacy is a free Sketch file reader with Linux builds (both UNVERIFIED). Adobe XD is end of life (UNVERIFIED). Successor choice: Figma or Penpot. Do not install XD.

## 16. Framer and Webflow
- Both are browser site builders (UNVERIFIED, vendor sites not read).
- Framer: design canvas that publishes a real site. Good animation. Free plan with Framer branding, paid plans to remove it and add a domain (UNVERIFIED).
- Webflow: visual builder that makes clean HTML and CSS. Steeper learning, CMS and ecommerce options, workspace plus site plans (UNVERIFIED).
- Bazzite: web apps only, nothing to install.
- Only worth it if Squarespace cannot do a page. If the reader has decided to stay on Squarespace (squarespace-expert), do not push a move.

## 17. Squarespace Design tools and website paths
- Squarespace 7.1 builds pages with Fluid Engine, a grid editor, and a Site Styles panel for fonts, colours and buttons (UNVERIFIED, squarespace.com not read; details are in squarespace-expert).
- Use Figma or Penpot to plan the page first, then rebuild in Squarespace. Export images at the right size first (squarespace-expert has the image size rules).
- Website paths for a non-programmer:
| Path | Best for | Cost shape | Effort |
|---|---|---|---|
| Squarespace | Brand site, shop, merch | Yearly plan | Low |
| Webflow | Custom layout, CMS | Subscription (UNVERIFIED) | Medium |
| Framer | Animated landing pages | Subscription (UNVERIFIED) | Low to medium |
| WordPress | Blog, plugins, full control | Hosting cost (UNVERIFIED) | Medium, upkeep needed |
| Static HTML with Claude | Plugin landing pages, docs, GitHub Pages | Free hosting possible (UNVERIFIED) | Claude writes, the reader reviews |
- Static HTML with Claude: the reader describes the page, Claude writes one HTML file plus CSS, the reader previews in the browser, then hosts it (GitHub Pages, see github-for-beginners). Ask Claude to keep it to one file, no frameworks.

## 18. Windows-only apps on Bazzite (Bottles recipe)
- Read the wine-proton-bottles skill for the full method. Short form (UNVERIFIED for design apps):
  1. Install Bottles from Flathub (flatpak install flathub com.usebottles.bottles).
  2. Create a bottle, type Application. Use the Soda or Caffe runner (UNVERIFIED runner names, pick the newest in Bottles).
  3. Add dependencies in the bottle: allfonts, vcredist, dotnet as the app needs.
  4. Add the installer .exe as a program. Run it. Then launch from the bottle.
  5. If it is blank or crashes: toggle DXVK / VKD3D in bottle settings, test GPU acceleration off.
  6. Back up the bottle once it works.
- Honest status (UNVERIFIED, WineHQ AppDB not read):
  - Affinity: community patched Wine builds exist (COMMUNITY search titles). Official support none.

## 19. Mockup to real workflow (any project)
1. Brief: one sentence goal, audience, size, colours, fonts (use color-palette-expert and graphic-design-expert).
2. Wireframe: grey boxes only, no colour. Tool: Excalidraw or Penpot. Ask: where does the eye go first.
3. High fidelity mockup: real fonts, colours, images, all states (hover, pressed, disabled). Tool: Figma or Penpot.
4. Review: the reader approves. Freeze the frame. Label it v1.
5. Handoff: export assets and a spec sheet (sizes, hex colours, fonts, spacing).
6. Build: Squarespace by hand, HTML by Claude, or JUCE for plugins.
7. Compare build to mockup side by side. Fix drift. This is the "mockup is the plugin" rule.

## 20. Responsive breakpoints (websites)
- Design three widths: phone, tablet, desktop. Common starting values (UNVERIFIED, general practice): 390 px, 768 px, 1440 px wide.
- Squarespace switches layouts at its own breakpoints. Check each page in its mobile preview. Do not assume.
  - Body text 16 px minimum on phone.
  - Images export at 2x of display size, then compress.

## 21. Design handoff with Figma Dev Mode (and Penpot)
- Figma Dev Mode (UNVERIFIED on exact paid terms): toggle in the toolbar, select a layer, read size, colour, font, spacing, copy CSS, export assets.
- Penpot (VERIFIED on page): developer handoff, design tokens and CSS like Grid and Flex layout make inspect values map to code. There is also a Penpot MCP server for code (VERIFIED on page, behaviour UNVERIFIED).
- What to hand Claude (for a non programmer): export PNG of each frame, plus SVG of icons, plus a list of hex colours and font names. Claude writes the HTML or JUCE code from these.
- Never hand over only a screenshot with no sizes. Always include real pixel sizes.

## 22. Exporting assets (cheat sheet)
| Use | Format | Size or setting |
|---|---|---|
| Website photo | WebP or JPG | max 2500 px wide, under 500 KB (Squarespace image rule, see squarespace-expert) |
| Logo on web | SVG plus PNG | PNG 2x, transparent |
| Icons | SVG | outlined strokes, no fonts |
| Plugin UI art | PNG (transparent) or SVG | exact pixel size, plus 2x |
| Knob filmstrip | One PNG, frames stacked | all frames same size |
| Poster print | PDF | 300 dpi images, 3 mm bleed, CMYK if asked |
| Merch print file | PNG transparent | print area size at 300 dpi (follow Printful or Printify template) |
| Social | PNG or JPG | platform size, sRGB |
| Favicon | PNG 512 and SVG | square, simple |

## 23. File format map
| Format | Made by | Opens in (Linux friendly first) |
|---|---|---|
| SVG | open standard | Inkscape, Penpot, Figma, browser, Affinity |
| PDF | open standard | Inkscape, Scribus, Okular, Affinity, Adobe |
| XCF | GIMP | GIMP (Krita and Photopea read it, UNVERIFIED) |
| KRA | Krita | Krita (GIMP reads it, UNVERIFIED) |
| ORA | OpenRaster | Krita, GIMP, MyPaint (UNVERIFIED) |
| PSD | Adobe | Photopea, Krita, GIMP, Affinity |
| AI | Adobe | Inkscape (partial), Photopea, Affinity |
| INDD | Adobe | InDesign only (ask for IDML or PDF) |
| FIG | Figma | Figma, Photopea (UNVERIFIED), Penpot (limited, UNVERIFIED) |
| PENPOT | Penpot | Penpot |
| AFFINITY files | Serif and Canva | Affinity only. Export PDF, SVG, PNG |
| SKETCH | Sketch | Lunacy, Photopea |
| ASE / ASEPRITE | Aseprite | Aseprite, LibreSprite, Pixelorama (partial) |
| BLEND | Blender | Blender |
- Interop rule: SVG for vectors, PNG for pixels, PDF for print. These always work.

## 24. Pixel art tools (Aseprite, LibreSprite, Pixelorama)
- Aseprite: paid, around US$20 on stores, source available, can be built from source free (UNVERIFIED all). Steam and itch.io builds. Runs on Linux (Steam Linux build, UNVERIFIED). Best animation and slicing.
- LibreSprite: free fork of an older Aseprite under GPL (UNVERIFIED). Fewer features. Availability on Flathub UNVERIFIED.
- Pixelorama: free open source, made with Godot (UNVERIFIED). Flathub ID com.orama_interactive.Pixelorama (UNVERIFIED).
- Beginner flow: new sprite 32x32, zoom 800 percent, pencil tool, lock palette, onion skin for animation, export sprite sheet PNG.
- Export: PNG sprite sheet at integer scale only (2x, 3x, 4x), never smooth scaling. JSON atlas if the game wants it.
- For games, use a dedicated pixel-art tool and a locked palette (see color-palette-expert).

## 25. Plugin GUI mockup workflow (Figma or Penpot to JUCE)
- Everything in this section is UNVERIFIED (no source read). It is general practice. Test with a tiny sample first.
- Rule: the approved mockup IS the product .
1. Create a frame at the real plugin window size (e.g. 900 x 500). Use whole pixel sizes.
2. Make a layer group per control: knob, slider, button, meter, label. Name them as parameter IDs (cutoff, resonance).
3. Draw static art (background, panel) separately from moving art (knob caps, needles).
4. Export:
   - Background as PNG at 1x and 2x.
   - Knob as one PNG filmstrip, or as SVG body plus a rotating pointer.
   - Icons and logos as SVG.
5. Record in a spec table: control name, x, y, width, height, parameter ID, range. Give it to Claude.
6. In JUCE, Claude can load SVG with Drawable::createFromSVG and draw PNG with drawImage. Custom look uses a LookAndFeel class, with scaling for high DPI (UNVERIFIED API details; confirm against JUCE docs and the vst-maker skill).
7. Build, take a screenshot of the real plugin, put it beside the mockup, list differences, fix.
8. Keep the same fonts in the mockup and in the plugin. Embed the font file in the plugin binary (UNVERIFIED approach, check licence of the font).
9. Light and dark: design once, use the standing brand rules of the project.

## 26. Not verified (read before trusting)
- Affinity: current unified app name, price, platforms, and any Linux status. Only canva.com/pricing was read, and it shows Affinity as accessible on Free and "with AI" on paid plans.
- Figma: all plan prices, seat types, Dev Mode price and free limits.
- Adobe: all Creative Cloud prices and plan names.
- Inkscape, Krita, Scribus, Blender, Photopea, Framer, Webflow, Lunacy, Sketch, Aseprite, LibreSprite, Pixelorama: licences, versions, Flatpak IDs, prices.
- All keyboard shortcuts (general knowledge, check in each app).
- Wine and Bottles results for every Windows app (WineHQ AppDB not read).
- Dev Mode details, JUCE code details, responsive breakpoint numbers.

## 27. Sources (fetched)
- https://www.canva.com/pricing/ : Canva plans and Affinity access (read 100,000 of 149,619 characters).
- https://penpot.app/pricing : Penpot plans and features (read).
- https://flathub.org/apps/org.gimp.GIMP : GIMP 3.2.6 Flatpak (read).
- Search result titles only, pages not read: etcentric.org, igeeksblog.com, theverge.com via scribe.disroot.org (Affinity); linux.org OMG! Ubuntu thread, scribe.disroot.org comment (Affinity on Linux); help.figma.com/hc/en-us/articles/27468498501527 and banani.co (Figma pricing); techradar.com, petapixel.com (Adobe pricing).
- Blocked or rate limited, not read: affinity.studio/pricing, figma.com/pricing, adobe.com/creativecloud/plans.html.
