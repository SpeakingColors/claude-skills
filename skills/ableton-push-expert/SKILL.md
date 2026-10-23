---
name: ableton-push-expert
description: Use when helping a non-programmer with Ableton Push 1, 2, 3 or Push 3 Standalone, covering models, modes, MIDI and display, updates, troubleshooting, Linux reality, and what custom tools can be built.
---

# Ableton Push 1, 2, 3 and Push 3 Standalone

Labels: VERIFIED (source) = read on a page I fetched. COMMUNITY = forum or user report. UNVERIFIED = not confirmed; say so, never guess.
Rules for Claude: Assume the reader is not a programmer. Plain words first, then one exact step. One change at a time, ask the reader to test, then continue. Ask which Push the reader has before model-specific advice. Never invent MIDI numbers: read them from a source or capture them (see hardware-protocol-capture skill).

## 1. Models
- Push 1: needs Live 9 or later. VERIFIED (help.ableton.com 115000036770, 209774445)
- Push 2: needs Live 9.5 or later; powered over USB but dims without the AC adapter. VERIFIED (115000036770, 209072549)
- Push 3: needs Live 11.3 or later; USB 2.0 port or higher. VERIFIED (115000036770)
- Push 3 (tethered, no CPU) needs a computer; Push 3 Standalone has its own computer. VERIFIED (ableton.com/en/push/tech-specs)
- Push 3 Standalone: Intel i3-1115G4, 8 GB RAM, 256 GB SSD, lithium iron phosphate battery (2 to 2.5 h), Wi-Fi, 3.95 kg. Tethered: 3.1 kg, no Wi-Fi. VERIFIED (tech-specs)
- Push 3 both versions: 64 MPE pads with XY sensors, RGB backlight, 2 inputs, 2 balanced outputs, headphone, ADAT expansion. VERIFIED (tech-specs)
- Upgrade Kit turns tethered into standalone (processor, drive, battery, heatsink). VERIFIED (ableton.com/en/push). Push 2 has no standalone upgrade. VERIFIED (Technical FAQ 8483166334748)
- Push 2 display: 960 x 160 pixels, 16 bit. VERIFIED (push-interface manual). Push 1 display, pad count, and Push 3 display size: UNVERIFIED (not read).
- Push 1 and Push 2 "will keep on being supported as long as possible". COMMUNITY (Ableton moderator, forum p=1810805, May 2023)
- Two Push 2 units on one computer, or Push 1 with Push 2: not supported. VERIFIED (Using Push 2 FAQ). Two Pushes on one Live: not supported. VERIFIED (Push 3 FAQ).

