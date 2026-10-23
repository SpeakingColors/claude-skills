---
name: logic-pro
description: Use when helping with Apple Logic Pro, covering versions, price, Mac-only status (no Linux), Audio Units, testing your own JUCE plugins, sidechain, hard dance workflow and bouncing.
---

# Apple Logic Pro

Researched 2026-10-23. Re-check versions and prices before quoting them.
Labels: VERIFIED (source number) = read on a page I fetched. COMMUNITY = forum or blog report. UNVERIFIED = not read on a page; test before relying on it.
Rules for Claude: Assume the reader is not a programmer. Plain words first, then one exact step. One change at a time, ask the reader to test, then continue.
Blocked or failed fetches: Reddit (blocked), Gearspace (fetch failed), KVR (fetch failed), apple.com/logic-pro/faq (fetch failed). Nothing here comes from those sites.

## 1. Versions, requirements, editions
- Current: Logic Pro for Mac 12.4 and Logic Pro for iPad 3.4. VERIFIED [1]
- Logic Pro 12 launched Jan 2026 with Apple Creator Studio; Intel Mac support was dropped. VERIFIED [2][3]
- Mac minimum: Apple support page says macOS 15.4 or later and Apple silicon. apple.com says macOS 15.6 or later. The two pages disagree, so quote both. VERIFIED [1][4]
- Intel: one forum user said v12 launched on Intel but lacks silicon-only features. COMMUNITY [5]. Apple does not support it. VERIFIED [1]
- iPad: iPadOS 26 or later and A12 Bionic or newer; some features need A17 Pro or newer. VERIFIED [1][4]
- There are no Intro/Pro editions. One app on Mac; MainStage is a separate app. VERIFIED [4]
- 12.0 (VERIFIED [6]): AI Session Players, Sound Library, Step Sequencer and Chord Track additions, new Plug-In Manager Hide and Ignore columns.
- 12.0 reviewed (VERIFIED [7]): Chord ID, Synth Player styles, QTA spatial playback, Quantec Room Simulator to 7.1.4. Verdict: useful, not groundbreaking.
- 12.2: Dolby Atmos export, legacy content via sound packs. 12.3: Beat Breaker filter, resonance, pan and randomize; Alchemy granular sync and formant shifting. VERIFIED [6]
- 12.4: AU fixes (see section 4). VERIFIED [6]. The release notes page lists no dates for versions. VERIFIED [6]
- Sound on Sound lists a new Studio Piano instrument (Aug 2026 article, title only). COMMUNITY [8]

## 2. Price and licensing
- One-time purchase for Mac: 199.99 USD. MainStage 29.99 USD. VERIFIED [4]
- Apple Creator Studio subscription: 12.99 USD per month or 129 per year, 30-day trial. Education 2.99 per month or 29.99 per year. Includes Logic Pro (Mac and iPad) and MainStage, plus Final Cut Pro and other Apple apps. VERIFIED [4][7]
- Both versions have the same features, per Apple. VERIFIED [4]
- Existing Logic owners upgrade to 12 for free. VERIFIED [7]
- The Mac app is bought once from the Mac App Store. The iPad app is subscription only. VERIFIED [3] (UK page). Starting Creator Studio stops a separate iPad subscription from renewing. VERIFIED [9]
- Logic 12 adds Manage Subscription to the app menu. VERIFIED [7]
- What happens to a Mac app you own if you also subscribe: UNVERIFIED (Apple page did not say).
- Apple Intelligence: apple.com says some AI features need an Apple Intelligence capable device. Which ones: UNVERIFIED [4]

