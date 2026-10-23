---
name: ableton-live
description: Use when helping with Ableton Live, covering editions, Live 12 features, Linux via Wine, hard dance workflow, sidechain, Warp, Max for Live, or testing your own plugins in Live.
---

# Ableton Live (Windows, macOS, Linux)

Researched 2026-10-23. Re-check versions and prices before quoting them.
Verify against current docs before acting on anything marked UNVERIFIED.
Labels: VERIFIED = read in a fetched page (number = Sources list). COMMUNITY = forum, blog or project report. UNVERIFIED = not checked.
Rules for Claude: Assume the reader is not a programmer. Plain words first, then one exact step. One change at a time, ask the reader to test, then continue.
Related skills: wine-proton-bottles (prefixes, runners, wineasio, backups), linux-audio-production (PipeWire, realtime, xruns), max-for-live-expert (Max devices), ableton-push-expert (Push 1, 2, 3), bitwig-studio (native Linux host).

## 1. Rule: query the Ableton knowledge tools first
If these tools exist in the session, use them before answering any Ableton question; do not answer from memory:
- search_live_manual for any feature or workflow question (the default tool).
- search_knowledge_base alongside it for how-tos, system requirements, licensing and troubleshooting.
- search_release_notes for "what changed in version X".
- search_transcripts or search_videos for tutorial material.
Tool names appear as mcp__...Ableton_Knowledge__*; load them via ToolSearch if deferred. If they are missing, say so and label answers UNVERIFIED.

## 2. Versions and editions
- Current: Live 12.4.7, released 22 Oct 2026 (Akai MPK Mini Plus II control surface). VERIFIED [1]
- 12.4.6 (15 Sep 2026): fixed a hang when rendering, bouncing or consolidating with many audio tracks in Beats Warp Mode. 12.4.5 (26 Aug 2026): bundled Max updated to 9.1.5. VERIFIED [1]
- 12.4 is a free update for all Live 12 users. It adds Link Audio (stream audio between Link peers), a refreshed Erosion (Erosion Legacy keeps old Sets intact) and a refined Chorus-Ensemble. VERIFIED [1][4]
- Link Audio: both Link and Link Audio must be on; a new Link page exists in Settings; Wi-Fi works but quality depends on the network. VERIFIED [1]
- Editions: Intro, Standard, Suite. VERIFIED [3][18]
- Intro: 16 audio and MIDI tracks, 16 scenes, 2 send/return tracks. Standard and Suite: unlimited tracks and scenes, 12 send/return tracks. VERIFIED [3]
- Max for Live is included only in Suite (Standard needs the add-on). Stem separation is Suite only. VERIFIED [3][18]
- Suite only devices include Operator, Wavetable, Meld, Granulator III, Echo, Hybrid Reverb, Pedal, Amp and Cabinet. VERIFIED [3] (page read to 100000 characters, list is partial)
- Live 12.0: Meld, Roar, MIDI Tools, Scale Awareness, Tuning Systems, Similarity Search, Mixer in Arrangement, browser tags. VERIFIED [1]
- Live 12.3: stem separation, group bouncing, Splice in the browser, Generators by Iftah. 12.1 added Sequencers; 12.2 added Expressive Chords. VERIFIED [18]
- Intro lacks the MIDI manipulation engine and AAS synths; Meld and Roar are Suite only. VERIFIED [18] (launch info)
- Prices: not read on any fetched page. Suite rent-to-own over 24 monthly payments exists. VERIFIED [4]. Prices and regional offers: UNVERIFIED, check ableton.com.
- Trial: a "Try Live 12 for free" link exists. VERIFIED [4]

## 3. Platforms

