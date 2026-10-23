---
name: ux-ui-designer
description: Use when designing, reviewing or testing interfaces for a non-programmer maker, covering audio plugin panels (JUCE knobs, meters, dark skins), a Squarespace site, an HTML test lab or a 16-bit game UI.
---

# UX and UI design for plugin panels, websites, test labs and game menus

Labels: VERIFIED (source) = read on a fetched page in the research session. COMMUNITY = opinion or common practice, check it. UNVERIFIED = not read, do not state as fact.
Assume the reader is not a programmer. Plain words first, then one exact step. One change at a time, ask the reader to test, then continue. Show a picture or mockup before code.
Look and colour work lives in other skills. Link, do not duplicate: graphic-design-expert (layout, type, imagery), color-palette-expert (palettes, contrast choices), photo-editing-color-grading, design-software-guide (Figma, Penpot, Affinity, Adobe, website building), drawing-tablets.
Plugin rules from vst-maker section 10 stay in force: ask for a palette first, mockups are interactive, controls sit under the display they affect, meters show dB scales, hover bubbles with an off switch, HiDPI, resizing, keyboard focus, double-click reset, version designs (v1, v2, v2.1). The approved mockup IS the product.

## 1. Rules of engagement

1. Ask first: who uses it, what is the main task, which device, which palette. Never assume.
2. Design the task, not the screen. One main job per view.
3. Show 2 or 3 options with a recommendation, then wait. Change one thing at a time.
4. Every claim you give carries a label. Say "UNVERIFIED" out loud when it is.
5. Test with a real person before calling anything done (section 16).
6. Never ship a static picture of a control. Interactive mockup first.

## 2. UX process (goal to test)

Design thinking has six phases in three stages: Understand (empathize, define), Explore (ideate, prototype, test), Materialize (implement). It is iterative and a flexible framework, not a rigid recipe. VERIFIED (nngroup.com/articles/design-thinking). The article calls implement the most important and most neglected phase.
Solo-maker version:
1. Goal: one sentence. "A producer sets a hardstyle kick in under 30 seconds."
2. Users: who, skill level, device, room (dim studio, couch with gamepad, phone).
3. Tasks: the 3 to 5 things they do most. Order by frequency.
4. Flow: draw steps on paper, from open to done. Count clicks.
5. Wireframe: boxes and labels only, no colour.
6. Prototype: interactive HTML (the test lab) or Penpot clickable frames.
7. Test: 3 to 5 people, think-aloud (section 16). Fix. Repeat.
Jobs to be done: describe the need as "When I [situation], I want to [action], so I can [outcome]". COMMUNITY (nngroup JTBD page could not be fetched). Example: "When a lead sounds thin, I want one macro to widen it, so I can stay in flow."
Mental models: a mental model is a simplified internal picture of how a system works, built from what a person believes they know. Designs that match it let people carry over what they know. Closing the gap between designer and user models is done with interviews, personas, journey maps. VERIFIED (lawsofux.com/mental-model).

## 3. Laws and principles (Laws of UX)

