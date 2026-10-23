---
name: ardour
description: Use when helping with the Ardour open source DAW on Linux, covering install on Bazzite, audio backends, plugins, Lua, MIDI, sidechain, routing, Cue page, export and hard dance workflow.
---

# Ardour (open source DAW, Linux, hard dance)

Labels: VERIFIED (source) = read on a page I fetched. COMMUNITY = forum user or developer post, may be old. UNVERIFIED = not read on a fetched page; do not rely on it.
Rule for Claude: Assume the reader is not a programmer. Plain words first, then one exact step. One change at a time, ask the reader to test, then continue. Check the version in Help > About before quoting menus.

## 1. Version and licence
- The ardour.org front page announced Ardour 9.8. The whatsnew page dates it August 23, 2026. VERIFIED (ardour.org, ardour.org/whatsnew.html)
- So "current 8.x" is out of date. 9.0 is the newest major line; 8.12 was the last 8.x listed. VERIFIED (whatsnew page lists 8.12, 9.0 to 9.8; Wikipedia says 9.0 was released February 5, 2026)
- Licence: GNU GPL v2. VERIFIED (community.ardour.org/download)
- Runs on Linux, macOS and Windows. VERIFIED (community.ardour.org/download)

## 2. How it is distributed and paid
- Two ways to get it: a ready-to-run program, or the source code. VERIFIED (community.ardour.org/download)
- The FAQ: the code is free. The team asks you to pay something for the ready-to-run version or for support. You can pay as little as US$1 for a download. VERIFIED (ardour.org/faq.html)
- Subscription tiers per month: Standard $10, Low Cost $4, Developing World $1, Institutional $50. VERIFIED (community.ardour.org/subscribe)
- A subscription gives unlimited updates while you stay subscribed. It does not affect "ownership" of the software. Billing runs through PayPal. VERIFIED (same page)
- The page shows fixed tiers only, so "pay what you want" is the FAQ wording (from $1). Whether the download page offers a custom one-off amount: UNVERIFIED.
- Without paying, you build from source or use your distro package. The team does not help with source builds. VERIFIED (FAQ, download page)
- Distro packages are not supported on the official forums. VERIFIED (manual Ubuntu page: "Ubuntu native packages are not supported in the official Ardour forums"). Paul Davis said the same of the build process in general. COMMUNITY (discourse thread 106182, 2021)

## 2a. Platforms (Windows, macOS, Linux)
| | Windows | macOS | Linux |
|---|---|---|---|
| Runs | Yes. VERIFIED (community.ardour.org/download) | Yes, notarized since 8.0. VERIFIED (news 8.1) | Yes. VERIFIED |
| Install | Official download, from US$1 or by subscription (section 2) | same | Official bundle, Flatpak, distro package (section 3) |
| Audio driver | Driver names: UNVERIFIED (manual page lists none for Windows). ASIO is the usual choice on Windows: UNVERIFIED | CoreAudio. VERIFIED (manual Audio/MIDI setup) | JACK, ALSA, PulseAudio, NetJack. VERIFIED (same page). PipeWire via JACK or ALSA (section 4) |
| Plugin formats | LV2, LADSPA, VST2, VST3. VERIFIED (manual Working with Plugins) | LV2, LADSPA, VST2, VST3, AU (AU is OS X only). VERIFIED | LV2, LADSPA, VST2 (LXVST), VST3. VERIFIED |
| Plugin folders | Windows VST3 standard folder is `C:\Program Files\Common Files\VST3` (yabridge README shows it inside a Wine prefix). Ardour's own default list: UNVERIFIED | `/Library/Audio/Plug-Ins/Components` (AU), `/VST`, `/VST3` (Spitfire support article). Ardour defaults: UNVERIFIED | LV2 `/usr/lib/lv2`, `/usr/local/lib/lv2`; LADSPA `/usr/lib/ladspa`; LXVST `/usr/lib/lxvst`. VERIFIED (manual) |
| MIDI | Windows and Mac MIDI backends: UNVERIFIED | UNVERIFIED | ALSA sequencer or raw, or None. VERIFIED (manual MIDI on Linux) |
| Licence | GPL v2; no activation. Paying only buys the ready-to-run build and updates | same | same; or build from source |
- Same session format on all three: UNVERIFIED (not read). Lua folder on Windows and Mac: UNVERIFIED (manual gives Linux `$HOME/.config/ardour8/scripts`).
- Windows plugins on Linux: yabridge (skill wine-proton-bottles section 8, skill linux-audio-production section 10). Fragile, see section 5.
- Push 2 is supported on Linux, and the Linux needs a udev rule (skill ableton-push-expert, section 10).

