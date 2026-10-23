---
name: audio-interface-digital-io
description: Use when advising on audio interfaces, digital I/O (ADAT, S/PDIF, MADI), clocking and mixers, incl. RME Digiface USB and Ferrofish Pulse 16, on Linux.
---

# Audio interfaces and digital I/O (music production on Linux)

Labels: VERIFIED (source) = read this session in the cited source. COMMUNITY = forum/user report or widely repeated engineering knowledge not re-checked here. UNVERIFIED = could not confirm; treat as open question. Do not upgrade a label without a new source.

## 1. Analog connections and levels
- XLR: balanced, 3-pin, mic or line. TRS 6.3 mm: balanced line (or stereo/headphone). TS 6.3 mm: unbalanced mono (instrument, synth). COMMUNITY.
- Mic level (tens of mV, needs preamp gain) vs line level (about 1 V) vs instrument/Hi-Z (high impedance, guitar/bass DI). COMMUNITY.
- Pro line reference +4 dBu (1.228 V RMS); consumer -10 dBV (0.316 V RMS). The two differ by about 11.8 dB. COMMUNITY.
- Hardware synths into converters: match the converter's reference level; a too-hot synth clips the AD, a too-quiet one wastes bits. COMMUNITY.
- Balanced cables reject hum; use TRS/XLR between balanced gear, TS only for short unbalanced runs. COMMUNITY.