- Fitts: time to acquire a target depends on distance and size. Make targets large, space them out, put them within easy reach. VERIFIED (lawsofux.com/fittss-law). Plugin use: big knob hit areas, no tiny close-packed buttons.
- Hick: decision time rises with the number and complexity of choices. Fewer options when speed matters, break tasks into steps, highlight a recommended option, introduce features gradually; over-simplifying makes it vague. VERIFIED (lawsofux.com/hicks-law). Plugin use: a main page of 6 to 10 controls, advanced on a second page.
- Miller: average person holds about 7 plus or minus 2 items in working memory. Do not treat 7 as a hard design limit; chunk content into groups. VERIFIED (lawsofux.com/millers-law).
- Jakob: people expect your product to work like the ones they already use. Reuse known patterns; when redesigning, let users keep the familiar version for a while. VERIFIED (lawsofux.com/jakobs-law). Plugin use: knobs turn on drag, double-click resets, like other plugins.
- Doherty threshold: respond within about 400 ms; use animation and progress bars to ease waits. VERIFIED (lawsofux.com/doherty-threshold).
- Cognitive load: mental resources needed to use an interface. Intrinsic load comes from the task; extraneous load comes from distracting or unnecessary design. Cut extraneous load. VERIFIED (lawsofux.com/cognitive-load).
- Progressive disclosure: show the most important options first, move advanced ones to a secondary screen. Two levels usually work best, three or more often confuse. Make the path to advanced obvious and label it. Base the split on frequency of use and test it. VERIFIED (nngroup.com/articles/progressive-disclosure). Plugin use: "Advanced" drawer, second page, right-click menus for rare items.
- Gestalt grouping (Laws of UX):
  - Proximity: near elements read as related. VERIFIED (lawsofux.com/law-of-proximity).
  - Common region: a border or background behind a group makes it read as one. VERIFIED (lawsofux.com/law-of-common-region).
  - Similarity: same colour, shape, size, orientation or movement reads as the same kind. VERIFIED (lawsofux.com/law-of-similarity).
  - Continuity, closure, connectedness are named as the other grouping principles on the proximity page. VERIFIED (name only); details UNVERIFIED.
- Affordance and signifier: an affordance is what an object allows; a signifier is the visible cue that tells you. Definitions from Norman. COMMUNITY (nngroup page could not be fetched). A knob needs a visible pointer line (signifier); a flat grey box does not say "drag me".

## 4. Nielsen's 10 heuristics (nngroup.com/articles/ten-usability-heuristics) VERIFIED

1. Visibility of system status: prompt feedback on what is happening.
2. Match between system and real world: familiar words, natural order.
3. User control and freedom: easy undo and back out.
4. Consistency and standards: same wording and behaviour inside, platform conventions outside.
5. Error prevention: constraints, defaults, confirmations.
6. Recognition rather than recall: show options, do not make users memorise.
7. Flexibility and efficiency: shortcuts for experts that do not slow novices.
8. Aesthetic and minimalist design: remove irrelevant or rarely needed content.
9. Help users recognize, diagnose and recover from errors: plain-language message, suggest a fix.
10. Help and documentation: searchable, task-focused, ideally in context.
Plugin mapping (COMMUNITY): 1 meters and readouts; 3 undo and A/B compare; 5 clamp ranges, confirm preset overwrite; 7 modifier-key fine adjust; 10 tooltips.

## 5. Information architecture and navigation

- Card sorting shows users' mental models: participants group labelled cards. Open sort (they make groups and names) is the most common. Qualitative studies need at least 15 participants, quantitative 30 to 50. VERIFIED (nngroup.com/articles/card-sorting-definition). For a solo maker with few testers, treat results as hints. COMMUNITY.
- Closed sort is "sometimes used for validation"; the article generally suggests tree testing instead. VERIFIED. Details of tree testing UNVERIFIED.
- Full IA study guide page was rate limited and not read. Rules below are COMMUNITY:
  - Group by user task, not by your internal structure.
  - Label with the words users use ("Shop", not "Merchandise Solutions").
  - Keep top-level navigation to about 5 to 7 items; put the rest under a parent or footer.
  - Show where you are (current item highlighted, breadcrumb on deep pages).
  - Search only if there is enough content to need it.
- Navigation patterns (COMMUNITY): top bar for sites; tabs for sibling views inside a plugin (Main, Mod, FX); a side list for presets; bottom bar or big buttons for touch; hamburger hides things, avoid for 5 or fewer items.
- Game menus: a top-level list of 5 to 8 verbs (Items, Skills, Equip, Status, Save), sub-lists open to the right, B button goes back one level. COMMUNITY.

## 6. Forms, errors, empty and loading states

