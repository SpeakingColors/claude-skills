---
name: cubase
description: Use when helping with Steinberg Cubase on Windows, macOS or Linux (Wine recipe), covering editions, licensing, Linux status, hard dance workflow, VST3 host behaviour and testing your own plugins.
---

# Steinberg Cubase

Labels: VERIFIED = read in a fetched page (source in brackets); COMMUNITY = forum or blog report; UNVERIFIED = not checked, test before relying on it.
Researched 2026-10-21; upgraded 2026-10-23 for all three platforms. Re-check versions and prices before quoting them.

## Version and editions
- Current major version is Cubase 15, surprise-launched 5 Nov 2025 (VERIFIED, MusicTech [1]). Latest build listed is 15.0.30, 3 Jun 2026 (VERIFIED, Steinberg download page [2]).
- Editions: Pro, Artist, Elements (VERIFIED [1][3]). One installer covers all three; the license decides which edition opens (VERIFIED [2]).
- Launch prices: Pro 579 EUR / 579.99 USD, Artist 329 / 329.99, Elements 99.99 / 99.99 (VERIFIED, Attack Magazine [3]). Prices may have changed since.
- Pro-only in 15: Expression Maps overhaul, AI stem separation, six new modulators, UltraShaper. Pro and Artist: Melodic Pattern Sequencer, PitchShifter, Writing Room Synths, 40 Drum Machine kits. All editions: 30 Chord Pad presets, Groove Agent SE 6, Sampler Track hot-swap, DAWproject support, Omnivocal beta (VERIFIED [3]).
- Cubase 16: no announcement found. A Steinberg moderator said it will be announced when it happens (VERIFIED, forum thread [4]). Grace period: buyers after 8 Oct 2025 get 15 free; moderator says the grace period "is not an entitlement" (VERIFIED [3][4]).
- Supported OS: Windows 10 22H2+, Windows 11 24H2+, Windows 11 on Arm, macOS 14, 15, 26 (VERIFIED [2]). Linux is not listed.

## Platforms
Related skills: wine-proton-bottles (Bottles, runners, wineasio, yabridge, backups), linux-audio-production (PipeWire, JACK, realtime), bazzite-kde-linux.

### Windows
- Version: Cubase 15, build 15.0.30 listed (VERIFIED [2]). OS: Windows 10 22H2 or newer, Windows 11 24H2 or newer, Windows 11 on Arm (VERIFIED [2]).
- Install: Steinberg Download Assistant, then Activation Manager, Library Manager and MediaBay come with the install (VERIFIED [2]). One installer for Pro, Artist, Elements (VERIFIED [2]).
- Audio: ASIO is the low-latency path; Steinberg's own ASIO driver or the interface maker's driver (UNVERIFIED, not on the page read). WASAPI also exists in Windows (UNVERIFIED for Cubase 15).
- Plugin folders: C:\Program Files\Common Files\VST3 (UNVERIFIED for Cubase, standard for VST3; yabridge README names the same Common Files\VST3 layout, VERIFIED).
- Licensing: Steinberg Licensing with a Steinberg ID; up to 3 computers, release one to move; works offline after activation (VERIFIED [6]).

### macOS
- OS: macOS 14, 15 and 26 (VERIFIED [2]).
- Install: same Download Assistant and installer (UNVERIFIED that steps are identical).
- Audio: Core Audio is the system driver; no ASIO needed (UNVERIFIED for Cubase 15 menus).
- Plugin folders: /Library/Audio/Plug-Ins/VST3 and the same path under ~/Library (UNVERIFIED, standard). Audio Units in Cubase: UNVERIFIED, test before promising.
- Licensing: same Steinberg ID, same 3-computer rule across Windows and macOS (VERIFIED [6] states the rule; per-OS differences not found, UNVERIFIED).
- Key commands use Cmd instead of Ctrl (UNVERIFIED).