## 3. Install on Bazzite (Fedora Atomic)
Three routes. Test one at a time.
1. Official download (bundle), recommended by the developers.
   - Manual steps on Ubuntu: download, mark "Allow this file to run as a program", double-click, follow prompts. VERIFIED (manual Ubuntu page)
   - The exact file type and installer name for Linux: UNVERIFIED (the download page text I got did not show it).
   - Running it on Bazzite: UNVERIFIED. Try it from the home folder first; it needs no rpm layering if it is self-contained (UNVERIFIED).
2. Flatpak: org.ardour.Ardour on Flathub, version 9.8.0, x86_64 and aarch64, free. VERIFIED (flathub.org)
   - Flathub marks it community-provided and "not verified by, affiliated with, or supported by Ardour Developers". VERIFIED (flathub.org)
   - Developer view in 2021: with a Flatpak, third-party plugins must live inside it; JACK is system-wide and sandboxed apps cannot use it, though PipeWire helps. COMMUNITY (Robin Gareus, thread 106182; old)
   - Flatpak plugin paths: Flatseal's PATH option passes LADSPA_PATH, VST3_PATH, LXVST_PATH but not LV2_PATH. `/usr` inside the sandbox is the runtime's, not the host's. Self-contained LV2 in ~/.lv2 works. COMMUNITY (thread 107984, Ardour 7 era)
   - Whether host VST3 in ~/.vst3 is visible to the Flatpak in 9.x: UNVERIFIED. Test with one plugin.
3. Distrobox with a distro package or the bundle inside it: UNVERIFIED, not sourced. Audio and MIDI access from the container is untested.
- Step by step for the reader: first try the Flatpak (easy to remove). If plugins or audio fail, try the official bundle.

## 3a. Install steps on Bazzite, one route at a time
Route A, Flatpak (try first, easy to remove). Version 9.8.0, community-provided, not supported by the Ardour team. VERIFIED (flathub.org)
1. Open the app store (Bazaar), search "Ardour", pick org.ardour.Ardour from Flathub, Install. Terminal form: `flatpak install flathub org.ardour.Ardour`. The command is standard Flatpak, UNVERIFIED for this app.
2. Start it from the menu. In Audio/MIDI Setup try JACK first (pipewire-jack), then ALSA. COMMUNITY (one user had silence with JACK and sound with ALSA, thread 111006)
3. Plugins: self-contained LV2 in `~/.lv2` worked in an Ardour 7 Flatpak. COMMUNITY (thread 107984). Host `~/.vst3` in 9.x: UNVERIFIED. Test with one plugin. Flatseal can pass LADSPA_PATH, VST3_PATH, LXVST_PATH but not LV2_PATH. COMMUNITY
4. MIDI keyboard: see it in the setup dialog (ALSA sequencer). If not, UNVERIFIED sandbox device rights; check Flatseal for device access.
Route B, official bundle (developer recommended). VERIFIED (download page, Ubuntu manual page)
1. Open community.ardour.org/download, pay or subscribe, download the Linux file. The file type: UNVERIFIED (not shown on the text I got). Write it down.
2. Move it to your home folder. Mark it "Allow this file to run as a program" (Properties, Permissions), double-click, follow the prompts. These are the manual's Ubuntu steps. Result on Bazzite: UNVERIFIED.
3. If it asks for packages the OS lacks: stop. Do not layer packages. Go to Route C.
Route C, Distrobox (container). UNVERIFIED, no source for Ardour in a container.
1. `distrobox create --name ardour --image ubuntu:24.04`, then `distrobox enter ardour`.
2. Run the Route B bundle inside, or `sudo apt install ardour`. Distro packages are unsupported on the official forums and may be old. VERIFIED (manual Ubuntu page)
3. `distrobox-export --app ardour` for a menu entry (app name may differ).
4. Audio from a container: PipeWire socket works; JACK and direct ALSA passthrough are UNVERIFIED (skill linux-audio-production section 12).
Route D, AppImage: no source found. UNVERIFIED. Do not suggest.
Route E, source build: the team does not help. VERIFIED (FAQ)
Install TEST: opens; Help > About shows 9.x; Audio/MIDI Setup starts the engine; test tone (sine) on both outputs; one MIDI note into a synth; add one LV2; save and reopen; export a 10 second WAV; no xruns in 5 minutes of playback.
Windows and macOS: use the official download. The macOS app is notarized (8.0 notes). Steps beyond that: UNVERIFIED.

