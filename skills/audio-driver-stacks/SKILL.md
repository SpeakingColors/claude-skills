---
name: audio-driver-stacks
description: Use when choosing or troubleshooting audio drivers across Windows (WASAPI, ASIO, FlexASIO), macOS (Core Audio) and Linux (PipeWire, JACK, ALSA), covering crackle, no device, latency and clocking.
---

# Audio driver stacks: Windows, macOS, Linux

Labels: VERIFIED (source) = read on a page I fetched this session. COMMUNITY = forum or user report, not official. UNVERIFIED = general knowledge or not read; test before trusting.
Rule for Claude: one change at a time, write down what changed, undo it if it did not help. Assume the reader is not a programmer. Plain words first, then one exact step. One change at a time, ask the reader to test, then continue.
Linux and Bazzite specifics (PipeWire config, rtkit groups, yabridge, RME Digiface) live in the skill linux-audio-production. This skill only compares stacks and adds what that skill lacks. Do not repeat it; link to it.
Research limit: the web fetch quota ran out mid-session. Reddit, KVR, JACK docs, WirePlumber docs, ASIO2WASAPI and Apple TN3190 were not read. See "Not verified".

## 1. The big picture
- An audio stack is layers: app, API (the language the app speaks), mixer/engine, driver, hardware. Fewer layers means lower latency but less sharing. UNVERIFIED (general)
- Windows: the Core Audio APIs came with Vista; DirectSound and the waveXxx (MME) functions are built on top of them. VERIFIED (learn.microsoft.com core-audio-apis-in-windows-vista)
- Pre-Vista capture used waveInOpen, DirectSoundCapture or DirectShow. VERIFIED (audio-endpoint-devices page)
- ASIO skips layers like KMixer, Direct KS and WASAPI and talks to the card directly. VERIFIED (Wikipedia ASIO)
- macOS: the HAL is "a device-independent, driver-independent interface to hardware" in the lowest API layer, beside I/O Kit and Core MIDI. VERIFIED (Apple Core Audio Overview archive, CoreAudioEssentials)
- Linux: ALSA is the kernel layer; PipeWire sits on it and offers JACK, Pulse and ALSA views. VERIFIED partly (docs.pipewire.org overview)
- Why drivers differ: each OS has one built-in model, ASIO is a vendor-written extra on Windows, macOS has one model for all, Linux has several servers. Vendors ship their own driver for lower latency, more channels and a control panel. COMMUNITY/UNVERIFIED reasoning
- USB class-compliant devices need no vendor driver; the OS class driver handles them. VERIFIED for macOS MIDI (Apple archive: Apple's supplied USB driver supports class-compliant devices) and Windows USB Audio 2.0 (usbaudio2.sys, Windows 10 1703+).
- Windows inbox USB Audio 2.0 driver limits: only one clock source, shared mode up to 8 channels, partner driver overrides it. VERIFIED (learn.microsoft.com usb-2-0-audio-drivers)

## 2. Windows API map
| API | What it is | Latency | Sharing |
|---|---|---|---|
| MME (waveOut) | Oldest API, built on Core Audio now | High | Shared |
| DirectSound | Games-era API, built on Core Audio now | Medium to high | Shared |
| WDM-KS | Kernel streaming, direct to the driver | Low | Usually exclusive |
| WASAPI shared | System engine mixes all apps | Medium, can be low | Shared |
| WASAPI exclusive | App owns the endpoint | Lowest of the Windows APIs | One app |
| ASIO | Vendor driver model, direct | Low | Usually one app |
- MME and DirectSound sit on Core Audio: VERIFIED (above). The latency and sharing columns for MME, DirectSound, WDM-KS: UNVERIFIED (general knowledge, the Microsoft KS page failed to load).
- WASAPI shared: "several applications can share an audio endpoint device". Exclusive: the app has exclusive use; system sounds and other apps go silent. VERIFIED (Microsoft exclusive-mode-streams)
- Exclusive mode lowest latency: it uses the minimum device period. VERIFIED (same)
- Since Windows 10 shared mode can use small periods (IAudioClient3) with latency comparable to exclusive mode. Microsoft says to evaluate that before exclusive mode. VERIFIED (same; low-latency-audio page)
- Windows 10 cut the engine render overhead to 1.3 ms; old default buffer was about 10 ms. Apps must request small buffers themselves. VERIFIED (low-latency-audio)
- If one app asks for a small buffer, every app on that endpoint and mode switches to it; it returns to 10 ms when that app quits. VERIFIED (same)
- Inbox HDAudio driver buffers range from 128 samples (2.66 ms at 48 kHz) to 480 samples (10 ms). VERIFIED (same)
- You can disable exclusive mode per device; apps then get shared streams only. VERIFIED (exclusive-mode-streams). Where that checkbox lives in the Sound control panel: UNVERIFIED.
- Windows may grab a device in exclusive mode and block your DAW: check that no other app holds it. COMMUNITY/UNVERIFIED

## 3. ASIO on Windows
- ASIO was released by Steinberg in 1997; ASIO 2.0 (1999) added direct monitoring. VERIFIED (Wikipedia)
- Hardware vendors supply their own ASIO driver. VERIFIED (Wikipedia)
- The SDK is free but needs a proprietary licence; in October 2025 Steinberg added a GPLv3 option. VERIFIED (Wikipedia; steinberg.net developers page showed no SDK text)
- ASIO only exists on Windows in the SDK. VERIFIED (Wikipedia)
- steinberg.net/asiosdk redirects to the download file ASIO-SDK_2.3.4_2025-10-15.zip, so the current SDK is 2.3.4 dated 2025-10-15. VERIFIED (redirect header only; zip not opened, licence text not read)
- Standard ASIO drivers are generally single-client: Microsoft, Qualcomm and Yamaha are building an inbox USB Audio Class driver with "multi-client ASIO support", which implies the usual drivers lack it. VERIFIED (Wikipedia, as inference)
- Rule: use the interface maker's own ASIO driver first. No vendor ASIO driver exists? Use FlexASIO or ASIO4ALL (below). UNVERIFIED (advice)

### ASIO4ALL
- Described as a "low latency ASIO driver for Windows audio". VERIFIED (asio4all.org)
- Newest listed: 2.15 Beta 1, 11 March 2021, Windows 10 only. Latest stable: 2.14, 23 May 2017. VERIFIED (asio4all.org)
- 2.15 notes: Intel SST support, WaveRT refactor, better USB Audio Class 2.0 support. VERIFIED (same)
- The page had no latency FAQ and no WDM-KS text. VERIFIED (absence on the fetched page)
- Caveats: the stable release is old; the 2.15 line is beta; for Windows 11 support the site says nothing. VERIFIED (what the page lists); Windows 11 behaviour UNVERIFIED.
- Prefer the vendor driver or FlexASIO when one exists; use ASIO4ALL only if both fail. UNVERIFIED (advice)

### FlexASIO
- "A flexible universal ASIO driver that uses the PortAudio sound I/O library." It can use WASAPI (shared and exclusive), KS (WDM-KS), DirectSound and MME. VERIFIED (github.com/dechamps/FlexASIO)
- Defaults: DirectSound, default devices, 32-bit float, 20 ms preferred buffer. VERIFIED (same)
- Needs Windows Vista or later; works for 32-bit and 64-bit hosts. VERIFIED (same)
- Config file: `FlexASIO.toml` in your user folder, for example `C:\Users\Name\FlexASIO.toml`. VERIFIED (CONFIGURATION.md)
- Options: backend, bufferSizeSamples, suggestedLatencySeconds, wasapiExclusiveMode. VERIFIED (same)
- Low-latency example from the docs:

```
backend = "Windows WASAPI"
bufferSizeSamples = 480

[input]
suggestedLatencySeconds = 0.0
wasapiExclusiveMode = true

[output]
suggestedLatencySeconds = 0.0
wasapiExclusiveMode = true
```
- 480 samples at 48 kHz is 10 ms one way. VERIFIED (math; docs give 1920 samples = 40 ms)
- FlexASIO reloads the config and asks the host to reset. VERIFIED (CONFIGURATION.md)
- Logging: create an empty `FlexASIO.log` in your user folder; it can cause glitches, so delete it afterwards. VERIFIED (GitHub page)
- Tools shipped: PortAudioDevices.exe (device list) and FlexASIOTest.exe. VERIFIED (GitHub page)
- A GUI for settings exists (FlexASIO GUI by flipswitchingmonkey). VERIFIED (GitHub page)
- Steps for a non-programmer: 1. Install FlexASIO. 2. Create the .toml file with the example above. 3. In the DAW pick "FlexASIO". 4. Raise bufferSizeSamples if you hear crackle. 5. Change one value per test.

### ASIO2WASAPI
- Wraps WASAPI as an ASIO driver. UNVERIFIED (name knowledge only; GitHub page failed to load). Treat FlexASIO as the documented option.

### Voicemeeter
- Audio mixer with a built-in virtual audio device; versions Standard, Banana, Potato. VERIFIED (vb-audio.com)
- One virtual ASIO with 8 channels in and out for up to 4 clients; its rate and buffer follow Main Output A1. VERIFIED (same)
- Output A1 supports WDM, KS, MME and ASIO. VERIFIED (same)
- Donationware: after 30 days the About box asks for a licence. VERIFIED (same)
- Install as administrator, reboot after install and uninstall. VERIFIED (same)
- Use it for streaming and routing mic, game and music. Not for tight DAW tracking. UNVERIFIED (advice)

### Windows audio enhancements
- Effects are Audio Processing Objects (APOs). Stream effects (SFX), mode effects (MFX), endpoint effects (EFX). VERIFIED (Microsoft APO architecture page)
- Raw mode means no processing; drivers must support Raw or Default. Windows 10 loads RAW MFX but not RAW SFX. VERIFIED (signal-processing-modes and APO pages)
- Effects types include equalizer, bass boost, noise suppression, AGC, AEC. VERIFIED (signal-processing-modes)
- The pages describe no single "disable enhancements" switch for users. VERIFIED (absence). The checkbox in the Sound control panel (Properties, Advanced or Enhancements): UNVERIFIED.
- Advice: for music work switch every enhancement off on the interface and use ASIO or WASAPI exclusive, which bypass the engine. Exclusive bypass: VERIFIED (low-latency-audio). Advice itself: UNVERIFIED.

### Sample rate and buffer on Windows
- Shared mode runs at one engine format; exclusive mode negotiates a format with the device (IsFormatSupported). VERIFIED (exclusive-mode-streams)
- A mismatch can give AUDCLNT_E_ENGINE_FORMAT_LOCKED errors in apps. VERIFIED (low-latency-audio)
- Set the same rate in the Windows Sound panel, the driver panel and the DAW. UNVERIFIED (advice, standard practice)

### Wine and wineasio (bridging to Linux)
- WineASIO is "an ASIO to JACK driver for WINE". VERIFIED (github.com/wineasio/wineasio)
- Version 1.3.0, last changelog 24 July 2025; library LGPL v2.1. VERIFIED (same)
- Build: `make 32` and `make 64`; copy .dll and .dll.so into Wine's lib dirs; newer Wine may want `wineasio64.so`. VERIFIED (same)
- Register in a prefix with the `wineasio-register` script; use WINEPREFIX for non-default prefixes. VERIFIED (same)
- Min and max buffer sizes are hard coded to 16 and 8192. A buffer the backend refuses may stop the JACK server. VERIFIED (same)
- Works "together with JACK". PipeWire-jack was not mentioned on the page; UNVERIFIED whether it works. See linux-audio-production for pw-jack.
- For Bottles and Bazzite steps use the skill wine-proton-bottles. UNVERIFIED (skill listing only)

## 4. macOS
### Core Audio and HAL
- Core Audio keeps "low latency through the signal chain". VERIFIED (Apple Core Audio Overview)
- Layers: HAL, I/O Kit, Core MIDI at the bottom; Audio Units above. VERIFIED (CoreAudioEssentials)
- Most apps do not use the HAL directly. VERIFIED (same)
- Mac apps pick devices through AUHAL; Audio MIDI Setup directs the Default I/O and System I/O units separately. VERIFIED (same)
- There is one audio model for all apps; no separate API choice like Windows. UNVERIFIED (general)
- Core Audio normally lets several apps share a device. UNVERIFIED (general knowledge; page did not say)

### Audio MIDI Setup
- Open it from Utilities. The guide covers audio devices, MIDI Studio, Bluetooth MIDI, MIDI over network and troubleshooting. VERIFIED (support.apple.com/guide/audio-midi-setup)
- Format and sample rate dropdowns per device: UNVERIFIED on a fetched page. Set the device rate there and match the DAW. UNVERIFIED (advice)

### Aggregate Device (combine interfaces)
- Steps: 1. Open Audio MIDI Setup. 2. Click Add at the bottom of the sidebar. 3. Choose Create Aggregate Device. 4. Tick Use for each device. VERIFIED (Apple)
- Set every device to the same sample rate first. VERIFIED (Apple)
- A Clock Source / Sync Source menu picks the primary clock; pick the device with the most reliable clock. VERIFIED (Apple "Set aggregate device settings")
- Tick Sync (drift correction, also resampling) on every device that is not the clock source. VERIFIED (same)
- A device with hardware sync (ADAT, word clock) should be the clock source. VERIFIED partly (Apple says choose the primary hardware-synchronised device)
- Warning: an aggregate adds drift correction work. Use one interface with enough inputs if you can. UNVERIFIED (advice)

### Multi-Output Device (hear the same audio on several outputs)
- Steps: Add, Create Multi-Output Device, tick Use on each output, choose the Primary Device. VERIFIED (support.apple.com ams7c093f372)
- "audio sent to the primary device also plays through any other device in the stack." VERIFIED (same)
- Drift correction on all devices except the clock source (BlackHole advice). COMMUNITY (BlackHole README)
- Volume keys often do not work on a Multi-Output Device. UNVERIFIED (common user report, not read)

### Virtual routing: BlackHole and Loopback
- BlackHole: loopback driver with "zero additional latency"; 2, 16, 64 channel builds (README also mentions 128, 256); Intel and Apple Silicon; GPL-3.0; macOS 10.10+. VERIFIED (github.com/ExistentialAudio/BlackHole)
- Install by installer or `brew install blackhole-2ch`. VERIFIED (same)
- App to app: sender output = BlackHole, receiver input = BlackHole. To still hear it, use a Multi-Output Device with Built-in Output first. VERIFIED (same)
- Do not use AirPods as the aggregate clock; their mic runs at a lower rate. VERIFIED (same, README)
- Avoid high sample rate with high channel counts. VERIFIED (same)
- Loopback (Rogue Amoeba): virtual devices from app and hardware sources, up to 64 channels, Pass-Thru devices; v2.5.0 supports macOS 14.5 through 27; free download is trial until licensed. VERIFIED (rogueamoeba.com/loopback). Its Apple Silicon status was not stated on that page.

### Driverless class-compliant and Apple Silicon
- Apple's built-in USB driver supports class-compliant MIDI devices. VERIFIED (Apple archive). Audio class compliance on current macOS: UNVERIFIED (TN3190 page body not read; only its title "USB audio device design considerations" is VERIFIED).
- For Apple Silicon Macs RME lists three driver options: DriverKit ("Apple's modern and recommended approach"), legacy kernel extension, and Class Compliant mode. VERIFIED (rme-audio.de macos-usb-3-driver-options)
- CC mode trade-offs there: higher latency than RME's driver, no fixed safety offsets. VERIFIED (same)
- Enabling CC mode on an RME device makes the Windows driver stop recognising it until switched back. VERIFIED (same, for the models listed)
- Apple Silicon needs DriverKit or class-compliant devices; kernel extensions need extra security steps. UNVERIFIED (general)
- If a vendor driver breaks after a macOS update: check the vendor site for a new driver first. UNVERIFIED (advice)

## 5. Linux in one page (comparison only)
- PipeWire: a graph of nodes with ports and links; handles audio, video, MIDI. VERIFIED (docs.pipewire.org overview)
- It reimplements JACK client libraries; `pw-jack` sets LD_LIBRARY_PATH so a JACK app loads them; it has no effect if PipeWire JACK is already system-wide. VERIFIED (pw-jack man page)
- It offers a virtual ALSA device for ALSA apps. VERIFIED (overview)
- Pulse compatibility is done by pipewire-pulse. UNVERIFIED (man page not read; the overview says only "similar mechanisms")
- Session manager: PipeWire alone does not manage the graph; WirePlumber (Lua scripts) is current, pipewire-media-session is the older one. VERIFIED (overview). WirePlumber's own docs failed to load, so config details: UNVERIFIED.
- ALSA is the kernel driver layer. JACK is a separate pro server that PipeWire can replace. UNVERIFIED (general; JACK docs blocked)
- Tools:
  - `pw-top`: ERR column is Xruns plus errors; QUANT is buffer samples; RATE is graph rate; W/Q is graph load; press `c` to reset ERR. VERIFIED (pw-top man page)
  - QUANT / RATE = period time; 1024 at 48000 is about 21.3 ms. VERIFIED (same)
  - `qpwgraph`, `Helvum`: graph patchbays. UNVERIFIED (no page read; see linux-audio-production section 8)
- Latency settings (from pipewire.conf docs): default.clock.rate 48000, default.clock.quantum 1024, min-quantum 32, max-quantum 8192, power-of-two-quantum true; allowed-rates is off by default because of known kernel and Bluetooth issues. VERIFIED (page_man_pipewire_conf_5)
- Runtime: `pw-metadata -n settings 0 clock.quantum 1024` is shown in the man page; clock.force-quantum is an integer, 0 releases it. VERIFIED (pw-metadata and pipewire man pages)
- Env vars: PIPEWIRE_QUANTUM forces rate and buffer; PIPEWIRE_LATENCY is a suggestion; PIPEWIRE_RATE is a suggestion applied when the graph is idle. VERIFIED (pipewire(1) man page). Value format: see linux-audio-production section 3 (UNVERIFIED there).
- Realtime: libpipewire-module-rt first tries RLIMIT_RTPRIO, then the Portal Realtime API or RTKit; rt.prio sets thread priority. VERIFIED (module-rt page)
- rtkit is the fallback daemon that grants realtime; groups and limits.d are the other way. For the Bazzite-specific steps use linux-audio-production section 5.
- Why it matters for comparison: Linux has no per-app "driver" choice like ASIO. You choose the layer an app talks to: native PipeWire, JACK-via-PipeWire, Pulse, or direct ALSA. UNVERIFIED (general)

## 6. Cross-platform math
- One-way buffer latency (ms) = buffer samples / sample rate x 1000. VERIFIED by pw-top page example (1024 at 48000 = 21.3 ms) and FlexASIO doc (1920 at 48000 = 40 ms).
- Table at 48 kHz: 32 = 0.67 ms, 64 = 1.33, 128 = 2.67, 256 = 5.33, 480 = 10, 512 = 10.67, 1024 = 21.3. VERIFIED (arithmetic)
- At 96 kHz the same buffer is half the time; at 44.1 kHz it is slightly longer. VERIFIED (arithmetic)
- Round trip is at least input buffer plus output buffer, plus converter and USB safety offsets. Windows definition: roundtrip is roughly render plus capture. VERIFIED (low-latency-audio). Converter and USB amounts: UNVERIFIED.
- Many drivers use 2 or 3 buffers, so real latency is higher than one buffer. UNVERIFIED (general). FlexASIO default suggestedLatency is 3 times the ASIO buffer. VERIFIED (CONFIGURATION.md)
- Starting buffers: tracking 128 or 256; mixing 512 or 1024. COMMUNITY (see linux-audio-production)
- Smaller buffers raise the glitch risk, as FlexASIO docs say. VERIFIED (CONFIGURATION.md)
- Lower latency also costs more power because the CPU wakes more often. VERIFIED (low-latency-audio)

### Measure round-trip latency (one step at a time)
1. Cable an output of the interface to an input (loopback cable).
2. Set the DAW to the buffer you want to test.
3. Play a short click on an output track; record it on an input track.
4. Zoom in; measure the gap between the played and the recorded click in samples.
5. Convert to ms with the formula above. Log buffer, rate, result.
6. Many DAWs and tools have a loopback calibration; use it if present. UNVERIFIED (general)
- The method is general practice. UNVERIFIED (no source fetched).

### Sample rate versus clock
- Sample rate is how many samples per second. The clock is the timing source that says when each sample moves. Two devices at "48 kHz" can still drift if they use different clocks. UNVERIFIED (general), supported by Apple's note that "even devices with matching rates may occasionally correct for clock drift." VERIFIED (Apple aggregate settings)
- Only one device should be the clock master; others follow. VERIFIED partly (Apple: choose the primary sync device; others use Sync). Windows and Linux equivalents: UNVERIFIED.
- Windows USB Audio 2.0 inbox driver supports only one clock source. VERIFIED (usb-2-0-audio-drivers)
- ADAT and S/PDIF carry the clock inside the data signal. The receiver must slave to it or you hear clicks. UNVERIFIED (general). For the Digiface sync source and ADAT, see linux-audio-production section 7 and the skill audio-interface-digital-io.
- ADAT at 96 kHz halves the channels (S/MUX). UNVERIFIED (general)

### Why xruns and crackle happen
- Xrun means the audio buffer ran empty or full: the app missed its deadline. Pipewire's pw-top defines Xrun as the graph not completing a cycle because a node had an Xrun or scheduling delays missed a deadline. VERIFIED (pw-top man page)
- Windows glitches: the app fails to write to the endpoint buffer before the hardware reads it. VERIFIED (exclusive-mode-streams)
- Common causes: buffer too small, CPU spikes, sample rate or clock mismatch, USB hubs or power saving, Wi-Fi/Bluetooth interference, bad plugin, bad cable. COMMUNITY/UNVERIFIED (common lists; not read from a page this session)
- Windows enhancements and the engine can add load or change the format. UNVERIFIED

## 7. Decision table: which API to choose
| Task | Windows | macOS | Linux |
|---|---|---|---|
| DAW recording, own ASIO driver exists | Vendor ASIO | Core Audio (vendor driver or class-compliant) | PipeWire driver in DAW, or JACK via pw-jack |
| DAW, no vendor ASIO | FlexASIO (WASAPI exclusive) then ASIO4ALL | Core Audio | Same as above |
| Windows plugins in Linux DAW | n/a | n/a | yabridge, see linux-audio-production |
| Games | WASAPI shared (default) | Core Audio default | Pulse layer (default) |
| Streaming with game plus music plus mic | Voicemeeter or app audio capture | BlackHole or Loopback | PipeWire loopback or qpwgraph |
| Listening only | WASAPI shared | Core Audio default | Default sink |
| Two interfaces together | Not in ASIO normally; use one driver or Voicemeeter | Aggregate Device | PipeWire handles both; clock via one device |
- This table is an advice summary. Supported parts: WASAPI shared and exclusive tradeoffs VERIFIED (Microsoft), FlexASIO backends VERIFIED, Voicemeeter virtual ASIO VERIFIED, aggregate steps VERIFIED, BlackHole VERIFIED, Loopback VERIFIED, pw-jack VERIFIED. The game and listening rows are UNVERIFIED (standard practice).
- Microsoft advises: try shared-mode low-period before exclusive mode unless you need bit-exact output or custom rates. VERIFIED (exclusive-mode-streams)

## 8. Troubleshooting trees (one change per step; log each)
### A. Crackling or dropouts
1. Note: constant crackle, or only at load, or only after hours?
2. Raise the buffer one step (for example 256 to 512). Gone? It was load; stop.
3. Windows: close other audio apps; if on WASAPI exclusive or ASIO, check no app holds the device.
4. Match sample rate in OS panel, driver panel and DAW. Mismatch causes errors. VERIFIED partly (ENGINE_FORMAT_LOCKED text)
5. Switch the USB port (rear, not hub). COMMUNITY (linux-audio-production)
6. Windows: turn off audio enhancements; try another API (WASAPI exclusive vs ASIO).
7. macOS: if using Aggregate Device, tick Sync (drift correction) on non-clock devices and set the most reliable clock. VERIFIED (Apple)
8. Linux: open `pw-top`; if ERR rises it is an xrun. VERIFIED (pw-top). Continue with linux-audio-production section 11.
9. Remove plugins one at a time to find a heavy one.
10. Different cable; test the same interface on another computer.

### B. No device found
1. Does the OS see the device at all? Windows: Device Manager and Sound panel. macOS: Audio MIDI Setup. Linux: `wpctl status`. UNVERIFIED (standard)
2. Replug into another port and cable. Reboot once.
3. Is the vendor driver installed? Windows ASIO drivers need to be installed; FlexASIO must be installed to show in the DAW. VERIFIED (FlexASIO page: installer)
4. Windows: another app may hold the device in exclusive mode. VERIFIED (exclusive-mode-streams: exclusive blocks others)
5. Windows: check that exclusive mode was not disabled on the device if the DAW needs it. VERIFIED (same)
6. FlexASIO: run PortAudioDevices.exe to list devices; test with FlexASIOTest.exe. VERIFIED (GitHub page)
7. Interface in class-compliant mode? Some RME devices need CC mode off for the Windows driver. VERIFIED (rme-audio.de, for those models)
8. macOS: reselect the device in the DAW preferences and in System Settings, Sound. UNVERIFIED
9. Linux: see linux-audio-production sections 4 and 7.

### C. Latency too high
1. Measure the real round trip first (section 6). Write the number.
2. Lower the buffer one step. Crackle now? Go back one step.
3. Check which API: MME and DirectSound are high latency; switch to ASIO or WASAPI exclusive. UNVERIFIED for MME/DirectSound numbers.
4. Windows: try shared mode with a small period if the app supports IAudioClient3. VERIFIED (Microsoft)
5. FlexASIO: set backend WASAPI, wasapiExclusiveMode true, suggestedLatencySeconds 0.0. VERIFIED (CONFIGURATION.md)
6. Aggregate Device on macOS adds work; test one interface alone. UNVERIFIED (advice)
7. Linux: set quantum with `pw-metadata -n settings 0 clock.force-quantum 256` and release with 0. VERIFIED (pipewire man page for the key)
8. Direct monitoring on the interface bypasses the computer. UNVERIFIED (general; ASIO 2.0 added direct monitoring VERIFIED)
9. Lower plugin load or freeze tracks (plugin delay counts).

### D. Device missing after an update
1. Note what updated: OS, driver, firmware, DAW.
2. Windows: check Device Manager and reinstall the vendor driver; a Windows Update driver may override. VERIFIED partly (Windows says a partner driver on Windows Update overrides the inbox UAC2 driver).
3. Windows ASIO: reselect the driver in the DAW; a new rate or backend may reset the config. UNVERIFIED
4. macOS: check the vendor site for a driver built for that macOS; consider class-compliant mode where the vendor offers it. VERIFIED partly (RME page lists CC mode as fallback)
5. macOS: reselect devices in Audio MIDI Setup; recreate the Aggregate Device. UNVERIFIED
6. Linux: `wpctl status`; restart services; if still missing, boot the previous image (`rpm-ostree rollback`). VERIFIED (linux-audio-production section 11 cites the command)
7. Check cables and the USB port after the reboot.
8. If one step fixes it, note the cause in your log so the next update is easy.

## 9. Standing advice for a non-programmer reader
- Windows and macOS: prefer vendor drivers; FlexASIO is the documented fallback. Keep Voicemeeter for streaming only.
- If Linux is your main target: use the linux-audio-production skill for setup; use this skill only to explain differences and compare behaviours.
- Keep a short log: change, date, result, so rollbacks are easy.

## Not verified (read these before relying on them)
- Reddit (r/audioengineering, r/linuxaudio, r/WeAreTheMusicMakers) and KVR threads: not read (fetch quota ran out). Any forum-style claim above is marked COMMUNITY/UNVERIFIED.
- Microsoft Kernel Streaming (WDM-KS) page failed to load twice; WDM-KS behaviour is UNVERIFIED.
- Second pass: JACK FAQ, JACK realtime page and WirePlumber docs were permission-blocked again; ASIO2WASAPI2 failed again.
- MME and DirectSound latency numbers: UNVERIFIED.
- ASIO2WASAPI (GitHub page failed); its current maintenance status: UNVERIFIED.
- ASIO4ALL: Windows 11 behaviour, WDM-KS notes, FAQ: UNVERIFIED.
- Windows Sound panel layout for exclusive-mode checkboxes and enhancements: UNVERIFIED.
- Apple TN3190 body (class-compliant USB audio rules), macOS aggregate/clock for sample-rate dropdowns, Apple Silicon audio driver rules beyond RME's page: UNVERIFIED.
- JACK docs (jackaudio.org FAQ and realtime pages): blocked; JACK latency formula (frames, periods): UNVERIFIED here.
- WirePlumber docs and PipeWire wiki (Config-JACK, Performance-tuning): blocked; use linux-audio-production for details.
- PIPEWIRE_LATENCY value format and pw-jack with wineasio: UNVERIFIED.
- ADAT/S-MUX details, loopback measurement method, xrun cause lists: general knowledge.

## Sources (fetched)
- https://learn.microsoft.com/en-us/windows/win32/coreaudio/exclusive-mode-streams
- https://learn.microsoft.com/en-us/windows-hardware/drivers/audio/low-latency-audio
- https://learn.microsoft.com/en-us/windows/win32/coreaudio/core-audio-apis-in-windows-vista
- https://learn.microsoft.com/en-us/windows/win32/coreaudio/audio-endpoint-devices
- https://learn.microsoft.com/en-us/windows-hardware/drivers/audio/audio-signal-processing-modes
- https://learn.microsoft.com/en-us/windows-hardware/drivers/audio/audio-processing-object-architecture
- https://learn.microsoft.com/en-us/windows-hardware/drivers/audio/usb-2-0-audio-drivers
- https://en.wikipedia.org/wiki/Audio_Stream_Input/Output
- https://www.asio4all.org/
- https://github.com/dechamps/FlexASIO and CONFIGURATION.md
- https://vb-audio.com/Voicemeeter/index.htm
- https://github.com/wineasio/wineasio
- https://support.apple.com/guide/audio-midi-setup/welcome/mac
- https://support.apple.com/guide/audio-midi-setup/combine-audio-devices-a-single-aggregate-ams6e21c3f61/mac
- https://support.apple.com/guide/audio-midi-setup/set-aggregate-device-settings-ams094c7edb4/mac
- https://support.apple.com/guide/audio-midi-setup/ams7c093f372/mac
- https://developer.apple.com/library/archive/documentation/MusicAudio/Conceptual/CoreAudioOverview/ (Introduction and CoreAudioEssentials)
- https://github.com/ExistentialAudio/BlackHole
- https://rme-audio.de/macos-usb-3-driver-options.html
- https://rogueamoeba.com/loopback/
- https://docs.pipewire.org/page_overview.html
- https://docs.pipewire.org/page_man_pw-top_1.html
- https://docs.pipewire.org/page_man_pipewire_conf_5.html
- https://docs.pipewire.org/page_module_rt.html
- https://docs.pipewire.org/page_man_pw-jack_1.html
- https://docs.pipewire.org/page_man_pw-metadata_1.html
- https://docs.pipewire.org/page_man_pipewire_1.html
- Not fetched or failed: steinberg.net developers page (no SDK text), kernel-streaming page, ASIO2WASAPI2, TN3190 body, JACK FAQ, WirePlumber docs, PipeWire wiki, KVR, Reddit.
