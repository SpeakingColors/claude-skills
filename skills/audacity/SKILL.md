---
name: audacity
description: Use when helping with Audacity 3.x or 4.x on Windows, macOS or Linux (Bazzite), covering install choice, Flatpak vs AppImage, macros and batch, Nyquist, loudness, spectral editing, kick sample prep.
---

# Audacity (3.x and 4.x, 2026)

Labels: VERIFIED (source) = read on a page I fetched. COMMUNITY = user report, not official. UNVERIFIED = not confirmed; do not rely on it.
Rule for Claude: Assume the reader is not a programmer. Plain words first, then one exact step. One change at a time, ask the reader to test, then continue. Use exact menu names. Bazzite KDE is the focus on Linux. Always ask which version runs (Help > About).
Reddit was blocked. forum.audacityteam.org returned only a title. Manual pages (manual.audacityteam.org) are written for 3.x.

## 1. Versions and price
- Current release is 4.0.1 (30 Sep 2026). 4.0.0 came out 3 Sep 2026. VERIFIED (audacityteam.org download, changelog, GitHub release 4.0.1)
- 3.7.9 (1 Sep 2026) is the newest 3.x patch; it adds ASIO on Windows and FFmpeg 9. VERIFIED (GitHub releases)
- 3.7.x is "primarily maintenance while we work on Audacity 4.0". VERIFIED (Flathub page)
- Price: the Flathub page says the app is free. VERIFIED (flathub.org). Licence text: UNVERIFIED.
- Audacity 4 is a Qt rewrite with the .aup4 project format. .aup3 converts but cannot be saved back to .aup3. VERIFIED (changelog 4.0.0)
- 4.0 workspaces: Modern, Classic, Music. Select, Envelope, Draw and Multi-tool modes are removed. VERIFIED (changelog 4.0.0)
- Not yet in 4.0: Time Tracks, Note/MIDI tracks, Mixer, Macro Manager and scripting pipe, VAMP and LADSPA hosting, play-at-speed. VERIFIED (changelog 4.0.0)
- Some effects, analyzers and export features are also missing in 4.0. Which ones: UNVERIFIED (page says "some", no list).
- Rule of thumb: need macros or batch? Use 3.7.x. Everything else: 4.0.1. INFERENCE from the missing list.

## 2. Platforms
### Windows
- Tested on Windows 10 and 11; may work on 8.1 and 7. MSI installer or portable .7z, x86_64 and ARM64. VERIFIED (download/windows)
- ARM64 build: Windows 11 or later, no plugin support, needs ARM64 FFmpeg. VERIFIED (same page)
- Official Windows builds include ASIO (4.0.0, 3.7.9). VERIFIED (changelog, releases)
- Plugin formats: VST3, Nyquist (4.0). Folder for VST3: UNVERIFIED (standard Windows VST3 folder is general knowledge only).
### macOS
- Tested on macOS 14 and 15; may work back to OS X 10.11. VERIFIED (download/mac)
- DMG choices: Universal (Intel plus Apple Silicon), ARM64 only (no plugins), x86_64 only. macOS 10.14 and older need the Intel DMG. VERIFIED (same page)
- Plugin formats: VST3, Nyquist, Audio Units. VERIFIED (changelog 4.0.0)
### Linux
- Plugin formats: VST3, Nyquist, LV2. LADSPA not in 4.0. VERIFIED (changelog 4.0.0)
- Folders (~/.vst3, ~/.lv2): UNVERIFIED. Ask Claude to check Audacity's plugin manager instead of guessing.
- Audio: Bazzite uses PipeWire. Which host to pick in the device toolbar (ALSA, PulseAudio, JACK): UNVERIFIED.
- See section 3 for install choice.
### All systems
- Keep projects on an internal SSD, not USB sticks or network drives. VERIFIED (download pages)
- Optional FFmpeg library adds WMA, M4A, AC3. VERIFIED (download/linux)
- Plugins are offered through MuseHub (Trinity EQ, Graillon 3, MuseFX named). VERIFIED (blog)

