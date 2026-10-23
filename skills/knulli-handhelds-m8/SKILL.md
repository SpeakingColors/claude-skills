---
name: knulli-handhelds-m8
description: Use when setting up Knulli CFW on a Trimui Brick/Brick Pro or Anbernic handheld, or running Dirtywave M8 Headless (Teensy 4.1) with m8c on one.
---

# Knulli handhelds and M8 Headless

Labels: VERIFIED (source number in brackets, see Sources), COMMUNITY (forum, blog, guide author, or as reported by users), UNVERIFIED (not found, do not present as fact).
Research date 2026-10-21. Some pages (knulli.org device pages, Trimui page) could not be fetched; they are listed as gaps.
Assume the reader is not a programmer: be concrete, label what is unverified, keep answers short, one step at a time.

## Brick Pro builds
- COMMUNITY (as reported by users, source: the earlier research notes behind this skill and [4]): The Trimui Brick Pro is not on the public Knulli release page. Builds for it have been distributed through the Knulli Discord, reportedly via a donation and an alpha channel. No public page documents this.
- The Brick Pro is not on the public release page [2], so do NOT send the reader to GitHub for a Brick Pro image. Ask the reader which file and version they have, and where it came from, before advising on flashing or updates.
- It is good to join the Knulli Discord and support the project via donation to get access to Brick Pro builds. Do not ask for or share personal names, handles or amounts.
- If the reader also runs Dirtywave M8 Headless on a Teensy board on the handheld, see the M8 sections below. Anbernic models vary: ask which model.

## What Knulli is
- VERIFIED [1]: Knulli is a custom firmware, a fork of Batocera for low-powered handhelds and devices without open kernel sources.
- VERIFIED [1]: Successor to the unmaintained Batocera v39/40 beta for RG35XX Plus/H.
- VERIFIED [2]: Release names so far include Gladiator II and Scarab. Scarab is tag 20260511, marked "Latest", no alpha/beta label on the release page.
- VERIFIED [2]: Scarab needs a re-flash (SD card 1 partition table changed), system folder configs do not carry over, clean install strongly recommended, migration guide exists, SD card 2 auto-migrates legacy userdata.
- VERIFIED [2]: Scarab changes: RetroArch 1.22.2, standalone Yabasanshiro (Saturn), Syncthing improvements, BatteryPlus, Silky RGB LED support.

## What "Scarab" and "Scarab Alpha" mean
- VERIFIED [2][3]: "Scarab" is the release codename of Knulli version 20260511.
- COMMUNITY [4]: A reviewer said "a fresh KNULLI Alpha" was available for the Brick Pro; a photo caption reads "TrimUI Brick Pro - KNULLI Scarab".
- COMMUNITY (as reported by users): the Brick Pro build is distributed through the Discord alpha channel, which matches the reviewer. No public page documents it.
- UNVERIFIED: the exact string "Scarab Alpha". Treat it as a reported name some users use for the Discord Brick Pro build of the Scarab line.
- UNVERIFIED: any Brick Pro asset on GitHub. The 20260511 release page lists "TrimUI Smart Pro, Brick/Hammer" only [2].

## Supported devices (check the live release page before flashing)
- VERIFIED [2] (release 20260511, stable downloads): Anbernic RG28XX, RG34XX, RG34XX-SP, RG35XX-PRO, RG35XX Plus/2024, RG35XX H, RG35XX SP, RG40XX H, RG40XX V, RGCubeXX.
- VERIFIED [2]: TrimUI Smart Pro and Brick/Hammer have stable downloads. Brick Pro is NOT on the public page (COMMUNITY: it is available via the Discord alpha channel).
- VERIFIED [2]: Other listed: Powkiddy V90S/V20/A12/A13, PS5000/PS7000, R36S, BATLEXP G350, MAGICX Mini M. GKD Pixel2 listed without a link.
- VERIFIED [3]: Scarab notes also name Miyoo Flip, Powkiddy X55, Retroid Pocket 5 as newly added (status per device not verified).
- VERIFIED [5]: The older device table showed Brick (Allwinner A133) and Smart Pro with builds, Brick Pro not mentioned. Page said "Do not attempt to install a package for a different device".
- COMMUNITY [4]: Brick Pro shares internals with Brick/Brick Hammer (A133 Plus, 1 GB RAM, 3.95 in 1024x768), so ports are expected to be easier.
- COMMUNITY [8]: Older Brick guide called Knulli "pre-alpha, some features broken". That was 2024 era; do not assume it applies now.
- UNVERIFIED: Per-feature status (wifi, bluetooth, audio, USB host) on Brick Pro alpha.