## 4. Audio backends
- Audio/MIDI Setup dialog lists JACK, ALSA and PulseAudio on Linux, CoreAudio on Mac, and NetJack for advanced users. VERIFIED (manual Audio/MIDI setup page)
- Smaller buffer means lower latency and more CPU load. VERIFIED (same page)
- Monitoring latency under 5 ms suits professional recording; A/D/A conversion alone adds about 1.5 to 2 ms. VERIFIED (manual Latency Considerations)
- Ardour has no direct PipeWire driver, as of a 2023 user post that is not a developer statement. COMMUNITY (thread 109287)
- Practical route on Bazzite (PipeWire system): pick JACK (pipewire-jack) or ALSA in the dialog. UNVERIFIED which is better.
- One user got no audio and no MIDI with JACK (pipewire-jack) while ALSA worked; no fix shown. COMMUNITY (thread 111006)
- Rule: one owner of the sound card at a time. Do not open the same card in ALSA while PipeWire holds it. (general practice, UNVERIFIED for Ardour)

## 5. Plugin formats
- Ardour lists LV2, LADSPA, AU (OS X only) and VST (VST2 and VST3). VERIFIED (manual Working with Plugins; ardour.org/features.html lists VST2, VST3, AU, LADSPA, LV2)
- VST3 on all supported platforms since version 6.5. COMMUNITY (Wikipedia, secondary)
- Linux paths from the old manual: LV2 `/usr/lib/lv2` and `/usr/local/lib/lv2` or LV2_PATH; LADSPA `/usr/lib/ladspa` or LADSPA_PATH; LXVST `/usr/lib/lxvst` or LXVST_PATH. VERIFIED (manual Getting Plugins). It gives no VST3 path. Standard ~/.vst3: UNVERIFIED for Ardour.
- Plugin Manager: LV2 is always scanned at startup. VST2, VST3 and AU scanning can be turned off in Preferences. Set VST2 and VST3 folders from the manager sidebar. VERIFIED
- CLAP: not supported. A developer relayed "no plans to add CLAP support at this point" in August 2024. COMMUNITY (tracker.ardour.org issue 9417). Still true in 9.8: UNVERIFIED.
- Windows VST via yabridge: works for some. On Ubuntu 25.04 with Ardour 8.12 the scan of yabridge plugins hung; workarounds were LD_LIBRARY_PATH for ardour-vst3-scanner, a libreadline symlink, or pinning Wine-Staging 9.21. COMMUNITY (thread 112568, which of these solved it is unclear)

## 6. Lua scripting
- Types: Editor Actions (10 slots), Hooks, Session Scripts, DSP Scripts (plugins), Script Console, `luasession` CLI. VERIFIED (manual)
- Linux folder: `$HOME/.config/ardour8/scripts` (the manual page says ardour8; 9.x folder name UNVERIFIED, likely ardour9). VERIFIED for 8
- Menus: Edit > Scripted Actions > Manage; Session > Scripting > Add/Remove Script; Window > Scripting for the console. VERIFIED
- DSP scripts are added like any plugin from the processor box. Scripts used in a session are saved inside the session. VERIFIED

## 7. MIDI
- MIDI on Linux: with the ALSA backend no JACK is needed and ALSA MIDI ports are detected automatically. JACK needs `-X alsa_midi` or a2jmidid. VERIFIED (manual MIDI on Linux; the page does not mention PipeWire)
- MIDI System choice in the setup dialog: ALSA sequencer or ALSA raw, or None. VERIFIED
- A MIDI track has one MIDI input and one output. Playback needs an instrument plugin, software synth or external hardware. VERIFIED (manual Track Types)
- 9.0: double-click a MIDI region for a pianoroll window or bottom pane; note brushing with Shift-drag fills notes at the grid. VERIFIED (news 9.0)
- 9.8: key and scale support, opt-in per track, can show or block out-of-scale notes. VERIFIED (whatsnew)