Forms (GOV.UK Design System):
- Every text input needs a visible label, above the input, short, sentence case. VERIFIED (design-system.service.gov.uk/components/text-input).
- Do not use placeholder text instead of a label or for hints; it vanishes when typing, some screen readers skip it, default placeholder colours often fail contrast. VERIFIED (same page).
- Hint text: one short sentence, no links. VERIFIED.
- Mark optional fields "(optional)"; never mark required fields with asterisks. Ask one thing per page where you can. Ask only what you need, once. VERIFIED (design-system.service.gov.uk/patterns/question-pages).
- Avoid range sliders: dragging is hard for some users; give a non-drag way. VERIFIED (same page). Plugin knobs still need a typed or keyboard route (section 9).
Errors:
- Say what went wrong and how to fix it, plain words, be specific. Avoid "An error occurred", "invalid", "oops", "please", "sorry". VERIFIED (design-system.service.gov.uk/components/error-message).
- Show the message next to the field and in a summary at the top; keep what the person typed; do not clear the form. VERIFIED (same page).
- Validate when the person tries to move on, not on leaving each field. VERIFIED (design-system.service.gov.uk/patterns/validation). Always validate on the server. VERIFIED.
- Do not use colour alone to show errors (WCAG 1.4.1, Level A). VERIFIED (w3.org Use of Color). GOV.UK adds a hidden "Error:" prefix for screen readers. VERIFIED.
Empty states (nngroup.com/articles/empty-state-interface-design) VERIFIED:
- Never leave a container blank; users cannot tell empty from loading from broken.
- Do not show "no items" while data still loads.
- Teach: say what goes here and how to fill it. Give a button that starts the task.
- Plugin use (COMMUNITY): empty preset list says "No user presets yet. Press Save to add one."
Loading and response time (nngroup.com/articles/response-times-3-important-limits) VERIFIED:
- 0.1 s feels instant: direct manipulation feedback must land here.
- 1.0 s keeps flow of thought; above 1 s show the system is working (cursor change).
- 10 s loses attention: percent-done indicator plus a clear way to cancel.
Error and loading state list to design for every screen (COMMUNITY): empty, loading, partial, error, offline or device missing, success, disabled.

## 7. Feedback and component states

Design each control in all states (COMMUNITY): default, hover, focus (keyboard), pressed or dragging, disabled, selected or on, error, modulated (value moved by an LFO or automation), automated (host is writing it), locked.
- Hover must look different from default. Disabled must still be readable, and inactive components are exempt from WCAG 1.4.11 contrast. VERIFIED (w3.org non-text-contrast).
- Show the value while dragging (popup bubble), show the unit, and show the default as a tick or ring. COMMUNITY.
- Every action gets feedback within 0.1 s (heuristic 1, response times above).
- Motion: keep short (about 100 to 300 ms), ease out, never block input. COMMUNITY (numbers UNVERIFIED). Motion that starts automatically, lasts over 5 seconds and runs beside other content needs pause/stop/hide (WCAG 2.2.2, Level A). VERIFIED. Respect the reduced-motion setting on websites. UNVERIFIED (MDN page blocked).

## 8. Accessibility (WCAG 2.2, w3.org/WAI/WCAG22/Understanding)

All VERIFIED on the pages named:
- Target Size Minimum, 2.5.8, AA: pointer targets at least 24 by 24 CSS px, or enough spacing (24 px circle on each target does not hit another). Exceptions: equivalent control, inline, user agent, essential.
- Dragging Movements, 2.5.7, AA: anything done by dragging must also work with a single pointer without dragging (click or tap). Exceptions: essential, user agent. For knobs: add click targets, arrow buttons, or a typed value box.
- Keyboard, 2.1.1, A: all functions via keyboard. Path-dependent exception covers freehand drawing only; dragging an object to a place and resizing must be keyboard-operable.
- Contrast Minimum, 1.4.3, AA: text 4.5:1; large text (18 pt or 14 pt bold, about 24 px or 18.5 px) 3:1; no rounding.
- Non-text Contrast, 1.4.11, AA: UI components and needed graphics 3:1 against neighbours; no rounding.
- Use of Color, 1.4.1, A: colour not the only cue.
- Reflow, 1.4.10, AA: content works at 320 CSS px wide without two-way scroll. Exceptions include games, data tables, diagrams, so a plugin test lab canvas may be exempt but the page around it is not.
- Focus Not Obscured Minimum, 2.4.11, AA: a focused control must not be entirely hidden by author content (sticky headers, popups).
- Focus Appearance, 2.4.13, AAA only: 2 px perimeter and 3:1 change. Use as a good target, not a requirement.
- Slider keyboard pattern (w3.org/WAI/ARIA/apg/patterns/slider): arrows change one step, Home and End jump to min and max, Page Up and Down change by a larger step (optional); role slider with aria-valuenow, valuemin, valuemax, valuetext, and a label; aria-orientation vertical for vertical sliders. VERIFIED. Use this as the keyboard model for knobs in the HTML test lab.
Screen readers and JUCE: JUCE exposes an accessibility handler API. Exact class names and Linux support UNVERIFIED (JUCE docs pages could not be fetched). Check the current JUCE docs before promising screen reader support.
Dense plugin UIs (COMMUNITY): offer UI scale, a high-contrast skin, text no smaller than the platform minimum you choose, and never rely on colour alone for meter zones.