### Windows
- Version and OS: Live 12 needs Windows 10 (22H2) or Windows 11 (22H2 or later). VERIFIED [2]
- Hardware: 5th gen Intel Core i5 or AMD Ryzen with AVX2; 8 GB RAM; about 6 GB for basic install plus up to 76 GB optional sound content; 1366x768 display. ARM machines run via emulation. VERIFIED [2]
- Live 12 does not open on a CPU without AVX2. VERIFIED [2] (help article title: "Live 12 doesn't open on Windows due to missing AVX2 requirement")
- Install: download the installer from your ableton.com User Account, run it, then authorize. VERIFIED [7]
- Audio driver: an ASIO interface is recommended and is needed for Link. VERIFIED [2]. ASIO4ALL is a generic option when the interface has no ASIO driver. VERIFIED [15]. WASAPI as a Live driver type: UNVERIFIED, check Settings > Audio > Driver Type.
- Plugins: Live supports VST2 and VST3 on Windows. VERIFIED [5]. Set a VST2 custom folder in Settings > Plug-ins (Ctrl+, opens Settings). VERIFIED [5]
- VST3 default folder `C:\Program Files\Common Files\VST3`: VERIFIED as the standard install place [16]; that Live scans it automatically is UNVERIFIED.
- Licensing: one licence has two authorizations, so two computers, one used at a time. VERIFIED [7]. Offline authorization with a hardware code and an .auz file exists. VERIFIED [6]
- Authorizing for all users on Windows has its own help article (title only). UNVERIFIED content [20]

### macOS
- OS: macOS 11.7.10 through macOS 27 on Apple silicon; through macOS 26 on Intel. VERIFIED [2]
- Hardware: Intel Core i5 or Apple silicon; 8 GB RAM; about 8 GB (Intel) or 10 GB (Apple silicon) for basic install plus up to 76 GB optional. VERIFIED [2]
- Install: same as Windows, from the User Account download. VERIFIED [7]
- Audio: Core Audio interface recommended. Live's input and output can use any Core Audio device. VERIFIED [2][15]
- Plugins: VST2, VST3 and Audio Units. Audio Units are macOS only; Audio Units 3 from Live 11.2. Turn on "Use Audio Units" in Settings > Plug-ins. VERIFIED [5]
- VST2 system folder is /Library/Audio/Plug-Ins/VST, switched by "Use VST plug-ins in System Folders". For other places use a custom folder or an alias. VERIFIED [5]
- VST3 and AU folder paths on macOS: UNVERIFIED (standard Apple paths are /Library/Audio/Plug-Ins/VST3 and /Library/Audio/Plug-Ins/Components).
- Licensing: same two authorizations. VERIFIED [7]. Authorizing for all users on macOS has its own help article (title only). UNVERIFIED content [20]
- Cross platform licence (one licence on Windows and macOS): UNVERIFIED.

### Linux
- There is no native Live for Linux. Live 12 lists only Windows and macOS. VERIFIED [2]
- Unofficial route: the ableton-linux project (see section 4). COMMUNITY [8]
- Push 3 standalone runs Live on its own hardware, not on a PC. COMMUNITY (KVR)
- Audio on Linux: PipeWire is the audio system; the project gives Live a PipeASIO driver on top of it. Set Driver Type ASIO and Audio Device PipeASIO. COMMUNITY [8]. Background in linux-audio-production.
- Plugin folders on Linux: Windows plugins live inside the Wine prefix, default `~/.wine-ableton/drive_c/Program Files/Common Files/VST3/`. COMMUNITY [8]. Native Linux VST or CLAP plugins are not supported, only an experimental Carla route. COMMUNITY [8][9]
- Licensing on Linux: you use your normal Ableton licence and activation. COMMUNITY [8] ("your installation files and activation details from Ableton"). Whether this follows Ableton's licence terms: UNVERIFIED, read the licence.

## 4. Run it on Linux (Wine, Bottles, Proton)
Status: community project only. Not supported by Ableton. Use Windows and macOS for anything that must not fail.

### 4.1 Which way to run it
- Best option: the ableton-linux installer (github.com/shibco/ableton-linux). It brings its own Wine build, PipeASIO, Link service and fixes. Not affiliated with Ableton. COMMUNITY [8]
- Runner used by the project: its own Wine fork `wine-d2d1-nspa-11.13` at `~/.local/opt/wine-d2d1-nspa-11.13/bin/wine`. COMMUNITY [8]. You do not pick Wine, Wine-staging, Proton, Proton-GE, Soda or Caffe yourself on this route.
- Prefix: `~/.wine-ableton`. COMMUNITY [8]
- Supports: Live 12 (Intro, Standard, Suite, Lite, Trial), Live 11, Max 8 and 9 with Max for Live, Splice, Ableton Cloud, Link, Push 1, 2 and 3. Move support "coming soon". COMMUNITY [8]
- Manual alternative (Bottles with a Soda or Wine-staging runner, WineASIO): described in KVR and a blog, less tested. COMMUNITY [19]. Details of Bottles and WineASIO are in wine-proton-bottles sections 4 and 7. A Flatpak WineASIO recipe is UNVERIFIED there too.
- Do not use Bottles and the project on the same prefix. UNVERIFIED rule of thumb.