## 2. Digital formats
- AES/EBU (AES3): 2 ch, balanced XLR 110 ohm, pro level. COMMUNITY.
- S/PDIF: 2 ch, coax (RCA, 75 ohm) or optical (TOSLINK). Consumer framing; same audio as AES3 in practice. COMMUNITY.
- S/PDIF is not rate-limited like ADAT: a Digiface USB S/PDIF output supports 192 kHz (RME staff, forum). VERIFIED (https://forum.rme-audio.de/viewtopic.php?pid=248243).
- ADAT (lightpipe): optical TOSLINK, 8 ch at 44.1/48 kHz. COMMUNITY (consistent with RME and Ferrofish pages below).
- ADAT SMUX: 88.2/96 kHz = 4 ch per port; 176.4/192 kHz = 2 ch per port. VERIFIED (RME staff: 8 ch single speed, 4 double, 2 quad, https://forum.rme-audio.de/viewtopic.php?pid=248243).
- Port-level channel math: four ADAT ports = 32 ch at 48k, 16 ch at 96k, 8 ch at 192k. VERIFIED (https://www.rme-audio.de/digiface-usb.html).
- RME calls the modes Standard / S/MUX / S/MUX4. VERIFIED (same page).
- MADI: up to 64 ch, optical or coax, 48 kHz base; 32 ch at 96k, 16 ch at 192k (channel count falls with rate). VERIFIED for the 64/32/16 split (Pulse 16 MX option page, https://proaudiodesign.com/products/ferrofish-pulse-16); coax vs optical medium is COMMUNITY.
- Dante / AVB: audio over Ethernet; Dante is proprietary (Audinate), AVB is IEEE standard needing AVB switches. Neither is needed for the ADAT and USB gear covered here. COMMUNITY. Digiface AVB has no CC mode per RME staff ("Sorry, no", 2025-08-23). VERIFIED (https://forum.rme-audio.de/viewtopic.php?id=41702).

## 3. Clocking
- Every digital link needs one shared sample clock; one device is master, all others slave (follow ADAT/S/PDIF input, or word clock). COMMUNITY.
- One-clock-master rule: exactly one clock source in the whole chain; never loop slaves back into each other. COMMUNITY.
- Word clock: BNC, 75 ohm, plain square wave at sample rate; terminate the last device (75 ohm). COMMUNITY.
- Jitter: timing error in the clock; audible only as subtle degradation; a bad cable or unlocked PLL is a bigger problem than "clock quality" debates. COMMUNITY.
- ADAT/S/PDIF carry clock in the data stream, so a slave can lock to its input. COMMUNITY.
- Symptoms of clock mismatch: periodic clicks, pops, or "lock lost" indicators. COMMUNITY.

## 4. Host connection
- USB class compliant (UAC2): no vendor driver; Linux uses snd-usb-audio. Vendor-driver devices need their own driver (often absent on Linux). COMMUNITY.
- Thunderbolt/PCIe: lower latency headroom, more channels; Linux support is per vendor. COMMUNITY.
- Latency math: buffer samples / sample rate = ms per buffer. 128 / 48000 = 2.67 ms; 64 / 48000 = 1.33 ms. Round trip is about 2 buffers plus converter and safety-offset latency. COMMUNITY (arithmetic).
- Converters add small fixed latency; USB adds safety offset; CC modes typically use larger fixed offsets (see RME section). VERIFIED for RME CC (https://forum.rme-audio.de/viewtopic.php?id=41702, Dante/Ravenna context).

## 5. Mixers and routing
- Digital mixers often double as multichannel interfaces (USB/ADAT/MADI to console). COMMUNITY.
- TotalMix-style routing matrix: any input or playback channel to any output, with submixes and low-latency monitoring, independent of the DAW. COMMUNITY.
- Digiface USB TotalMix FX: routing and mixing of all inputs and playback channels, no DSP so no FX, up to 17 stereo submixes, Control Room section, remote via Mackie or OSC. VERIFIED (https://www.rme-audio.de/digiface-usb.html).

## 6. Device: RME Digiface USB
Specs
- 66 channels, 192 kHz; four TOSLINK I/Os, each ADAT (8 ch) or S/PDIF (stereo), outputs selectable individually; 32 in/32 out ADAT plus phones on channels 33/34. VERIFIED (https://www.rme-audio.de/digiface-usb.html).
- Standard 32 ch to 48 kHz, S/MUX 16 ch at 96 kHz, S/MUX4 8 ch at 192 kHz. VERIFIED (same).
- Sample rate range 28 to 200 kHz; ADAT input lock 31.5 to 50 kHz. VERIFIED (same).
- Clock sources: Internal, ADAT In, S/PDIF In. No word clock connector or source listed. VERIFIED (same page lists no word clock; absence, not an explicit statement).
- USB 2.0 bus powered, below 2 W; phones out +9.5 dBu at 0 dBFS. VERIFIED (same).
- No buttons or controls; settings are lost without power ("no memory", RME staff). VERIFIED (https://forum.rme-audio.de/viewtopic.php?pid=248243).

CC (class compliant) mode: how it is enabled
- It is a firmware state set with RME's Firmware Update Tool (FUT); there is no hardware switch ("this will have to happen in software", RME staff). VERIFIED (https://forum.rme-audio.de/viewtopic.php?id=42916 and ?pid=248243).
- Manual wording quoted by a user: "Flash the Digiface USB into CC mode using the firmware update tool"; defaults: Clock Internal, Output ADAT format; main setting is Clock Source (Internal, Optical 1-4). COMMUNITY (manual quote relayed by a forum user; manual v1.3 02/2026 exists per RME page).
- RME download page (FUT for Mac and Windows dated 2026-09-02) lists Digiface USB firmware "Hw Rev X: 18, CC 2" and "Hw Rev G: 35, CC 7". VERIFIED (https://www.rme-audio.de/digiface-usb.html); meaning of "CC n" as the CC firmware version is UNVERIFIED (page does not explain it).
- CC option reached the Windows FUT around mid-January 2026; a user ran fut.exe on Windows. VERIFIED that Windows FUT has the option (forum id=42916, user report; the page says the date is "2 weeks ago" per poster, so exact date COMMUNITY).
- Whether the Mac FUT offers the CC option for Digiface USB: UNVERIFIED (the Mac FUT is documented for Digiface Dante/Ravenna CC only; for those, "CC is not part of the Windows FUT", https://rme-audio.de/macos-usb-3-driver-options.html).
- Needs Windows or Mac? VERIFIED for flashing: a computer with a working RME driver is required ("It needs a computer with a working driver"); no Linux flashing tool is mentioned anywhere I found. A Windows PC with the FUT is the documented route. Short answer: if you own one, you need a Windows (or possibly Mac) machine; a Linux-only PC such as Bazzite alone cannot flash.
- Flashing can fail with an old driver; one user fixed a FUT that closed after the device list by updating to driver 1.0.15 (MADIface USB series, which RME staff confirmed covers Digiface USB). VERIFIED (forum id=42916). Windows driver 0.9845 also lists Digiface USB (last 32-bit driver). VERIFIED (RME page).
- Switching back to normal driver mode is also done with the FUT. COMMUNITY (user did it, forum id=42916).
- Caveat: RME once pulled the Windows FUT after "an unexpected issue", then re-uploaded a fixed one. VERIFIED (pid=248243).

CC mode limits
- No TotalMix routing in CC mode; routing is done in the DAW or ALSA mixer. COMMUNITY (user report, forum id=42916). Note RME says TotalMix FX is fully operational in CC mode for Digiface Dante/Ravenna only. VERIFIED (macos-usb-3 page); applicability to Digiface USB UNVERIFIED.
- General CC limits (Dante/Ravenna statement): fixed safety offsets (higher latency than RME drivers), no playback visualization in DigiCheck NG, no error counter. VERIFIED for those models; for Digiface USB UNVERIFIED.
- Channels reported: 16 in / 18 out at 96 kHz (16 ADAT + 2 phones); one Arch/Bitwig user saw 16/16 in JACK though ALSA showed 34. COMMUNITY.
- Inputs auto-detect ADAT or S/PDIF per input; outputs default to ADAT; S/PDIF out in CC mode needs a libusb vendor-request program (usb_vendor), not an ALSA control. VERIFIED (RME staff, forum id=42916); the program is untested by me. Example `./usb_vendor 1 0 0 0` sets output 1 to S/PDIF; try sudo if the device will not open.
- 192 kHz works with four stereo S/PDIF outputs (RME staff). VERIFIED (pid=248243).

Linux status
- Kernel snd-usb-audio quirk (Sept 2024, patch series by community authors, applied by Takashi Iwai) supports the standard-firmware device ID 2a39:3f8c: streaming at 32 to 192 kHz; playback 34/18/10 ch and capture 32/16/8 ch for 1x/2x/4x rates; boot quirk sets internal clock, ADAT outputs, 48 kHz. VERIFIED (https://lkml.iu.edu/hypermail/linux/kernel/2409.0/00331.html).
- Mixer quirk adds ALSA controls: Input 1-4 Sync/Format/Rate, Output 1-4 Format (ADAT or S/PDIF), Sync Source (Internal or Input 1-4), Current Sync Source, System Rate, Current Rate. No matrix mixer, output gain or meters (expected from a userspace app). VERIFIED (https://lkml.iu.edu/hypermail/linux/kernel/2409.0/00332.html).
- Extra PID patch applied 2024-12-02 for an alternate hardware version, marked for stable. VERIFIED (https://lkml.iu.edu/hypermail/linux/kernel/2412.0/01342.html). Which PID is CC mode: the forum program quotes 0x2a39:0x3fb2 for the CC-mode device; UNVERIFIED whether that is the "extra PID".
- That the mixer controls first shipped in 6.12 is a community claim; patch dated Sept 2024 and an AUTOSEL 6.10 backport mail exists. Exact first kernel UNVERIFIED; Bazzite's kernel is newer anyway (check `uname -r`).
- Crackle reports: Raspberry Pi/CamillaDSP user had crackling and phasing-like distortion after minutes or days in regular mode, and no output in CamillaDSP in CC mode; outcome after reflash not reported. COMMUNITY (forum id=42916). Another user said plug/unplug distortions on Linux went away with newer firmware. COMMUNITY.

How to prepare for CC mode safely (recommendation)
- Back up TotalMix settings first (TotalMix FX: File > Save Workspace/Preset); the device has no memory, but workspaces live on the host. COMMUNITY (general TotalMix practice).
- Update RME Windows driver (1.0.15 or newer MADIface USB series) before running FUT. VERIFIED that old drivers broke FUT.
- Flash in the FUT with the Digiface directly on a USB port (no hub), PC on mains, do not unplug. COMMUNITY (generic firmware practice).
- Keep a path back: do not remove the Windows RME driver/FUT, since reverting also needs the FUT. VERIFIED (revert via FUT, forum).
- Test on Linux (for example Bazzite): `aplay -l`, `amixer -c <card> contents`, then check Sync Source and Input Sync.

## 7. Device: Ferrofish Pulse 16 (plain model, without the MADI, USB or Dante options)
Model name
- The plain Pulse 16 has 16 analog in and out, ADAT, BNC word clock, power, MIDI in and out; no USB port and no MADI. This matches the Ferrofish Pulse 16 page (16 TRS in/out, 4+4 ADAT, BNC in and out, two DIN5 MIDI for remote control, 12 V). VERIFIED (https://proaudiodesign.com/products/ferrofish-pulse-16).
- Some manuals and notes say "Pulse 16 DX". The DX is sold with ADAT, MADI and Dante options (retail listing), so that name does not fit a plain unit with only ADAT. If you own one, check the label on the back or the front display to see which model it is. Use "Pulse 16" for the plain model.
- The DX guide's FCC page lists "PULSE16 / PULSE16 DX MX" as models, so one manual may cover several; whether the plain model shares every DX menu is UNVERIFIED.
Specs
- 16 balanced TRS analog in and 16 out, plus front headphone out; 4 ADAT in and 4 ADAT out; 32-bit/192 kHz converters (ESS ES9840Q ADC, ES9017 DAC). VERIFIED (https://www.fullcompass.com/prod/657042-ferrofish-pulse-16-ae-16-in-16-out-ad-da-converter-with-adat, AE model page); the plain Pulse 16 page (proaudiodesign) lists 16 TRS in/out and 4 ADAT in/out. VERIFIED.
- Analog gain range digital: +20 to -8 dBu in 1 dB steps (+24 dBu build-to-order variant: +24 to -4). VERIFIED (https://proaudiodesign.com/products/ferrofish-pulse-16).
- Word clock: BNC in and out, switchable 75 ohm termination on input; internal 125 MHz oscillator, PLL; syncs to ADAT or word clock. VERIFIED (both pages).
- ADAT channel counts per the retailer page: 16 ch at 32/44.1/48; 16 ch at 64/88.2/96; 8 ch at 128/176.4/192. That text reads as 16 ch at 48k though 4 ports x 8 is 32 ch; ambiguous. UNVERIFIED which mode a plain Pulse 16 uses at each rate; read the manual.
- SMUX4 for 192 kHz ADAT requires the MADI MX factory option which cannot be retrofitted. VERIFIED (proaudiodesign page). Implication for a unit without the MADI option: ADAT at 176.4/192 kHz may not be available at all or only as SMUX2; UNVERIFIED, confirm in manual/firmware.
- Remote control: two DIN5 MIDI connectors; MIDI over MADI needs the MX option. VERIFIED (proaudiodesign). The AE model page also lists USB-C remote config with RemoteFish software, MIDI CC control, TRS-MIDI Type A. VERIFIED for AE model; applies to non-AE Pulse 16: UNVERIFIED.
- ferrofish.com product page was blocked in this session (permission not granted); manuals not read. Spec table above comes from retailers.

Remote control over MIDI SysEx (USBPcap captures of RemoteFish 2.1 on a real unit, firmware v5.04, through a Roland UM-ONE mk2 in class compliant mode; the captures call the unit "DX")
- Frame: `F0 00 11 22 <5-byte unit id> <cmd> ... F7`; the unit id is learned from the probe answer. CONFIRMED in the captures.
- Clock source `01 01 vv`: 00 Master, 01 ADAT, 02 BNC. CONFIRMED.
- Master sample rate `01 02 vv`: 00..08 = 32, 44.1, 48, 64, 88.2, 96, 128, 176.4, 192 kHz. CONFIRMED.
- Gotcha: RemoteFish sent the same `01 02` command for its MIDI routing, MADI 96k frame, MADI short frame and BNC termination controls, so touching them changed the sample rate by accident (the unit ran at 44.1 kHz while the GUI still showed 48). Re-pick the rate to fix; the GUI does not resend a value it already shows. Real commands for those four controls: unknown.
- Presets 1-6: Save N = `02 07 <N-1>`, Load N = `02 06 <N-1> 07`. Faders: `10 <idx> <val>`, input gain 0 to 28 dB, output level 28 + dB. CONFIRMED. Meter replies are not decoded (UNVERIFIED).

## 8. Typical chain (recommendation, not verified for every unit)
- Pulse 16 ADAT OUT 1-4 to Digiface ADAT IN 1-4; Digiface ADAT OUT 1-4 to Pulse 16 ADAT IN 1-4 (Digiface USB to PC).
- Clock master: Pulse 16 internal (or its word clock), Digiface set to follow its ADAT input; or Digiface internal master with Pulse slaved to ADAT. Pick one and never both. In Digiface Linux terms: Sync Source = Input 1 (the ADAT port from the Pulse) when the Pulse is master.
- Why Pulse as master: it has a low-jitter internal oscillator and word clock outputs for other gear; Digiface has none. VERIFIED specs (above), conclusion is a recommendation.
- Keep rates at or below 96 kHz (SMUX, 16 ch) for full channel use; 44.1/48 kHz gives all 32 ch. VERIFIED per RME page; a plain Pulse 16's SMUX behaviour UNVERIFIED.
- Set both devices to the same SMUX mode (ADAT port count follows sample rate); a mismatch is the top "no signal" cause.

## 9. Troubleshooting
- No signal: check Digiface Input Sync/Rate in `amixer`; Sync Source set to a port with a live sender; SMUX mode vs sample rate; DAW sample rate equals system rate.
- Clicks/crackle: clock mismatch (two masters or none), buffer too small, USB hub/port issue, Pipewire quantum; reproduce at 256 samples first. COMMUNITY.
- Wrong SMUX mode: channels 5-8 missing or doubled at 96 kHz means one side is in 8-channel mode; verify both devices show the same rate. COMMUNITY.
- Channel order: with SMUX, channel numbering of ports shifts (4 ch per port at 96k, ports then contiguous); verify with a test tone per channel. COMMUNITY.
- Clock lock lost: re-seat TOSLINK, confirm single master, avoid daisy loops; ADAT lock range on Digiface is 31.5 to 50 kHz at base rate. Lock range VERIFIED (RME page).
- Optical cable problems: use quality TOSLINK, no tight bends, dust caps on, fully click in; cheap cables fail at the Digiface's four-port load first. COMMUNITY.
- S/PDIF vs ADAT confusion: Digiface outputs default to ADAT; set Output N Format to S/PDIF only if the receiver is S/PDIF. VERIFIED (mixer patch + RME staff).

## Sources
- https://www.rme-audio.de/digiface-usb.html
- https://rme-audio.de/macos-usb-3-driver-options.html
- https://forum.rme-audio.de/viewtopic.php?id=42916
- https://forum.rme-audio.de/viewtopic.php?pid=248243
- https://forum.rme-audio.de/viewtopic.php?id=41702
- https://lkml.iu.edu/hypermail/linux/kernel/2409.0/00331.html
- https://lkml.iu.edu/hypermail/linux/kernel/2409.0/00332.html
- https://lkml.iu.edu/hypermail/linux/kernel/2412.0/01342.html
- https://proaudiodesign.com/products/ferrofish-pulse-16
- https://www.fullcompass.com/prod/657042-ferrofish-pulse-16-ae-16-in-16-out-ad-da-converter-with-adat