### Linux
- No native Linux version, not a supported platform (VERIFIED [2]; COMMUNITY [8]). See "Linux status" and the Wine recipe below.
- Audio on Linux for native apps would be PipeWire or JACK (see linux-audio-production). Under Wine it goes through wineasio (section "Run it on Linux").
- Plugin folders for bridged Windows plugins: ~/.vst3/yabridge (VERIFIED, wine-proton-bottles section 8).
- Licensing on Linux: Steinberg Licensing needs the Activation Manager (a Windows program) to run inside Wine. Result: UNVERIFIED, no confirmed report found.

## Licensing
- eLicenser (USB dongle) was switched off 20 May 2025 (VERIFIED, Sound On Sound [5]). Cubase 15 uses Steinberg Licensing, a Steinberg ID system (VERIFIED, Steinberg Help Center [6]).
- A license can be active on up to 3 computers; release it on one to move it. After activation it works offline (VERIFIED [6]).
- eLicenser products cannot be used under Steinberg Licensing; old licenses must be registered in MySteinberg and upgraded via the Download Assistant (VERIFIED [6]).
- Install needs Steinberg Download Assistant, Activation Manager, Library Manager, MediaBay (VERIFIED [2]).
- Reported activation failures: "no license found", Activation Manager stuck on sign-in. Reported fixes: reinstall Download Assistant; open Activation Manager first and wait for authorization; do not run it as Administrator (COMMUNITY, Steinberg forum [7]).

## Linux status
- No native Linux version, and Linux is not a supported platform (VERIFIED [2]; COMMUNITY, Home Studio Grooves, Aug 2026 [8]).
- No Steinberg staff statement on Linux was found; the long Linux request thread is users only (VERIFIED, read pages 27 and 29 of [9]).
- Wine: one user wrote in Mar 2026 that Cubase and Nuendo do NOT run on Wine, suspecting copy protection and licensing (COMMUNITY [9]). Another says Wine does not work with iLok-style protection (COMMUNITY [9]).
- Blog says licensing and plugin licensing are the main Wine failure points and low-latency audio was the hardest part (COMMUNITY [8]). It did not name a tested Cubase version.
- WineHQ AppDB: could not be fetched (fetch blocked), so no AppDB rating is confirmed (UNVERIFIED).
- Bazzite plan: do not count on Cubase. Native options are Bitwig and Reaper; keep Cubase on a Windows or macOS machine if needed (my recommendation, based on the above).
- If you try Wine anyway: use a Bottles prefix, WineASIO over PipeWire-JACK for audio, and yabridge for plugin GUIs (COMMUNITY, general practice; Wine 9.21 staging recommended for yabridge in Mar 2026 [9]). Cubase itself on this stack: UNVERIFIED.

## Run it on Linux (Wine, Bottles, Proton)
Honest status first. No source I read shows Cubase 15 running under Wine. One user wrote in Mar 2026 that Cubase and Nuendo do not run (COMMUNITY [9]). WineHQ AppDB could not be read, so no rating is confirmed (UNVERIFIED). Treat everything below as an experiment, not a promise. Do not buy Cubase to try this. If you already own it, try it on a copy and keep notes.
Details of every tool are in wine-proton-bottles. Do one step, test, then go on.