### 4.2 Requirements (check before installing)
- x86-64 Linux meeting Live's hardware needs, glibc 2.35 or newer, PipeWire 1.4.2 or newer. COMMUNITY [8]
- Linux 6.14 or newer with NTSync active. NTSync became a requirement in release 2026.08.24.1. COMMUNITY [8][10]
- GStreamer base and good plugins; coreutils, tar, zstd, flock. COMMUNITY [8]
- Whether Bazzite's current kernel has NTSync active, and whether GStreamer, zstd and flock are present: UNVERIFIED. Bazzite is not mentioned in the project changelog. [10]
- Your Live installer ZIP from ableton.com and your activation details. COMMUNITY [8] Which OS download to pick: the README only says "installation ZIP", UNVERIFIED (expect the Windows one).

### 4.3 Step by step on Bazzite (one step at a time, test after each)
1. Open Konsole. Type `uname -r` and press Enter. Needs 6.14 or higher. If lower, stop and tell me. COMMUNITY [8]
2. Type `pipewire --version`. Needs 1.4.2 or higher. UNVERIFIED that the command prints that format. Details in linux-audio-production.
3. Download the Live 12 installation ZIP from your Ableton account. Keep it in Downloads. COMMUNITY [8]
4. Download `install-ableton-latest.run` from the project's latest release page. COMMUNITY [8]
5. Ask the installer for a dry run first: `sh ~/Downloads/install-ableton-latest.run plan install`. It lists what it would do. COMMUNITY [11]
6. Install: double-click the .run file, or type `sh ~/Downloads/install-ableton-latest.run install`. Press Enter to accept each default question. COMMUNITY [8][11]
7. If several Live ZIPs are in Downloads, point to one: add `--live-installer "$HOME/Downloads/Ableton Live 12 Installer.zip"`. COMMUNITY [8]
8. If the installer stalls at "initialise prefix", close any Ableton USB Driver window, then run the `update` command. COMMUNITY [9]
9. Start Live from the application menu, or type `ableton-live`. COMMUNITY [8]
10. Authorize Live with your account. Offline way: choose "No Internet on this computer", use the hardware code on a computer with internet, download the .auz file, drag it into the dialog. VERIFIED [6]. Whether online authorization works under this Wine: UNVERIFIED.
11. Settings > Audio: Driver Type ASIO, Audio Device PipeASIO. If no sound, set the device to None and back to PipeASIO. COMMUNITY [8][9]
12. If audio crackles, test one launch with a bigger buffer: `env PIPEASIO_PREFERRED_BUFFERSIZE=512 ableton-live`. COMMUNITY [9]. Installer default buffer is 128; choices 64, 128, 256, 512, 1024. COMMUNITY [11]
13. Realtime setup, once, then log out and in: `~/.local/share/ableton-wine/setup-realtime.sh`. COMMUNITY [9]. Bazzite group rules: see linux-audio-production section 5.
14. Run the test checklist in section 4.5.

### 4.4 Settings that matter
- Prefix settings and winetricks: the installer creates and configures the prefix itself. I found no winetricks step. COMMUNITY [8]. A KVR user needed all VC++ runtimes via winetricks on their own manual prefix. COMMUNITY (KVR)
- Audio driver: PipeASIO 1.5.0 or newer works through PipeWire's JACK-compatible layer and needs PipeWire 1.4.2+. Release 2026.07.17.2 replaced WineASIO with PipeASIO. COMMUNITY [10]. Real-time scheduling for PipeASIO is off by default. COMMUNITY [10]. WineASIO env vars (for the manual route) are in wine-proton-bottles section 7. VERIFIED [17]
- Installer options: `--audio-buffer`, `--rt`, `--power`, `--dpi`, `--shortcuts`, `--audio-threads`, `--link`. COMMUNITY [11]
- Link: runs as service `ableton-linkd`, default `session` mode. Needs UDP port 20808 open on a firewall. Show Link Toggle under Settings > Link, Tempo & MIDI. COMMUNITY [8][9]
- GNOME shortcut clashes: `ABLETON_SHORTCUTS=take`. This is a GNOME item; on KDE it is UNVERIFIED. COMMUNITY [9]
- Plugin windows that resize in a loop: right-click the plugin, turn off Auto-Scale Plugin Window. COMMUNITY [9]
- OpenGL plugin GUI fails: switch the prefix to GLX with `WINEPREFIX=~/.wine-ableton ~/.local/opt/wine-d2d1-nspa-11.13/bin/wine reg add 'HKCU\Software\Wine\X11 Driver' /v UseEGL /d N /f`. COMMUNITY [9]