## 8. Busses, routing and sidechain
- Bus: a pseudo-track that mixes tracks for shared processing; holds no regions. VCA groups gain, solo, mute without carrying audio. VERIFIED (manual Track Types)
- Aux bus: Session > Add Track, Bus or VCA, choose Audio Busses. Then right-click the track's processor box, "New Aux Send...", pick the bus. VERIFIED (manual Aux Sends)
- Send above the fader is pre-fader (red); below is post-fader (green). Post-fader suits shared effects. VERIFIED
- Aux sends keep the track's own route to the mix. Subgroups usually remove it and send the bus to the mix. VERIFIED (manual Comparing Aux Sends and Subgroups)
- Bus outputs auto-connect to the master; the manual advises against changing defaults. VERIFIED (manual Signal Routing)
- Sidechain steps (manual example, bass ducked by drums). VERIFIED (manual Sidechaining)
  1. Add a sidechain-capable plugin to the bass track (the manual uses a-Compressor).
  2. Right-click the plugin, choose "Pin Connections...".
  3. Pick the drum track as the sidechain source. Ardour adds an "SC" send to the drum track.
  4. Set the send level in that window or on the SC send.
  5. Check: an arrow shows at the compressor's sidechain input and the bass gain dips on each kick.
- If the source holds more than the kick, use a send to an extra track with a low-pass EQ and do not route it to Master. VERIFIED (same page)

## 9. Mixbus relation
- Harrison's Mixbus, LiveTrax and Xdubber are based on Ardour. Mixbus adds Harrison's proprietary DSP and a console-like workflow. COMMUNITY (Wikipedia, secondary)
- Mixbus price, Linux build and compatibility with Ardour sessions: UNVERIFIED (harrisonaudio.com failed to fetch).

## 10. Session setup
- New Session dialog: name, folder, optional template, and a time domain choice (audio time or beat time). VERIFIED (manual New Session Dialog)
- Factory templates listed (as of 5.12): Empty, Advanced Session, Recording Session, Live Band. VERIFIED. Current list: UNVERIFIED.
- Step list for the reader: 1) name the session, 2) pick a folder on the fastest drive, 3) choose Empty or Recording template, 4) set interface, 44.1 or 48 kHz and a 256 sample buffer, 5) save, 6) take a snapshot before big edits. Values are starting points, UNVERIFIED.

## 11. Recording
- Recorder page: set monitoring, create a new playlist per take, arm tracks, record, watch xrun count in the Last Take Manager. VERIFIED (manual The Recorder)
- 9.0 default recording format is RF64 (WAV that switches for large files). VERIFIED (news 9.0)

## 12. Export
- Open Session > Export > Export to Audio file(s). VERIFIED (manual Export Dialog)
- "Analyze Exported Audio" shows Peak, True Peak, Integrated Loudness and loudness range. VERIFIED
- Stems: Session > Export > Stem Export. Pick tracks or busses; "Apply track/bus processing" bakes effects in. VERIFIED (manual Stem Exports)
- Sample-rate and normalize controls in the dialog: not described on the page I read. UNVERIFIED.

## 13. Cue and Clips page
- Grid of slots, each holding an audio or MIDI clip. Scenes are called cues. VERIFIED (manual Non-Linear Workflow Principles)
- Launch by controller pad, mouse wheel over the slot, or the Play button. VERIFIED
- Follow actions: repeat, previous or next slot, or jump to a scene slot. VERIFIED
- Clips browser always visible; drag clips into slots; dropping on a full slot replaces it. VERIFIED (manual Clips in the Cue Window)
- 9.0: record straight into cue slots, edit cue contents, cue markers on the timeline. VERIFIED (news 9.0, features page)

## 14. Ardour 8 and 9 features
- 8.0: Arrangement ruler and sidebar, Quick Groups, region groups, freehand automation drawing, grid tool for tempo, MIDI arpeggiators, Launchpad Pro, macOS notarization. VERIFIED (ardour.org/news/8.1.html)
- 9.0: pianoroll windows, cue recording and editing, Region FX, Realtime Perceptual Analyzer, mixer strip import and export, multi-touch GUI. VERIFIED (news 9.0)

## 15. Known limits
- No CLAP (section 5).
- Windows plugins on Linux are fragile (section 5).
- Flatpak is community-made and plugin access is limited (section 3).
- PipeWire has no native driver per a user post (section 4); PipeWire and JACK threads show mixed results. COMMUNITY
- Reddit and other forums were not read. A Linux audio forum search was not done.