## 2a. Platforms (Windows, macOS, Linux)
| | Windows | macOS | Linux |
|---|---|---|---|
| Logic Pro | None. VERIFIED [1][4] | Yes, Apple silicon, macOS 15.4 or 15.6 and later (section 1) | None. VERIFIED [1][4] |
| Install | n/a | Mac App Store, one-time purchase, or Apple Creator Studio subscription. VERIFIED [3][4] | n/a |
| Audio path | n/a | Core Audio. Class-compliant USB interfaces need no extra driver (said of macOS in the Waveform manual, VERIFIED, not on a Logic page). Logic's own audio settings page: UNVERIFIED | n/a |
| Plugin format | n/a | Audio Units only (section 4). Folders in section 5 | n/a |
| Licence | n/a | Apple account; Mac app is bought once. VERIFIED [3] | n/a |
- Windows and Linux users need another DAW. See section 3a.
- Your own JUCE plugins: Linux and Windows builds cannot be AU. JUCE builds AU on macOS only. VERIFIED [11]
- Moving a song to another PC: Logic projects open on Mac only (iPad opens packages, VERIFIED [46]). Use stems.
  1. On the Mac: File > Save a Copy As, so all recordings are included. VERIFIED [44]
  2. Bounce each group as 24-bit WAV, all from the same start point (general practice, UNVERIFIED for Logic). Stem steps: UNVERIFIED (section 10).
  3. Copy the WAV files to a USB drive. Import them into the new DAW on the same bar. MIDI export steps: UNVERIFIED.
  4. Third-party AU plugins have no Linux twin. Check each vendor for a VST3 or LV2 build. UNVERIFIED per vendor.

## 3. Linux and Wine status
- Logic Pro is Mac and iPad only. Apple lists only macOS and iPadOS. VERIFIED [1][4]
- Wine is NOT a route. Logic is a macOS program, and Wine runs Windows programs. Bottles, Proton and winetricks do not help. (my reasoning from the platform facts above)
- I found no report of Logic Pro running under Wine, Proton or Bottles. UNVERIFIED. Treat as impossible.
- Darling (macOS apps on Linux) says it is far from running Logic Pro. Commenters add: App Store copy protection, and nobody has rebuilt the macOS audio and MIDI frameworks. COMMUNITY [10]
- macOS in a virtual machine on Linux: UNVERIFIED. Apple licence terms, GPU, Core Audio latency and USB passthrough were not read. Do not plan around it.
- Linux builds of your own plugins cannot produce Audio Units. JUCE builds AU only on macOS. VERIFIED [11]

## 3a. Linux alternatives (native, no Wine)
Read the linked skill before advising on each one.
1. Ardour (skill: ardour). Free GPL v2 DAW, Linux, macOS and Windows. VERIFIED (ardour skill). Cue page for loop sketching, like Live Loops in idea. VERIFIED (ardour skill, manual)
2. Reaper (skill: reaper). Native Linux build. Details in that skill.
3. Bitwig Studio (skill: bitwig-studio). Native Linux, PipeWire driver since 4.3. VERIFIED (linux-audio-production skill, Bitwig support page).
4. Tracktion Waveform 14 (skill: waveform). Linux build listed on tracktion.com, Pro features unlocked on Linux. VERIFIED (waveform skill). Has Chord track, Step clips, Clip Launcher, Arranger track, Pattern Generator.
- Feature mapping (idea level only; check each skill): Live Loops to Waveform Clip Launcher or Ardour Cue page; Step Sequencer to Waveform Step clips; Chord Track to Waveform Chord track; Compressor sidechain exists in all four.
- No known equivalent of Session Players, Stem Splitter or ChromaGlow in these DAWs. UNVERIFIED.
- Audio and plugin setup for any of them: skill linux-audio-production (PipeWire, JACK, realtime, plugin paths).
- Plan for a Bazzite studio PC: pick one alternative, test with one old song, keep Logic only if you own a Mac. (my recommendation)