### 4.5 Windows plugins and yabridge
- Windows installers: run them in the same prefix: `env WINEPREFIX="$HOME/.wine-ableton" "$HOME/.local/opt/wine-d2d1-nspa-11.13/bin/wine" "/path/to/PluginInstaller.exe"`. COMMUNITY [8]
- A single .vst3 bundle: copy it into `~/.wine-ableton/drive_c/Program Files/Common Files/VST3/`. COMMUNITY [8]
- yabridge is NOT needed here. It bridges Windows plugins into native Linux hosts (Bitwig, Ardour, Reaper). Live runs inside Wine and loads the Windows plugin directly. VERIFIED [16] for what yabridge does; that Live needs no bridge is COMMUNITY [8]
- Use yabridge only for the Bitwig route. It does not work with Flatpak DAWs and needs Wine Staging. Wine 9.22 and 10.x did not work with yabridge 5.1.1. VERIFIED [16]. See linux-audio-production section 10.
- Plugins with iLok, serial or online activation: may fail. Some copy protected plugins fail under Wine. COMMUNITY (KVR). Test each one before a project depends on it.
- The project plans a compatibility table for plugins; none was published in the README. COMMUNITY [8]

### 4.6 Test that it works (checklist)
1. Live starts and shows the authorization state. 2. Settings > Audio shows PipeASIO with no error.
3. Play a clip for 10 minutes at buffer 256 with no dropouts. 4. Record one audio clip from the interface.
5. Load one Ableton instrument and one Windows VST3. Open its window, save the Set, reopen, check state.
6. Max for Live: drop one Max device in a Set and see it load (see max-for-live-expert).
7. Plug in the MIDI controller; unplug and replug while Live is open. COMMUNITY [8] says reconnect is supported.
8. Export Audio/Video once and play the file. 9. Close and reopen Live, test again. 10. Check `pw-top` for ERR counts (linux-audio-production).

### 4.7 Known problems and fixes
- No sound: toggle Audio Device None then PipeASIO. COMMUNITY [9]
- Crackle with two audio devices: use one device for both in and out; run `~/.local/share/ableton-wine/audio-report.sh`. COMMUNITY [9]
- Audio stops or runs at the wrong speed: wait a few seconds; else close Live and run `pw-metadata -n settings 0 clock.force-quantum 0`. COMMUNITY [9]
- High latency: lower the buffer in `pipeasio-settings`, toggle the device, run realtime setup. COMMUNITY [9]
- Max for Live: CDM calls support experimental. COMMUNITY (cdm.link, via max-for-live-expert). WineHQ bug 57109 "Max for Live fails to start" and bug 57260 "Severe graphical issues" were on plain Wine; I did not read their resolution. COMMUNITY (titles only)
- Live 11 only: Max for Live needs a one-time repair, and WMA or video import can crash. COMMUNITY [9]
- Graphics card note greyed out for Enable GPU Renderer: run `update`. COMMUNITY [9]
- Push 3: needs a udev rule in /etc/udev/rules.d (vendor 2982, product 1969). Control mode only is tested. COMMUNITY [8]. Push 2 duplicate rows break the connection. COMMUNITY [9]. More in ableton-push-expert.
- Send bug reports with edition, release number, distro and desktop; never attach installers, authorization files or licence keys. COMMUNITY [9]

### 4.8 Backup, update, uninstall
- Back up Live Sets and samples separately; do not trust a prefix copy alone. See wine-proton-bottles section 11.
- Back up the prefix: close Live, copy the whole `~/.wine-ableton` folder. UNVERIFIED as a restore method (the README only says the prefix holds Live and authorization). COMMUNITY [8]
- Update: `sh ~/Downloads/install-ableton-latest.run update`. It keeps Live, authorization and projects, and never updates itself. Read the changelog first. COMMUNITY [8]
- Uninstall: `uninstall` keeps the prefix; `uninstall --delete-prefix` removes Live and its authorization, but keeps Sets stored outside the prefix. COMMUNITY [8][11]
- Latest release I could read in the changelog: 2026.08.28.1 (release 2026.08.27.1 was withdrawn). COMMUNITY [10]. Newer ones may exist.
- Authorization is lost with `--delete-prefix`; deauthorize or note your two-computer count first. UNVERIFIED how deauthorize works under Wine.

