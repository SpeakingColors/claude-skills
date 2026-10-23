---
name: wavelab
description: Use when helping with Steinberg WaveLab 13 (Pro or Elements) in 2026, covering editions, prices, Windows/macOS, Bazzite via Bottles, Master Section, batch, loudness, spectral editing, CD/DDP.
---

# Steinberg WaveLab 13 (Pro and Elements, 2026)

Labels: VERIFIED (source) = read on a page I fetched. COMMUNITY = user report, not official. UNVERIFIED = not confirmed; do not rely on it.
Rule for Claude: Assume the reader is not a programmer. Plain words first, then one exact step. One change at a time, ask the reader to test, then continue. Say clearly at the start that WaveLab has no Linux version.
13.0 manual pages loaded mostly as index pages; "v11" or "v12" marks older manuals whose menus may have moved. Reddit was blocked. A fetch limit ended research early, so Steinberg activation pages were not read.

## 1. Versions and prices
- WaveLab 13 is current. Article dated 29 Jan 2026 (date from URL). VERIFIED (synthtopia.com)
- Pro 13: 499.99 USD / 499 EUR. Elements 13: 99.99 USD / 99.99 EUR. Upgrades exist. VERIFIED (synthtopia, Plugin Boutique)
- UK download prices: Pro 422 GBP, Elements 81 GBP incl. VAT. VERIFIED (Thomann UK)
- Perpetual licence, up to 3 simultaneous activations, online activation needed. VERIFIED (Thomann UK)
- New in 13: Dolby Atmos mastering, multicore rendering, sidechain, MasterRig 2, VocalChain, Pitch Shifter, UltraShaper. VERIFIED (Sound On Sound, Plugin Boutique)

## 2. Platforms
### Windows
- Windows 11 (24H2 or later) or 64-bit Windows 10 (22H2 or later). Intel i5 8th gen or Ryzen 3000, 4+ cores, 8 GB RAM. VERIFIED (Plugin Boutique)
- 1920x1080 display, 4 GB free disk, internet for install and activation. VERIFIED (Thomann UK)
- Audio driver: ASIO hardware recommended for low latency. VERIFIED (Plugin Boutique)
- Plugins: VST3 (64-bit) and ARA only. No VST2, no AU. VERIFIED (Thomann UK)
- VST3 folder: C:\Program Files\Common Files\VST3 is the usual place. UNVERIFIED (general knowledge).
- WaveLab 13 crashed Windows during plugin scan in one forum thread; details not read. COMMUNITY (thread title only, UNVERIFIED cause)
### macOS
- Sources disagree: macOS 13 or later (Thomann), 15 or later (Sound On Sound), Tahoe/Sonoma/Sequoia (Plugin Boutique). Check steinberg.net.
- Intel i5 late 2018 or Apple silicon (native app or Rosetta 2); Metal graphics. VERIFIED (Plugin Boutique)
- Audio: Core Audio is the system driver. UNVERIFIED for WaveLab. VST3 folder /Library/Audio/Plug-Ins/VST3: UNVERIFIED.
### Linux
- No native build. Nothing official on Wine.
- Old report: WaveLab 6 locked up under Wine with more than one VST; marked fixed May 2022. COMMUNITY (WineHQ bug 51376)
- WaveLab 13 under Wine or Bottles: UNVERIFIED. See section 11.
### Licensing
- Steinberg activation is online. Whether eLicenser or the Steinberg Licensing app is used for 13: UNVERIFIED (pages not read). A forum thread titled "Cannot activate new purchase of wavelab elements" exists. COMMUNITY (title only)

## 3. Pro or Elements
- Pro 13: Audio Editor, Audio Montage, Batch Processor, Dolby Atmos, full spectral editor, loudness control, CD and DDP editing, 384 kHz, 64-bit, unlimited tracks. VERIFIED (Thomann UK, Plugin Boutique)
- Elements 13: stereo to 96 kHz, 3 audio tracks, MasterRig, RestoreRig, batch processing, spectrogram view, audio CD burning, 25+ VST3 effects. VERIFIED (Thomann UK)
- Elements: no DDP, no DVD, no surround. VERIFIED (Thomann UK)
- Elements and Pro montages are not compatible. COMMUNITY (Steinberg forum)
- WaveLab 9 thread: Elements had no spectrum editing; loudness analysis and normalizer were Pro only. COMMUNITY, 2016, may have changed.
- Plugin Boutique lists spectral editing for Elements 13; Thomann lists only a spectrogram view. Conflict: UNVERIFIED.
- Official comparison table did not load. UNVERIFIED.

