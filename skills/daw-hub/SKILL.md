---
name: "daw-hub"
description: Use first for any DAW, audio editor or audio processing question; picks the right app for the job and routes to the detailed skill, on Linux (Bazzite), Windows or macOS.
---

# DAW and audio software hub

This is the front door. It does not hold the details. It picks the right app, then you load the detailed skill and answer from that.
Rules for Claude: the user is not a programmer. Short answer first, one step at a time, bullets for steps. Never invent versions, prices or menu names. If the detailed skill labels something UNVERIFIED, say so and test it.
Labels used everywhere: VERIFIED (read in a source), COMMUNITY (forum or project report), UNVERIFIED (not checked).
Re-check versions and prices on the vendor page before quoting; the detailed skills were researched in Oct 2026.

## 1. How to use this hub
1. Ask or work out: which job (section 3), which OS (Bazzite, Windows, macOS), which app.
2. Load the detailed skill from section 2 with the Skill tool.
3. For setup problems also load the support skill from section 4.
4. Answer from the detailed skill. Copy its labels. If it has a test checklist, give it as steps.

## 2. App map (skill name, role, Linux reality)
Linux reality is the one-line summary; the skill has the proof and the steps.

DAWs
- bitwig-studio: DAW. Native Linux build, Flatpak on Bazzite. Best native choice for plugins and modular work.
- reaper: DAW. Native Linux. Light, scriptable, good plugin tester.
- ardour: DAW. Open source, native Linux.
- waveform: Tracktion Waveform. Linux build exists; see skill for install on Bazzite.
- ableton-live: DAW. No native Linux. Community route only (ableton-linux project, Wine). Not for gigs.
- fl-studio: DAW. No native Linux. Wine via Bottles, fragile. Check the guide before every update.
- cubase: DAW. No native Linux. No confirmed Wine report. Keep on Windows or macOS.
- studio-one-fender-studio-pro: DAW (Studio One is now Fender Studio Pro). Linux public beta .deb reported by a retailer blog (COMMUNITY). Test in a distrobox.
- logic-pro: DAW. Mac only, no Linux.
- pro-tools: DAW. See skill for Linux or Wine status and iLok limits.

Editors and mastering
- wavelab: mastering and audio editor, Steinberg. Bazzite via Bottles per skill.
- sound-forge: audio editor, Windows app. See skill for Wine status.
- audacity: free audio editor, simple edits and clean up.

Max and controllers
- max-for-live-expert: build and debug Max for Live devices.
- ableton-push-expert: Push 1, 2, 3 and Push 3 Standalone.

Music craft (app independent)
- electronic-music-producer: melody, chords, rhythm, arrangement ideas.

## 3. Job picker (pick one, then follow section 1)
- I want the best native Linux DAW now: bitwig-studio first, reaper second, ardour third.
- I want my Ableton or FL workflow on Linux: ableton-live or fl-studio, plus wine-proton-bottles. Say plainly it is unofficial.
- I need Cubase or Logic or Pro Tools: only Windows or macOS are safe. Read the Linux section of the skill before promising anything.
- I need to test my own VST3 or CLAP plugin: every DAW skill has a Test checklist. Start with bitwig-studio or reaper on Linux; repeat in the others.
- I need to edit or clean one audio file: audacity, or wavelab or sound-forge for pro work.
- I need to master a track or an EP: wavelab for the tool.
- I need to build a Max device: max-for-live-expert.
- I need to control the DAW with hardware: ableton-push-expert, plus the DAW skill.

## 4. Support skills (load alongside when setup breaks)
- bazzite-kde-linux: the OS, Flatpak, distrobox, rollback.
- linux-audio-production: PipeWire, WirePlumber, JACK, realtime, xruns, interfaces.
- audio-driver-stacks: ASIO, WASAPI, Core Audio, ALSA, PipeWire side by side.
- audio-interface-digital-io: interfaces, ADAT, clocking, RME Digiface USB.
- wine-proton-bottles: Bottles, runners, wineasio, yabridge, backups.
- vst-maker: building your own plugins (JUCE, VST3).

## 5. Install order on Bazzite (generic, one step at a time)
1. Update the system and reboot once (bazzite-kde-linux).
2. Check audio works with the interface (linux-audio-production): `aplay -l`, then `pw-top`.
3. Install one native DAW first (bitwig-studio or reaper). Prove audio, MIDI and one plugin.
4. Only then add Wine based apps. One bottle per app. Duplicate the bottle before any experiment.
5. Back up projects and samples outside any bottle or prefix.

## 6. Cross platform rules that hold in every skill
- Plugin folders differ per OS; each DAW skill lists them with labels. Do not guess.
- Windows plugins on Linux: inside Wine apps they install in the same prefix; for native Linux hosts use yabridge (needs Wine Staging; not for Flatpak hosts). See wine-proton-bottles.
- Native Linux plugin builds do not load in a Windows DAW running in Wine. Test them in a native Linux host.
- Never update Wine, a runner or the DAW right before a gig or deadline.
- Keep a Windows or macOS fallback for paid work when a DAW runs only through Wine.

## 7. Debug flow (teach this, so the user learns it)
1. What exactly happens? Copy the error text.
2. Does it happen in a native host too? (isolates the plugin from the Wine layer)
3. Change one thing, test, write the result down.
4. Load the support skill for the layer that fails (audio, Wine, OS).
5. If a source is missing, say UNVERIFIED and test instead of guessing.

## 8. Not covered here
- Prices, versions and OS minimums: always from the detailed skill, re-checked on the vendor page.
- Any app without a skill: research it first, then label every claim.