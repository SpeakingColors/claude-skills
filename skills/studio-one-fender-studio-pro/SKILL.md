---
name: studio-one-fender-studio-pro
description: Use when asked about Studio One or Fender Studio Pro on Windows, macOS or Linux (native beta, Wine recipe), covering naming, versions, workflow, plugin formats, ARA and testing your own plugins.
---

# Studio One, now Fender Studio Pro

Verify against current docs before acting on anything marked UNVERIFIED.
Labels: VERIFIED = read in a fetched page; COMMUNITY = forum or blog report; UNVERIFIED = not checked.

## Naming and versions
- Studio One became Fender Studio Pro, effective 13 January 2026 (VERIFIED, Sound On Sound news, 20 Jan 2026). PreSonus accounts move from MyPreSonus to MyFender. Quantum and AudioBox lines are rebranded Fender; other PreSonus products keep the PreSonus name.
- Fender Studio Pro 8 is the first Fender-branded release, succeeding Studio One Pro 7 (VERIFIED, SOS review). A "Fender Studio Pro 8.1" headline exists on the SOS site; its contents were not read (UNVERIFIED).
- Old names still appear in forums and docs: say "Studio One (now Fender Studio Pro)" when searching.
- Licences (VERIFIED, SOS news, USD): Perpetual 199.99; Pro+ annual subscription plus perpetual 179.99; upgrade 99.99; monthly 19.99. SOS review lists UK perpetual at 169.99 GBP incl. VAT. Check Fender's store for current prices.
- Free upgrade for subscribers and for perpetual buyers under 12 months old (VERIFIED, SOS review).
- Fender Studio (free app, separate product): 8 tracks without a free Fender Connect account, more after registering (VERIFIED, OMG Ubuntu). Do not confuse it with Studio Pro.

## Platforms
Related skills: wine-proton-bottles (Bottles, runners, wineasio, yabridge, backups), linux-audio-production (PipeWire, JACK, realtime), bazzite-kde-linux.