## 3. Linux install on Bazzite: Flatpak or AppImage
Bazzite's main install source is the Flatpak store (Bazaar or Flathub). VERIFIED (docs.bazzite.gg via wine-proton-bottles skill)
### Option A: Flatpak (Flathub)
- Flathub lists Audacity 3.7.8, x86_64 and aarch64, 23 MiB. VERIFIED (flathub.org, at fetch time)
- It is community-made, unverified, and not supported by Muse Group. Issues go to the Flathub GitHub. VERIFIED (same page)
- Good for: macros and batch (3.7.x), automatic updates via Bazaar, sandbox. 
- Flatpak 4.x on Flathub: UNVERIFIED (page showed 3.7.8).
- Sandbox folder access list: UNVERIFIED (page showed none). If a folder is invisible, use Flatseal to add it, or move files to Documents or Downloads.
- A commenter says Flathub builds of Muse-era Audacity set a "disable networking" flag. COMMUNITY (LWN comment; may not apply now)
### Option B: Official AppImage (4.0.1)
- Only official Linux download: AppImage, x86_64 and ARM64. Needs FUSE 2. ARM64 build has no plugins. VERIFIED (download/linux)
- Team tests on Ubuntu 22.04. 4.0.1 fixed the AppImage failing to start on some distributions. VERIFIED (download page, release 4.0.1)
- Good for: Audacity 4 with the newest fixes. Not sandboxed, so folders just work. 
- Steps: 1) download the file; 2) move it to ~/Applications; 3) right-click, Properties, Permissions, tick Is executable; 4) double-click.
- FUSE 2 present on Bazzite: UNVERIFIED. If it will not start, tell Claude the exact error.
- Updates are manual: download the new file. INFERENCE.
### Which one
- Want macros: Flatpak 3.7.8. Want Audacity 4: AppImage. Try both side by side; projects differ (.aup3 vs .aup4), so copy files first.
- Do not open the same project in 4.0 and then expect 3.x to read it. VERIFIED (release notes)

## 4. Best for
- Quick waveform edits, trims, fades, format conversion, simple restoration, spectrogram inspection.
- Not a mastering suite. DDP or CD-master workflow: UNVERIFIED (not searched).
- Hard dance kick and sample prep: yes, section 10.

## 5. Plugins and effect chain
- Effects apply one at a time to a selection. A chain needs a macro (3.x only). VERIFIED (manual macros)
- Presets work across built-in, destructive and realtime effects in 4.0. VERIFIED (changelog)
- Generated controls appear when a plugin has no own UI (4.0). VERIFIED (changelog)
- VST3 setting changes used to revert at playback start; fixed in 4.0.1. VERIFIED (release 4.0.1)

## 6. Macros, batch and Nyquist
- Macros (3.x): Tools > Macro Manager, make a macro, Insert commands, set parameters. VERIFIED (manual)
- Warning: commands with no saved parameters use the last values from manual runs. VERIFIED (manual)
- Batch: Tools > Apply Macro > Palette, pick macro, Apply Macro to > Files. Files in one folder, about 500 at once. VERIFIED (manual)
- Output: set in Directories Preferences; else a macro-output folder in Documents. VERIFIED (manual)
- Export or import a macro as TXT in Macro Manager. VERIFIED (manual)
- Audacity 4 adds multiple export (each track or label to its own file). VERIFIED (release 4.0.1)
- Nyquist is Lisp-based; Audacity uses a subset; plugins are .ny files. VERIFIED (manual nyquist)
- Nyquist Prompt and .ny install steps: UNVERIFIED (not on the page read).
- Scripting pipe (mod-script-pipe) is not in 4.0. VERIFIED (changelog)