Step by step (Bottles, Flatpak, on Bazzite; all steps UNVERIFIED for Cubase unless a label says otherwise):
1. Install Bottles from Bazaar or Flathub (VERIFIED, wine-proton-bottles section 3). Give it access only to the folder holding the Cubase installer, with Flatseal or `flatpak override --user --filesystem="/path/to/folder" com.usebottles.bottles` (VERIFIED, wine-proton-bottles).
2. New bottle: name it Cubase15, environment Software, runner Caffe (VERIFIED defaults, wine-proton-bottles section 4). Windows version: Windows 10 or 11 if Bottles offers a choice (UNVERIFIED). 64-bit prefix is a must for yabridge (VERIFIED, README).
3. Dependencies: in the bottle, Dependencies, install the vcrun and .NET entries your Bottles version lists. Look in the list; do not guess names (VERIFIED advice, wine-proton-bottles section 5). Add corefonts. Install one at a time.
4. Download the Steinberg Download Assistant on any machine, or in the bottle's browser. Run its installer inside the bottle (Run executable). Expect it to fail first; note the exact message (COMMUNITY [7] reports Download Assistant and Activation Manager sign-in problems even on Windows).
5. Activation: sign in with your Steinberg ID in Activation Manager. Steinberg Licensing is account based (VERIFIED [6]). If Activation Manager stays stuck: do not run as Administrator (COMMUNITY [7]).
6. Old licences: eLicenser, Soft-eLicenser and USB dongle do not work with Cubase 15; eLicenser was switched off 20 May 2025 (VERIFIED [5][6]). So a dongle is not an option here. Older Cubase versions that need Soft-eLicenser or a dongle under Wine: UNVERIFIED, expect failure. Wine and iLok-style protection: reported not to work (COMMUNITY [9]).
7. Audio, WineASIO: build or get wineasio matching the bottle's Wine (VERIFIED requirement, wine-proton-bottles section 7). Register with `wineasio-register` for the bottle prefix. Bottles Flatpak uses its own runner, so a system-wide install does not reach it; a Flatpak recipe is UNVERIFIED (wine-proton-bottles). If this stalls, stop here and use the fallback in step 8.
8. Fallback audio: Wine's PulseAudio driver gives worse latency but may work (UNVERIFIED). In Cubase, Studio, Studio Setup, VST Audio System, pick the driver (UNVERIFIED menu path).
9. PipeWire/JACK: PipeWire's JACK layer serves wineasio. Set the graph buffer first (`pw-metadata -n settings 0 clock.force-quantum 256`, VERIFIED command, linux-audio-production section 3). WineASIO env var WINEASIO_PREFERRED_BUFFERSIZE; a size the backend rejects can stop JACK (VERIFIED, wine-proton-bottles section 7).
10. Windows VST3 plugins: yabridge needs Wine Staging, tested on 9.21; 9.22 and 10.x failed with yabridge 5.1.1 (VERIFIED, README). It does not work with Flatpak hosts (VERIFIED). A Wine Cubase hosts plugins inside the same prefix instead, so plugins install in the bottle and need no yabridge (UNVERIFIED). Use yabridge only for native Linux hosts such as Bitwig (see bitwig-studio skill).
11. Backup before experiments: Bottles, bottle menu, Duplicate (clone as template); Full Backup (VERIFIED, wine-proton-bottles section 11). Back up Cubase projects and sample libraries separately, outside the bottle.

How to TEST that it works (stop at the first fail, report it):
1. Cubase starts and shows a window within 60 seconds.
2. Activation Manager shows a valid Cubase licence, and it survives a restart.
3. Studio Setup lists an audio driver and a sample rate you can set.
4. Play an audio file for 10 minutes with no crackle at a 512 buffer; then 256.
5. Open the VST Plug-in Manager; stock plugins load; one of your own VST3s loads.
6. Save, close, reopen a project; plugin state restored.
7. Export Audio Mixdown works and the file plays.
8. Run `pw-top`: ERR column stays flat during playback (COMMUNITY meaning, linux-audio-production).

Known problems and fixes (all UNVERIFIED for Cubase; general Wine):
- GUI glitches or black windows: toggle DXVK off in the bottle (wine-proton-bottles section 5); try runner Vaniglia, then Caffe (VERIFIED order, section 10).
- Crash with no message: run Bottles from a terminal and read ERROR lines (VERIFIED, wine-proton-bottles).
- Stuck processes after a crash: `ujust fix-proton-hang` (VERIFIED).
- Activation Manager or Download Assistant fail: reinstall the Download Assistant; open Activation Manager first and wait (COMMUNITY [7], Windows advice).
- Missing text in plugin GUIs: install corefonts or allfonts (VERIFIED, yabridge README, for yabridge).
- Keep the prefix on ext4 or btrfs, not NTFS (VERIFIED, wine-proton-bottles).

What NOT to rely on for gigs or deadlines:
- Licence persistence: online checks may fail without notice. Keep a Windows or macOS install for paid work (my recommendation).
- Low-latency live monitoring or live playing through Wine: untested.
- Copy-protected plugins (iZotope, D16 and others) cannot authorise (VERIFIED, yabridge README).
- Updating Wine, Bottles or the OS mid-project: a new Wine can break the prefix (VERIFIED for yabridge, README).
- Native alternative on Bazzite: Bitwig or Reaper (my recommendation).

