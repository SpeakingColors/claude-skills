---
name: bitwig-studio
description: Use when helping with Bitwig Studio on Windows, macOS or Linux (Bazzite focus), covering install, Flatpak, plugin hosting, VST3/CLAP, yabridge, audio setup and testing your own JUCE plugins.
---

# Bitwig Studio (Windows, macOS, Linux; hard dance)

Verify against current docs before acting on anything marked UNVERIFIED.
Labels: VERIFIED = read in a fetched page (source named); COMMUNITY = forum or blog report; UNVERIFIED = from memory, not checked.
Last re-checked 2026-10-23. Related skills: linux-audio-production (PipeWire, realtime, xruns), wine-proton-bottles (yabridge and Wine details), bazzite-kde-linux.

## How to work with the reader
- Assume the reader is not a programmer. Plain words first, then the exact click path. One change at a time, ask the reader to test, then continue.
- Ask which version the reader runs (Help, About) before quoting menus.

## 1. Platforms

### Versions and editions (all platforms)
- Current download is Bitwig Studio 6.1.4 (VERIFIED, bitwig.com download page; Flathub shows "Changes in version 6.1.4", VERIFIED). 6.1 had a public beta in June 2026 (COMMUNITY, search result title, Sonic State; page not read).
- 6.0 went live 11 March 2026 (VERIFIED, Sound On Sound). See section 9 for what it added.
- 6.1 highlights: Sliced Sampler, root key analysis, Spectral and Fragments play modes, drag-and-drop Sampler creation, Tuner device (VERIFIED, 6.1 release notes).
- Editions: Essentials USD 99, Producer USD 199, Bitwig Studio USD 399 (VERIFIED, bitwig.com buy page). Only the full Studio edition has The Grid (VERIFIED, Bitwig "three flavors" story). Check the store for current prices.
- Each edition has more devices: Essentials 40, Producer 92, Studio 154 instruments and effects (VERIFIED, same story). Projects open across editions in player mode (VERIFIED).
- 12 months of updates are free with each purchase (Upgrade Plan). Upgrades between editions cost nothing extra (VERIFIED, buy page). 16-Track is no longer sold (VERIFIED, story).
- One installer covers all editions (VERIFIED, download page). Full content needs at least 26 GB free disk (VERIFIED).

### Windows
- Requirement: Windows 10 or 11, 64-bit. Installers for x86 64-bit and ARM 64-bit (VERIFIED, download page).
- Install: run the downloaded installer, sign in to your Bitwig account (UNVERIFIED steps).
- Audio: Bitwig has a WASAPI support page (COMMUNITY, search result title only, content not read). ASIO is the usual low-latency path on Windows (UNVERIFIED for Bitwig 6.1 menus).
- Plugin folders: Common Files VST3 and CLAP folders under C:\Program Files (UNVERIFIED, standard for the formats; yabridge README names the same Common Files layout inside a Wine prefix, VERIFIED).
- Licensing: license is registered automatically to your Bitwig account after purchase. Gift, EDU and tutorial licenses are not auto-registered (VERIFIED, buy page). How many computers a license covers: the buy page does not say (UNVERIFIED).

### macOS
- Requirement: macOS 12 (Monterey) or later (VERIFIED, download page). Apple Silicon versus Intel: not stated on the page (UNVERIFIED).
- Install: one macOS installer on the page (VERIFIED); drag to Applications is the usual flow (UNVERIFIED).
- Audio: Core Audio is the system driver (UNVERIFIED for Bitwig menus; standard for macOS).
- Plugin folders: /Library/Audio/Plug-Ins/VST3 and /Library/Audio/Plug-Ins/CLAP, plus the same under ~/Library for one user (UNVERIFIED, standard). Audio Unit support in Bitwig: UNVERIFIED, test before promising.
- Licensing: same Bitwig account as Windows (VERIFIED, buy page, account-based).

### Linux (native build)
- Requirement: Ubuntu 24.04 or later, or a modern distro with Flatpak (VERIFIED, download page). The 6.1 notes say the same and add that a Vulkan or GL compatible video driver is needed (VERIFIED).
- Two installers: Ubuntu DEB and Flatpak (VERIFIED, download page). No RPM is offered (VERIFIED by absence on that page).
- Audio: PipeWire support since Bitwig 4.3 (VERIFIED, Bitwig support page). PipeWire also allows several interfaces at once (VERIFIED, same page).
- Plugin folders: ~/.vst3, ~/.clap, ~/.vst (UNVERIFIED for Bitwig specifically; the yabridge README places bridged plugins in ~/.vst3/yabridge and ~/.clap/yabridge, VERIFIED).
- Licensing: same Bitwig account, no separate Linux license (UNVERIFIED, buy page lists no per-OS terms).