## 9. Audio plugin UI specifics

Mouse behaviour in JUCE Slider (raw.githubusercontent.com juce_Slider.h, master) VERIFIED:
- setMouseDragSensitivity sets the distance the mouse must travel to cover the full range (relative-drag rotary modes).
- setVelocityBasedMode: faster mouse movement gives bigger changes; setVelocityModeParameters sets sensitivity, threshold, offset and key-swap.
- Holding ctrl (or command, when key swap is enabled) toggles velocity-sensitive mode.
- setDoubleClickReturnValue: reset by double-click, or single click with a modifier (alt by default).
- setSliderSnapsToMousePosition: thumb jumps to click on linear bars (default true). Turn off for precise sliders.
- setPopupDisplayEnabled: popup bubble while dragging or hovering. setScrollWheelEnabled: wheel control on by default.
- Styles include RotaryVerticalDrag (up-down drag) and RotaryHorizontalVerticalDrag.
Host convention for fine adjust, Ableton Live manual (ableton.com/en/manual/live-keyboard-shortcuts) VERIFIED: Shift while dragging gives finer resolution; arrow keys step; Shift+arrows fine step; Delete returns to default; typing digits enters a value; Enter confirms, Esc cancels. Copy these where JUCE allows: Shift fine, double-click reset, type-in.
Design choices (all COMMUNITY unless noted; KVR and JUCE forum pages were not readable, so no thread is cited):
- Knob versus slider: knobs save space and fit hardware-style skins; sliders show value by length and suit faders, EQ gain and long-throw values. Use sliders for levels and mix, knobs for tone controls. Choose one drag model for the whole plugin.
- Drag direction: vertical drag for knobs is the common default; circular drag is less common and less precise. UNVERIFIED which is preferred by most users.
- Value readout: show a number with unit on hover or drag (-12.0 dB, 440 Hz, 35 %). Allow click-to-type. Use the same rounding everywhere.
- Scales: log for frequency, dB for gain, linear for percent. Mark centre for bipolar controls.
- Layout: signal flow left to right; group by section with a common region (border or panel); label every control; related controls adjacent (proximity). Input meter far left, output meter far right (vst-maker section 10 puts meters far right: follow it).
- Tooltips: delay about one second, off switch (vst-maker).
- Preset browser: current name always visible, previous/next arrows, search, favourites, "modified" marker, Save and Save As, empty state text, factory and user separated. COMMUNITY.
- A/B compare and undo: heuristic 3 says give users a way back. COMMUNITY for the plugin form.
- Resizing: JUCE AudioProcessorEditor has setResizable, setResizeLimits, setConstrainer, and setScaleFactor "can be called by a host to tell the editor to use a non-unity GUI scale". VERIFIED (juce_AudioProcessorEditor.h). Design on a fixed aspect ratio with a few preset sizes (100, 150, 200 percent). COMMUNITY.
- HiDPI: draw vector shapes or provide @2x artwork; test at 100 and 200 percent scale on Linux. Linux behaviour per desktop UNVERIFIED.
- Latency of visual feedback: knob follows the mouse within 0.1 s (response limits above). Meters refresh by Timer at 30 to 60 Hz (COMMUNITY); pause when hidden (vst-maker).
- Meter ballistics and colours (COMMUNITY, exact numbers UNVERIFIED): fast attack, slower release; peak hold line that decays; separate peak and RMS or LUFS where useful; green normal, yellow near top, red at or above 0 dBFS; dB ticks with labels; clip indicator that stays lit until clicked. Add a non-colour cue (a clip marker, a number) per WCAG 1.4.1.
- Automation and modulation: show host-automated and LFO-moved values on the control (a ring or a moving dot), so the knob does not "lie". COMMUNITY.
- Dense UIs: group, use progressive disclosure (second page, collapsible sections), keep the top 8 controls always visible. Hick and Miller apply.