### Windows
- Current: Fender Studio Pro 8 (VERIFIED, SOS review). Exact OS minimums (Windows 10 or 11?) were not read: UNVERIFIED. Check Fender's requirements page.
- Install: download from your MyFender account, run the installer (UNVERIFIED steps).
- Audio: ASIO (the interface maker's driver, or ASIO4ALL style generic) or Windows audio (UNVERIFIED for 8).
- Plugin folders: C:\Program Files\Common Files\VST3 for VST3; VST2 folder set in Studio One options (UNVERIFIED).
- Licensing: Fender account; perpetual or Pro+ subscription (VERIFIED, SOS). Number of activations: UNVERIFIED.

### macOS
- OS minimums: not read, UNVERIFIED. Apple Silicon support: UNVERIFIED for 8.
- Audio: Core Audio (UNVERIFIED for menus). Plugin folders: /Library/Audio/Plug-Ins/VST3, Components for AU (UNVERIFIED, standard).
- Formats: AU is available on Mac; ARA2 for Melodyne (UNVERIFIED for v8).
- Licensing: same account as Windows (UNVERIFIED per-OS terms).

### Linux
- A Public Beta .deb exists: Ubuntu 24.04 LTS or later, x86_64, 8 GB RAM, 40 GB disk (COMMUNITY: Shimamura blog, 17 March 2026; not Fender's page).
- An AUR package named fender-studio-pro-8 appears in search results (COMMUNITY, title only, page not read because of the fetch limit). It suggests the .deb is repackaged by users: UNVERIFIED.
- The free Fender Studio app has a Flatpak from Fender's site, not Flathub, Ubuntu 24.04 plus Flatpak (VERIFIED, OMG Ubuntu, May 2025). That is a different product.
- Audio on Linux: JACK or PipeWire layer (UNVERIFIED for the beta; no source read). See linux-audio-production.
- Plugin folders: ~/.vst3 (UNVERIFIED for the beta).
- Licensing: Fender account login; offline behaviour UNVERIFIED.
- Windows vs macOS vs Linux: the Linux build is a beta, unsupported, so expect missing features compared with Windows and macOS (COMMUNITY: no official support, ARM did not work).

## Linux status
- There is a Linux build of Studio Pro: a Public Beta distributed as a .deb, Ubuntu 24.04 LTS or later, x86_64, 8 GB RAM, 40 GB disk (COMMUNITY: Japanese retailer blog, 17 March 2026; I did not find Fender's own page, so treat the beta status as UNVERIFIED against Fender).
- Same blog reports it ran on Fedora Sway Spin after extracting the .deb with `ar x`; no official support; ARM did not work. This is the best route for a Fedora Atomic user: try a distrobox (Ubuntu 24.04) or extract the .deb, rather than Wine (UNVERIFIED that it works on Bazzite).
- The free Fender Studio app is distributed as a Flatpak from Fender's site, not Flathub, requiring Ubuntu 24.04 plus Flatpak (VERIFIED, OMG Ubuntu, May 2025). Studio One Pro Linux support was reported in 2023 per the same article.
- Wine/Bottles: I found no verified Wine report for Studio Pro 8 and no WineHQ AppDB entry (UNVERIFIED). If the native beta is usable, prefer it. If Wine is the only path, expect the issues below.

## Run it on Linux (native beta first, then Wine, Bottles, Proton)
Honest status. No Wine report for Studio Pro 8 was found, and WineHQ AppDB was blocked by a bot check (UNVERIFIED). ProtonDB has no known entry I could read (UNVERIFIED). The native beta is the better first try.

### Route A: native Linux beta in a distrobox (UNVERIFIED that it works on Bazzite)
1. Get the .deb from Fender's download area (needs a Fender account). Note the exact file name; if there is no Linux file, stop and tell Claude what you see.
2. Create an Ubuntu 24.04 distrobox (Bazzite ships distrobox; see bazzite-kde-linux). Install the .deb inside it with apt (UNVERIFIED).
3. Alternative from the blog: extract the .deb with `ar x` on Fedora Sway Spin; it ran there (COMMUNITY, Shimamura). Not tried on Bazzite.
4. Audio: the container needs PipeWire access. This is the usual weak point (UNVERIFIED). Test with section "TEST checklist" below.
5. Report back with the version string and any error text.

### Route B: Windows build under Wine with Bottles (all UNVERIFIED for Studio Pro 8; Bottles facts from wine-proton-bottles)
1. Install Bottles (Flatpak) from Bazaar. Allow only the installer folder (`flatpak override --user --filesystem="/path/to/folder" com.usebottles.bottles`, VERIFIED, wine-proton-bottles section 3).
2. New bottle: name StudioPro8, environment Software, runner Caffe (VERIFIED defaults). 64-bit prefix.
3. Dependencies: install vcrun and .NET entries Bottles lists, one at a time. Do not guess names (VERIFIED advice). Add corefonts.
4. Run the Fender installer (.exe) in the bottle with Run executable. Add the program shortcut. Black screen or silent crash: copy the program folder into the bottle's C: drive and add the exe again (VERIFIED, wine-proton-bottles section 9).
5. Sign in to your Fender account in the app. Activation is online (UNVERIFIED for 8; Studio One used a PreSonus account, VERIFIED in section "Naming"). If sign-in loops, try a different runner (Vaniglia, then a Proton runner).
6. WineASIO: match Wine's bitness, run `wineasio-register` for the bottle prefix (VERIFIED, wine-proton-bottles section 7). The Flatpak Bottles runner does not see a system install; no verified Flatpak recipe exists, so do not invent one. Fallback: Wine's PulseAudio driver, worse latency (UNVERIFIED).
7. PipeWire quantum: `pw-metadata -n settings 0 clock.force-quantum 256` (VERIFIED command, linux-audio-production section 3). Set it before opening the DAW.
8. Windows VST3: install the plugin in the same bottle; Studio Pro then loads it inside Wine (UNVERIFIED). yabridge is for native Linux hosts: it needs Wine Staging, tested on 9.21, fails on 9.22 and 10.x with yabridge 5.1.1, and does not work with Flatpak hosts (VERIFIED, README). Commands: `yabridgectl add`, `yabridgectl sync` (VERIFIED).
9. Licensing caveats: iLok-style or copy-protected plugins are likely to fail (UNVERIFIED, wine-proton-bottles). iZotope and D16 plugins cannot authorise (VERIFIED, yabridge README).
10. Backup: Bottles, Duplicate before experiments; Full Backup archive for the bottle (VERIFIED, wine-proton-bottles section 11). Back up Songs and sample libraries separately.

### TEST checklist: does it work?
1. App opens, no crash within 60 seconds.
2. Fender login accepted and the licence shows as active; survives a restart.
3. An audio device is listed; a 48 kHz song plays 10 minutes with no crackle at 512, then 256.
4. `pw-top` ERR column stays flat during playback (COMMUNITY meaning).
5. A stock instrument plays from MIDI input.
6. One of your own VST3 plugins loads; save, close, reopen restores it.
7. Export Mixdown works and the WAV plays.

### Known problems and fixes (UNVERIFIED unless labelled)
- Black window or glitchy GUI: toggle DXVK off; try Vaniglia (VERIFIED order, wine-proton-bottles section 10).
- Blank text in plugin GUIs: corefonts or allfonts (VERIFIED, yabridge README).
- Stuck processes: `ujust fix-proton-hang` (VERIFIED).
- ARM did not work for the native beta (COMMUNITY, Shimamura).
- Prefix on ext4 or btrfs, not NTFS (VERIFIED).

### Do NOT rely on this for gigs or deadlines
- Beta software, no support. Online licence checks may fail. Wine updates can break the prefix.
- Keep a Windows or macOS install for paid work. Native alternatives on Bazzite: Bitwig or Reaper (my recommendation).

## What to expect under Wine (all UNVERIFIED, general Wine behaviour)
1. Licensing/activation uses a Fender/PreSonus account and online checks; may fail under Wine.
2. Audio: use WineASIO over PipeWire-JACK. Build steps documented for Ableton under Bottles on Fedora apply the same way (see ableton-live skill sources).
3. Plugin GUIs may need yabridge instead of loading Windows plugins inside the prefix.
4. ARA, video track and the Fender-specific plugins are untested.
Report any result to the reader as a community-style result only after trying it.

## Workflow (features from SOS review where marked VERIFIED)
- Song page: the main recording/mixing view; in version 8, Songs are called sessions (VERIFIED, SOS review). Project page was renamed Mastering Page; Show page now has a video track (VERIFIED).
- Project/Mastering page: master several songs, apply the final limiter, export a DDP or WAV set. Use it for a hardstyle EP.
- Scratch Pads: alternate arrangement sections you can try without touching the main timeline (UNVERIFIED in v8 details).
- Arranger track: define sections (Intro, Build, Drop) and reorder them as blocks; the timeline follows (UNVERIFIED v8 details).
- Chord Track: chords drive harmony; v8 has a simplified chord wheel and an AI Chord Assistant that suggests alternatives (VERIFIED).
- Pipeline: insert external hardware (e.g. a hardware synth or drum machine) as an effect loop via audio I/O, with latency compensation (UNVERIFIED).
- Mix FX / Mix Engine: Studio One's console with channel strips and bus FX; v8 adds a channel overview (VERIFIED, SOS news).
- Native Fender amp/effects plugins (Mustang, Rumble Native) and updated samplers are new; AI audio-to-note conversion (VERIFIED, SOS news).

## Hard dance workflow
1. Template: Kick, Rumble, Sub, Leads, FX, Drums in folder tracks. Save as Song template.
2. Sidechain: add the Pro EQ/Compressor on the bass track and choose the kick track as the Sidechain source in the plugin's sidechain menu (UNVERIFIED exact UI).
3. Kick: render the distorted kick to audio and edit it in the Audio editor.
4. Use the Arranger track to sketch 16 or 32 bar sections.
5. Master on the Project/Mastering page with a limiter and a loudness meter.

## Expert use: hard dance and trance (sourced facts, then recommendations)
- Fender Studio Pro 8 keeps the Arranger track, Chord Track, Mix Engine and Mastering Page (VERIFIED, SOS review and news; names as in "Workflow").
- Chord Track in v8: simplified chord wheel and AI Chord Assistant (VERIFIED). Good for trance chord stacks.
- Tempo ranges: hardstyle 150 to 160 BPM, UK hardcore 160 to 175, trance 135 to 145 (UNVERIFIED, genre knowledge).
- Kick: render the distorted kick to audio, then EQ and compress the bounce. Rumble: kick tail, low-pass, sidechain to the kick (UNVERIFIED, shared recipe).
- Master on the Mastering Page: limiter, loudness meter, DDP or WAV set (VERIFIED feature, per Workflow list).
- These are the same on Windows and macOS. On Linux they apply only if the beta or Wine route runs.

## Plugin formats and ARA
- Windows/Mac: VST2, VST3, AU (Mac), and ARA2 for Melodyne (UNVERIFIED for v8).
- Linux beta: plugin format support was not in the sources read; assume VST3 and test with your own plugin (UNVERIFIED).
- CLAP: UNVERIFIED; assume unsupported.

## Test checklist for your own plugins in this DAW
1. Scan: place the VST3 in ~/.vst3 (or the folder the beta scans) and rescan; check Plug-in Manager.
2. Preset recall: save a song with the plugin, reload, compare parameters.
3. Automation: write automation from the plugin GUI and the host lane; check playback.
4. Sample rate change: switch the song sample rate in Song Setup; plugin must not crash or go silent.
5. Offline render: Export Mixdown with the plugin and compare to realtime; also test "Export stems".
6. Latency reporting: place on a track with parallel dry copy; verify compensation.
7. State save and reload: close and reopen the song; check the plugin window size and chunk data.
8. Fender Studio Pro Linux beta is unsupported, so log any crash with the version string.
9. Cross-platform: same song on Windows, macOS and Linux; plugin found, same state, same render.
10. Wine only: plugin window opens, resizes and closes without freezing the app.

## Not verified
Windows and macOS minimum OS and chip support for Fender Studio Pro 8; Fender's own Linux page; whether the Linux beta runs on Bazzite, in a distrobox or via the AUR package; any Wine, Bottles or Proton result for Studio Pro 8; WineHQ AppDB and ProtonDB ratings (AppDB blocked); activation limits per account; audio driver menus on all three systems; plugin formats in the Linux beta; the "Fender Studio Pro 8.1" contents. Fetch limit reached 2026-10-23, so Fender vendor pages could not be re-read; version facts come from the earlier SOS research.

## Sources (fetched)
- https://www.soundonsound.com/news/studio-one-becomes-fender-studio-pro
- https://www.soundonsound.com/reviews/fender-studio-pro-8
- https://www.shimamura.co.jp/update/?p=20213
- https://www.shimamura.co.jp/shop/shintokorozawa/?p=7666
- https://www.omgubuntu.co.uk/2025/05/fender-studio-linux-audio-recording-app
- https://github.com/robbert-vdh/yabridge/blob/master/README.md (yabridge limits)
- Search results only, pages unread: aur.archlinux.org/packages/fender-studio-pro-8, WineHQ AppDB (blocked)