## 4. Plugin formats and Audio Units
- Logic hosts Audio Units only. VST and VST3 are not hosted. Apple's old manual says Logic cannot host VST or RTAS; wrapper tools exist. VERIFIED [12] (Logic Pro 9 manual, old). Current-version statement: UNVERIFIED.
- Apple silicon Macs: Logic supports most AU v2 and v3 plug-ins. Intel-only builds need Rosetta installed. VERIFIED [13]
- Logic itself should not run under Rosetta. Exception: ARA plug-ins such as Melodyne. VERIFIED [13]
- Under Rosetta (or on Intel), Stem Splitter, ChromaGlow and some Mastering Assistant presets are missing. Fix: Get Info on Logic Pro, untick Open using Rosetta. VERIFIED [14]
- Plug-in Manager: needs Show Advanced Tools on in Advanced settings. Validation runs on first open, after Logic updates, and after plug-in installs. Results show in the Compatibility column. VERIFIED [15]
- Failed plug-ins: click Show All, tick Use at your own risk; Disable Failed Audio Units if it misbehaves. VERIFIED [15]
- 12.4 fixed: AUs vanishing from the Plug-in Manager top level after restart, cancelled scans, Rosetta switch triggering a scan, AUv3 time signature and down beat. Added surround side chains for AUs. VERIFIED [6]
- 12.0 fixed: AUv3 windows resizable, meters in latency-compensated plug-ins. VERIFIED [6]
- Recently installed plug-in missing, in order (VERIFIED [16]):
  1. Confirm 64-bit. Restart Mac and Logic. Check the slot menu.
  2. Settings > Plug-in Manager. Filter by manufacturer. If "failed validation", select it and click Reset & Rescan Selection.
  3. Still failing: Full Audio Unit Reset, then reopen Logic.
  4. Last resort: move the files in ~/Library/Caches/AudioUnitCache to the Desktop, restart.
- Native Instruments also advise giving Logic Full Disk Access and deleting the plug-in's cached plist. COMMUNITY (vendor article) [17]

## 5. Testing your own JUCE plugins in Logic
Needs a Mac (or a macOS CI runner). If you build on Linux, AU testing happens elsewhere. VERIFIED [11] for AU being macOS only.
- CMake `juce_add_plugin`: FORMATS AU, PLUGIN_MANUFACTURER_CODE needs at least one uppercase letter, PLUGIN_CODE needs exactly one uppercase letter, AU_MAIN_TYPE (kAudioUnitType_*), IS_SYNTH, NEEDS_MIDI_INPUT, COPY_PLUGIN_AFTER_BUILD. VERIFIED [11]
- Keep PLUGIN_CODE fixed. By default it is random per configure, which breaks saved projects. VERIFIED [11]
- Install to ~/Library/Audio/Plug-Ins/Components/ or /Library/Audio/Plug-Ins/Components/. auval only sees those. VERIFIED [18]
- Validate in Terminal (not iTerm or SSH, which hide third-party AUs). COMMUNITY [19]
  - Effect: `auval -strict -v aufx PLUGCODE MANUCODE`. Synth: `aumu`. Effect with MIDI: `aumf`. VERIFIED [18]
  - Stale cache: `killall -9 AudioComponentRegistrar`, or log out and in. VERIFIED [18]
  - Error 4099: bus layout does not match the AU type you registered. VERIFIED [18]
- Logic does not use pluginval's stress test, so a plug-in can fail stress and still load. COMMUNITY [18]
- A crash in auval was traced to a downsampler reading past its buffer at low sample rates. COMMUNITY [20]
- Build arm64 (and x86_64 only if you need Intel). Universal binary advice: UNVERIFIED.
Test checklist (run in Logic):
1. Plug-in Manager: shows Passed, correct manufacturer and category.
2. Insert on a track; open and close the window ten times; resize.
3. Save project, quit, reopen: parameters and GUI state restored.
4. Automation: write from the GUI and from a lane; no zipper noise.
5. Change project sample rate (44.1, 48, 96 kHz); no silence or crash.
6. Bounce (File > Bounce > Project or Section) Offline and Realtime; files match.
7. Latency: compare with a dry copy (null test); check Low Latency mode.
8. Duplicate track, copy settings, many instances with different presets.
9. Bypass and transport stop: no clicks, no stuck notes.
10. Synths: MIDI input, Scripter feeding the plug-in, Step Sequencer.

