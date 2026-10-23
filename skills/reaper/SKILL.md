---
name: reaper
description: Use when helping with REAPER (Cockos) 7.x, covering licensing, native Linux install on Bazzite, audio backends, plugin formats, yabridge, scripting, routing, sidechain and testing your own plugins.
---

# REAPER 7.x (Linux, hard dance)

## How to work with the reader
- Assume the reader is not a programmer. Plain words first, then one exact step.
- One change at a time, ask the reader to test, then continue.
- Labels: VERIFIED (source) = read on a fetched page; COMMUNITY = forum or user report; UNVERIFIED = not read, never guess.
- Fetch status: forum.cockos.com and stash.reaper.fm were not readable (JS check, robots). Reddit was blocked. The REAPER user guide PDF came back as binary. Cockos wiki pages on templates, custom actions and themes failed.

## Version and licensing
- Current: REAPER 7.82, released 4 Oct 2026. VERIFIED (reaper.fm/download.php).
- Discounted license: 60 USD. Commercial license: 225 USD. Prices exclude VAT and local tax. VERIFIED (reaper.fm/purchase.php).
- Discounted is allowed for: personal use only; individuals or businesses earning up to 20,000 USD gross per year with REAPER; educational or non-profit. Everyone else needs commercial. VERIFIED.
- Evaluation: 60 days, full function, no strings. VERIFIED.
- A new license includes free upgrades through version 8.99. One key can sit on several computers if used on only one at a time. Purchases are final. VERIFIED.
- Only one version of REAPER exists, so there are no editions. VERIFIED (purchase page).

## Platforms (Windows, macOS, Linux)
- Windows: 7.82 installers for x64 (17 MB), x86 and Windows 11 ARM (arm64ec, beta). Page says XP through Windows 11. VERIFIED (download page).
- macOS: Universal dmg (Intel and ARM64, recommended for 10.15 and later), Intel x86_64 and i386 dmgs. Page says macOS 10.5 through 26. VERIFIED.
- Linux: tarball for x86_64, i686, aarch64, armv7l (see Install on Bazzite). VERIFIED.
- Licence is the same on all three: one key, one version of REAPER, prices above. VERIFIED (purchase page).
- Audio path, Windows: Preferences > Audio > Device. Default is Wave Out; ASIO is recommended for best performance; the ASIO config button opens the driver panel. VERIFIED (Cockos wiki). WASAPI, ReaASIO and ASIO4ALL: UNVERIFIED (not on pages read).
- Audio path, macOS: Core Audio. UNVERIFIED (not on pages read).
- Audio path, Linux: ALSA, JACK, PulseAudio; on Bazzite use JACK mode via pipewire-jack (see Audio backends).
- Plugin folders: Linux ~/.vst, ~/.vst3, ~/.lv2, ~/.clap (VERIFIED). Windows and macOS folders: UNVERIFIED here.
- Formats: VST, VST3, LV2, AU, CLAP, DX, JS. AU is macOS only and DX Windows only. AU and DX placement UNVERIFIED; homepage lists the formats only.
- Windows plugins on Linux: yabridge (see Plugin formats). Running the Windows REAPER under Wine or Bottles: no source read, so UNVERIFIED and not advised; the native build exists.
- Cross-platform projects: Linux copy and paste across REAPER instances added in 7.54. VERIFIED (changelog). Moving projects between OSes: UNVERIFIED; plugin names and paths may differ, so keep bridged plugins identical in name.

## Linux status
- Native Linux builds are offered for x86_64, i686, aarch64 and armv7l as .tar.xz. VERIFIED (download page).
- The old Cockos wiki calls the Linux builds "experimental/unsupported, use at your own risk". The wiki is dated; the download page now lists Linux as a normal platform. VERIFIED both.
- Linux fixes keep landing: 7.73 JACK realtime override for pw-jack users; 7.74 u-he drag/drop fix and XDG_DOCUMENTS_DIR; 7.78 plugins forwarding keystrokes; 7.81 GTK+ loaded by default; 7.82 GTK+ no longer loaded by default (only with IME on or an extension asking for it). VERIFIED (whatsnew.txt).
- 7.81 added dark theme auto-detect and the --no-gtk switch. VERIFIED.
- Tiling window manager tooltip fix: set gdk_borderless_are_override_redirect=1 in reaper.ini. VERIFIED (wiki, old page).