## 10. Layout, type, spacing, grid

- 8 pt grid: spacing and sizes in multiples of 8 (4 for fine detail). Material Design uses 8 dp spacing for touch targets (see section 11). The 8 pt rule itself is COMMUNITY.
- Type scale: pick a base size and a ratio (for example 1.25) and use 4 to 6 sizes only. COMMUNITY.
- Hierarchy: size, weight, contrast and position, not decoration. One primary action per view. See graphic-design-expert for type and layout craft.
- Alignment: align to a few edges; equal gutters; consistent padding inside groups; more space between groups than inside them (proximity).
- Plugin panel unit: pick a grid cell (for example 8 by 8 px at 100 percent) and snap every knob, label and meter to it.

## 11. Touch, responsive and mobile first

- Android: touch targets at least 48 by 48 dp (about 9 mm), spaced 8 dp or more apart; the visible icon can be 24 dp with a larger touch area; range 7 to 10 mm. VERIFIED (support.google.com/accessibility/android/answer/7101858). m3.material.io pages needed JavaScript and could not be read.
- Apple 44 by 44 pt: widely quoted. UNVERIFIED (developer.apple.com HIG page needs JavaScript and the .md version was blocked).
- Web floor: 24 CSS px (WCAG 2.5.8, AA, section 8). Aim for 44 to 48 px on touch screens. COMMUNITY.
- Mobile first (COMMUNITY): design the narrow layout first, then add columns as width grows; test at 320 px (WCAG reflow). Set the viewport meta tag; MDN page was blocked, so UNVERIFIED here.
- Squarespace 7.1 handles breakpoints itself; check mobile view in the editor before publishing (skill squarespace-expert).
- Touch plugin or test lab: knobs need vertical drag, big hit areas, no hover-only info, no tiny sliders; add +/- buttons or a number box. Two-finger or long-press for fine adjust. COMMUNITY.

## 12. Dark UI specifics

- NN/g: light mode gave better performance for most users with normal vision, more so at small text sizes and in simulated night; dark mode helps some low-vision users and saves power on some displays; do not make dark the default for a general audience, offer an option. Opinions of readability do not match performance. VERIFIED (nngroup.com/articles/dark-mode). Evidence is mixed.
- For plugins, dark skins are the norm in dim studios. COMMUNITY. Therefore compensate:
  - Avoid pure white text on pure black; use off-white on a dark grey. COMMUNITY.
  - Keep text at 4.5:1 and controls at 3:1 (section 8).
  - Raise surfaces with lighter greys rather than shadows; use one accent colour.
  - Desaturate bright accents a little; bright saturated colour on dark vibrates. COMMUNITY.
  - Check small labels first; they fail first.
- Offer a light or high-contrast skin where practical. See color-palette-expert for palettes.

## 13. Design systems and tokens