## 6. Built-in instruments and tools (what the pages say)
- Alchemy: three views (Browse, Simple, Advanced). Four sources A to D per preset. VERIFIED [21][22] apple.com says over 3,000 sounds. VERIFIED [4]
- Retro Synth: exists; 12.3 fixed its fields and added Save As for wavetables. VERIFIED [6] Design details: UNVERIFIED.
- Drum Machine Designer: a track stack, main track plus one subtrack per pad. Each pad has input and output note. Notes on the main track route by pad. Not a plug-in. VERIFIED [23]
- Session Players: Drummer, Bass, Keyboard, Synth. They follow the Chord Track. VERIFIED [4] Synth Player: Simple Pad, Modulated Pad, Rhythmic Chords; 808 Bass, Pump Bass, Sequenced Bass. VERIFIED [24][7]
- Synth Players can drive Logic synths and samplers, third-party AUs and hardware via External Instrument. VERIFIED [7]
- Stem Splitter: Control-click an audio region > Processing > Stem Splitter, pick preset, Apply. Makes a summing stack, mutes the original. Needs M1 or later. VERIFIED [25]
- ChromaGlow: saturation plug-in from Logic 11. Five models (tube, tape, preamp), Drive, Low bypass, cuts, Mix. COMMUNITY [26]
- Live Loops: grid of cells and scenes. New project > Live Loops. Record into a cell while others play. Copy cells or record a grid run into the Tracks area. VERIFIED [27]
- Smart Tempo: modes Keep, Adapt, Automatic; region setting Off, Bars, Bars and Beats; Smart Tempo Editor to fix beat markers. VERIFIED [28]
- Flex Time and Pitch: Command-F shows Flex. Track Flex button, then choose Flex Pitch or a Flex Time algorithm. Needs Show Advanced Tools. VERIFIED [29]. Algorithm names: UNVERIFIED.
- Beat Breaker: slices audio; modes Time, Volume, Repeat, Cutoff, Resonance, Pan. COMMUNITY [30]

## 7. Sidechain and routing
- Compressor sidechain (VERIFIED [31][32]):
  1. Insert Compressor on the bass track.
  2. Click the Side Chain button.
  3. In the plug-in header Side Chain menu, pick the kick track (or a bus).
  4. Choose Max or Sum detection.
  5. Lower Threshold until the bass ducks with the kick.
- The sidechain source only triggers; its audio is not passed through. VERIFIED [31]
- Any plug-in with a Side Chain menu works the same way. Source can be a track, a hardware input or a bus. VERIFIED [32]
- Third-party AU sidechain works if the plug-in exposes a sidechain bus. Your own plug-ins: UNVERIFIED, test it.
- Aux channel strips are for sends, subgroups and multi-output instruments. Bus strips exist mostly for old projects. VERIFIED [33][34]
- Aux is created by making a send assignment, or via Mixer Options > Create New Auxiliary Channel Strip. VERIFIED [33]
- Send level pre or post fader: UNVERIFIED (page did not cover it).
- Rumble or kick bus pattern: send kick and rumble to one aux group, compress the leads from that source. (my recommendation)

## 8. Scripter, MIDI FX, control surfaces
- Scripter runs JavaScript on MIDI in real time. Turn on Enable Complete Features in Settings > Advanced first. VERIFIED [35]
- Click Open Script in Editor for the Script Editor. Scripts save with project, setting or patch. VERIFIED [35]
- JavaScript version depends on macOS JavaScriptCore, so update macOS. VERIFIED [35]
- API functions listed (older 10.4.5 docs): HandleMIDI, ProcessMIDI, GetParameter, SetParameter, ParameterChanged, Reset. VERIFIED [36] Newer ones such as PluginParameters appear in a community guide. COMMUNITY [37]
- Community Scripter developer guide, Apache-2.0, with HandleMIDI and PluginParameters examples. COMMUNITY [37]
- MIDI plug-ins: Arpeggiator, Chord Trigger, Modifier, Modulator, Note Repeater, Randomizer, Scripter, Transposer, Velocity Processor. Names VERIFIED [38]; purposes are general knowledge.
- Control Surfaces: set up in the Control Surfaces menu Setup window; Logic often auto-detects. VERIFIED [39] (Launchpad page only)
- Logic Remote (iPad or iPhone): open the app, pick your Mac. Gives Mixer, Touch Instruments, Smart Controls, key commands. VERIFIED [40]
- "Logic Remote scripts": I found nothing by that name. UNVERIFIED. Scripter is separate.

