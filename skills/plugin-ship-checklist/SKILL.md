---
name: plugin-ship-checklist
description: Use before releasing a plugin or app: old saves keep loading, the real editor matches the mockup, resizing, easy installs and updates, release workflow, manuals, and host gotchas.
---

# Plugin ship checklist: lessons from real releases

Companion to `vst-maker`, `juce-expert` and `mockup-is-the-plugin`. Each item is a mistake someone actually made, so check it before saying a plugin is "ready". Labels: COMMUNITY (project experience), VERIFIED (read in docs), UNVERIFIED.

## 1. Old saves must keep loading
- Keep parameter ids stable; never reuse an id for a different meaning.
- Add new parameters with a default that leaves the old sound unchanged.
- Never delete a parameter without a migration in `setStateInformation` (map old to new).
- Store a state version number.
- Keep fixture files of old states and a CI test that loads them. The sound may change a little; reading must still work.
- If defaults change, presets that never mentioned a parameter silently take the new default: write the old values into old presets explicitly.

## 2. Ship the real editor, and check it
- The plain generic parameter list is a development stand-in and never goes in a release (see `mockup-is-the-plugin`).
- Never claim "the editor is built from the mockup" without looking. Render the real editor headless in CI (for example `xvfb-run` plus `createComponentSnapshot`), compare it with the mockup, and push the PNGs to a snapshots branch if CI artifacts cannot be downloaded.
- Then load it in pluginval and in at least one real host before telling anyone it is ready.
- Say plainly in the status what is still a stand-in.

## 3. Window and UI rules
- Fixed aspect ratio, resizable from all four corners and all four sides, the whole UI scales uniformly, size is saved. JUCE: `setResizable`, `ComponentBoundsConstrainer::setFixedAspectRatio`, `ResizableBorderComponent`. Test in a real host (UNVERIFIED in hosts).
- Optional convenience: double click on a decorative edge resets the window to 100%; the zoom control shows percent of that default.
- Two views of one parameter (a small graph and a big one) must both repaint when the value changes from anywhere (the other view, host automation, a preset). Do not rely on a view's own mouse events; repaint on the editor's frame tick or from a parameter-attachment callback.
- Show values as readable text with units and sensible rounding (never raw "80.000000"); write key values down next to graphs, for example crossover frequencies on dark chips.
- Preset UX: Save asks before overwriting (overwrite, save as new, cancel); rename exists; factory sounds saved or renamed become the user's own copy; never tell the user to "save a copy first".
- Mockups cannot use `confirm()` or `prompt()`; use an in-page dialog.
- Canvas helper bug: a high-DPI helper that falls back to `canvas.height` when CSS height is `auto` multiplies the size by the pixel ratio on every redraw. Use `clientHeight` and test at deviceScaleFactor 2.
- Do not wait for IntersectionObserver in a framed page before drawing; it can report "not visible" at first.

## 4. JUCE gotchas
- `ParameterAttachment::setValueAsCompleteGesture` takes the real value, not 0 to 1. A normalised index worked for two choices and picked the wrong item for three or more. Test every choice control with its last item. COMMUNITY.
- A choice or segment control must be tested at every item, not just the first two.
- Web-view editors (a page served from BinaryData in a browser component) work but add platform dependencies (WebView2 on Windows, WebKitGTK on Linux), need bundled fonts for offline use, and were untested on real Windows in the project that tried it. Native drawing is the safer default (see `mockup-is-the-plugin`).

## 5. VST3 facts that explain bugs (VERIFIED, Steinberg VST3 developer portal)
- A VST3 plugin has a processor and an edit controller. The processor must work without the controller; DSP state must never depend on the editor. JUCE hides the split.
- `process()` may run on the audio thread: no allocation. Initialise and terminate run on the UI thread.
- Bus arrangement changes are allowed only while the plugin is inactive. Input and output buffers may be the same memory, so do not blindly clear outputs.
- Block size is capped by the maximum announced block, but blocks vary.
- Parameter edits from the GUI use beginEdit, performEdit, endEdit in that order, UI thread only.
- Restore order: processor state first, then the controller; the controller must not fire handler callbacks while restoring.
- Do not send private messages from the processor to the controller from `process()`.

## 6. Easy install and update
- Goal: installing an update is as easy on Linux as on Windows and macOS: double click, no terminal, install over the old version without uninstalling.
- Windows (Inno Setup): keep the same AppName and install folder so setup upgrades in place; close the DAW first, the VST3 is locked. Say on the folder page what goes there (standalone and manual) and that the VST3 goes to the common VST3 folder.
- macOS: a .pkg with fixed identifiers and install locations overwrites cleanly.
- Linux: a `.flatpak` bundle should open in the software centre with a double click; the terminal fallback is `flatpak install --user` (add `--reinstall` if present). UNVERIFIED on every distro; test. Idea: a static Flatpak repo on GitHub Pages lets the software centre show updates.
- Free plugins stay offline: no update checks at run time. A settings gear in the header can show the version and buttons that open the project page and releases page in the browser (`juce::URL::launchInDefaultBrowser`).
- Consistent publisher name, install folder and preset folder (for example `userApplicationDataDirectory/<Publisher>/<Product>/presets`).

## 7. Release workflow
- The plugin version comes from the release tag (the workflow writes the project VERSION before CMake), so menu, installer and release match; no manual bump.
- If the release for that tag exists, upload with `gh release upload --clobber`; `gh release create` would fail on a rerun and leave the old zip live. An empty tag box can mean build only.
- The workflow builds `main` as it was when it started; after later pushes, rerun with the same tag.
- Before any push: `git pull --rebase`. Other sessions or people push to the same repos.
- Never commit generated caches (`__pycache__`); one held an absolute path.
- To apply one change across many repos: shallow-clone each, grep, patch, push; set the right commit identity first because fresh clones use another one.

## 8. Manuals people enjoy
- Include an Interface tour: a full-window screenshot with numbered control badges and lettered display badges, a one-line signal flow, one page per panel (crop, what each display shows with axes and colours, a numbered table of every control with range, default and tooltip text), and an "under the hood" page.
- Build it from data: screenshot the real editor with a headless browser, read tooltips from the page's `data-tip` attributes, write JSON, then let a script build the pages. Replace test-page screenshots with the compiled editor's screenshots when available.

## 9. Final gate (tick all)
- [ ] Old-state fixture loads; version number stored.
- [ ] Real editor snapshot compared with the mockup.
- [ ] pluginval passes; opened in a real host on each OS you claim.
- [ ] Resizing and HiDPI checked; choice controls tested at every item.
- [ ] Alias, level-match and responsiveness tests pass (see `plugin-dsp-quality`).
- [ ] Installer upgrades in place; uninstall works.
- [ ] Release created from the tag; links tested.
- [ ] Manual matches this version.