## 4. Best for
- Mastering, restoration, analysis, album assembly, CD and DDP delivery. VERIFIED (Thomann UK)
- Batch work, loudness and true-peak normalization. VERIFIED (Thomann UK)

## 5. Plugins and effect chain
- Master Section is the last block before hardware, file or meters: level, effects, resample, dither. VERIFIED (steinberg.help 13.0)
- Bundled: MasterRig 2, Bass Manager, MixerDelay, SuperVision, VocalChain, UltraShaper. VERIFIED (Thomann, Sound On Sound)
- Dither goes in the final slot of the Master Section. Lin Dither may need enabling in Preferences > Plug-ins. COMMUNITY (forum, v12)
- Plug-ins can be removed by dragging them out of the slot (13). VERIFIED (Sound On Sound)

## 6. Batch and scripting
- Batch Processor handles any number of audio or montage files with Master Section plug-ins, presets and offline effects. VERIFIED (steinberg.help 13.0)
- It can change format, rename by rule, add metadata, run an app when done, use several cores. VERIFIED (v12 manual)
- Example: normalize 24-bit files, fade out, dither to 16-bit 44.1 kHz; save as a batch processor file. VERIFIED (v12)
- Easy start (v11): in the Master Section right-click Render, Create Batch Processor from Settings. VERIFIED (v11)
- Open or create from the Startup Assistant. VERIFIED (13.0 table of contents)
- Scripting or macros: not found on pages read. UNVERIFIED.

## 7. Loudness and export
- Loudness Normalizer (v11): Loudness to Achieve (EBU R-128 is -23 LUFS), Reference, Peaks (digital or true), Max Peak Level, Softness. VERIFIED
- Reference: whole file, top of loudness range, or maximum short-term. VERIFIED (v11)
- Keep Remove DC Offset on. "Warn If Unmatched" does not work in batch. VERIFIED (v11)
- Very high targets can distort because the limiter runs out of room. VERIFIED (v11)
- 13 adds loudness and true-peak normalization across ADM files. VERIFIED (Sound On Sound)
- Streaming LUFS targets: UNVERIFIED. Ask which service.
- Audio Montages can be written to audio CD or a DDP image. VERIFIED (v12 meta text; steps not read)
- DDP is Pro only. VERIFIED (Thomann; Steinberg forum)

## 8. Spectral editing (Pro)
- Audio Editor > Spectrum tab. Tools: Rectangle, Lasso, Brush, Magic Wand, Time Selection. VERIFIED (v12)
- Playback: Regular, Solo Selection, Mute Selection. VERIFIED (v12)
- Audio Inpainting: 1) Spectrum tab; 2) pick a selection tool; 3) draw around the problem; 4) right-click Audio Inpainting to adjust; 5) click it. VERIFIED (v12)

## 9. Common problems
- Lin Dither missing in the Master Section: see section 5. COMMUNITY
- Elements montage opens as a File Group in Pro. COMMUNITY
- macOS version confusion: section 2.
- Plugin scan crash on Windows: COMMUNITY, cause UNVERIFIED.

## 10. Recipe: prepare a kick sample
General practice; dialog names from v11/v12 where marked.
1. Open the kick in the Audio Editor. Zoom into the start.
2. Select silence before the hit and delete it.
3. Delete the dead tail. Fade out the last few ms. Fade tool location: UNVERIFIED.
4. Loudness Normalizer suits full tracks; for a one-shot use a peak normalize. Tool name: UNVERIFIED.
5. Optional: Spectrum tab, Rectangle selection, Solo Selection to find rumble. VERIFIED tools.
6. Master Section final slot: Lin Dither only if reducing bit depth.
7. Render to WAV 24-bit. Render dialog: UNVERIFIED.
8. Many kicks: right-click Render, Create Batch Processor from Settings, add files.