### 4.9 Do NOT rely on it for gigs
- No vendor support, a small volunteer team, hard kernel and PipeWire requirements, releases that change defaults. COMMUNITY [8][10]
- A withdrawn release blocked updates once (2026.08.27.1). COMMUNITY [10]
- Never update the night before a show. Keep a Windows or macOS fallback with the same Set, or use Bitwig natively.
- Do not rely on Max for Live, copy protected plugins, Push 3 or Link Audio under Wine without testing. UNVERIFIED

## 5. Expert use (hard dance, trance, hardstyle)
1. Session vs Arrangement: sketch loops in Session View, then record or drag clips to Arrangement. Tab switches views. Live manual: Resampling input records the Main output into a track. VERIFIED [14]
2. Racks: Macro Controls can address any number of parameters across devices in a Rack, good for filter, drive and reverb builds. Drum Racks have Choke groups (sixteen) for open and closed hats. VERIFIED [14]
3. Kick: layer click, body and tail in a Drum Rack; add Saturator or Pedal and a Limiter; resample to audio. Device choice is UNVERIFIED genre practice; Pedal is Suite only. VERIFIED [3]
4. Rumble: resample the kick tail, add Reverb, low-pass with EQ Eight, sidechain to the kick. UNVERIFIED genre practice.
5. Sidechain: unfold the Compressor or Glue Compressor with the title bar toggle, enable Sidechain, pick the Kick track in the choosers. Gain sets trigger level; Dry/Wet at 100% means fully triggered by the source. The headphone button listens to the sidechain only. VERIFIED [12]. For third party plugins see help article "Sidechaining a third party plug-in" (title only). [20]
6. Warp: Beats, Tones, Texture and Re-Pitch play neutrally when the clip tempo equals the Set tempo. Complex and Complex Pro are never neutral and use more CPU; use them for full mixes. Complex Pro has Formants and Envelope controls. VERIFIED [13]. Use Beats for drum loops, Re-Pitch for tape style pitch: UNVERIFIED genre advice.
7. Sample rate: mixing files of other rates degrades playback; convert offline. Pick 44.1 or 48 kHz per project. VERIFIED [14]
8. Delay compensation is on by default; Reduced Latency When Monitoring trades sync for lower latency on monitored tracks. VERIFIED [14]
9. Export: WAV, AIFF or FLAC. Dither only once; render 32-bit if you will process further. Triangular is the safe default. VERIFIED [14]
10. Splice: in the browser since 12.3, works with Search with Sound. VERIFIED [18]
11. Tempo: hardstyle 150 to 160, UK hardcore 160 to 175, trance 135 to 145 BPM. UNVERIFIED genre knowledge.
12. Max for Live: use for Sequencers, LFOs, modulators. Building patches: cycling74.com/learn and max-for-live-expert.
13. Push as a hands-on controller: see ableton-push-expert.
14. Linux production advice: use Bitwig natively for stable work and treat Live as secondary. Opinion, UNVERIFIED.

## 6. Test checklist for your own plugins in this DAW
Works the same on all three systems unless a line says otherwise.
1. Scan. Windows: put the VST3 in `C:\Program Files\Common Files\VST3` or set a custom folder. macOS: VST3 or AU in the system folder, "Use Audio Units" on. Linux: copy into the Wine prefix VST3 folder (section 4.5). Then Settings > Plug-ins > Rescan. VERIFIED [5] for Rescan.
2. Clean scan: hold Alt (Windows) or Option (macOS) while pressing Rescan to rebuild the database. VERIFIED [5]
3. Crash on scan: Live names the plugin on relaunch; a second crash makes it unavailable until reinstall. VERIFIED [5]
4. Preset recall: save a Set and a device preset (.adg), reload, compare.
5. Automation: automate parameters from the device lane; check smoothing and stepping.
6. Sample rate change in Settings > Audio; plugin resets without errors.
7. Offline render: Export Audio/Video and compare with a Resampling track. VERIFIED [14] for both features.
8. Latency reporting: Delay Compensation is on; null-test against a dry copy. VERIFIED [14] for the feature.
9. State save and reload: close and reopen the Set; state and window restored. Freeze Track and unfreeze.
10. Sidechain: if the plugin has a sidechain input, test Live's sidechain chooser (shown on the left of supported plugin devices). VERIFIED [5]
11. Plugin window: test Auto-Hide Plug-In Windows and Multiple Plug-In Windows settings. VERIFIED [5]
12. Linux/Wine only: test Windows builds in the prefix. For Linux builds test in Bitwig, since Live supports no native Linux plugins. COMMUNITY [8]
13. Wine only: test the GUI with Auto-Scale Plugin Window on and off, and the GLX switch if the GUI is OpenGL. COMMUNITY [9]