### Comparison (what differs)
- Windows: widest plugin choice, ASIO, no sandbox layer around Bitwig itself (UNVERIFIED).
- macOS: Core Audio, simplest audio setup (UNVERIFIED).
- Linux: native, but Windows plugins need yabridge, and yabridge does not work with the Flatpak (VERIFIED, yabridge README).
- Bitwig itself is the same program on all three. Projects move between systems. Plugin presence is what breaks: a project using a Windows-only plugin shows it missing on Linux (UNVERIFIED, expected behaviour).

## 2. Install on Bazzite (Fedora Atomic): Flatpak versus other

Recommended: Flatpak. Bazzite is immutable, so an Ubuntu DEB does not install directly (see bazzite-kde-linux).
1. Open Bazaar (or Discover) and search for Bitwig Studio, or use the Flathub page. App ID is com.bitwig.BitwigStudio (VERIFIED, Flathub page). It is marked proprietary, Medium Risk, Desktop Only (VERIFIED).
2. Terminal alternative: `flatpak install flathub com.bitwig.BitwigStudio` (UNVERIFIED exact command, standard Flatpak syntax).
3. Bitwig says Flatpak 1.1 or later is needed and permissions are pre-configured; change them with Flatseal (VERIFIED, Bitwig support page).
4. Sign in with your Bitwig account on first launch (VERIFIED, support page: "activate it ... on first launch").
5. Flatpak audio access: the manifest has --device=all and --filesystem=xdg-run/pipewire-0 (VERIFIED, from the linux-audio-production skill, Flathub manifest).

Other routes:
- Distrobox with Ubuntu 24.04 plus the DEB: UNVERIFIED, not tested. Reason to try it: yabridge needs a non-Flatpak DAW (VERIFIED limit). Audio and GUI passthrough in a distrobox are untested here.
- rpm-ostree layering: not possible for Bitwig, no RPM exists (VERIFIED by absence). Do not layer Wine to chase this (wine-proton-bottles, section 12).
- Do not run Bitwig under Wine. It is native (wine-proton-bottles, section 1).

## 3. Sandboxing: two different layers

1. Flatpak sandbox: limits what folders and devices Bitwig can see. Tool: Flatseal (VERIFIED, support page).
2. Bitwig plugin hosting mode: how isolated plugin processes are (VERIFIED, user guide). Dashboard, Settings tab, "Plug-in Hosting Mode".
   - Within Bitwig: a plugin crash can crash the audio engine.
   - Together: one shared plugin process; engine survives.
   - By manufacturer: grouped per maker.
   - By plug-in: instances of one plugin share a process.
   - Individually: one process per instance, most resources.
- A per-plugin list forces chosen plugins to Individually (VERIFIED). A mode change applies after reopening the project or reloading the audio engine (VERIFIED).
- Crashed plugin: Device Panel shows a notice; use Reload Plug-in or Reload All Plug-ins (VERIFIED).
- For plugins under development: set Individually, so a crash never loses the session (my recommendation).

## 4. Plugin formats, paths and Flatpak visibility
- Bitwig hosts VST3 and CLAP on Linux. VST2 in version 6: UNVERIFIED. CLAP is first-class in Bitwig (COMMUNITY, general; not on the pages read).
- Support page: install plugins as Flatpaks where possible; otherwise put them in a folder Bitwig can reach, such as your home directory. "Anything installed in /usr/lib won't be available" (VERIFIED, Bitwig support page).
- Flatpak plugin extension point org.freedesktop.LinuxAudio.Plugins, subfolders vst, vst3, clap, lv2, ladspa, runtime version must match (VERIFIED, linux-audio-production skill, Bitwig manifest 25.08).
- COMMUNITY (Fedora forum, earlier read): some users saw no plugins even from home paths. Page could not be re-fetched on 2026-10-23 (access prompt unanswered).
- Practical order for your own plugin, one step at a time:
  1. Copy the .vst3 folder into ~/.vst3 and the .clap file into ~/.clap (UNVERIFIED that the Flatpak sees both by default).
  2. In Bitwig, Dashboard, Settings, Locations: check the plugin folders and rescan (UNVERIFIED exact menu names in 6.1).
  3. If it does not appear, open Flatseal, select Bitwig Studio, add `~/.vst3` and `~/.clap` under Filesystem (UNVERIFIED sufficient).
  4. If still missing, read section 8 (scan failures).
