---
name: mockup-is-the-plugin
description: Use when a plugin or app has an approved mockup and a real editor is being built, shown or released: the mockup and the product are one design, port it faithfully and test the backend separately.
---

# The mockup is the plugin

Idea: an approved mockup is the product's look. The real window must match it. Do not treat them as two designs.

Labels: VERIFIED (read on a source page), COMMUNITY, UNVERIFIED (general practice, test it). This skill is general practice unless marked.

## Rules
1. The approved mockup and the plugin are one product. Never write "separate design" or "the mockup is separate". If the real window does not match yet, say "the real window is not ported yet" and make that the next task.
2. A plain parameter-list window is only a development stand-in. Say so the first time you show it. It never ships in a release.
3. Port the mockup natively (same layout, knobs, displays, colours, tooltips, pages). Do not embed the mockup HTML in a web view for a plugin: it adds weight and extra system packages, and it can behave badly inside some hosts and sandboxes (Flatpak, Linux DAWs). UNVERIFIED for any one host, test it. Do not quietly redesign.
4. When a repo has a mockup and no real editor, start with the editor port before adding more backend features, unless the owner says otherwise.
5. Take the repo screenshot from the real window once ported, never from the stand-in.

## Method to port a mockup
1. Open each mockup page in a browser automation tool (for example Playwright).
2. Read every control's position, size, label and tooltip from the page, and write them to a data file (a layout header or JSON).
3. Generate the editor layout from that file, so the numbers are not retyped by hand.
4. Map each control to its parameter id by name; list any control with no parameter and any parameter with no control.
5. Render the real window offscreen, screenshot it, and compare it with a screenshot of the mockup page by page. Fix differences before moving on.
6. Keep the mockup in the repo (docs/) so later changes start from it.

## Backend lessons for hardware controller plugins
- Build the pure C++ core first (parameter map, encode, decode, outgoing message queue) with tests that run without the plugin framework, for example a shell script that builds with address and undefined-behaviour sanitizers.
- Write a small software model of the device from the vendor's MIDI document and round-trip every map entry (minimum, middle, maximum, default, several channels). The model checks your reading of the document, not the real device; say so. Break the code on purpose once to prove the tests catch it.
- Read the vendor's NRPN and CC notes closely. Devices differ in how they send NRPN (for example whether the MSB is always sent, and when a 14 bit value applies). Never assume; follow the document and confirm with a MIDI monitor on the real device.
- Never automate or bulk-send global setup values (master tune, protection, power-up patch, routing).
- Never guess unknown formats (SysEx patch dumps, packed bit layouts, value names): leave them out and list them in a ROADMAP file.

## Checks before saying "done"
- Does the real window show the same pages, labels and tooltips as the mockup?
- Is every control wired to a parameter, and does automation from the host move it?
- Does it scale (small and large window, high-DPI screen)? UNVERIFIED until tested.
- Is the screenshot in the repo from the real window?