## Install on Bazzite (Fedora Atomic)
Three routes. Prefer route A.
- A. Tarball plus script (recommended). The tarball contains install-reaper.sh. It installs into the home folder or system wide, can add desktop support, and creates an uninstall script. VERIFIED (Cockos wiki). Bazzite is immutable, so choose the home-folder install. UNVERIFIED that the script runs unchanged on Bazzite; test it.
  1. Download reaper782_linux_x86_64.tar.xz from reaper.fm/download.php.
  2. Extract it into a new empty folder.
  3. Open a terminal in the extracted folder, run `./install-reaper.sh`, choose the home install.
  4. Start REAPER from the menu. Check Help > About for 7.82.
- B. Flathub app fm.reaper.Reaper, version 7.82. It is community packaged, not verified by Cockos. VERIFIED (Flathub page). Permissions were not listed on the page.
- COMMUNITY (Zorin forum): with the Flatpak, yabridge plugins showed "Failed to scan". The .sh install fixed that. The same user said JACK setup was automatic in the Flatpak and not in the .sh install.
- yabridge does not support Flatpak DAWs. VERIFIED (yabridge README).
- C. Distrobox with the tarball inside: UNVERIFIED, not tested; audio and GUI passthrough may bite.
- Portable mode: run from the extracted folder when a reaper.ini is present. VERIFIED (wiki).
- Realtime: wiki suggests rtprio 98 and memlock unlimited for low latency. VERIFIED (old page). On Bazzite use the groups from the linux-audio-production skill (realtime group on Fedora). UNVERIFIED for REAPER specifically.

## Audio backends on Linux
- REAPER offers ALSA, JACK and PulseAudio, plus ALSA raw MIDI and JACK MIDI. VERIFIED (wiki). PipeWire is not named on the wiki or in the 7.x changelog pages I read.
- PulseAudio needs no setup but latency is high. VERIFIED (wiki), COMMUNITY (Lemmy thread: latency too high).
- Best route on Bazzite (PipeWire system): use REAPER's JACK mode through pipewire-jack, and link ports with QjackCtl or qpwgraph. COMMUNITY (Lemmy thread). The 7.73 note about "pw-jack users" supports this. VERIFIED (changelog line), the exact settings key UNVERIFIED.
- Direct ALSA: a Lemmy poster said yabridge plugins worked only via ALSA, but then no other app could play sound. COMMUNITY. Avoid unless the card is exclusive on purpose.
- COMMUNITY: with JACK a user got a dummy output and an undetected MIDI kit; pavucontrol fixed some dummy output cases.
- The ALSA "RT priority" option needs rtprio rights. JACK may need rtprio and memlock. VERIFIED (wiki).
- A USB interface such as the RME Digiface USB: UNVERIFIED in REAPER. Plan: confirm in `aplay -l`, pick the card in REAPER, 48 kHz, buffer 256, lower only if stable.

## ReaInsert (hardware insert)
- ReaInsert sends a track out to hardware and back, with latency compensation. VERIFIED (RME forum thread).
- Setup (COMMUNITY, RME forum): 1) put ReaInsert on an empty track; 2) bypass the hardware and press Ping detect once; 3) record with "Record: Output / Latency Compensated".
- Loopback test (VERIFIED, reaper.blog): cable from an interface output to an input, ping detect, add the sample result to the input offset, ping again until 0. Mute speakers first.
- Fit for hardware synth audio, or outboard FX. UNVERIFIED on Linux; the sources never mention Linux.

## Plugin formats on Linux
- reaper.fm lists VST, VST3, LV2, AU, CLAP, DX and JS, with LV2 and CLAP on all platforms including Linux. VERIFIED (homepage).
- The Cockos wiki says LV2 is not supported. That page is older; trust the homepage.
- Paths: VST in ~/.vst, VST3 in ~/.vst3, LV2 in ~/.lv2, CLAP in ~/.clap. In Options > Preferences check VST, LV2 and CLAP paths, then rescan. VERIFIED (linuxgamecast article).
- CLAP in 7.x: factory presets (7.68), CLAP 1.2.7, CLAP_EVENT_IS_LIVE (7.80). VERIFIED (changelog).
- Windows plugins: yabridge. REAPER 7.12 is listed as fully working for VST2, VST3 and CLAP. Needs Wine Staging; Wine 9.22 and 10.x reportedly failed with yabridge 5.1.1 (tested on 9.21). Current status UNVERIFIED. VERIFIED (README).
- yabridge steps: `yabridgectl add "<plugin folder>"`, then `yabridgectl sync`. Output goes to ~/.vst3/yabridge and ~/.clap/yabridge. VERIFIED.
- REAPER and yabridge: drag and drop onto a plugin window may need the editor_force_dnd option. Enable "Allow complete unload of VST plug-ins" in the VST preferences. VERIFIED (README).
- Carla can host other formats. VERIFIED (wiki, old). See wine-proton-bottles and linux-audio-production skills for Wine setup.