- Keep release builds on an older glibc, or the plugin fails to load (COMMUNITY, JUCE forum: "GLIBC_2.38 not found").

## 5. Windows plugins on Linux: yabridge
Full recipe is in wine-proton-bottles section 8 and linux-audio-production section 10. Facts here, all from the yabridge README (VERIFIED):
- yabridge runs 32-bit and 64-bit Windows VST2, VST3 and CLAP plugins in 64-bit Linux hosts.
- It needs Wine Staging. Tested on 9.21. Wine 9.22 and 10.x did not work with yabridge 5.1.1 at the time of the README. Check the issue tracker before installing a newer Wine (README current on 2026-10-23, VERIFIED statement; later releases UNVERIFIED).
- "yabridge doesn't work with flatpak packages." So Flatpak Bitwig cannot load bridged plugins (VERIFIED).
- Commands: `yabridgectl add <plugin folder>`, `yabridgectl sync`. Output goes to ~/.vst3/yabridge and ~/.clap/yabridge (VERIFIED).
- Known fixes: missing fonts, install corefonts or allfonts via winetricks. Some JUCE plugins need DXVK and Vulkan for GUI updates. iZotope and D16 plugins cannot authorise under Wine (VERIFIED, README).
- Realtime warnings (RLIMIT_RTTIME, memlock) and the `chrt -f 10 whoami` test: README (VERIFIED), details in linux-audio-production section 5.
- Decision for Bazzite: native Linux plugins first. If a Windows plugin is a must, accept the distrobox route (UNVERIFIED) or keep that work on a Windows machine.

## 6. Audio engine and PipeWire/JACK
- Combined audio devices (several interfaces as one) work on Linux in recent versions (VERIFIED, 5.3 guide). System Out and System In+Out follow the OS choice.
- Steps for a class compliant USB interface such as the RME Digiface USB (via snd-usb-audio, UNVERIFIED for the Digiface specifically):
  1. Confirm the card in `aplay -l`.
  2. In Bitwig Dashboard, Audio, choose the backend (PipeWire or ALSA/JACK) and your interface.
  3. Start at 44.1 or 48 kHz and a 128 to 256 sample buffer. Lower only if stable.
  4. Watch DSP load and xrun count in the Dashboard.
- Use one audio server owner: if PipeWire holds the card, do not open it in ALSA mode at the same time (UNVERIFIED rule of thumb).
- Realtime scheduling, groups, limits: linux-audio-production sections 5 and 6.
- Windows and macOS: same buffer advice applies. Match the sample rate in the OS audio panel and in Bitwig (UNVERIFIED).

## 7. MIDI and controller scripts
- Hardware synths over USB MIDI show in Dashboard, MIDI Controllers. Add devices, then enable Track input or Remote control as needed (UNVERIFIED path, earlier notes).
- Controller scripts are JavaScript (Controller API). User scripts live in Documents/Bitwig Studio/Controller Scripts (UNVERIFIED on Linux). In the Flatpak, check the Documents folder in Flatseal.
- Generic MIDI keyboards work without a script. For hardware synths use MIDI tracks with the External Instrument device.

## 8. Reading plugin scan failures
- A failed scan shows as an error in the plugin manager or notifications (COMMUNITY, JUCE forum: `CouldNotReadMetadataException`).
- Logs: Bitwig logs under ~/.BitwigStudio/log on Linux (UNVERIFIED). Flatpak: under ~/.var/app/com.bitwig.BitwigStudio/ (UNVERIFIED).
- Procedure: 1) `ldd Plugin.so` for missing libraries; 2) run `pluginval` on the VST3 (UNVERIFIED use here, standard in JUCE); 3) launch Bitwig from a terminal and read stderr; 4) `objdump -T` for glibc symbols.

## 9. Core workflow
- Bitwig 6 added: Automation Mode on the A key, Detail Editor panel, Spread and Spray Can tools, automation saved in clips, Clip Alias, project key signature with Snap to Key, Audition tool, four Grid modules, permanent backup on opening older projects (VERIFIED, Sound On Sound).
1. Clips: Launcher for sketching, Arranger for the final timeline (UNVERIFIED details).
2. Devices and containers (FX Layer, Instrument Layer, Chain, Drum Machine): nested chains let one macro drive many devices.
3. The Grid (Studio edition only, VERIFIED): custom distortion, supersaw stacks, sidechain shapers.
4. Modulators: LFO, ADSR, Steps, Envelope Follower, Macro, Random. Non-destructive, can be per voice.
5. Multisampling and Sampler device: capture a hardware synth (UNVERIFIED menu names).
6. Hybrid tracks take audio and note clips. External Instrument brings in hardware. Bounce in Place commits to audio.