- A design system is shared tokens, components and rules so every screen looks and behaves the same. COMMUNITY.
- Tokens are named values: color.bg, color.accent, space.2 (16 px), radius.1, font.label. Components use tokens, never raw values. COMMUNITY.
- For a plugin suite: one token file for colours, one for sizes, one set of knob, slider, button, meter and tooltip components reused across all plugins; the same layout skeleton (header with preset bar, body, footer). COMMUNITY.
- Document each component: purpose, states (section 7), sizes, keyboard behaviour, do and don't.
- GOV.UK Design System is a good model of documented components with research notes (design-system.service.gov.uk). VERIFIED that it documents components with rules (several pages read). Fluent: page read had no guidance content; UNVERIFIED. Material 3: UNVERIFIED (JavaScript page).
- Penpot variables or Figma variables can hold tokens. UNVERIFIED for current feature names.

## 14. Website UX and conversion basics (Squarespace)

All COMMUNITY unless marked; test with real visitors. See squarespace-expert for builder steps.
- One goal per page: listen, download, or buy. One primary button per screen, above the fold.
- Plain headline that says what it is and who it is for. Plugin page: name, one line, screenshot, download button, licence, system support.
- Show proof: screenshot or audio/video demo, version, changelog, honest limits.
- Fewer choices on the path to download (Hick, VERIFIED law above).
- Navigation: 5 to 7 items, shop and contact easy to find; keep the same on every page (consistency).
- Forms: only needed fields, labels visible, clear errors (section 6). Newsletter: email only.
- Speed: images compressed; aim for response within 0.1 to 1 s feel (section 6 limits apply to interaction; page load targets UNVERIFIED).
- Trust: privacy note, no dark patterns, real contact. Clear prices and shipping on merch.
- Measure: pick one number (downloads per visit) and compare before and after a change. Do not change five things at once.
- Accessibility on the site: alt text, headings in order, link text that makes sense alone, contrast per section 8.

## 15. Game UI: JRPG menus, dialogue, controller, touch

- Text size: Xbox Accessibility Guideline 101 minimums for default text: console 26 px at 1080p (52 at 4K), PC 18 px at 1080p (36 at 4K); players should be able to scale text to 200 percent; do not count on platform magnifiers; text must stay readable over any background (example: black outlines). VERIFIED (learn.microsoft.com XAG 101). Those are for modern high-res text. For a 16-bit game the internal resolution is small; keep the pixel font at an integer multiple scale and offer a text-size option. COMMUNITY.
- Pixel fonts: pick a font designed on a grid, use only at its native size or exact integer multiples, no anti-aliasing blur, no sub-pixel positions. 8 px fonts are hard to read on a TV; prefer 12 to 16 px source height for dialogue. COMMUNITY, numbers UNVERIFIED.
- Dialogue box: bottom third of screen, name tag on the box, 2 to 3 lines, high contrast panel, portrait on one side, a blinking "more" arrow, A advances, B or Start skips or fast-forwards, speed setting. COMMUNITY.
- JRPG menu: vertical list with a clear cursor (arrow plus highlighted row; do not use colour alone, WCAG 1.4.1), wrap-around at ends, A confirm, B back, X or Y for secondary action, shoulder buttons switch tabs, detail pane updates as the cursor moves (recognition not recall), always show the controls hint. COMMUNITY.
- Controller navigation: every element reachable by D-pad; focus order matches visual order; remember last cursor position per menu; no hover-only info; mouse and touch also work; never trap focus. Same rules as keyboard (WCAG 2.1.1 VERIFIED in spirit; game application COMMUNITY).
- Touch: large on-screen buttons, at least 48 dp equivalent (Android, VERIFIED above), spaced apart; keep thumbs off the content; menus are tap-to-select, not hover. Show gamepad hints only when a gamepad is connected. COMMUNITY.
- Safe areas: keep key text and HUD inside a margin from the screen edge (TVs may crop). Common figure is 5 percent, but XAG page had no safe-zone number. UNVERIFIED. Apple safe-area guidance UNVERIFIED.
- Feedback: sound and a small cursor move on every input, within 0.1 s. COMMUNITY (limit VERIFIED).
- Accessibility basics: remappable controls, text scale, no colour-only status (use icons with colour), reduced flashing, pause anywhere. Game Accessibility Guidelines site was blocked: UNVERIFIED.
- Pixel UI art (panels, frames, icons): see graphic-design-expert.