## Install, update and dual boot
- VERIFIED [6]: Download the image for your exact device from the latest GitHub release, flash it to an SD card, let Knulli format storage. Do not format manually afterwards. Remove SD cards from other slots before first boot. First boot is slow (partition expand). For the Brick Pro the image comes from the Discord instead (COMMUNITY, as reported by users).
- VERIFIED [6]: One card works; for long term use put OS on card 1 and games, themes, saves on card 2. Built-in formatter can switch to ext4.
- COMMUNITY [7]: Flash with Rufus (OS card in slot 1), format data card exFAT non-bootable. Another guide [8] used Balena Etcher on the Brick.
- COMMUNITY [4]: On Brick Pro the reviewer ran Knulli from a microSD and switched back to stock by changing cards. No dual boot mechanism documented. UNVERIFIED: any bootloader dual boot.
- VERIFIED [6]: Update docs are separate pages (Update, Major Updates). FAQ [1] says most releases allow a manual update; some need a fresh flash. Alpha-channel builds may update differently: ask the reader how their build updates (UNVERIFIED).
- COMMUNITY [7]: Update from Start > Updates & Downloads, set Update Type to Stable, run over wifi.
- UNVERIFIED: Trimui-specific boot steps (knulli.org Trimui page was blocked).

## Folder layout, BIOS, saves
- VERIFIED [6]: Games in `roms/<system>/`. BIOS files go in `bios/` on the share partition.
- VERIFIED [9]: Share name `share` maps to `/userdata`. Files outside `/userdata` are read-only and reset on reboot.
- COMMUNITY [7]: `saves/` holds saves and states; `cheats/` holds cheats.
- COMMUNITY [10]: Check missing BIOS at Main Menu > Game Settings > Missing Bios Check. Read `_info.txt` in an emulator folder first.
- VERIFIED [9]: After copying games run Start > Game Settings > Update gamelists.

## Network: wifi, ssh, samba
- VERIFIED [6]: Wifi under Start > Network settings. If it fails try router WPA1+WPA2 instead of WPA2+WPA3; experimental WIRELESS_HYBRID_FIX under System Settings > Services.
- COMMUNITY [7][10]: Use a 2.4 GHz SSID; same-name dual band SSIDs caused failures.
- VERIFIED [11]: SSH user `root`, default password `linux`. Enable in System Settings > Services (Scarab and later). `ssh root@knulli`. Change password in System settings > Security.
- VERIFIED [9]: Samba is off by default (since Gladiator II). Enable in Services. `\\\\KNULLI` or `smb://KNULLI`, user root, password linux. SFTP port 22. HTTP transfer not supported.

## Menus, controls, extras
- COMMUNITY [7]: Themes in User Interface Settings; more via Updates & Downloads (needs wifi). Shaders in Game Settings > Game Rendering & Shaders (global). Per-system settings in Per System Advanced Configuration; per-game by long press A.
- COMMUNITY [10]: Pair Bluetooth in Controller & Bluetooth Settings; Controller Mapping and Player Assignments for assignments; A/B swap under Frontend Developer Options; per-game PadToKey profile via long press A.
- COMMUNITY [7]: Author set RetroArch hotkeys (save state R1, load L1, rewind L2, fast forward R2). Verify defaults on the Knulli hotkey page before relying on them.
- VERIFIED [6]: Scraper supports ScreenScraper, TheGamesDB, ArcadeDB. ScreenScraper needs a free account.
- VERIFIED [6]: PortMaster: connect wifi, run `Install.PortMaster` from Ports. COMMUNITY [10]: some ports need the ROM card as ext4.
- VERIFIED [6]: RetroAchievements credentials under Game Settings > RetroAchievement Settings.

## M8 Headless on Teensy 4.1
- VERIFIED [12]: Firmware repo is Dirtywave/M8HeadlessFirmware, for a Teensy 4.1 connected to a host over USB. Teensy 4.0 or older will not work.
- VERIFIED [12]: microSD FAT32, good random read speed. Known good: Lexar Professional 1800x 64GB, SanDisk 32GB Ultra microSDHC. Samples in `/Samples`, WAV mono or stereo, full path max 127 chars.
- VERIFIED [13]: Flash steps: download `M8_Vx_x_x_HEADLESS.hex` via right click "View raw" (not the Download button); unplug other Teensy/M8 devices; connect Teensy directly, no hub; open TyUploader (TyTools), pick Teensy (may show HalfKay, Teensyduino or M8), Upload the hex; name changes to "M8" when done.
- VERIFIED [13]: Update by repeating the same flash with the newest hex. "IHEX parse error" means a bad download. White button on Teensy resets.
- VERIFIED [13]: Display clients: M8WebDisplay (m8.run), m8c, TouchDesigner. Official audio guidance is to monitor the "M8 Input" USB audio device on the computer.
- VERIFIED [14]: Latest changelog seen: 6.5.2 C (2026-04-13). 6.5.0 added USB Drive mode, 24-bit USB audio at lower latency, multichannel USB audio routing.
- VERIFIED [13]: Backup: close the client, unplug Teensy, remove card, copy to a computer. Card slot is not spring loaded; reseat fully. Formatting erases the card; cards over 32GB: exFAT.
- UNVERIFIED: Dirtywave's own docs on running headless on handhelds or Knulli.