## 1a. Platforms (Windows, macOS, Linux)
| | Windows | macOS | Linux |
|---|---|---|---|
| Needs | Live 12 minimum: Windows 10 22H2 or 11 22H2+, AVX2 CPU, 8 GB RAM. VERIFIED (help.ableton.com 115001663530) | Apple silicon on Big Sur 11.7.10+, or Intel up to Tahoe 26. VERIFIED (same) | No official Live. Wine project only (section 10) |
| Push needs | Push 1: Live 9 and OpenGL 3.0 GPU. Push 2: Live 9.5. Push 3: Live 11.3, OpenGL 3.0 GPU. All: USB 2.0 or higher, internet for authorization and updates. VERIFIED (115000036770) | same | same hardware; software route in section 10 |
| Audio | ASIO driver advised for Live. Push 3 has a built-in audio interface, pick it in Live's Audio Settings. VERIFIED (115001663530, Push 3 manual). Clock source is set in the driver control panel, not on Push. VERIFIED (Push release notes 2.3.2) | Core Audio advised. VERIFIED (115001663530) | PipeASIO in the Wine project. VERIFIED (shibco README) |
| Extra driver | Push 3 needs a separate display driver; fix by uninstalling "Ableton Push 3 Display" in Device Manager. VERIFIED (KB 10295607009436) | None found. Push 2 on a MacBook: turn off Automatic graphics switching. VERIFIED (KB 360001045784) | udev rule (section 10) |
| Plugins | Live: VST2, VST3 (see max-for-live-expert 1a) | VST2, VST3, AU | Windows plugins in the prefix only |
| Licence | Push 1, 2, 3 tethered: bundled Live edition UNVERIFIED. Standalone ships Live 12 Intro | same | Own Live licence; project does not change it. VERIFIED (README) |
- Windows scripts folder `\ProgramData\Ableton\Live x.x\Resources\MIDI Remote Scripts\`; macOS `/Applications/Ableton Live X.app/Contents/App Resources/MIDI Remote Scripts/`. Logs in section 8. COMMUNITY (blog.azuki.vip)
- Two Pushes on one Live: not supported on any OS. VERIFIED (115000036770)

## 2. Live edition and licensing
- Standalone ships with Live 12 Intro (16 tracks max). A Standard or Suite licence unlocks that licence's devices and unlimited tracks. VERIFIED (Push 3 Technical FAQ)
- Authorizing Standalone needs a computer on the same network or Wi-Fi. VERIFIED (Connecting Push 3 to your Computer, 8483411204252)
- Which Live edition is bundled with a Push 1, 2 or tethered 3: UNVERIFIED.
- Push 2 interface doc licence: "A license to use this manual is hereby granted"; copying or redistributing the doc needs Ableton's consent. VERIFIED (push-interface doc header). Link to it, do not copy it.
- Ableton gives no support for custom Remote Scripts. COMMUNITY (Cycling '74 thread, quoting an Ableton person)

## 3. Modes
- Control Mode (computer runs Live) versus Standalone Mode (Push 3 Standalone only). VERIFIED (Push 3 manual)
- To switch: press Setup, Status tab, then the display button (Control Live / Standalone). VERIFIED (manual)
- In Control Mode connect the power supply too, for full display brightness and no battery drain. VERIFIED (manual)
- User Mode: press the User button in Control Mode. Built-in functions turn off; the display shows only that User Mode is on. VERIFIED (manual, KB 209071249)
- User Mode in Standalone: build a Set with mappings in Control Mode, save it, transfer it to Push. VERIFIED (manual)
- Push 2 "Live mode" and "User mode" are also MIDI modes set by SysEx (section 5). VERIFIED (push-interface)
- User Mode steps in Live: Preferences, Link/Tempo/MIDI, User Port: Track and Remote on for input, Remote on for output. Encoders: Relative (lin 2's Comp.) mapping. VERIFIED (KB 209071249)
- In User Mode all buttons send momentary CC (cannot toggle); touching an encoder sends a Note, turning sends CC; pads on Push 1/2 send Notes; the User button cannot be mapped. VERIFIED (KB 209071249)
- Push 3 pads as remote: set Expression Mode to Poly or Mono Aftertouch in Control Mode before entering User Mode. VERIFIED (KB 209071249)

## 4. Connections and power
- Push 3 back: USB-C to computer (Control Mode, also its audio interface); USB-A for class-compliant MIDI devices and hubs; MIDI in/out on TRS-A; sustain pedal works, expression pedal does not. VERIFIED (Technical FAQ, Connecting article)
- Push 3 keyboards, mice and touchscreens on USB-A: not supported. Third-party sound cards over USB-A: not supported. VERIFIED (Technical FAQ)
- Push 3 power: yellow button on the back; hold 3 s to power off; hold 10 s to force off. VERIFIED (manual)
- Use only the included power supply. VERIFIED (Technical FAQ). Heat sink gets hot; max ambient 40 C. VERIFIED (same)
- Push 3 Standalone Wi-Fi: hotspot (Setup, Status; Wi-Fi then Hotspot) for file transfer and Link; a device on the hotspot loses internet. VERIFIED (Push release notes 2.1, Connecting article)
- Push 2 on USB power only: display and pads dim. VERIFIED (Using Push 2 FAQ)

## 5. MIDI implementation (Push 2, official)
Source: github.com/Ableton/push-interface, doc/AbletonPush2MIDIDisplayInterface.asc, revision 1.1, firmware 1.0.60. VERIFIED (read in full). Push 3 has no published equivalent: UNVERIFIED (none found).
- Two MIDI ports: Live port and User port. Linux names: "Ableton Push 2 nn:0" (Live) and ":1" (User). VERIFIED
- Only one program can open a port. For an outside app, turn Track/Sync/Remote off for the User port in Live. VERIFIED
- Pads: Note On 0x90 / Note Off 0x80; notes 36 (bottom left) to 99 (top right). VERIFIED (examples: 36 and 99; "36-99" in the chart)
- Buttons: CC 0xB0, value 127 pressed, 0 released. Example: metronome is CC 9. VERIFIED
- Encoders: turn = CC, relative two's complement (1 to 63 right, 127 to 64 left); touch = Note On velocity 127, release 0. Examples: master encoder CC 79, tempo CC 14, leftmost track encoder note 71. VERIFIED
- The full number table (every button and encoder) is an image in the doc. I did not read it: UNVERIFIED. Capture instead.
- Aftertouch: channel pressure by default, or poly key pressure (SysEx 0x1E). VERIFIED
- Touch strip: touch as Note, position as pitch bend; LEDs set by SysEx 0x19. VERIFIED
- SysEx frame: F0 00 21 1D 01 01 [command id] [args] F7. VERIFIED
- Useful commands: 0x0A set MIDI mode (0 Live, 1 User, 2 Dual); 0x03 set colour palette entry; 0x05 reapply palette; 0x06 LED brightness; 0x08 display brightness; 0x1A statistics (shows if external power is attached). VERIFIED
- Do not send undocumented or reserved commands: the doc warns they can brick the unit. VERIFIED
- Push 1 MIDI map: UNVERIFIED (not read).

## 6. Pad and LED colour (Push 2)
- Set an LED: Note On (pads) or CC (buttons), number picks the LED, velocity 0 to 127 picks a palette colour. VERIFIED
- MIDI channel picks animation (blink, pulse, one shot); channel 0 means none. VERIFIED
- Examples: 0x90 0x63 0x7F top right pad red; 0x90 0x24 0x7E bottom left pad green. VERIFIED
- Colour index 127 red, 126 green, 125 blue, 124 dark grey, 123 light grey, 122 white, 0 black. Doc says other entries may change; read the rest with SysEx 0x04. VERIFIED
- The palette can be rewritten with SysEx 0x03 then 0x05. VERIFIED
- Pad and colour behaviour on Push 1 and Push 3: UNVERIFIED.

## 7. Push 2 display
- USB composite device: MIDI plus one bulk interface for the display; use libusb. VID 0x2982, PID 0x1967. Bulk OUT endpoint 0x01. VERIFIED
- Per frame: send the 16 byte header FF CC AA 88 then 12 zero bytes; then 160 lines, each 2048 bytes (1920 pixel bytes plus 128 filler). VERIFIED
- Pixel: 16 bit little endian, bits b4..b0 g5..g0 r4..r0 (BGR565). XOR every line with pattern E7 F3 E7 FF repeating. VERIFIED
- Python library push2-python (MIT) wraps all of this; tested by its author only on macOS (Linux and Windows untested). COMMUNITY (github.com/ffont/push2-python)
- Windows display driver is a separate installer for Push 3 (named push2-display-driver-installer). VERIFIED (KB 10295607009436). Whether Push 3's display uses the Push 2 protocol: UNVERIFIED.

## 8. Python Remote Scripts
- Push 1 and 2 scripts are readable on GitHub as decompiled copies from the gluon account (Live 10). COMMUNITY (Cycling '74 forum)
- Push 3 script is not Python and is not among the Live 12 scripts. COMMUNITY (Cycling '74 thread). Ableton note: Push 2 now uses the same technology as Push 3 instead of a remote script; option -Push2UseLegacyScript in Options.txt. COMMUNITY (same thread, quoting release notes; I did not read the note myself)
- Script folders: Windows `\ProgramData\Ableton\Live x.x\Resources\MIDI Remote Scripts\`; macOS `/Applications/Ableton Live X.app/Contents/App Resources/MIDI Remote Scripts/`. Put a new script in its own subfolder. COMMUNITY (blog.azuki.vip, written for Live 10)
- Log: macOS `~/Library/Preferences/Ableton/Live x.x.x/Log.txt`; Windows `\Users\[name]\AppData\Roaming\Ableton\Live x.x.x\Preferences\Log.txt`. COMMUNITY (same)
- Live 12 uses Python 3.11 and can no longer be reliably decompiled; unofficial docs exist (forum p=1837228). COMMUNITY
- Official scripts: Ableton ships them inside Live. Third-party: copy a folder, pick it under Control Surface. Back up first. COMMUNITY
- Push 3 Standalone: users cannot upload their own remote scripts (2023). COMMUNITY (Ableton moderator, forum p=1810817). Push software 2.4 adds a Control Scripts page for supported third-party controllers. VERIFIED (release notes 2.4 snippet via Push manual search)
- Max for Live Python API gained a pad_layout property on Push 2/3 (Live 12.3). VERIFIED (release notes 2.3)

## 9. Max for Live
- On Push 3 Standalone most Core Library M4L devices work; third-party ones are not guaranteed. Connection Kit devices (Arduino, Camera, OSC Send, etc.) do not work. VERIFIED (KB 8506527153308)
- New mappings, sample import and sequencer note entry are limited in M4L on Push standalone. VERIFIED (same)
- M4L cannot draw custom graphics on the Push display (Dec 2023 to Oct 2024). COMMUNITY (forum p=1819601)
- Push 3 control objects show as generic ControlProxy; some Push 2 patches break. COMMUNITY (Cycling '74 thread)

## 10. Linux and Bazzite reality
- No official Live for Linux. Bitwig is a native Linux host (bitwig-studio skill). Live under Wine: skills ableton-live and max-for-live-expert section 14. Push through the Wine project: see section 10a.
- Push 2: Ardour has supported it since 5.4 with USB 2 or 3, no power supply needed (only brighter). VERIFIED (manual.ardour.org)
- Push 2 on Linux needs a udev rule: `SUBSYSTEM=="usb", ATTR{idVendor}=="2982", ATTR{idProduct}=="1967", MODE="0666", GROUP="audio"`, user in group audio. VERIFIED (Ardour manual). On immutable Bazzite, where the file goes and reload steps: UNVERIFIED.
- Push 2 in Bitwig: DrivenByMoss (LGPL-3.0, Push I/II listed, repo has Linux scripts); a 2015 article says Push 2 works in Bitwig on Linux. VERIFIED (github.com/git-moss/DrivenByMoss, cdm.link). Push 3 not mentioned on the repo page: UNVERIFIED for 3.
- Reaper: only a 2014 OSC tool by darth_fader (.exe, Windows likely). COMMUNITY (forum p=1600426). No current Reaper Push support found: UNVERIFIED.
- Push 3 as plain USB MIDI on Linux: UNVERIFIED. Push 3 display on Linux: UNVERIFIED. Test with `aseqdump -l` and `lsusb` first.

## 10a. Run it on Linux (Wine, Bottles, Proton) or alternatives
Push is hardware; it needs Live (or its own standalone). Three ways, best sourced first.
Way 1: Push 3 Standalone. It runs Live 12 Intro itself, no Linux computer needed. VERIFIED (Push 3 Technical FAQ). Use Control Mode only if a computer runs Live.
Way 2: Live in the unofficial Wine project (github.com/shibco/ableton-linux, LGPL-2.1, not Ableton's). Install steps and requirements: max-for-live-expert section 14, Recipe A. Then:
1. Push 1: connect it, start Live; Live detects it. VERIFIED (README)
2. Push 2: connect BEFORE starting Live. Settings > Link, Tempo & MIDI: one row, control surface `Push2`, input and output "Ableton Push 2 Live Port", Remote on for both. Remove extra rows. VERIFIED (README, TROUBLESHOOTING.md)
3. Push 2 display dark: close Live, replug Push 2, start Live. VERIFIED (TROUBLESHOOTING.md)
4. Push 3: the README gives a udev rule; the troubleshooting page says Push 3 and Move are not supported yet. The pages disagree, so UNVERIFIED. If you try (Live 12, Control Mode):
   a. `printf '%s\n' 'SUBSYSTEM=="usb", ATTR{idVendor}=="2982", ATTR{idProduct}=="1969", MODE="0660", TAG+="uaccess"' | sudo tee /etc/udev/rules.d/60-ableton-push3.rules >/dev/null`
   b. `sudo udevadm control --reload-rules`
   c. On a Standalone Push 3 pick Control Mode. Unplug, replug, then start Live.
   d. Leave the Push 3 control-surface rows empty; Live creates it. Firmware update prompts: follow them. VERIFIED (README for a to d). Whether /etc/udev is writable and persistent on Bazzite: UNVERIFIED (/etc is writable on Atomic, COMMUNITY, linux-audio-production skill).
5. Audio: pick the interface or Push as Audio Device under ASIO > PipeASIO. Whether Push 3 as audio interface appears under PipeASIO: UNVERIFIED.
Way 3: Push 2 with a native Linux DAW.
1. Ardour supports Push 2 (since 5.4, USB 2 or 3). Udev rule for Push 2: `SUBSYSTEM=="usb", ATTR{idVendor}=="2982", ATTR{idProduct}=="1967", MODE="0666", GROUP="audio"`, user in group audio. VERIFIED (Ardour manual). Bazzite placement: UNVERIFIED.
2. Bitwig: DrivenByMoss supports Push 1 and 2. VERIFIED (repo). See skill bitwig-studio.
Wine/Bottles by hand for Live: skill wine-proton-bottles plus max-for-live-expert Recipe B. Push through that route: UNVERIFIED.
TEST checklist:
1. `lsusb` lists 2982 (VID for Ableton). UNVERIFIED command output; VID value VERIFIED (push-interface).
2. Pads light when Live starts. 3. Display shows Live content. 4. Play pads, hear sound. 5. Turn an encoder, see a value change. 6. Save a Set, reopen. 7. Unplug and replug while Live runs. 8. Restart the PC and repeat.
Known problems: Push 2 display dark (Way 2 step 3); Push 3 unsupported per one page; one program per MIDI port (section 5); dim display without AC (Push 2).
Backup: Sets before any Push or Live update (section 11); the Wine prefix per max-for-live-expert section 14.
Do NOT rely on it for gigs. Gig plan: Push 3 Standalone, or a Windows/Mac laptop.

## 11. Updates and recovery
- Standalone: asterisk on the Software tab, press Update; keep the power supply connected; software includes firmware; it restarts. VERIFIED (manual)
- Control Mode: Live updates carry Push software; do not unplug mid-update. UNVERIFIED (Updating Push 3 article failed to fetch).
- Newest release page seen: Push 2.4.7 with Live 12.4.7, 22 Oct 2026. VERIFIED (release-notes/push-12)
- Stuck booting with flashing pads: power off, power on, when pads blink wait 5 s, hold power until off, power on; backup software starts. VERIFIED (KB 12439522504860)
- Recovery Method 1 (Wi-Fi): download latest .swu, hold User and press Power, choose "Start Push in Recovery Mode", go to http://push.local/update. VERIFIED (KB 10726712498076)
- Recovery Method 2: USB-A drive (8 GB+) flashed with the recovery image in BalenaEtcher, same boot choice. It deletes all data on Push's drive. VERIFIED (same)
- Back up Sets before any update or recovery.

## 12. Troubleshooting (one change at a time)
- No lights or display: power supply in, hard power off 10 s, retry. VERIFIED (manual). Try the included PSU and a different USB port; USB power article (9109387410716) failed to fetch, so specifics UNVERIFIED.
- Push 2 pads lit but display flashing on MacBook: turn off Automatic graphics switching. VERIFIED (KB 360001045784); Mac only.
- Windows Push 3 display dead: uninstall "Ableton Push 3 Display" in Device Manager, replug, start Live. VERIFIED (KB 10295607009436)
- Dim display or pads: no AC adapter (Push 2) or low battery (Push 3). VERIFIED
- Log which step fixed it.

## 13. What Claude can build, and what is blocked
Realistic:
- A Push 2 pad light show, display app, or custom controller on Linux or any OS with push2-python or libusb plus MIDI, using the User port. Needs the udev rule on Linux.
- User Mode mappings in Live or Bitwig for Push 1/2/3 (no code).
- A Max for Live device that reads Push 3 controls: works for basics, fragile.
- A Python Remote Script for a Push-like controller in Live (not Push 3 itself).
- Push 3 Standalone: MIDI through USB-A controllers; Wi-Fi file transfer; Push Hack over SSH (unofficial, section 14).
Blocked or unproven:
- Push 3 official display or MIDI spec: none found. Do not invent bytes.
- Uploading a user Remote Script to Push 3 Standalone: not supported. M4L custom display on Push 3: no.
- Firmware flashing or undocumented SysEx: refuse.
- Running Live natively on Linux: impossible.

## 14. Push 3 Standalone hacking (unofficial)
- It runs Linux; SSH was set up by registering a public key at push.local/ssh (2023). COMMUNITY (forum p=1815827)
- Push Hack (MIT, github.com/federico-pepe/ableton-push-hack) offers display takeover, LED and MIDI control via SSH. Not endorsed by Ableton; reinstall after each Push update; an update with it present can freeze the unit. VERIFIED (README)
- Warranty effect: UNVERIFIED. Replacing the SSD needed re-activation once. COMMUNITY. Always back up first.

## Not verified
Push 1 hardware and MIDI map; full Push 2 number image; Push 3 USB MIDI/display protocol; Push 3 on Linux (Wine project pages disagree); bundled Live per model; Updating Push 3 article and USB power FAQ (fetch failed); Ardour udev fix outcome; Reaper current support; Reddit and Cycling '74 not searched directly; bundled Live edition per model; Push 3 price; Bazzite udev steps; gluon repo page (fetch failed).

## Sources (fetched)
- github.com/Ableton/push-interface (README, doc .asc rev 1.1); github.com/Ableton (repo list)
- ableton.com/en/push/tech-specs; ableton.com/en/push; ableton.com/en/release-notes/push-12
- help.ableton.com: 8483166334748, 8483411204252, 115000036770, 209774445, 209072549, 209071249, 10726712498076, 12439522504860, 8506527153308, 10295607009436, 360001045784
- Push 3 manual and Push release notes via Ableton Knowledge search tool (manual page itself failed to fetch)
- manual.ardour.org/using-control-surfaces/Ableton_Push2; discourse.ardour.org/t/unable-to-enable-ableton-push-2-in-linux/104342
- github.com/shibco/ableton-linux (README, TROUBLESHOOTING.md); help.ableton.com 115001663530 and 115000036770 (Live and Push requirements); Push release notes 2.3.x (via Ableton knowledge search)
- github.com/ffont/push2-python; github.com/git-moss/DrivenByMoss; github.com/federico-pepe/ableton-push-hack; github.com/Maus3rVonDutch/ableton-ssl-uf8-scripts
- cdm.link (Push 2 in Bitwig, Push Hack); isotonikstudios.com Push Hack post; blog.azuki.vip/ableton-midi
- forum.ableton.com p=1837228, 1815827, 1810817, 1811648, 1810805, 1819601, 1600426; cycling74.com forums (push12-vs-push3 thread, remote scripts 10.0.2 thread); elektronauts Overbridge thread