## 16. Usability testing for a solo maker

Why 5: each user finds about 31 percent of problems, so 5 users find about 85 percent; run several small rounds (for example 3 rounds of 5) with fixes between them rather than one big study; never test with one person; use 3 or 4 per distinct user group. VERIFIED (nngroup.com/articles/why-you-only-need-to-test-with-5-users).
Think-aloud: ask users to verbalise thoughts as they use the UI; you stay quiet; prompt neutrally when they go silent; note where you influenced them and discard those parts; it is qualitative, not statistics. VERIFIED (nngroup.com/articles/thinking-aloud-the-1-usability-tool). Tasks should be realistic, wording matters, participants can read tasks aloud. VERIFIED (nngroup.com/articles/usability-testing-101).
Script (wording is COMMUNITY, structure follows the pages above):
1. "We test the design, not you. You cannot fail. I cannot help during the tasks."
2. "Please say out loud what you see, what you expect and what confuses you."
3. Give one task card at a time, for example "Make the lead brighter and save it as 'My Lead'." Not "Click the filter knob".
4. Prompts only: "What are you thinking?", "What did you expect to happen?" Never explain the UI.
5. After each task: "How easy was that, 1 to 5?" Write the answer.
6. End: "What was the most confusing part? What would you change?"
Record: task, success (yes, helped, no), time, quotes, severity (blocker, annoying, nice to fix). Fix blockers first, retest.
Remote: share the HTML test lab link, record screen and voice with the person's consent. COMMUNITY.
For audio plugins, include one person who is not a producer (checks labels) and one who is (checks workflow).

## 17. Heuristic review checklist (one page, tick each)

Status and feedback
- [ ] Every control reacts within 0.1 s; long jobs show progress and cancel
- [ ] Current value, unit and preset name are visible
Clarity
- [ ] Each control has a label and a visible signifier (pointer line, arrow, border)
- [ ] Groups are clear by proximity or common region; max about 7 items per group
- [ ] Main page shows the frequent controls; rare ones are one step deeper (two levels at most)
Consistency
- [ ] Same behaviour everywhere: drag, double-click reset, Shift fine, type-in
- [ ] Words match the audience's words; same name for the same thing
Control and errors
- [ ] Undo or A/B or reset exists; destructive actions confirm
- [ ] Errors say what and how to fix; input is kept; not colour-only
- [ ] Empty, loading, error and device-missing states are designed
Accessibility
- [ ] Text contrast 4.5:1 (large 3:1); controls and meter edges 3:1
- [ ] Every function works by keyboard; drag actions have a non-drag route
- [ ] Targets at least 24 px (web), 48 dp on touch; focus always visible and not hidden
- [ ] No info by colour alone; moving content can pause; UI scale works
Responsive and platform
- [ ] Works at 320 px (site) and at 100 and 200 percent scale (plugin)
- [ ] Gamepad, keyboard, mouse and touch all work (game and test lab)
Dark UI
- [ ] Off-white on dark grey, one accent, small text checked first
Tested
- [ ] 5 people did think-aloud; blockers fixed; second round done

## 18. Recipe: design a plugin panel in 6 steps

1. Define the job. Write the one-sentence goal, the target user, and the 3 most-used tasks. Ask for the palette (color-palette-expert).
2. List parameters and rank them. Frequent ones go on the main page (max about 8 to 10); rare ones on page two. Decide scales (dB, Hz log, %).
3. Sketch the layout on paper. Signal flow left to right; display in the middle, the controls directly under what they change; input meter left, output meter far right; preset bar on top. Snap to the 8 grid.
4. Build the interactive mockup (HTML test lab): every knob drags (vertical), Shift fine, double-click reset, type-in, value popup, display and meters react. Design all states from section 7.
5. Review with the checklist in section 17, then with the contrast numbers. Fix, label as v1.
6. Test with 3 to 5 people (section 16), change the top 3 problems, save as v2, retest. Only then build the JUCE editor, and make it match the approved mockup.