## VST3 host behaviour and your JUCE plugins
- Cubase is the Steinberg VST3 host, but that does not make it lenient; treat it as the strict reference host (my recommendation).
- Latency: Cubase can disable a VST3 whose reported latency exceeds its threshold. Raising Preferences > VST > "Delay Compensation Threshold" to at least ~372 ms fixed a JUCE plugin reporting 16384 samples (COMMUNITY, JUCE forum, old thread [10]; re-test on 15).
- Constrain Delay Compensation: turns on a VST3's low latency ("Live") mode where one exists and bypasses plugins without one on instrument, record-armed, group and output channels; ignores FX channels. Turn off after recording (VERIFIED, Steinberg manual [11]).
- Note Expression works only with VST3 instruments that support it (VERIFIED, manual [12]). MPE input can be recorded as note expression (page title seen, content not read; UNVERIFIED).
- Sidechain: activate the plugin's external side-chain button, then pick it in a channel send's Side-chain submenu (VERIFIED, Sound On Sound, written for Cubase 4.1 [13]). That article says most third-party plugins did not support it then; current behaviour with third-party VST3 sidechain buses is UNVERIFIED, test with your own compressor.

## Hard dance workflow (features exist; step details UNVERIFIED for 15 unless noted)
- Chord Track: chord and scale events can control or transpose MIDI, instrument and audio playback (VERIFIED, manual v12 [14]).
- Chord Pads: one pad plays a full chord on the instrument track; Circle of Fifths assistant, Adaptive Voicing, recording captures MIDI (VERIFIED, SOS [15]). Good for trance chord stacks.
- Arranger Track: define sections of any length, reorder with repeats, keep several chains, flatten to linear when final; only one per project (VERIFIED, manual v12 [16]). Use for intro, build, drop, break.
- Sampler Track: drop kick or vocal chops, hot-swap via MediaBay in 15 (VERIFIED [3]).
- Groove Agent SE 6 and Drum Machine: new in 15 (VERIFIED [3]). Hardstyle kicks: still render your distorted kick to audio (my recommendation).
- MixConsole and Control Room: both exist; setup specifics not fetched (UNVERIFIED for 15).
- Template idea: kick, rumble, sub, leads, FX, drums in folder tracks; a "Kick Sidechain" group or FX channel; Arranger track at top; save as project template (my recommendation).
- Master: bounce at 24 or 32-bit float, leave headroom, limit in a dedicated master project (my recommendation).

## Expert use: hard dance, trance (facts I can source; the rest is my recommendation)
- Tempo: Cubase project tempo and tempo track support any BPM; hardstyle 150 to 160, UK hardcore 160 to 175, trance 135 to 145 (UNVERIFIED, genre knowledge).
- Chord Pads plus Chord Track for trance stacks: one pad plays a full chord; recording captures MIDI (VERIFIED [15]).
- Arranger Track: build Intro, Build, Drop, Break chains; keep alternatives; flatten when final (VERIFIED [16]).
- Sampler Track: kick and vocal chops, hot-swap via MediaBay (VERIFIED [3]).
- Pro-only in 15: Expression Maps overhaul, stem separation, six modulators, UltraShaper (VERIFIED [3]). UltraShaper use for distortion: UNVERIFIED.
- Mastering: Cubase has no project page; bounce stems and master in a dedicated project (my recommendation).
- Kick workflow: render the distorted kick to audio, then EQ, clip and compress the bounce. Rumble: kick tail, low-pass, sidechain to the kick (UNVERIFIED, shared with other DAW skills).
- Platform note: plugin and workflow facts above are the same on Windows and macOS; on Linux they apply only if Cubase runs (see recipe).

