---
name: waveform
description: Use when helping with Tracktion Waveform (Pro or Free, version 14) on Linux, covering editions, install on Bazzite, audio setup, plugins, racks, sidechain, step clips and hard dance production.
---

# Tracktion Waveform 14 (Linux, hard dance)

## How to work with the reader
- Assume the reader is not a programmer. Plain words first, then one exact click path.
- One change at a time, ask the reader to test, then continue.
- Labels: VERIFIED (source), COMMUNITY (forum or user report), UNVERIFIED (not read on a fetched page, say so, never guess).
- Waveform has a small community. Many answers live on KVR, not Reddit. Reddit was blocked in my fetch tool, so no Reddit claims are made here.
- Ask which exact version the reader runs (Help > About) before quoting menus.

## Editions and price
- Current version is Waveform 14, launched 29 June 2026 (VERIFIED, Sound On Sound, Gearnews). The manual says 14.0.50 (VERIFIED, manual What's New).
- Waveform Free 14: free, no track limit, no export limit, no commercial limit (VERIFIED, Dubspot). Includes 14 audio effects, 8 MIDI effects, 11 utility plugins, 4 instruments (VERIFIED, tracktion.com).
- Waveform Pro 14: $249 regular (VERIFIED, tracktion.com, SOS). Upgrades start at $149 on tracktion.com. A launch sale ($149, upgrades from $89) ended 15 July 2026 (VERIFIED, Rekkerd). Prices change, check the store.
- Paid expansions for Free start at $30: Multi Channel, Launcher, DJ Mix Tools, Pro Video, Recording Engineer, MIDI Producer, Synth Pack (VERIFIED, tracktion.com Free page).
- Pro adds (VERIFIED, manual Introduction): chord track, Groove Doctor, extra instruments and effects, Quick Actions panel, MIDI effects. The Arranger Track is Pro only (VERIFIED, manual). Plugin Rack macros are Pro (VERIFIED, manual). Multi-channel audio is Pro (VERIFIED, manual What's New).
- 30-day Pro trial exists (VERIFIED, tracktion.com).
- A free account is needed to download (VERIFIED, tracktion.com signup page, It's FOSS for older versions).

## Linux status
- tracktion.com lists "Waveform Linux 14", tested on Ubuntu 24.04 64-bit. You install Waveform Free 14 first. "Waveform Pro features are unlocked automatically while running on Linux" (VERIFIED, tracktion.com Free and Pro pages).
- At launch, press said Linux was "coming soon" (VERIFIED, SOS, Rekkerd, Gearnews). So the Linux build came after 29 June 2026. I did not find the date (UNVERIFIED).
- Only .deb packages are documented for older versions (VERIFIED, AddictiveTips 2020: "no official package for any other type of distribution"). Fedora has no RPM (VERIFIED, same page).
- Flatpak, AppImage, Flathub: UNVERIFIED, I found no source for any of them. The Free page does not name a download file type. VERIFIED (tracktion.com, 2026-10-23)

## Platforms (Windows, macOS, Linux)
| | Windows | macOS | Linux |
|---|---|---|---|
| OS | Windows 10 or 11, 64-bit | macOS 13 or later, Intel or Apple silicon | Tested on Ubuntu 24.04 64-bit |
| Install | Free signup, download Waveform Free 14 | same | Install Waveform Free 14 first |
| Audio driver | Windows Audio (WASAPI), Windows Audio (Exclusive), DirectSound (avoid), ASIO (best for an interface; install the maker's driver first) | Core Audio only; class-compliant USB needs no driver | JACK recommended; PipeWire needs pipewire-jack, pipewire-alsa, wireplumber |
| Default buffer | 256 samples | 512 samples | 1024 samples |
| Plugins | VST, VST3 (AU is macOS only) | VST, VST3, AU | VST, VST3, LV2, LADSPA folder settings |
| Licence | Free, or Pro 249 USD | same | Pro features unlocked automatically |
- VERIFIED: OS lines and Linux unlock line (tracktion.com Free page); audio rows and buffers (manual Audio Device Setup, fetched 2026-10-23); plugin formats on the Free page "VST, VST3 and AU".
- Default plugin folders per OS: UNVERIFIED (the manual settings page could not be fetched). Use Settings > File Locations and add the folder by hand.
- On Windows and macOS the extras are paid: Pro 249 USD, expansions from 30 USD (see Editions). Pro 30-day trial. VERIFIED (tracktion.com)
- Whether the Linux unlock needs a login or works offline: UNVERIFIED.
- AU is a macOS-only format (Ableton manual, VERIFIED), so it does not apply to the Linux build.
- Windows and macOS users: ASIO needs the interface maker's driver; re-run latency calibration after any buffer or rate change (manual). Cross-platform Edit files: UNVERIFIED.

## Install on Bazzite (Fedora Atomic)
Native .deb does not fit Bazzite. No source I read names a Linux file type for Waveform 14. Do the steps in order and report what the reader sees.
1. Sign in at tracktion.com, open the downloads page, choose Waveform Linux 14. Write down the exact file name and ending (.deb, .AppImage, .tar, other). Do not guess.
2. Look for Flatpak first. In the app store (Bazaar) search "Waveform" and "Tracktion". Flathub entry: not found in any source (UNVERIFIED). If one exists, install it and stop here.
3. If the file ends in .AppImage (UNVERIFIED that it does): move it to `~/Applications`, right-click, Properties, Permissions, tick "Is executable", double-click. Command form: `chmod +x file.AppImage` then `./file.AppImage`. UNVERIFIED for Waveform.
4. If the file ends in .deb, use Distrobox with Ubuntu 24.04, the tested distro (VERIFIED, tracktion.com). All UNVERIFIED for Waveform:
   a. `distrobox create --name waveform --image ubuntu:24.04`
   b. `distrobox enter waveform`
   c. `sudo apt update` then `sudo apt install ./Waveform*.deb` (run from the folder holding the file)
   d. `distrobox-export --app waveform` to get a menu entry (the app name may differ; check `ls /usr/share/applications`)
   e. Inside the box also install `pipewire-jack` and `pipewire-alsa` (manual advice for Linux, VERIFIED) and `ubuntu-restricted-extras` (fonts; COMMUNITY fix for crashes).
5. Distrobox audio: PipeWire is reached through the host socket. JACK or direct ALSA passthrough from a container is UNVERIFIED (linux-audio-production skill, section 12). Test sound first with the ALSA type pointed at the PipeWire device.
6. Plugins in a container: the home folder is normally shared, so `~/.vst3` should be visible. UNVERIFIED. Flatpak or container plugin paths: see linux-audio-production section 9.
7. Windows plugins: yabridge does not work with Flatpak hosts (wine-proton-bottles skill, section 8). With a Distrobox host it is UNVERIFIED.
8. Fallback if all fail: use the bitwig-studio or ardour skill, or a plain Ubuntu 24.04 install on another disk.
Install TEST: app opens; Help > About shows 14; audio test tone plays; MIDI keyboard seen; scan a VST3; save and reopen a project; quit and reopen 3 times.

## Audio on Linux (VERIFIED, manual Audio Device Setup)
- The manual recommends JACK on Linux. The system uses PipeWire, so add pipewire-jack, pipewire-alsa and wireplumber.
- Default rate is 44100 Hz. Use 44100 or 48000.
- Start at a 256 sample buffer. Melodyne Essential needs at least 1024.
- Latency calibration: connect an output to an input with a cable, then Auto-Detect and Run Test, then Apply. Repeat after changing rate or buffer.
- COMMUNITY (KVR, 13.5 beta): with PipeWire-JACK one user saw high CPU and many xruns. PipeWire-ALSA was better, but the engine sometimes stopped under heavy plugin load.
- COMMUNITY (KVR, 13.1 beta): one user stopped crashes by setting Audio Device Type to ALSA, then picking Jack or PipeWire as the device. Not an official fix.
- Start test: ALSA type with the PipeWire device first, then try JACK.

## Plugin formats
- Linux folder settings exist for VST (VST2), VST3, LV2 and LADSPA (Linux only) (VERIFIED, manual Settings > File Locations). Formats shown depend on the build.
- The manual Introduction lists VST, VST3 and Audio Unit (VERIFIED), which is generic for all platforms.
- CLAP: not mentioned in anything I read (UNVERIFIED). Assume no CLAP. Your own JUCE plugins should ship VST3 (and LV2 if built).
- Scan: Settings > Plugins > Scan for Plugins. Adding a folder may not trigger a scan, so scan by hand (VERIFIED, manual).
- Validate Selected and Validate File check one plugin (VERIFIED, manual).
- Plugin sandboxing is off by default, runs plugins in a separate process, and is chosen per plugin in the Sandbox column. Reopen edits after changing it (VERIFIED, manual). A crash took down the whole app with sandboxing off (VERIFIED, MusicTech review).
- COMMUNITY (KVR, 13.5): bundled VST3 Collective, BioTek 2 and Subtractive crashed on Ubuntu 20.04. VST2 versions were mostly fine. Ubuntu 25.10 ran without tweaks. Ubuntu 24.04 needed extra installs.
- COMMUNITY (KVR): installing ubuntu-restricted-extras (fonts) fixed crashes for some users.

## Tracktion Engine and Tracktion Graph
- Waveform is built on Tracktion Engine, a JUCE module for sequence based audio apps, from a file player to a full DAW (VERIFIED, GitHub README). Platforms include Linux. Needs C++20.
- Licence: GPL or commercial, and JUCE needs its own licence for distribution (VERIFIED, README).
- Tracktion Graph is a module of the engine. It holds audio graph classes, node players (including multithreaded ones), latency and summing nodes (VERIFIED, tracktion_graph.h source). The header calls it experimental with an unstable API.
- Engine plugin format flags: not found in the header I read (UNVERIFIED). Do not claim the engine's formats equal Waveform's.
- Waveform 14 audio engine was rewritten with plugin delay compensation across routing (press claim, Gearnews). Treat as a claim.

## Macros and scripting (two different things)
- Rack Macros: knobs in a Rack Type that move many plugin parameters at once. Pro only (VERIFIED, manual Racks).
- Script Macros: text lists of actions, JavaScript syntax for loops (VERIFIED, manual Macros). Actions are called on the Waveform object, e.g. Waveform.setName(...).
- Show them: Settings > Keyboard Shortcuts > enable Show Script Editor. Run from a key, Run Script > User Macros, or a custom menu. Export as .Waveformscript XML (VERIFIED, manual).
- The AI Assistant (new in 14) uses your own OpenAI or Anthropic key, billed by the provider. Enable in Settings > AI. It sends project context over the internet (VERIFIED, manual AI Assistant). Warn the reader about privacy and cost.
- Other scripting such as a Lua or Python API: UNVERIFIED, none found.

## Modifiers and MIDI effects
- Modifiers (the modulation system) are six types: LFO, Envelope Follower, Random, Step, Breakpoint, MIDI Tracker (VERIFIED, manual Modifiers).
- Add one: drag New Modifier Generator onto a track or onto a plugin, double-click it, drag the assignment handle onto a parameter. Check Depth is above zero.
- Step modifier has 2 to 64 steps and syncs to Free, Transport or Note. Good for a drawn pump shape.
- The Envelope Follower reacts only to its own track's audio (VERIFIED), so it will not follow a kick on another track.
- MIDI effects go before the instrument in the chain (VERIFIED, manual MIDI Effects). Pro: Arpeggiator, Chord Companion, MIDI Modifier (a transposer), Note Repeater, MIDI Filter. All editions: Chord Player, Monitor, Patch Bay, Note Names, MIDI CC.
- Do not mix up "MIDI Modifier" (the transposer plugin) with Modifiers (the modulators).
- Version 14 notes: MIDI Randomisation, MIDI Strum, Drum Grid, step probability (VERIFIED, tracktion.com Pro features page). Menu paths not read (UNVERIFIED).

## Racks and routing (VERIFIED, manual Racks and Effects Bus Tracks)
- A Rack Type is the blueprint. A Rack Instance sits on a track. Edits to the type change every instance. Racks cannot nest.
- Make one: Plugin Browser > Plugin Racks > drag Create New Empty Rack onto a track. Or select plugins, right-click, wrap into a rack.
- Wire in the Rack Editor by dragging nodule to nodule. Audio to audio, MIDI to MIDI, modifiers to parameters.
- Sends: Aux Send after Volume and Pan on each track, Aux Return on a bus track left of the effect. Set the effect 100% wet.

## Sidechain how-to
Easy way (VERIFIED, manual Using Plugins and Built-in Effects):
1. Put the Compressor on the bass track.
2. In the plugin header, top left, open the sidechain assignment list.
3. Pick the kick track.
4. Set a fast attack and a release that fits the kick gap. Raise ratio until the bass ducks.
5. Trim with the Sidechain gain control.
Rack way (VERIFIED, manual Racks):
1. Right-click an input nodule on a plugin inside the rack.
2. Choose "Use this input as a side-chain from:".
3. Pick the source track and channel.
No-sidechain pump (idea built from verified parts, UNVERIFIED as a combo): a Step modifier on a Volume and Pan level, synced to Transport, drawn as a kick-shaped duck.

## Sample Browser, Step clips, Pattern Generator, Chord track
- Browser: Search tab with Categories (Plugins, Presets, Racks, Samples, Clips, Tracks) and Smart Lists. Files tab shows plain folders, SoundFont and SFZ (VERIFIED, manual Browser).
- Loops at project tempo and key: Search > Samples, click a loop, preview Menu > Match tempo and Match pitch, then drag to a track (VERIFIED).
- Step clip steps (VERIFIED, manual Step Clips): add a drum instrument, insert a Step Clip, set loop, click cells. Default 16 steps of a quarter beat. V/G editor sets velocity and gate. Row options include Note On Every and Groove. Convert to MIDI clip for the piano roll.
- Pattern Generator (all editions): MIDI clip > Pattern Generator tab > Arpeggio, Chords, Bassline or Melody. Turn Auto Update off before hand edits, or edits are overwritten (VERIFIED).
- Chord track (Pro): hidden by default, show from View > Global tracks. Alt+C adds a chord at the playhead. Up to 64 chords per progression. Pattern generators and audio clips can follow it (VERIFIED, manual).
- Clip Launcher: press M for the mixer, click the grid button. Scenes, follow actions with probabilities. Record to arrangement with the global record button (VERIFIED, manual).
- Arranger Track (Pro): hold a modifier key and drag to make sections. Moves clips and tempo events with the section (VERIFIED).

## Master Mix and export
- Master Mix: Pro and OEM plugin for the master. Pre and post EQ, 3-band crossover with a compressor per band, a final stage with soft clip and gate, DC filter, up to 100 presets, Mem A and B (VERIFIED, manual Built-in Effects).
- Export: set In and Out markers, Export > Render to a file, keep Only Render Marked Region on. Dither on by default. Normalize off. MP3 at 320 kbps CBR (VERIFIED, manual Mixing Down).
- Render Each Track to a Separate File makes stems for another DAW or a mastering engineer.
- If a mastering engineer will master it, leave the master empty (VERIFIED, manual).

## Hard dance workflow (steps combine verified features with genre knowledge)
Tempo ranges: hardstyle 150 to 160 BPM, UK hardcore 160 to 175, trance 135 to 145 (genre knowledge, UNVERIFIED in Waveform sources).
1. Turn sandboxing on for new or beta plugins. Save an Edit as a template with tracks: Kick, Rumble, Sub, Lead, Screech, Pluck, Drums, FX, Vocal.
2. Kick: build in a 4OSC or a sampler track, bounce to audio with Render, then EQ and compress the audio.
3. Rumble: copy the kick tail, high-pass the body, add Natural reverb, low-pass at 150 to 250 Hz, sidechain it to the kick with the Compressor.
4. Leads: layer a supersaw plugin over a mono saw. Put each layer in its own track, or in one Rack with a Rack Macro for the filter.
5. Arrange: use the Arranger Track in 16 or 32 bar blocks. Use Clip Launcher scenes to sketch drops, then record to the arrangement.
6. Chords: draw the key in the Chord track, then let the Pattern Generator make bass and arps. Edit the result by hand after turning Auto Update off.
7. Build: Step modifier or automation on a filter, plus Pitch Shifter or Reverb sends for risers.
8. Master: Master Mix or Limiter on the master, checked with the Spectrum utility. Render with dither on.

## Test checklist for your own plugins in Waveform
1. Copy the VST3 to ~/.vst3 (and LV2 to ~/.lv2), add the folder in Settings > File Locations, scan.
2. Use Validate File on the plugin. Read the log (Help > Show the Tracktion log file, VERIFIED).
3. Run it sandboxed and unsandboxed. Compare.
4. Save, close, reopen: state and window size restored.
5. Automate a parameter and attach a Step modifier to it.
6. Change sample rate and buffer. No crash, no silence.
7. Render offline and compare with a live bounce.
8. Test a loop region for stuck or missing notes (known risk).
9. Check CPU against a pure ALSA setup and a JACK setup.

## Known Linux problems summary
- Crashes opening projects in 13.3 (COMMUNITY, KVR). Fixed for some by ms-ttf fonts and ubuntu-restricted-extras.
- VST3 versions of bundled plugins crash on Ubuntu 20.04 (COMMUNITY, KVR).
- All of the KVR items are from 13.x. I found no 14 Linux bug reports (UNVERIFIED).

## Not verified
- Whether Waveform 14 Linux ships as .deb only, and its release date; default plugin folders per OS; the manual Settings page (fetch limit reached); whether the Linux unlock needs a login.
- Any Flatpak, AppImage or Flathub build.
- Whether the .deb runs in distrobox on Bazzite, including audio, MIDI and plugin paths.
- CLAP support, and the plugin formats the Engine itself builds.
- Free vs Pro limits on Linux beyond tracktion.com's "unlocked on Linux" line, and whether it needs a Pro licence on other systems.
- Step clip edition, Drum Grid and MIDI Randomisation menu paths.
- Sample rate, sandboxing and plugin settings on Linux. The Plugin Processing section of the settings page.
- Linux audio driver names in the Audio Devices page.
- Any Lua or Python API.
- Reddit and Tracktion forum posts (blocked), docs.tracktion.com (robots blocked).
- The Fedora 33 Waveform 11 thread body, KVR Linux FAQ (client error).

## Sources (fetched)
- https://www.tracktion.com/products/waveform-pro
- https://www.tracktion.com/products/waveform-free
- https://www.tracktion.com/products/waveform-free-features
- https://www.tracktion.com/signup/free
- https://www.tracktion.com/training/manuals
- https://tracktion.github.io/waveform_manual/latest/ (pages: introduction, whats-new, audio-device-setup, using-plugins, racks, macros, modifiers, midi-effects, step-clips, chord-track, pattern-generator, browser, built-in-effects-plugins, utility-plugins, effects-bus-tracks, clip-launcher, arranger-track, ai-assistant, mixing-down, reference-settings, getting-help, midi-editing)
- https://github.com/Tracktion/tracktion_engine and raw.githubusercontent.com/Tracktion/tracktion_engine/develop/modules/tracktion_graph/tracktion_graph.h and modules/tracktion_engine/tracktion_engine.h
- https://www.soundonsound.com/news/tracktion-unleash-waveform-14-daw
- https://musictech.com/reviews/digital-audio-workstations/tracktion-waveform-14-pro-review/
- https://bedroomproducersblog.com/2026/06/29/waveform-free-14/
- https://blog.dubspot.com/tracktion-waveform-free-14-2026
- https://www.gearnews.com/tracktion-waveform-free-studio/
- https://sonicstate.com/news/2026/07/03/tracktion-releases-waveform-14/
- https://rekkerd.org/tracktion-launches-waveform-14-with-redesigned-interface-multi-channel-surround-tools-ai-assistant/
- https://www.addictivetips.com/ubuntu-linux-tips/waveform-free-audio-workstation-linux
- https://itsfoss.com/tracktion-t7-daw
- https://www.kvraudio.com/forum/viewtopic.php?p=9198462
- https://www.kvraudio.com/forum/viewtopic.php?p=9167408
- https://www.kvraudio.com/forum/viewtopic.php?p=9030120
- https://www.kvraudio.com/forum/viewtopic.php?p=8957540
- https://en.wikipedia.org/wiki/Tracktion_Waveform
- https://www.omgubuntu.co.uk/tag/tracktion?amp
