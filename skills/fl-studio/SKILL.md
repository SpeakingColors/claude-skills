---
name: fl-studio
description: Use when helping with FL Studio, covering versions, licensing, running it on Linux via Wine or Bottles, hard dance workflow, mixer sidechain, and testing your own plugins in it.
---

# FL Studio (Image-Line): Windows, macOS, Linux

Researched 2026-10-23. Re-check versions and prices before quoting them.
Verify against current docs before acting on anything marked UNVERIFIED.
Labels: VERIFIED = read in a fetched page (number = Sources list). COMMUNITY = forum, blog or guide by a user. UNVERIFIED = not checked.
Rules for Claude: Assume the reader is not a programmer. Plain words first, then one exact step. One change at a time, ask the reader to test, then continue.
Related skills: wine-proton-bottles (Bottles, runners, wineasio, yabridge, backups), linux-audio-production (PipeWire, realtime, xruns), bitwig-studio (native Linux host for plugin tests).
Failed fetches this session: image-line manual pages (audio settings, plugins, mixer), image-line release archive, system-requirements page, WineHQ AppDB (Access Denied), Image-Line forum thread (blocked by permission), hourly fetch limit reached late. Nothing below comes from those pages.

## 1. Versions and licensing
- Current generation is FL Studio 2026, a free update for everyone including existing owners. VERIFIED [1] The older skill said 2025; that is now outdated.
- Point version: a community guide names 26.1.3 and 26.1.4 (Aug 2026). The newest point version: UNVERIFIED, check image-line.com. COMMUNITY [5]
- 2025 features (still in the product line): Loop Starter, mixer to 500 tracks, Gopher AI assistant, Emphasis limiter (All Plugins only), FL Studio Mobile instruments and effects, per-clip stretch, pitch and reverse, Bassline mode in the Chord Progression Tool, FL Studio Remote app. VERIFIED [3]
- Lifetime free updates: buy an Edition once and every later update for that Edition is free. A full release comes each year. VERIFIED [1][3]
- Licence covers both Windows and macOS and carries over if you switch computers or platforms. VERIFIED [1] Linux is not mentioned. VERIFIED [1]
- Editions: Fruity, Producer, Signature Bundle, All Plugins. VERIFIED [2]
- Fruity: 53 effects, 23 instruments, no audio recording, no Edison, Newtime or Newtone. VERIFIED [2]
- Producer: adds audio recording, denoising, Edison, Newtime, Kepler, Slicex, Sytrus, Maximus, Vocodex, Spreader. 59 effects, 27 instruments. VERIFIED [2]
- Signature Bundle: adds Newtone, DirectWave Full, Harmless, Pitcher, Gross Beat, Fruity Video Player. 65 effects, 29 instruments. VERIFIED [2]
- All Plugins: adds Harmor, Drumaxx, Morphine, Sawer, LuxeVerb, Transmitter, Emphasis. 71 effects, 39 instruments. VERIFIED [2]
- Upgrades are pro-rated, you pay the difference. VERIFIED [2]
- Price: the page title says "From $99"; per-edition prices were not shown. VERIFIED [2] (partial). Check the pricing page.
- Rent-to-Own Plus: pay monthly, after 12 payments the licence is yours; FL Cloud continues until cancelled; availability varies by region. VERIFIED [1][2]
- FL Cloud is a separate optional subscription. VERIFIED [1]
- For hard dance, Producer or higher is needed for audio clips and recording. VERIFIED [2] (Fruity has no audio recording)

## 2. Platforms