## 16. Hard dance workflow (genre advice is UNVERIFIED; the Ardour steps are verified above)
Tempo: hardstyle 150 to 160, UK hardcore 160 to 175, trance 135 to 145 BPM. (general genre knowledge)
1. New session from the Empty template. Set tempo first, in the Tempo ruler.
2. Tracks: Kick, Rumble, Sub, Lead 1, Lead 2, Screech, Pluck, Drums, FX. Add a Kick Group bus. Save as a session template.
3. Kick: layer click, body and tail on separate tracks, route all to the Kick bus (subgroup, section 8).
4. Rumble: copy the kick tail, low-pass near 150 to 250 Hz, sidechain it from the kick (section 8 steps).
5. Leads: your own synth plugin (VST3) on a MIDI track; high-pass at different points per layer; sidechain from the kick.
6. Reverb and delay: one aux bus each, post-fader sends (section 8).
7. Sketching: use the Cue page for loop ideas, then record clips to the timeline. Mixing linear and cue work is a documented chapter. VERIFIED (TOC)
8. Arrange with the Arrangement ruler (8.0) for intro, build, drop. VERIFIED (news 8.0)
9. Master: limiter on the master bus; check with the Loudness Analyzer and export report. VERIFIED (features page, Export Dialog)
10. Stems out with Stem Export when sending to a mix engineer.

## Not verified
- Official Linux download file name and how it installs on Bazzite; Windows audio driver names and plugin folders; macOS default plugin folders in Ardour; session portability between OSes.
- Flatpak visibility of ~/.vst3 and ~/.clap in 9.x; distrobox use.
- Whether a custom pay-what-you-want amount exists beyond the $1 FAQ wording.
- 9.x Lua folder name; best PipeWire setup for Ardour; realtime on Bazzite.
- VST3 default paths on Linux; Windows VST success on Bazzite with yabridge.
- Cue quantize options; export sample-rate and normalize controls.
- Mixbus price and session compatibility; Reddit and Linux audio forum views.

## Sources (fetched)
- https://community.ardour.org/download
- https://community.ardour.org/subscribe
- https://ardour.org/faq.html
- https://ardour.org/ (front page, 9.8)
- https://ardour.org/whatsnew.html
- https://ardour.org/features.html
- https://ardour.org/news/8.1.html
- https://ardour.org/news/9.0.html
- https://manual.ardour.org/toc/
- https://manual.ardour.org/sessions-tracks/sessions/audiomidi-setup/
- https://manual.ardour.org/working-with-sessions/the-new-session-dialog/
- https://manual.ardour.org/setting-up-your-system/platform-specifics/ubuntu-linux/
- https://manual.ardour.org/setting-up-your-system/setting-up-midi/midi-on-linux/
- https://manual.ardour.org/working-with-plugins/ , /plugin-manager/ , /getting-plugins/
- https://manual.ardour.org/lua-scripting/ , /lua-scripting/class_reference/
- https://manual.ardour.org/signal-routing/ , /aux-sends/ , /comparing-aux-sends-and-subgroups/ , /sidechaining/
- https://manual.ardour.org/working-with-tracks/track-types/
- https://manual.ardour.org/recording/the-recorder/ , /recording/monitoring/latency-considerations/
- https://manual.ardour.org/exporting/export-dialog/ , /working-with-sessions/interchange-with-other-daws/stem-exports/
- https://manual.ardour.org/cue/non-linear-workflow-principles/ , /clips/clips-in-the-cue-window/ , /cue/setting-up-cues/
- https://manual.ardour.org/appendix/files-and-directories/
- https://flathub.org/apps/org.ardour.Ardour
- https://support.spitfireaudio.com/en/articles/11815335-where-are-the-au-vst-aax-plugins-on-mac
- https://github.com/robbert-vdh/yabridge (README, Windows VST3 prefix path)
- https://en.wikipedia.org/wiki/Ardour_(software)
- https://discourse.ardour.org/t/ardour-as-snap-or-flatpak/106182
- https://discourse.ardour.org/t/ardour7-in-flatpak-overcoming-the-sandboxing-with-flatseal/107984
- https://discourse.ardour.org/t/solved-yabridge-in-ardour-8-12-on-ubuntu-25-04-and-later-versions/112568
- https://discourse.ardour.org/t/pipewire-1-0-is-it-time-now/109287
- https://discourse.ardour.org/t/ardour-won-t-output-audio-nor-receive-midi-input-with-jack-pipewire-jack/111006
- https://discourse.ardour.org/t/new-plugin-standard/107337
- https://tracker.ardour.org/view.php?id=9417
- Not fetched (error): ardour.org/news/8.0.html, ardour.org/subscribe.html, harrisonaudio.com/mixbus, GitHub (access blocked), several discourse threads returned only the first post