## 9. Hard dance workflow
Tempo: hardstyle 150 to 160 BPM, UK hardcore 160 to 175 (general genre knowledge). Techniques below are my recommendation unless a source is shown.
1. Template: kick, rumble, sub, leads, FX, drums; save with File > Save As Template. VERIFIED [44]
2. Kick: build in Drum Machine Designer or Alchemy, add distortion, then bounce in place to audio (File > Bounce > And Replace All Tracks, or bounce a single track in place). VERIFIED [42] for bounce and replace.
3. Rumble: copy the kick tail, reverb it, filter lows, then sidechain to the kick (section 7).
4. Reverse bass: reverse an audio region of the bass before each kick. Exact Logic menu for Reverse: UNVERIFIED (Apple page found was the iPad guide).
5. Sidechain: Compressor on bass and rumble, source kick (VERIFIED [31]).
6. Clip Distortion and ChromaGlow for grit. Clip Distortion exists (title only seen). Controls UNVERIFIED.
7. Warp and fix timing: Flex Time on vocals; Smart Tempo for loops (section 6).
8. Arrangement: Live Loops to sketch, then record the grid into the Tracks area (VERIFIED [27]).
9. Reference and mix: master bounce at 24-bit, leave headroom.

## 10. Exporting, bouncing, project management
- File > Bounce > Project or Section. Pick formats, Start and End (end a bit late for tails), Realtime or Offline, Normalize, Bounce. VERIFIED [43] (10.1 docs; menus may differ in 12.4)
- Offline mode works only with internal sources. Do not use Include Audio Tail with mastering plug-ins. VERIFIED [43]
- Default bounce folder ~/Music/Logic/Bounces. VERIFIED [43] (10.1 docs)
- Bounce and Replace All Tracks: File > Bounce > And Replace All Tracks. VERIFIED [42]
- Stems: Sound on Sound has an "Exporting Stems With Track Stacks" article (title only). UNVERIFIED steps
- Save As: Package (one file) or Folder. Needs Show Advanced Tools. Save a Copy As includes all recordings for archiving. VERIFIED [44]
- File > Project Settings > Assets chooses what is copied into the project (audio, Sampler, Alchemy, Space Designer, library content). Apple advises saving all assets with the project. VERIFIED [45]
- iPad opens packages only. Missing files: File > Project Management > Consolidate on Mac. VERIFIED [46]
- Key Commands: Logic Pro > Key Commands > Edit, Learn by Key Label, export a set. VERIFIED [47]
- Known keys: Command-N new from template; Command-F show Flex; E opens Cell Editor; Option+G global tracks; Command-End insert scene. VERIFIED [27][29][24]

## 11. Common problems
- Plug-in missing or failed: section 4 steps.
- ChromaGlow or Stem Splitter missing: Rosetta is on, section 4.
- Scripter does nothing: Enable Complete Features. VERIFIED [35]
- Launch trouble on managed or offline Macs fixed in 12.0.1. VERIFIED [6]
- Logic quit on QTA files on macOS Tahoe. COMMUNITY [7]
- Sound Library size mismatch after 12.2 update with library on external drive; no answer. COMMUNITY [5]
- Intel crash fix on zoom listed in 12.2 notes. COMMUNITY [5]

## Not verified
Linux or Wine running Logic (assumed impossible); macOS VM licensing and latency; Core Audio settings page for Logic; stems export and MIDI export steps; third-party AU vendors with Linux builds; RAM and disk requirements; which AI features need Apple Intelligence; Mac app status if you also subscribe; Retro Synth details; Flex Time algorithm names; Reverse region menu on Mac; Clip Distortion controls; send pre/post fader; stems export steps; third-party AU sidechain with your own plug-ins; universal binary advice; shortcuts beyond section 10; release dates per version; any content on Reddit, Gearspace or KVR.