## Extensions and scripting
- SWS/S&M Extension: v2.14.0 (7 Sept 2025), needs REAPER 5.982 or later, Linux builds for x86_64, i686, aarch64, armv7l as .tar.xz. VERIFIED (sws-extension.org).
- ReaPack: package manager for scripts, JSFX, extensions, themes. v1.2.6 (8 Sept 2025). Linux build is labelled beta; needs libcurl, libxml2, OpenSSL, SQLite3. Install: put the file in the UserPlugins folder of the resource path, restart. VERIFIED (reapack.com).
- Open the resource path via Options > Show REAPER resource path. VERIFIED (ReaPack page).
- ReaScript: EEL2 (built in), Lua 5.4 (built in), Python (install separately, enable in Preferences > Plug-Ins > ReaScript). API docs: Help > ReaScript documentation. VERIFIED.
- JSFX: text files in EEL2 that become plugins. Edit by saving under a new name so upgrades do not overwrite. VERIFIED.
- Custom actions (Action List macros), themes (ReaperThemeZip, ReaPack themes), project and track templates: menus and folders UNVERIFIED (wiki pages failed). Ask the reader to look in the Actions menu, and offer to check the REAPER user guide together.
- Script idea: mpl_Create ReaComp sidechain routing.lua via ReaPack automates sidechain routing. VERIFIED (reaper.blog mention).
- 7.82 added EnumThemeColors and better Get/SetThemeColor in ReaScript. VERIFIED.

## Routing and sidechain how-to (VERIFIED, reaper.blog and Cockos wiki)
1. Put ReaComp (or a JS compressor) on the bass or lead track.
2. Set the bass track channels to 4 (Track channels drop-down).
3. On the kick track, add a send to the bass track and set the send to channels 3/4.
4. In ReaComp, set Detector input to Auxiliary. For a JS effect, tick Side-chain (it uses 3/4 on its own). For a VST, pick 3/4 in the plugin's pin input box.
5. Play. The bass should duck on each kick.
- Shortcut: drag the kick routing button onto the ReaComp window, then set Auxiliary. VERIFIED (reaper.blog).
- Kick should send to the sidechain only. Untick its main send to the bass if the kick leaks in (UNVERIFIED detail).
- Folder tracks, FX chains (.RfxChain files in the FXChains folder; Linux case-sensitivity bug fixed in 7.71 VERIFIED), and track templates: UNVERIFIED beyond that.

## Rendering (VERIFIED, Cockos wiki Render page, which says it needs updating)
- Source: Master mix, Stems (selected tracks), or Add items to new tracks (pseudo-freeze).
- Bounds: Entire project, Loop selection, Custom.
- Defaults: WAV 44.1 kHz 24-bit. Also 16 bit, 32 bit float, AIFF, FLAC, MP3, OGG, WavPack, Wave64.
- Resample mode defaults to highest quality.
- Dither, normalise or limit, tails, render queue, online render: UNVERIFIED here.

## Controllers and Push
- Preferences > Control Surfaces > Add. Pick a mode, set MIDI in and out. VERIFIED (wiki). OSC is supported with .ReaperOSC pattern files in the config directory. VERIFIED (reaper.fm OSC page).
- Ableton Push 1, 2 and 3 are supported by DrivenByMoss (version 26.6.5, needs REAPER 7.55 or later). It has a Linux download (.tar.gz). VERIFIED (mossgrabers.de).
- Push 2 or 3 display and pads working under Linux: UNVERIFIED. Install steps are in the download's manual; read it together.
- Other listed controllers: Maschine, Komplete Kontrol, Launchpad, APC40, MPC, Fire, Mackie MCU. VERIFIED.
- Hardware synths as plain MIDI keyboards: UNVERIFIED in REAPER. Add them as MIDI inputs in Preferences > MIDI Devices.

