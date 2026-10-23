---
name: sound-forge
description: Use when helping with Sound Forge (Boris FX, formerly MAGIX) 2026, covering editions, prices, Windows-only status, trying it on Bazzite via Bottles, batch, scripting, restoration and loudness.
---

# Sound Forge (Boris FX, 2026)

Labels: VERIFIED (source) = read on a page I fetched. COMMUNITY = user report, not official. UNVERIFIED = not confirmed; do not rely on it.
Rule for Claude: Assume the reader is not a programmer. Plain words first, then one exact step. One change at a time, ask the reader to test, then continue. Say clearly at the start that Sound Forge has no Linux version.
Reddit was blocked. A web fetch limit ended my research early, so MAGIX/Boris system requirements and licence pages were not read.

## 1. Owner and names
- Boris FX bought Sound Forge, Vegas Pro and Acid Pro from MAGIX, announced 30 Mar 2026. VERIFIED (blog.borisfx.com)
- Sound Forge stays a standalone app, integrates with Vegas Pro, included in Vegas Pro Ultimate. VERIFIED (same post)
- 2026 names: Sound Forge and Sound Forge Plus; help is "Sound Forge Pro 2026 Online Help". VERIFIED (Boris FX help, Thomann)
- Older MAGIX names (Pro 18, Pro Suite 18, Audio Studio 17) are the previous generation. VERIFIED (magix.com UK page, jumbled)
- 2026 version number: UNVERIFIED.

## 2. Editions and prices
- Sound Forge: $24.95/month, $149.95/year, $189.95 upgrade and support, $299.95 perpetual. VERIFIED (Boris FX post)
- Sound Forge Plus: $33.95/month, $199.95/year, $249.95 upgrade, $399.95 perpetual. VERIFIED (same post)
- Plus adds Melodyne 5 Essentials, Vandal, VariVerb II, 3D Reverb. VERIFIED (vegascreativesoftware.com pricing)
- Thomann UK: 265 GBP incl. VAT, perpetual, one simultaneous activation. VERIFIED (thomann.co.uk)
- MAGIX owners can upgrade at one price until 5 Dec 2026. VERIFIED (Boris FX post)
- Free trial: 15 days, full version. VERIFIED (vegascreativesoftware.com)
- Old MAGIX UK prices (Pro 18, 199 GBP) are outdated. VERIFIED but superseded.

## 3. Platforms
### Windows
- Windows 10 (64-bit) or later. AMD or Intel CPU, 2 GB RAM, 2 GB disk, ASIO interface for recording. VERIFIED (Thomann UK)
- Older MAGIX page: Windows 10 and 11, 512 MB RAM minimum, one-time registration, internet to validate. VERIFIED (magix.com specifications, older version)
- Audio driver path: ASIO is listed as required hardware on Windows. VERIFIED (Thomann UK). WASAPI: UNVERIFIED.
- Plugins: VST2 and VST3 hosting, plus ARA. No AU. VERIFIED (Thomann UK). Folder paths: UNVERIFIED.
- Licence: perpetual or subscription, online activation, one activation at a time. VERIFIED (Thomann UK, Boris FX post)
### macOS
- Mac OS is not supported by the 2026 product. VERIFIED (Thomann UK)
- A separate Sound Forge Pro Mac line existed (Mac 3). Its 2026 status: UNVERIFIED.
- AU hosting not supported. VERIFIED (Thomann UK)
### Linux
- No native build. Nothing official on Wine.
- Sound Forge Pro 17 and 18 gave Error 57 at startup in Wine 9.0 RC4 and Bottles on Linux Mint; nobody got it working; thread locked. COMMUNITY (forum.winehq.org p=146214)
- Suspected cause: failed link to registration servers. COMMUNITY, secondhand, unconfirmed.
- The 2026 version under Wine: UNVERIFIED. Treat it as "probably not working" until a trial proves otherwise.