## m8c client
- VERIFIED [15]: laamaa/m8c supports Linux (AppImage), Windows, macOS. Config `config.ini` in `~/.local/share/m8c` (Linux). `--list` lists devices, `--dev` forces a port, `--config` loads another file.
- VERIFIED [15]: Default keys: arrows move, Z/Left Shift = Shift, X/Space = Play, A/Left Alt = Opt, S/Left Ctrl = Edit, Esc = keyjazz, F1 config, F2 log, F12 audio routing toggle, R resets display.
- VERIFIED [15]: Gamepads use SDL controller mappings; custom `gamecontrollerdb.txt` goes beside `config.ini`. Hold Back/Select ~2 s opens the menu only when no M8 is connected. Gamepad reset is Select+Start+Opt+Edit.
- VERIFIED [15]: Audio routing options `audio_buffer_size` (0 = SDL default) and `audio_device_name`.

## M8 on Trimui Brick (Knulli)
- COMMUNITY [16]: A paid written guide (Gumroad) covers m8c on the TrimUI Brick. It names only the Brick, does not mention Knulli on the visible page, and its steps were not visible. Do not treat as official.
- UNVERIFIED: That m8c runs on Knulli Scarab/Scarab Alpha on Brick Pro, how it is installed (PortMaster, native port, or stock OS app), keymap mapping to Brick Pro buttons, USB host/OTG behavior, bus power to the Teensy, and audio latency. No source found. If the reader already has this running, ask how it is launched and what they see before guessing.
- VERIFIED [8]: Brick USB-C is listed as charging, data, USB host. No OTG steps given. Brick Pro behavior unverified.
- Practical plan for diagnosing a rig (advice, not verified results): SSH in, `lsusb` to see the Teensy, check `/dev/ttyACM*` exists, `aplay -l` for the "M8" USB audio device, then measure latency by ear. Try a powered OTG hub or Y cable if the Teensy resets.

## Troubleshooting
- No boot after flashing: reseat card, confirm correct device image, remove other cards (VERIFIED [6]). Reset button pressed after a previous CFW card (COMMUNITY [7]).
- Wifi fails: 2.4 GHz, WPA1+WPA2, hybrid fix option (VERIFIED [6], COMMUNITY [10]).
- Games missing: Update gamelists (VERIFIED [9]); remove Apple `._*` files (COMMUNITY [10]).
- Black screen in TouchDesigner or "IHEX parse error": reflash with a fresh hex (VERIFIED [13]).
- m8c "No M8 device found": check cable, headless firmware, `--list`; Linux serial permission (dialout group) (VERIFIED [15]).
- No m8c audio: toggle routing F12, set `audio_device_name` (VERIFIED [15]).
- Missing M8 samples: Teensy cannot see card, reseat (VERIFIED [13]).

## Safe procedure before flashing
- Confirm which exact file the reader has and where it came from (Discord alpha channel for the Brick Pro); do not mix Brick and Brick Pro images [2][5].
- Back up the stock card or device data first (a Brick guide notes another CFW overwrote ROMs and BIOS) [8].
- Use a spare SD card for the OS; keep the stock card untouched so you can swap back [4].
- Verify the target drive letter before flashing; the wrong drive gets erased [8].
- Copy off saves, BIOS and ROMs before any major update or reflash; Scarab wipes legacy layout [2].
- Charge the battery above 50 percent; do not unplug during first boot expansion.
- For the Teensy: back up the M8 SD card, note current firmware version, unplug all other M8/Teensy devices, no USB hub [13].
- Keep a copy of the old hex so you can roll back.

## Sources
1. https://knulli.org/faq/knulli/
2. https://github.com/knulli-cfw/knulli-linux/releases (tag 20260511, Scarab)
3. https://newreleases.io/project/github/knulli-cfw/knulli-linux/release/20260511
4. https://retrohandhelds.gg/?p=40559 (Brick Pro, Knulli Alpha)
5. https://knulli.org/devices/
6. https://knulli.org/play/quick-start
7. https://joeysretrohandhelds.com/guides/knulli-setup-guide/
8. https://retrohandhelds.gg/trimui-brick-setup-guide/
9. https://knulli.org/play/add-games/network-transfer/
10. https://github.com/LennartHennigs/Knulli-and-RGXX-Notes
11. https://knulli.org/configure/ssh/
12. https://github.com/Dirtywave/M8HeadlessFirmware
13. https://github.com/Dirtywave/M8Docs/blob/main/docs/M8HeadlessSetup.md
14. https://github.com/Dirtywave/M8HeadlessFirmware/blob/main/changelog.txt
15. https://github.com/laamaa/m8c
16. https://louiewithapen.gumroad.com/l/m8c
Not fetched (blocked): knulli.org home and Trimui device pages. Not found: Reddit/forum threads on M8 on Knulli.