## 7. Loudness and export
- 3.x: Effect > Volume and Compression > Loudness Normalization. Default perceived loudness -23 LUFS (EBU); RMS default -20 dB. VERIFIED (manual)
- Leave "Normalize stereo channels independently" off. "Treat mono as dual-mono" is on by default. VERIFIED (manual)
- Do it as the last editing step before export. VERIFIED (manual)
- Limiter: Effect > Volume and Compression > Limiter. Presets Master Limiter (to -1 dB), SFX Limiter, VO Limiter. VERIFIED (manual)
- Streaming LUFS targets: not on pages read. UNVERIFIED. Ask which service.
- A true-peak or LUFS meter to check the result: UNVERIFIED. Re-import the export and check it.
- Menu locations in 4.x: UNVERIFIED.

## 8. Spectral editing
- Track dropdown, Spectrogram. Turn on Enable Spectral Selection in Spectrograms Preferences. VERIFIED (manual)
- Drag to select frequency and time. Q toggles the last selection. VERIFIED (manual)
- Effect menu: Spectral Delete, Spectral edit multi tool, parametric EQ, shelves. VERIFIED (manual)
- Best for one steady tone like 50 Hz hum. VERIFIED (manual)
- Spectrogram settings: window size, window type (Hann default), scales (linear, log, Mel, Bark, ERB), algorithms. VERIFIED (manual)
- 4.0 has a redesigned, faster spectrogram. Spectral effects in 4.0: UNVERIFIED.

## 9. Common problems
- Back up the .aup3 before opening in 4. 4.0.0 had a corruption bug after a failed save; fixed in 4.0.1. VERIFIED
- Non-ASCII file names failed to open before 4.0.1. VERIFIED (release notes)
- "-9996 Invalid device" with input monitoring was fixed in 4.0.1. VERIFIED
- AppImage will not start: check FUSE 2, update to 4.0.1. VERIFIED (download page, release)
- Missing macro menu in 4: expected, see section 1. VERIFIED

## 10. Recipe: prepare a kick sample
Goal: a clean one-shot WAV. General practice, not from a fetched page. Menu names in 4.x: UNVERIFIED.
1. File > Import the kick. Zoom in on the start.
2. Select silence before the hit and delete it. The hit starts at the first wave.
3. Select the dead tail at the end and delete it.
4. Select the last few milliseconds and apply Fade Out so the end does not click.
5. Apply Limiter, preset Master Limiter (peaks stay under -1 dB). VERIFIED preset.
6. Play it. Clicks at the start or end: undo and move the cut.
7. File > Export as WAV, 24-bit if offered. Name it Kick_Hard_F.wav.
8. Do not use LUFS on a one-shot; check peak level. General knowledge, UNVERIFIED.
9. For many kicks, 3.7.x: build a macro with Fade Out and Limiter, then Apply Macro to Files.

## 11. Alternatives on Linux
- Tenacity: free open-source multi-track editor, Windows, macOS, Linux, BSD; builds on Codeberg; no version stated. VERIFIED (tenacityaudio.org)
- Ardour: hosts VST2, VST3, AU, LADSPA, LV2; non-destructive editing, region gain, fades. VERIFIED (ardour.org/features). OS list and price: UNVERIFIED.
- ocenaudio and Kwave: pages blocked or not read. UNVERIFIED. Do not recommend features.

## Not verified
- Licence text; plugin folders per OS; FUSE 2 on Bazzite; Flatpak sandbox access; Flatpak 4.x.
- Missing effects and exports in 4.0; menu names in 4.x; spectral effects in 4.x; Nyquist install steps.
- Audio host choice on Linux; DDP or CD support; ocenaudio, Kwave, Ardour OS and price.
- Reddit (blocked) and forum.audacityteam.org (title only).

## Sources (fetched)
- audacityteam.org: download, download/windows, download/mac, download/linux, blog, changelog, changelog/4.0.0
- github.com/audacity/audacity/releases and tag Audacity-4.0.1; flathub.org/apps/org.audacityteam.Audacity
- manual.audacityteam.org: macros, loudness_normalization, spectral_selection, spectrogram_view, nyquist, limiter
- linuxiac.com 4.0.1 article; lwn.net/Articles/1092439/; tenacityaudio.org; ardour.org/features.html
- wine-proton-bottles skill (Bazzite software sources, from docs.bazzite.gg)