## Not verified
- Live prices, current store offers and regional rent-to-own terms.
- Whether WASAPI is a Live driver type on Windows; the exact Driver Type list.
- Default VST3 and AU scan folders on Windows and macOS; whether a licence works across Windows and macOS.
- Bazzite kernel NTSync status, GStreamer, zstd, flock presence; whether the ableton-linux installer runs cleanly on Bazzite.
- Whether Ableton online authorization succeeds under Wine; deauthorizing under Wine.
- Which OS download the ableton-linux installer expects.
- Max for Live stability under the project; Link Audio under Wine; Push 3 over USB under Wine beyond the README.
- WineHQ AppDB ratings for Live (page blocked: Access Denied).
- The system requirements page on ableton.com (client error); the help.ableton.com article was read instead.
- Newer ableton-linux releases than 2026.08.28.1.
- Genre practice lines marked UNVERIFIED in section 5 (hardstyle kick design, rumble, tempo ranges).

## Sources (fetched)
1. https://www.ableton.com/en/release-notes/live-12/ (WebFetch and Ableton knowledge MCP search_release_notes)
2. https://help.ableton.com/hc/en-us/articles/115001663530-Live-Minimum-System-Requirements
3. https://www.ableton.com/en/live/compare-editions/ (first 100000 of 128256 characters)
4. https://www.ableton.com/en/live/
5. https://www.ableton.com/en/manual/using-plug-ins/
6. https://help.ableton.com/hc/en-us/articles/360000573444-Authorizing-Live-Offline
7. https://www.ableton.com/en/live-manual/12/first-steps/
8. https://raw.githubusercontent.com/shibco/ableton-linux/main/README.md
9. https://raw.githubusercontent.com/shibco/ableton-linux/main/TROUBLESHOOTING.md
10. https://raw.githubusercontent.com/shibco/ableton-linux/main/CHANGELOG.md
11. https://raw.githubusercontent.com/shibco/ableton-linux/main/INSTALLER.md
12. https://www.ableton.com/en/manual/live-audio-effect-reference/ (via knowledge MCP)
13. https://www.ableton.com/en/manual/audio-clips-tempo-and-warping/ and /audio-fact-sheet/ (via knowledge MCP)
14. https://www.ableton.com/en/manual/routing-and-i-o/ , /managing-files-and-sets/ , /working-with-instruments-and-effects/ , /instrument-drum-and-effect-racks/ (via knowledge MCP)
15. https://www.ableton.com/en/manual/accessibility-and-keyboard-navigation/ (Audio Setup text, via knowledge MCP)
16. https://raw.githubusercontent.com/robbert-vdh/yabridge/master/README.md
17. https://github.com/wineasio/wineasio
18. https://musictech.com/news/music/ableton-live-12-3/ and https://synthanatomy.com/2023/11/ableton-live-12-intro-standard-and-suite-what-are-the-differences.html
19. https://www.kvraudio.com/forum/viewtopic.php?p=8884394 ; https://git.ewpratten.com/evan/ewpratten.com/raw/branch/gh_ci/content/blog/2024-01-05-wineasio-bottles-ableton.md ; https://list.winehq.org/hyperkitty/list/wine-bugs@list.winehq.org/thread/BUBJCEFFLA7ZAFTQTDMFDTUU4WOXUBOS/ (title only)
20. help.ableton.com article titles from the knowledge MCP, not opened: Authorizing Live for all users on Windows and macOS, Sidechaining a third party plug-in, Plug-ins Tips and Troubleshooting, VST/AU plug-in doesn't appear in Live's Browser