## 19. Tools on Linux

- Penpot: open-source design platform, self-hostable, uses open standards CSS, HTML, SVG, JSON, supports CSS Grid and Flex layouts. VERIFIED (penpot.app). Browser use and Linux use not stated on that page: UNVERIFIED.
- Figma in a browser: UNVERIFIED (not fetched). Excalidraw (sketches), Inkscape (vector, SVG skins): UNVERIFIED (not fetched). Pencil and paper is fine for step 3.
- For software choices and workflows see design-software-guide; for tablets see drawing-tablets.

## 20. Troubleshooting a UI that "feels wrong"

1. Users do not find a control: add a label and signifier; check contrast; move it into the main page.
2. Users find it but misuse it: wrong mental model; rename; copy a convention from other plugins (Jakob).
3. Knob feels jumpy or too slow: tune drag distance; add Shift fine; consider velocity mode (section 9).
4. Panel feels crowded: remove, group, hide advanced (Hick, Miller, progressive disclosure).
5. Users cannot read it: raise text size and contrast; test at 100 percent scale first.
6. Game menu confuses on gamepad: check focus order, back button, cursor memory, controls hint.
7. Site visitors leave: one clear goal, one clear button, shorter page, retest.

## Not verified

- Apple HIG 44 pt target and safe areas (page needs JavaScript; .md blocked).
- Material 3 pages (m3.material.io needed JavaScript); only the Android help page was read.
- Microsoft Fluent guidance, MDN responsive/mobile first, reduced motion, Game Accessibility Guidelines (blocked or empty).
- NN/g pages not read: affordances and signifiers, jobs to be done, IA study guide, user-centered design (fetch errors or hourly limit).
- JUCE forum, KVR, Reddit r/userexperience and r/UI_Design, Tracktion and Reaper themes: not readable; everything attributed to community practice is COMMUNITY.
- Meter ballistics numbers, motion durations, pixel font sizes, 8 pt grid origin, 5 percent safe area, JUCE accessibility class names, Linux HiDPI behaviour.
- Figma in browser, Excalidraw, Inkscape features on Linux.
- The skills graphic-design-expert, color-palette-expert, photo-editing-color-grading, design-software-guide, drawing-tablets were not present in the skills folder when written; the links are by name only.

## Sources (fetched)

- https://www.nngroup.com/articles/ten-usability-heuristics/
- https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/
- https://www.nngroup.com/articles/thinking-aloud-the-1-usability-tool/
- https://www.nngroup.com/articles/usability-testing-101/
- https://www.nngroup.com/articles/design-thinking/
- https://www.nngroup.com/articles/progressive-disclosure/
- https://www.nngroup.com/articles/card-sorting-definition/
- https://www.nngroup.com/articles/empty-state-interface-design/
- https://www.nngroup.com/articles/response-times-3-important-limits/
- https://www.nngroup.com/articles/dark-mode/
- https://lawsofux.com/ (fittss-law, hicks-law, millers-law, jakobs-law, law-of-proximity, law-of-common-region, law-of-similarity, doherty-threshold, cognitive-load, mental-model)
- https://www.w3.org/WAI/WCAG22/Understanding/ (target-size-minimum, focus-appearance, focus-not-obscured-minimum, dragging-movements, contrast-minimum, non-text-contrast, keyboard, reflow, pause-stop-hide, use-of-color)
- https://www.w3.org/WAI/ARIA/apg/patterns/slider/
- https://design-system.service.gov.uk/ (components/error-message, components/text-input, patterns/validation, patterns/question-pages)
- https://support.google.com/accessibility/android/answer/7101858
- https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/101
- https://raw.githubusercontent.com/juce-framework/JUCE/master/modules/juce_gui_basics/widgets/juce_Slider.h
- https://raw.githubusercontent.com/juce-framework/JUCE/master/modules/juce_audio_processors/processors/juce_AudioProcessorEditor.h
- https://www.ableton.com/en/manual/live-keyboard-shortcuts/ (via Ableton knowledge search)
- https://penpot.app/