## 4. Best for
- Sample-level editing, peak and loudness metering, restoration, batch conversion. VERIFIED (vegascreativesoftware.com, Thomann)
- Restoration: DeHisser, DeClicker, DeCrackler, DeClipper, Noise Reduction. VERIFIED (same)
- Mastering aid: Wave Hammer 2.0 for dynamics and loudness. VERIFIED (vegascreativesoftware.com)
- Up to 32 channels, 384 kHz, 64-bit, event-based non-destructive mode, WaveColor display. VERIFIED (Thomann UK, vegascreativesoftware.com)
- Automatic record start with pre-record buffer. VERIFIED (same)
- DDP: Wikipedia lists DDP export for the product line. 2026 edition: UNVERIFIED. CD writing: UNVERIFIED.

## 5. Plugins and effect chain
- Process menu: Normalize, Fade, EQ, Resample, Bit-Depth Converter, Time Stretch, Auto Trim/Crop, Channel Converter, DC Offset. VERIFIED (Boris FX help, applying_effects)
- Effects menu: Dynamics, Noise Gate, Pitch, Reverb, Wave Hammer, DeClicker/DeCrackler, DeClipper, DeHisser. VERIFIED (same)
- Apply an effect: select audio (no selection means whole file), choose command, pick preset, Preview, OK. VERIFIED (same)
- Plug-in Manager organizes favorites and chains in the FX Plug-Ins menu. How to build a chain: UNVERIFIED.

## 6. Batch and scripting
- Tools > Batch Converter. Add files or a folder (top level only), pick or build settings, click Run Job. VERIFIED (Boris FX help, Pro)
- Settings: effect chain with presets, metadata (overwrite or keep), watermark, several export formats at once, output folder and name suffix. VERIFIED (same)
- Presets cannot be edited in place; delete and re-save. Up to 16 presets in the Explorer context menu. VERIFIED (same)
- Scripting: JScript, VBScript or C#, or compiled DLL. View > Script Editor; ready scripts at Tools > Scripting. VERIFIED (scripting overview)
- The Batch Converter is built with scripting. Scripting in the non-Pro edition: UNVERIFIED.

## 7. Loudness and export
- Peak and loudness metering are listed for both editions. VERIFIED (vegascreativesoftware.com)
- Statistics dialog (Tools toolbar) analyzes audio. VERIFIED (Boris FX help)
- Pro 11/12 users read integrated, short-term, momentary loudness and true peak via Statistics. COMMUNITY (Vegas forum 112342)
- Those users say the meter only measures; you set gain yourself. COMMUNITY
- 2026 Normalize with a LUFS target: UNVERIFIED. Treat it as peak or RMS.
- Batch export formats named: WAV, MP3, FLAC. VERIFIED (vegascreativesoftware.com)

## 8. Spectral editing
- Spectrum analysis or spectral editor in 2026 help: UNVERIFIED.
- Repair tools: Interpolate, Replace, Copy Other Channel; Crossfade Loop and Sampler dialogs. VERIFIED (Boris FX help, Tools toolbar)
- Older Pro editions bundled SpectraLayers Elements 9 (Pro) or SpectraLayers Pro (Pro Suite). VERIFIED for 17/18. 2026: UNVERIFIED.

## 9. Run it on Linux (Bottles) for a non-programmer on Bazzite
Honest status: UNVERIFIED that it works. Always test the free 15-day trial first, never buy first. VERIFIED trial.
Source of the Bottles facts below: wine-proton-bottles skill (Bottles and Bazzite docs).
1. Install Bottles from Bazaar or Flathub (Flatpak). VERIFIED
2. Put the installer in one folder, for example ~/Downloads. Give Bottles that folder only: `flatpak override --user --filesystem="/home/USER/Downloads" com.usebottles.bottles`. Restart Bottles. VERIFIED
3. In Bottles click Create. Name: SoundForge. Environment: Software. Runner: Caffe. VERIFIED
4. One program per bottle. Do not share this bottle. VERIFIED
5. Dependencies: look in the Dependencies list for .NET and Visual C++ runtimes, install one at a time. Exact names: UNVERIFIED, read the list.
6. Run the installer: Programs, Add shortcut or Run executable. Choose the Sound Forge setup .exe.
7. If the installer shows a black screen, copy the installer folder into the bottle with Browse C: and run it from there. VERIFIED
8. Launch from Programs. If Error 57 appears, that matches the failed thread: stop here and see step 12. COMMUNITY
9. Audio: WineASIO is an ASIO driver for JACK; PipeWire's JACK layer can serve it. COMMUNITY. A recipe for the Bottles Flatpak is UNVERIFIED; do not invent one.
10. Fallback audio is Wine's own driver (higher latency): UNVERIFIED. Use only for editing, not recording.
11. Licence caveat: Sound Forge needs one-time online registration. It may fail under Wine. Sound Forge uses Boris FX/MAGIX activation; eLicenser is not mentioned in sources read. VERIFIED (older MAGIX page; Thomann) / UNVERIFIED for 2026.
12. Triage, one change at a time: try Vaniglia runner, toggle DXVK off, run Bottles from a terminal and read ERROR lines. VERIFIED
13. Backup: Bottles > bottle > Full backup before experiments, and Duplicate the bottle as a template. VERIFIED