## Sources (fetched)
1. https://support.apple.com/en-us/125029 2. https://www.synthtopia.com/content/2026/01/30/apple-logic-pro-12-mainstage-4-now-available-heres-whats-new/ 3. https://www.production-expert.com/production-expert-1/apple-announce-logic-pro-12-pushes-deeper-into-ai-and-appears-to-leaves-intel-macs-behind
4. https://www.apple.com/logic-pro/ and https://www.apple.com/logic-pro/specs/ 5. https://logic-users-group.com/threads/logic-pro-12-2-released.12447/latest 6. https://support.apple.com/en-us/109503
7. https://www.soundonsound.com/reviews/apple-logic-pro-12 8. https://www.soundonsound.com/daws/logic 9. https://support.apple.com/en-us/126080
10. https://hn.svelte.dev/item/49515830 11. https://github.com/juce-framework/JUCE/blob/master/docs/CMake%20API.md 12. https://help.apple.com/logicpro/mac/9.1.6/en/logicpro/usermanual/chapter_10_section_13.html
13. https://support.apple.com/en-us/102082 14. https://support.apple.com/en-us/120406 15. https://help.apple.com/logicpro/mac/10.4/en.lproj/lgcp9e26ef17.html
16. https://support.apple.com/en-ng/122179 17. https://support.native-instruments.com/hc/en-us/articles/360014454117-My-Native-Instruments-Plug-in-Fails-Validation-in-Logic-Pro 18. https://moonbase.sh/articles/debugging-your-audio-unit-plugin-with-auval-aka-auvaltool/
19. https://forum.juce.com/t/pluginval-au-plugins-returning-no-types-but-play-fine-in-logic/36687 20. https://forum.juce.com/t/plugin-fails-logic-pro-x-auval/19128 21. https://support.apple.com/en-mz/guide/logicpro/lgsi34c3f59e/mac
22. https://support.apple.com/ar-om/guide/logicpro/lgsi2b6c09bc/mac 23. https://support.apple.com/it-ch/guide/logicpro/lgsi7e4c8c73/mac 24. https://www.soundonsound.com/techniques/logic-pro-synth-players
25. https://support.apple.com/en-is/guide/logicpro/lgcp61bae908/mac 26. https://musicradar.com/how-to/logic-chromaglow 27. https://support.apple.com/en-us/102113
28. https://support.apple.com/ar-qa/guide/logicpro/lgcp9281e70c/mac 29. https://help.apple.com/logicpro/mac/10.4/en.lproj/lgcp15968647.html 30. https://www.soundonsound.com/techniques/logic-pro-how-best-use-beat-breaker
31. https://support.apple.com/hu-hu/guide/logicpro/lgcef1bec9f3/mac 32. https://help.apple.com/logicpro/mac/10.4/en.lproj/lgcpbc21a1fd.html 33. https://support.apple.com/it-ch/guide/logicpro/lgcp8e7db552/mac
34. https://support.apple.com/en-mz/guide/logicpro/lgcpc5e3029c/mac 35. https://support.apple.com/en-al/guide/logicpro/lgce728c68f6/mac 36. https://help.apple.com/logicpro/mac/10.4.5/en.lproj/lgce19021147.html
37. https://github.com/musios-app/logic-pro-scripter 38. https://help.apple.com/logicpro-effects/mac/10.2/en.lproj/lgcec21fdd03.html 39. https://support.apple.com/en-me/guide/logicpro-css/ctlsda51c419/mac
40. https://support.apple.com/guide/logicremote-logicpro-ipad/chsff8c943/ipados 42. https://support.apple.com/hu-hu/guide/logicpro/lgcpd51ba7d3/mac 43. https://help.apple.com/logicpro/mac/10.1/en.lproj/lgcp785a41c3.html
44. https://help.apple.com/logicpro/mac/10.1/en.lproj/lgcpce128e82.html 45. https://support.apple.com/en-mz/guide/logicpro/lgcp58b54e81/mac 46. https://support.apple.com/en-us/101624
47. https://support.apple.com/en-us/HT210089