## Key commands (Windows/Ctrl layout; macOS uses Cmd, UNVERIFIED; Linux has none)
- Space play/stop; Ctrl+Z undo; Ctrl+S save; Shift+Ctrl+S save as; F3 MixConsole; Alt+F3 MixConsole in lower zone; Ctrl+Alt+E toggle lower zone; E channel settings; T add track dialog (VERIFIED, Cubase Key Commands Guide [17]).
- Tools: 1 select, 3 split, 4 glue, 7 mute; J snap; H/G zoom in/out horizontally (VERIFIED [17]).
- Not covered by the guide: Project Setup, Devices, Bounce, Render in Place, Key Editor keys. Look them up in Key Commands (UNVERIFIED).

## Test checklist for your own plugins (run in Cubase on Windows, macOS or Wine)
1. Scan: VST Plug-in Manager lists the VST3, no blocklist entry; check instrument vs effect category.
2. Preset recall: save project, close, reopen; compare all parameters, patch name and GUI state.
3. Automation: write from the GUI and from a host lane; check Read/Write, undo, and no zipper noise.
4. Sample rate change: 44.1, 48, 96 kHz in Project Setup and in the audio device; no crash, silence or stuck tails.
5. Offline render: Export Audio Mixdown and Render in Place versus realtime; they must match, including random or LFO phase.
6. Latency and PDC: report latency, raise the delay threshold test, check Constrain Delay Compensation on and off; null test against a dry duplicate.
7. State restore: project with several instances and different presets; duplicate track, copy settings, reload.
8. Bypass and enable/disable: no clicks, no stuck notes; reset on transport stop.
9. Sidechain bus (if any): confirm host offers it and routing survives reload.
10. Note Expression or MPE (if supported): record and replay.
11. Cross-platform: same project on Windows and macOS; plugin found, same state, same render.
12. Wine only: plugin GUI opens, resizes, and does not freeze Cubase when closed.

## Not verified
Cubase 15 under Wine or Proton (any result); WineHQ AppDB rating; Steinberg Licensing inside Wine; ASIO and Core Audio menus in 15; Windows and macOS plugin folders as Cubase scans them; AU and VST2 support in 15; Cmd shortcuts; per-OS licence differences. Fetch limit reached 2026-10-23, so Steinberg system requirements, AppDB and licensing pages were not re-read; versions come from the 2026-10-21 research. Check whether Cubase 16 has appeared.

## Sources (fetched)
1. https://musictech.com/news/cubase-15-everything-you-need-to-know/
2. https://o.steinberg.net/en/support/downloads/cubase_15.html
3. https://www.attackmagazine.com/news/cubase-15-released-heres-whats-new/
4. https://forums.steinberg.net/t/when-cubase-16-is-accounced-released-when-i-can-safely-buy-it-with-the-grace-period-thanks/1039945
5. https://www.soundonsound.com/news/steinberg-elicenser-support-end-may
6. https://helpcenter.steinberg.de/hc/en-us/articles/26707291820562
7. https://forums.steinberg.net/t/cubase-15-install-issues/1013695
8. https://homestudiogrooves.com/run-cubase-on-linux/
9. https://forums.steinberg.net/t/cubase-and-nuendo-support-for-linux/716449?page=29 (also page=27)
10. https://forum.juce.com/t/setlatencysamples-int-newlatency-in-cubase-and-bitwig-in-vst3-win-and-mac/15061
11. https://archive.steinberg.help/nuendo/v12/en/cubase_nuendo/topics/vst_instruments/vst_instruments_constrain_delay_compensation_c.html
12. https://archive.steinberg.help/nuendo/v11/en/cubase_nuendo/topics/note_expression/note_expression_halion_sonic_se_c.html
13. https://www.soundonsound.com/techniques/side-chaining
14. https://archive.steinberg.help/cubase_pro/v12/de/cubase_nuendo/topics/chord_functions/chord_functions_chord_track_c.html
15. https://www.soundonsound.com/techniques/cubase-using-chord-pads
16. https://archive.steinberg.help/nuendo/v12/en/cubase_nuendo/topics/arranger_track/arranger_track_c.html
17. https://daftdogmusic.com/wp-content/uploads/2026/06/Cubase-Key-Commands-Guide-John-Walden.pdf
