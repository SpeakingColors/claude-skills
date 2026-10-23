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

## 9b. More JUCE and build gotchas (COMMUNITY, from real builds)
- Newer JUCE versions remove old APIs. Example: `juce::Font::getStringWidthFloat` was removed; use `juce::GlyphArrangement::getStringWidth(font, text)`. Read the BREAKING_CHANGES file of the JUCE version you update to, and build in CI against the new version before releasing a security update.
- `juce::Label` constructed with one string sets the component name, not the shown text, so labels can appear blank. Use `setText`.
- Local JUCE configure without X11 development headers or ALSA: pass compile definitions such as `-DJUCE_USE_XRANDR=0 -DJUCE_USE_XINERAMA=0 -DJUCE_USE_XCURSOR=0 -DJUCE_USE_XRENDER=0 -DJUCE_USE_XSHM=0 -DJUCE_ALSA=0 -DJUCE_JACK=0`. UNVERIFIED for your setup; it only helps compile-checks.
- A repo that builds two VST3 bundles (an instrument and an effect from one code base): stage every `*.vst3` with `find -print0` in the release workflow, and build both Flatpak targets.
- Flatpak extension format (copied from a Flathub audio plugin manifest): runtime `org.freedesktop.LinuxAudio.BaseExtension`, prefix `/app/extensions/Plugins/<Name>`, VST3 in `<prefix>/vst3`. Plugin extensions must match the host's Freedesktop runtime branch; check which branches exist (one project found 24.08 and 23.08 had no LinuxAudio base on Flathub and used 25.08). Re-check.
- Flatpak hosts could not always read plugin files in `/usr/lib/vst3` or the home folder, or presets stored under `~/.local/share/<vendor>` (single-user reports, 2023 and 2024): embed factory presets and assets in the plugin (JUCE BinaryData) and test in a Flatpak host.
- Release zips that cannot be downloaded in the CI sandbox cannot be inspected there: make the workflow itself check that each installer contains the `.vst3`.
- Windows installers: an unsigned installer gets a strong SmartScreen block; signing options (Azure Artifact Signing, an OV certificate, SignPath Foundation for qualifying open source) change, so read the current Microsoft page. macOS: unsigned or ad-hoc signed packages trigger Gatekeeper; notarisation needs a Developer ID certificate, hardened runtime and `notarytool`. VERIFIED earlier from Microsoft and Apple docs; re-check prices and rules before quoting.
- Per-repo hygiene: README screenshot of the real window, `docs/index.html` with manual, source and test links, and a "not affiliated with" line when you name a vendor's hardware or products. Enable GitHub Pages yourself if you want the docs page live.
- Screenshot recipe: headless Chromium with `deviceScaleFactor` 1.5 to 2; hide tooltip overlays before shooting; for the real JUCE window build the Standalone target and run it under `xvfb-run`, wait a few seconds, capture the root window and crop. Do not use manual tour images as README shots (they carry numbered badges). Never commit a build symlink to a third-party JUCE tree.

## 9c. Licensing of assets and ideas
- Studying a commercial product's feature list, screenshots and manual is fine; copying its code, presets, samples, name, layout or look is not. Note "ideas only" in the notes.
- Third-party waveform packs may be personal-use only even when free to download. Do not bundle or redistribute them. Generate your own waveforms, or let users load their own from a folder. The AKWF single-cycle waveforms are described by their author as CC0; confirm at the original source before bundling. UNVERIFIED here.
- JUCE projects: AGPLv3 unless you hold a commercial JUCE licence. Say which one applies in the README (see `juce-expert` section 1).

## 9d. Cross-instance features (analysers, linked EQs)
- Sharing data between plugin instances in one host (shared memory or a process-wide singleton) is UNVERIFIED: some hosts run plugins in separate processes or sandboxes. Test in every host you claim to support before promising it. Report latency differences between tracks when comparing them.
- A plugin can only analyse what the host sends it; it cannot capture other applications' audio.

## 9. Final gate (tick all)
- [ ] Old-state fixture loads; version number stored.
- [ ] Real editor snapshot compared with the mockup.
- [ ] pluginval passes; opened in a real host on each OS you claim.
- [ ] Resizing and HiDPI checked; choice controls tested at every item.
- [ ] Alias, level-match and responsiveness tests pass (see `plugin-dsp-quality`).
- [ ] Installer upgrades in place; uninstall works.
- [ ] Release created from the tag; links tested.
- [ ] Manual matches this version.