## 10. Expert use: hardstyle, UK hardcore, trance
Tempo ranges: hardstyle 150 to 160 BPM, UK hardcore 160 to 175, happy hardcore 165 to 180, trance 135 to 145 (UNVERIFIED, general genre knowledge).
1. Template: Kick, Rumble, Sub, Lead 1/2, Screech, Pluck, Vocal, FX, Drums, Noise/Risers. Group kick and rumble. Save as template (UNVERIFIED menu).
2. Kick: clean click, pitched body, distorted tail on separate tracks. Bounce the distorted kick to audio, then EQ and compress the bounce.
3. Rumble: copy the kick tail, remove the body, add reverb or long decay, low-pass 150 to 250 Hz, hard sidechain to the kick, tune to the track key.
4. Leads: supersaw (2 to 3 detuned saws) over a thinner mono saw. Different high-pass points. Sub below 120 Hz only on the sub track. Poly Grid or your own synth plugin.
5. Sidechain: Compressor device, Sidechain input set to the Kick track (UNVERIFIED exact UI). Or Envelope Follower or Steps modulator on a Tool device Volume with a drawn duck shape. Steps gives a consistent pump.
6. Trance: unison saw/pluck, high-pass, reverb and delay sends ducked by the kick.
7. Mix bus: glue compression on groups, limiter on master, Bitwig Spectrum to compare kick and bass.
8. Arrangement: 16 or 32 bar blocks. Risers, snare rolls, filter sweeps with Automation Mode (VERIFIED feature, Bitwig 6).
9. Same on all platforms: this workflow does not change per OS; only plugin availability does (UNVERIFIED).

## 11. Plugin test checklist (your own JUCE plugins)
Run on Linux first. Repeat on Windows and macOS builds when available.
1. Scan: VST3 in ~/.vst3, CLAP in ~/.clap, rescan, confirm it shows in the browser.
2. Preset recall: load factory preset, tweak, save project, reload. Parameters match.
3. Automation: automate from the device lane; no zipper noise.
4. Sample rate: switch 44.1, 48, 96 kHz; no crash, silence or stuck tails.
5. Offline render: File, Export Audio versus live bounce; identical output.
6. Latency: lookahead reported correctly; null test against an inverted duplicate.
7. State: save, close Bitwig, reopen; state and window size restored. Duplicate device. Freeze track.
8. Hosting modes: run Individually and Within Bitwig.
9. Flatpak: test once with the Flatpak and once with default permissions. Note which folders were needed.
10. CLAP and VST3 builds behave the same (parameters, modulation, state).
11. Sidechain input (if any): appears and survives reload (UNVERIFIED).
12. Crash recovery: kill the plugin; Reload Plug-in works (VERIFIED feature).

## Not verified
Bitwig Windows and macOS audio driver menus; Windows and macOS plugin folders as Bitwig scans them; computers allowed per license; macOS Apple Silicon support; Audio Unit support; VST2 in 6.x; Flatseal permissions that fully fix plugin visibility; distrobox plus yabridge plus Bitwig; Bitwig log paths; Flatpak CLI exact command; Fedora forum thread (blocked, not re-read); fetch limit reached 2026-10-23 so Bitwig user guide audio settings, system requirements page and pricing details beyond the buy page were not re-read.

## Sources (fetched)
1. https://www.bitwig.com/download/ 2. https://flathub.org/apps/com.bitwig.BitwigStudio 3. https://www.bitwig.com/support/technical_support/52/ 4. https://www.bitwig.com/buy/
5. https://bitwig.com/stories/introducing-three-flavors-of-bitwig-studio-254/ 6. https://downloads.bitwig.com/6.1/Release-Notes-6.1.html 7. https://www.bitwig.com/userguide/latest/vst_plug-in_handling_and_options
8. https://github.com/robbert-vdh/yabridge/blob/master/README.md 9. https://www.soundonsound.com/news/bitwig-studio-6-launches 10. https://omgubuntu.co.uk/2025/08/bitwig-studio-6-beta-changes-linux-daw
11. https://forum.juce.com/t/bitwig-studio-on-linux-cant-add-my-vst3-to-library/58621 12. https://support.ujam.com/hc/en-us/articles/360011016500-Rescan-Bitwig 13. https://www.bitwig.com/userguide/latest/welcome_to_bitwig_studio/