TEST checklist (tick each, report results):
- Installer finished without error. Activation or trial start works.
- App opens and shows the main window at the right size.
- Open a WAV, zoom in to sample level, play it, hear sound.
- Apply Fade and Normalize; undo works.
- Batch Converter runs on 3 files and writes output.
- Load a VST3 plugin; scan does not crash.
- Close and reopen; settings remembered.
- Record 10 seconds if an input is needed (expect problems).
Known problems: Error 57 (above); WineASIO not set up for Flatpak; Windows plugins need a Windows path inside the bottle.
Prefix backup folder: `~/.var/app/com.usebottles.bottles/data/bottles`. VERIFIED
Do not install Wine system-wide with rpm-ostree as a first move. VERIFIED

## 10. Linux alternatives
- Audacity: native on Linux, see the audacity skill. VERIFIED
- Ardour: VST2, VST3, AU, LADSPA, LV2 hosting, non-destructive editing. VERIFIED (ardour.org/features). OS and price: UNVERIFIED.
- Tenacity: free open source, Windows/macOS/Linux/BSD. VERIFIED (tenacityaudio.org)
- ocenaudio, Kwave: not read. UNVERIFIED.
- Honest take: for kick prep on Bazzite, Audacity is enough; Sound Forge is for a Windows machine.

## 11. Common problems
- Error 57 on Linux. COMMUNITY
- Activation needs internet. VERIFIED
- Add Folder in Batch Converter skips subfolders. VERIFIED

## 12. Recipe: prepare a kick sample (Windows)
General practice; menu names from the Boris FX help list unless marked.
1. File > Open the kick. Zoom in on the start.
2. Select silence before the hit and delete it.
3. Select the dead tail and delete it.
4. Select the last 5 to 20 ms. Process > Fade, Fade Out. Settings: UNVERIFIED.
5. Process > Normalize, Peak, about -1 dB. Mode names: UNVERIFIED.
6. Play it; check start and end for clicks.
7. File > Save As: WAV, 24-bit. Template names: UNVERIFIED.
8. Many kicks: Tools > Batch Converter with Fade and Normalize, then Run Job.

## Not verified
- 2026 version number; Boris/MAGIX system requirements page; Mac status; subscription terms.
- Wine, Bottles or Proton result for the 2026 version; WineASIO recipe; licence server behaviour.
- LUFS normalize, spectral editor, DDP and CD in 2026; plugin folders; WASAPI.
- Reddit (blocked); MAGIX forum; ocenaudio, Kwave, Ardour OS and price.

## Sources (fetched)
- blog.borisfx.com press post; vegascreativesoftware.com /sound-forge/ and /pricing/
- cdn.borisfx.com Sound Forge 2026 help: scripting overview, the batch converter, applying_effects, the_tools_toolbar
- thomann.co.uk/boris_fx_sound_forge.htm; magix.com/gb/sem/sound-forge-pro version-comparison and specifications
- forum.winehq.org p=146214; vegascreativesoftware.info forum 112342; en.wikipedia.org/wiki/Sound_Forge
- ardour.org/features.html; tenacityaudio.org; wine-proton-bottles skill (Bottles docs, Bazzite docs)