## Hard dance workflow
Tempo ranges: hardstyle 150 to 160 BPM, UK hardcore 160 to 175, happy hardcore 165 to 180, trance 135 to 145. General genre knowledge.
1. Template: Kick, Rumble, Sub, Lead 1/2, Screech, Pluck, Vocal, FX, Drums, Risers. Save as a project template. UNVERIFIED menu; offer to find it together with the reader.
2. Kick: layer click, body and distorted tail. Render the distorted kick to a new track (Add items to new tracks) and EQ the bounce.
3. Rumble: kick tail, high-pass the body away, add reverb, low-pass near 150 to 250 Hz, sidechain it hard to the kick. Tune to the key.
4. Leads: supersaw plus mono saw, high-pass each at a different point, sub only on the sub track. Use any supersaw plugin.
5. Sidechain: use the section above. Duck rumble hard, leads lightly.
6. Mix bus: glue compression on groups, limiter last.
7. Arrangement: 16 or 32 bar blocks, risers and filter automation.
8. Stems for mastering: Render Stems with selected tracks.

## Test checklist for your own JUCE plugins
1. Copy VST3 to ~/.vst3 and CLAP to ~/.clap. Options > Preferences > Plug-ins, rescan, check the list.
2. Not found: read the scan messages. Common cause is a newer glibc than the host. Check `ldd`.
3. Preset recall: save project, reopen, parameters match.
4. Automation: record a parameter, check no zipper noise.
5. Sample rate change: 44.1, 48 and 96 kHz; no silence or crash.
6. Render offline and compare with a live bounce. Null test against the live bounce.
7. Latency: if the plugin reports lookahead, confirm REAPER compensates (PDC). Null test a delayed copy.
8. Duplicate the track and the FX chain; state and window size restore.
9. Run `pluginval` on the VST3 first (UNVERIFIED as REAPER step, standard JUCE practice).
10. Keyboard focus in plugin windows: 7.78 and 7.81 fixed several Linux focus bugs. If keys fail, check the version.

## Troubleshooting
- No sound: check Preferences > Audio device; with JACK mode confirm links in qpwgraph.
- Dummy output: pavucontrol or qpwgraph; COMMUNITY.
- Plugin "Failed to scan": Flatpak sandbox (COMMUNITY) or Wine mismatch. Move to the tarball install first.
- Strange UI glitches after update: 7.82 changed GTK loading; try `--no-gtk` or the reverse. UNVERIFIED which helps.
- Crash on a bridged plugin: test it alone in a new project; read yabridgectl status.

## Not verified
- PipeWire support in REAPER (no page names it); PipeWire-specific settings.
- Exact install-reaper.sh behaviour on Bazzite, and Flatpak permissions.
- A USB interface such as the RME Digiface USB in REAPER on Linux; ReaInsert on Linux.
- Push 2/3 display on Linux; hardware synths as MIDI keyboards.
- Templates, custom actions, themes, FX chain folders, render dither/limit/queue (pages unreadable).
- Wine 10.x status with yabridge today; REAPER user guide PDF contents.
- Core Audio, WASAPI, ASIO4ALL, Windows and macOS plugin folders, Wine/Bottles running Windows REAPER.
- Reddit and forum.cockos.com threads.

## Sources (fetched)
- https://www.reaper.fm/download.php
- https://www.reaper.fm/purchase.php
- https://www.reaper.fm/whatsnew.txt
- https://www.reaper.fm/
- https://www.reaper.fm/userguide.php
- https://www.reaper.fm/sdk/reascript/reascript.php
- https://www.reaper.fm/sdk/js/js.php
- https://reaper.FM/sdk/osc/osc.php
- https://www.cockos.com/wiki/index.php/REAPER_for_Linux
- https://www.cockos.com/wiki/index.php/Render
- https://www.cockos.com/wiki/index.php/Preferences_Audio_Device
- https://www.cockos.com/wiki/index.php/ASIO
- https://www.cockos.com/wiki/index.php/Preferences_Control_Surfaces
- https://www.cockos.com/wiki/index.php/Sidechaining_using_Reaper_or_Jesusonic
- https://flathub.org/apps/fm.reaper.Reaper
- https://www.sws-extension.org/
- https://reapack.com/
- https://github.com/robbert-vdh/yabridge
- https://www.mossgrabers.de/Software/Reaper/Reaper.html
- https://reaper.blog/2019/11/sidechain-2019/
- https://reaper.blog/2018/11/rec_latency_offset/
- https://forum.rme-audio.de/viewtopic.php?id=33861
- https://linuxgamecast.com/2023/08/reaper-on-linux-installing-plugins/
- https://lemmy.4d2.org/post/104631
- https://forum.zorin.com/t/getting-jack-to-work-with-non-flatpak-reaper/54086
- https://forum.zorin.com/t/flatpak-or-non-flatpak-reaper-with-midi-pipewire/54255
- https://www.linux-magazine.com/Issues/2022/257/Reaper