## 11. Run it on Linux (Bottles) for a non-programmer on Bazzite
Honest status: UNVERIFIED that WaveLab 13 works. Test a trial first. A Steinberg trial for Pro 12 and 13 existed per a forum post. COMMUNITY. Do not buy before the TEST passes.
Bottles facts come from the wine-proton-bottles skill (Bottles and Bazzite docs).
1. Install Bottles from Bazaar or Flathub. VERIFIED
2. Give Bottles one folder only, for the installer: `flatpak override --user --filesystem="/home/USER/Downloads" com.usebottles.bottles`. Restart Bottles. VERIFIED
3. Create bottle: name WaveLab, environment Software, runner Caffe. VERIFIED
4. Dependencies: add .NET and Visual C++ runtimes one at a time; read the list for names. UNVERIFIED names.
5. Installer: Steinberg uses a download assistant on Windows. Whether it runs under Wine: UNVERIFIED. Use the offline installer from the account if offered.
6. Run the setup .exe via Run executable. Black screen: copy the folder into C: with Browse C: and retry. VERIFIED
7. WaveLab needs 64-bit Windows, a 1920x1080 screen and Windows 10 22H2 or later. Set the bottle Windows version to Windows 10 in bottle settings. VERIFIED requirement; setting location UNVERIFIED.
8. Licence: online activation, 3 machines. Activation may fail under Wine. eLicenser/Steinberg Licensing behaviour on Linux: UNVERIFIED.
9. Audio: WineASIO is an ASIO driver for JACK; PipeWire can serve it. COMMUNITY. A Bottles Flatpak recipe: UNVERIFIED. Wine's own driver is the fallback: UNVERIFIED.
10. WaveLab hosts VST3 only. Linux VST3 plugins will not load in Wine; use Windows VST3 inside the bottle. Bridging with yabridge does not work with Flatpak DAWs. VERIFIED (skill)
11. Triage one change at a time: Vaniglia runner, toggle DXVK, run Bottles from a terminal and read ERROR lines. VERIFIED
12. Backup: full backup in Bottles, and Duplicate the bottle as a template before changes. VERIFIED

TEST checklist (report each):
- Installer ends cleanly; activation or trial start works.
- Main window opens at correct size; menus draw properly.
- Open a WAV, zoom to sample level, play with sound.
- Master Section opens; add a plugin; render a file.
- Batch Processor runs on 3 files.
- Spectrum tab draws and Audio Inpainting runs (Pro).
- Plugin scan finishes without a crash.
- Close and reopen; settings kept.
Known problems: old Wine crash with several VSTs (fixed 2022 for v6); plugin scan crash on Windows in 13; activation unknown. COMMUNITY
Prefix backup folder: `~/.var/app/com.usebottles.bottles/data/bottles`. VERIFIED
Avoid `rpm-ostree install wine` as a first move. VERIFIED

## 12. Linux alternatives
- Audacity: native, see the audacity skill. VERIFIED
- Ardour: VST2, VST3, AU, LADSPA, LV2 hosting. VERIFIED (ardour.org/features). OS and price: UNVERIFIED.
- Tenacity: free open source, Windows/macOS/Linux/BSD. VERIFIED (tenacityaudio.org)
- ocenaudio, Kwave: not read. UNVERIFIED.
- No sourced Linux tool matches WaveLab mastering, DDP, or Master Section. UNVERIFIED (not searched widely).

## Not verified
- Steinberg activation system for 13; macOS minimum; Pro vs Elements official table; Elements spectral editing.
- WaveLab 13 under Wine; WineASIO recipe; installer behaviour; plugin folders; Core Audio details.
- 13.0 manual pages for loudness, spectrum, dither, CD/DDP steps; scripting.
- Streaming targets; Reddit (blocked); ocenaudio, Kwave, Ardour OS and price.

## Sources (fetched)
- synthtopia.com (WaveLab 13); soundonsound.com/news/steinberg-release-wavelab-13
- thomann.co.uk steinberg_wavelab_pro_13 and elements_13; pluginboutique.com 16675 and 16676
- steinberg.help/r/wavelab-pro/13.0 batch_processing_c, master_section_c
- archive.steinberg.help wavelab_pro v11 (loudness normalizer, master section batch), v12 (batch, spectrum tab, inpainting, audio_montage_write)
- forums.steinberg.net threads 661335, 1040135, 985672; winehq.org wine-bugs 2022-May/574421
- ardour.org/features.html; tenacityaudio.org; wine-proton-bottles skill
- Search result titles only (not read): Steinberg forum threads 1034166 and 1035805