### Windows
- Version and OS: Windows 10 or 11, 2 GHz CPU with SSE2, 4 GB RAM, 4 GB free disk. Recommended: quad-core, 8 GB or more, SSD. VERIFIED [1]
- Install: download the installer from image-line.com, run it, sign in to your Image-Line account. VERIFIED [1] for download; sign in step COMMUNITY [5]
- Audio driver: ASIO is the pro path. FL Studio ASIO (Image-Line's own driver) and the Audio Settings page (Options > Audio Settings): UNVERIFIED, the manual page failed to fetch.
- WASAPI and MME driver options in FL: UNVERIFIED.
- Plugin folders: VST3 default `C:\Program Files\Common Files\VST3` (standard install place, VERIFIED as such by yabridge docs [6]). FL's own scan list: Options > Manage plugins, Find installed plugins. UNVERIFIED (manual not fetched).
- Licensing: account based, unlock in the app by login. COMMUNITY [5]

### macOS
- OS: macOS 10.15 or later on Apple silicon or Intel; Apple silicon runs natively without Rosetta. Same RAM and disk as Windows. VERIFIED [1]
- Audio: Core Audio. UNVERIFIED in FL's manual (not fetched); it is the macOS system driver.
- Plugin folders: VST3 `/Library/Audio/Plug-Ins/VST3`, AU `/Library/Audio/Plug-Ins/Components`. UNVERIFIED (standard Apple paths, FL manual not fetched).
- Formats FL hosts on macOS (VST2, VST3, AU, CLAP): UNVERIFIED.
- Licensing: same account licence, works on both platforms. VERIFIED [1]

### Linux
- No native Linux version. VERIFIED [1] (page lists only Windows and macOS) and no Image-Line support statement appeared in the forum view. COMMUNITY (Image-Line forum megathread, partial)
- Only route: Wine through Bottles. See section 3.
- Audio on Linux: PipeWire plus JACK layer. WineASIO needs a build matching Wine; see wine-proton-bottles section 7. VERIFIED [7]
- Plugin folders on Linux: Windows plugins go inside the bottle's C: drive, `Program Files/Common Files/VST3`. UNVERIFIED for FL; standard Windows path, mirrors the Ableton Wine route.
- Licensing on Linux: trial opens first, then log in with your account and enter the code. Works for one user. COMMUNITY [5]

## 3. Run it on Linux (Wine, Bottles, Proton)
Status: unofficial and unsupported. COMMUNITY [5]. Use Windows or macOS where a show depends on it.

### 3.1 Which runner
- Bottles runners people use: Soda, Kron4ek, Proton GE. COMMUNITY [5]. Bottles also has Caffe and Vaniglia (see wine-proton-bottles section 4). VERIFIED there.
- The guide's screenshots show `ge-proton10-25`, Windows 11 compatibility mode, DXVK and VKD3D on. COMMUNITY [5]
- Wine-staging is needed only for yabridge, not for FL itself. VERIFIED [6]
- Warning (Aug 2026): FL Studio 26.1.4 has a new certificate that Wine cannot verify. Error `WINTRUST_DefaultVerify returning 80096004`. Use 26.1.3 or lower until Wine is fixed. COMMUNITY [5]
- Workaround from the same guide: a custom Proton fork "DAW GE Proton" by KitsuneDev (github.com/KitsuneDev/daw-proton-ge/releases). Unpack it into `~/.var/app/com.usebottles.bottles/data/bottles/runners/<your-name>/` so that `bin`, `lib` and `share` sit directly inside. COMMUNITY [5]. The upstream Wine fix is merge request 11824. COMMUNITY [5]
- FL Cloud plugins appear to leak memory (Jan 2026 note). COMMUNITY [5]
- Check the guide again before every FL update. Reason: new FL builds have broken Wine before.

### 3.2 Step by step on Bazzite (one step at a time, test after each)
1. Install Bottles from the Bazaar store or Flathub (Flatpak id `com.usebottles.bottles`). VERIFIED in wine-proton-bottles section 3. Also install Flatseal. COMMUNITY [5]
2. Open Bottles. Preferences > Runners. Install Soda, Kron4ek or Proton GE. Tick Pre-release only if you need a newer one. COMMUNITY [5]
3. If you will use FL 26.1.4 or newer, install the DAW GE Proton runner by hand (section 3.1). COMMUNITY [5]
4. Create a bottle. Name it "FL Studio". Pick the runner. Environment: Software (see wine-proton-bottles section 5). COMMUNITY [5] for runner; environment choice UNVERIFIED for FL.
5. In the bottle open Options > Dependencies. Install `allfonts`. COMMUNITY [5]
6. Download `msgothic.ttc` (FSKiller/Microsoft-Fonts on GitHub). In the bottle press Browse, open `windows/Fonts`, drop the file there. This shows sharps and flats in notation. COMMUNITY [5]
7. In the bottle settings check Runner, DXVK and VKD3D. Set Windows version to Windows 11 under Compatibility. COMMUNITY [5]
8. Download the Windows installer from image-line.com. Copy it to the bottle C: drive or give Bottles access to Downloads (wine-proton-bottles section 3 shows the override).
9. In the bottle choose Run Executable and pick the installer. Skip the 64-bit FL plugin. Skip FL Cloud Plugins unless wanted. The WebView2 installer is slow, wait. COMMUNITY [5]
10. If the installer does not start, close Bottles fully and try again. COMMUNITY [5]
11. When done, go back to the main Bottles list and reopen the bottle. FL64 appears in Programs. COMMUNITY [5]
12. First start is Trial mode. MIDI input "FAIL" messages can be disabled. Log in and enter the validation code. The desktop may say Bottles "is not responding"; press Wait. Restart FL without saving. COMMUNITY [5]
13. After installing anything, run `flatpak kill com.usebottles.bottles` and start fresh, because Edge WebView processes can hang. COMMUNITY [5]
14. Run the test checklist in section 3.5.

### 3.3 Audio: wineasio, PipeWire, JACK
- WineASIO is an ASIO driver that talks to JACK. PipeWire's JACK layer can serve it. VERIFIED [7] for JACK; PipeWire part COMMUNITY. See wine-proton-bottles section 7.
- Register it in the bottle's prefix with `env WINEPREFIX=<prefix> wineasio-register`. Bottles stores bottles in `~/.var/app/com.usebottles.bottles/data/bottles`. VERIFIED [7] and wine-proton-bottles section 2.
- Flatpak problem: Bottles uses its own runner, not system Wine, so copying wineasio into /usr will not work. A working Flatpak recipe: UNVERIFIED. Do not invent one.
- In FL: Options > Audio Settings, pick the ASIO device (menu name UNVERIFIED).
- Env vars: `WINEASIO_PREFERRED_BUFFERSIZE` power of two, default 1024; a size the backend cannot do can shut JACK down. VERIFIED [7]
- Fallback without wineasio: Wine's own audio via the PulseAudio driver. Higher latency. UNVERIFIED
- Check with `pw-top` and read linux-audio-production sections 3, 5 and 11.

### 3.4 Plugins and yabridge
- Windows plugins for FL: install them in the same bottle, with the plugin's installer (Run Executable). They land in the bottle's own Program Files. Then rescan inside FL. UNVERIFIED for FL; same logic as the Ableton route.
- Correction to the old skill: yabridge is not the way to load plugins inside FL. yabridge bridges Windows plugins into native Linux hosts such as Bitwig, Ardour, Reaper. VERIFIED [6]
- yabridge limits: does not work with Flatpak DAWs, needs Wine Staging, Wine 9.22 and 10.x did not work with yabridge 5.1.1. VERIFIED [6]
- Commands for the Bitwig route: `yabridgectl add "$HOME/.wine/drive_c/Program Files/Common Files/VST3"`, `yabridgectl sync`, `yabridgectl status`. Bridged plugins appear in `~/.vst3/yabridge`. VERIFIED [6]
- Copy protected plugins and iLok: may fail. Online activation and WebView based logins may hang. UNVERIFIED for FL; D16 plugins could not be authorized in current Wine. VERIFIED [6]
- Native Linux plugins (your own JUCE builds) do not load in a Windows FL. Test them in Bitwig.

### 3.5 Test that it works (checklist)
1. FL starts without a certificate error. 2. Help > About shows the version (26.1.3 or lower if on stock Wine). UNVERIFIED menu path.
3. Login and licence show as active; edition name correct. 4. Audio Settings shows the ASIO device; play a pattern for 10 minutes with no dropouts.
5. Record audio input from the interface (Producer or higher).
6. Load one FL instrument and one Windows VST3; open its window; save and reload the project.
7. Play MIDI from a keyboard. 8. Render a WAV and play it. 9. Quit FL; run `ps` or a process monitor and kill leftover Edge WebView processes. COMMUNITY [5]
10. Reopen and repeat 4 to 8.

### 3.6 Known problems and fixes
- Certificate error 80096004 on 26.1.4 and newer: downgrade to 26.1.3 or use DAW GE Proton. COMMUNITY [5]
- Installer will not start: restart Bottles. COMMUNITY [5]
- No FL64 in Programs: reopen the bottle. COMMUNITY [5]
- Login hangs with "not responding": wait. Browser login link needs `MimeType=x-scheme-handler/flstudio` in the .desktop file; works with Flatpak Chromium, not Flatpak Firefox. COMMUNITY [5]
- Hung WebView processes: `flatpak kill com.usebottles.bottles`. COMMUNITY [5]
- Plugin GUI glitches: try DXVK off in bottle preferences. UNVERIFIED (wine-proton-bottles section 5)
- Crash triage order: wine-proton-bottles section 10.
- High-DPI scaling, USB MIDI through the PipeWire bridge: UNVERIFIED general Wine areas.

### 3.7 Backup of the prefix
- Bottles: Backup > Full backup archive (contains personal files), Config backup (bottle.yml), and Duplicate as a template before experiments. VERIFIED, wine-proton-bottles section 11.
- Make a duplicate before every FL update. Keep the old FL installer file for the last good version.
- Back up projects (.flp) and samples separately, outside the bottle.

### 3.8 Do NOT rely on it for gigs
- Unofficial, one person's guide, a single new FL build can break it for weeks. COMMUNITY [5]
- Licence validation, WebView and FL Cloud parts are the weak points. COMMUNITY [5]
- Freeze the working FL version and runner; do not update before a show. Keep a Windows or macOS fallback.

## 4. Expert use (hard dance, trance, hardstyle)
Items marked VERIFIED are about product facts; workflow advice is UNVERIFIED genre practice unless stated.
1. Channel Rack: one channel per sound. Right-click a channel to route to a mixer track (Ctrl+L auto-assigns). UNVERIFIED
2. Piano roll: ghost notes, scale highlight, chord tools. Chord Generator and Bassline mode exist in 2025/2026. VERIFIED [2][3]
3. Mixer routing: kick bus, bass bus, lead bus, master. The mixer reaches 500 tracks. VERIFIED [3]
4. Sidechain: right-click the Kick track's send arrow on the bass track and choose "Sidechain to this track"; then pick the sidechain input in the compressor. Or a Fruity Peak Controller linked to bass volume. UNVERIFIED in fetched docs.
5. Patcher for layered leads with a macro. UNVERIFIED
6. Fruity Limiter as sidechain compressor or master limiter. Maximus (Producer and above) for multiband work on the master. VERIFIED [2] for edition; feature use UNVERIFIED.
7. Kick: layer click, body and distorted tail; waveshape; bounce to audio; EQ. Needs Producer for audio. UNVERIFIED practice.
8. Rumble: kick tail, reverb, low-pass, sidechain to the kick, tune to key.
9. Edison for sample edits (Producer and above). VERIFIED [2]
10. Harmor, Sytrus: Sytrus is in Producer, Harmor needs All Plugins. VERIFIED [2] (old skill said Sytrus was All Plugins; the pricing page puts it in Producer)
11. Gross Beat (Signature and above) for stutter and gating effects. VERIFIED [2]
12. Loop Starter for genre-based loop stacks. VERIFIED [3]
13. Arrangement: Playlist with pattern clips. Tempo hardstyle 150 to 160, UK hardcore 160 to 175, trance 135 to 145 BPM. UNVERIFIED genre knowledge.
14. Linux: for stable hard dance production use Bitwig natively and treat FL in Wine as an option for people who want the FL workflow. Opinion, UNVERIFIED.

## 5. Test checklist for your own plugins in this DAW
Same on all three systems unless noted.
1. Scan. Windows: put the VST3 in `C:\Program Files\Common Files\VST3`. macOS: `/Library/Audio/Plug-Ins/VST3` (UNVERIFIED path). Linux/Wine: the bottle's VST3 folder. In FL use Manage plugins and Find installed plugins; the plugin should appear as Generator or Effect. UNVERIFIED menu names.
2. Preset recall: save an FL preset (.fst) and a project, reload, compare.
3. Automation: right-click a knob, Create automation clip; check smoothing.
4. Sample rate change in the audio settings; plugin resets without errors.
5. Offline render: Export audio with the high quality options and compare with a realtime render.
6. Latency reporting: check delay compensation on the mixer slot and null-test against a dry copy.
7. State save and reload: save the .flp, restart FL, reload; check state and window.
8. Multiple instances: add 4 copies on different mixer tracks, check CPU and no shared-state bugs.
9. Sidechain input: if the plugin has one, route the Kick track and test.
10. Windows and macOS: run the same project on both and compare renders.
11. Wine only: test JUCE GUI under OpenGL and software rendering; test the bottle with DXVK on and off. Windows builds only; Linux builds belong in Bitwig.
12. Never test a new plugin build inside the bottle you use for work. Use the duplicate bottle.

## Not verified
- Newest FL point version, release date, and per-edition prices (pricing page showed "From $99" only).
- FL audio driver names on Windows and macOS (FL Studio ASIO, WASAPI, Core Audio); the Audio Settings menu layout.
- FL plugin folders and scan menu names on all three systems; formats hosted (VST2, VST3, AU, CLAP).
- Sidechain menu wording and Fruity Limiter or Compressor input names in the current build.
- Any Image-Line statement on Linux or Wine support; the full Image-Line forum megathread.
- WineHQ AppDB ratings for FL Studio 2026 (page blocked).
- Whether wineasio works with Bottles Flatpak on Bazzite; whether FL needs it at all.
- Whether DAW GE Proton works with every FL build; whether Wine merge request 11824 has landed.
- Whether FL works with the Bazzite Flatpak sandbox permissions beyond the guide's Flatseal tips.
- macOS minimum version beyond "10.15 or later" as quoted from image-line.com.

## Sources (fetched)
1. https://www.image-line.com/fl-studio (version, requirements, lifetime updates, platforms)
2. https://www.image-line.com/fl-studio/pricing (editions and contents)
3. https://www.image-line.com/fl-studio/lifetime-free-updates and https://www.image-line.com/archive/release-2/ (2025 features, earlier session)
4. https://forum.image-line.com/viewtopic.php?p=1629108 (earlier session, partial view)
5. https://github.com/Torbuntu/fl-studio-linux-setup (README, fetched raw)
6. https://raw.githubusercontent.com/robbert-vdh/yabridge/master/README.md
7. https://github.com/wineasio/wineasio (README)
8. https://git.ewpratten.com/evan/ewpratten.com/raw/branch/gh_ci/content/blog/2024-01-05-wineasio-bottles-ableton.md
9. Linked skills: wine-proton-bottles, linux-audio-production (their own Sources lists)
