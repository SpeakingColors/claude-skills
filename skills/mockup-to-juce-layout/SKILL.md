---
name: mockup-to-juce-layout
description: Use when an approved HTML mockup must become a native JUCE editor: extract positions, icons and tooltips from the DOM with Playwright, generate Layout.h and Icons.h, port, check by snapshot.
---

# From mockup to native JUCE window

Extends `mockup-is-the-plugin` (the mockup IS the product). Labels: MEASURED (done for a 24 operation audio editor, 53 icons), UNVERIFIED.

## Recipe
1. Open the mockup in Playwright at a fixed viewport. Read the stage rectangle, then for every `button`, knob and canvas: `getBoundingClientRect()` minus the stage origin, text, `data-*` tooltip, SVG `outerHTML`, computed colour. Save as JSON. Keep the extraction scripts in `tools/` so the port can be regenerated.
2. Generate two headers with a small Python script: `Layout.h` (named rectangles in design pixels, op table with tooltip, shortcut and colour) and `Icons.h` (SVG strings). Wrap each icon's inner elements in `<g fill="none" stroke="#hex" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">` using the colour the browser computed; JUCE's SVG parser does not resolve `currentColor`. Check that running the generator again reproduces the headers byte for byte.
3. Build the editor at the design size (for example 1382 x 876) and scale it: `content->setTransform(AffineTransform::scale(getWidth() / designW))`, a `ComponentBoundsConstrainer` with a fixed aspect ratio, and a scale menu. Draw panels, wood or frame, header and logo in `paint()` from the DOM measurements.
4. Fonts: `juce_add_binary_data` with ABSOLUTE paths (`${CMAKE_CURRENT_SOURCE_DIR}/assets/...`); relative paths failed under Ninja with "missing and no known rule". MEASURED. Use `FontOptions(typeface).withHeight(h)` in JUCE 8.
5. Take the tooltip text from the mockup data, not from memory. It also tells you what a button really does (a "grab" button turned out to keep the last seconds heard, not to drag a file).
6. Render the real window offscreen and compare with a screenshot of the mockup, page by page (see `juce-headless-test-snapshot`).

## Gotchas found
- Non-ASCII text in a `const char*` is read as Latin 1 and shows as garbage. Build the String with `juce::CharPointer_UTF8("\xe2\x96\xbe")`. MEASURED.
- Child components often call a refresh callback while the constructor is still creating widgets: a null pointer crash. Guard with a `ready` flag set at the end of the constructor. MEASURED.
- A button that repeats the arrow glyph the style already draws shows "...": pick the plain style. MEASURED.
- Things the plugin cannot do yet stay visible but greyed out (alpha 0.3, disabled, tooltip "Not in this build yet") and are listed in the README and ROADMAP. Never delete them from the layout, and never pretend they work.
- Web-only controls (browser audio start, "demo loop") are dropped on purpose and written down.
