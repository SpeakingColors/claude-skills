---
name: rog-ally-x-bazzite
description: Use when helping with the ASUS ROG Ally X running Bazzite-Deck, covering specs, setup, controls, TDP, firmware, SSD swap, known issues, plus a Bazzite deck setup on a desktop PC.
---

# ROG Ally X on Bazzite
## How to work with the reader
- Assume the reader is not a programmer: plain words first, then the exact step.
- One change at a time. After each change, ask the reader to test before the next one.
- Label claims: VERIFIED (source), COMMUNITY (forum or user report), UNVERIFIED (not confirmed, say so, never guess).
- Bazzite changes fast. Check the version first: run `rpm-ostree status` in a terminal (UNVERIFIED as an Ally-specific step, standard Bazzite command; docs page fetched only mentions `rpm-ostree rollback`).
## Big warning: Bazzite 44 changed the handheld stack
- VERIFIED (windowsforum Bazzite 44 article): Bazzite 44 (stable 44.20260820) removed Handheld Daemon (hhd). It is replaced by InputPlumber, SteamOS-Manager, PowerStation, OpenGamepadUI.
- VERIFIED (GamingOnLinux Bazzite 44, Bazzite Handheld Wiki page): TDP is now in the Steam Quick Access Menu (QAM), RGB too; OpenGamepadUI (OGUI) adds extras.
- VERIFIED (Bazzite Handheld Wiki): Guide + B opens OGUI on any device as a fallback.
- Old guides that say "open the HHD overlay" or "set charge limit in HHD" are out of date for 44. VERIFIED (Universal Blue Discourse Ally page 2414) says that older page itself is old documentation.
- The Bazzite ASUS Ally page says "may contain outdated information". VERIFIED (docs.bazzite.gg ASUS page). Treat its issue list as hints, not current truth.
- COMMUNITY (windowsforum): early 44 reports are mixed: lost mappings, missing TDP slider, dock problems, Decky crashes.
- Before any big update: keep the old deployment for rollback. VERIFIED (Bazzite docs): `rpm-ostree rollback`, or pick the old entry in the GRUB menu.
- Rollback restores the OS only, not game data or Steam profiles. VERIFIED (windowsforum).
## Specs (ROG Ally X, model RC72LA)
- CPU: Ryzen Z1 Extreme, 8 cores 16 threads, Zen 4, RDNA 3, 4 nm. VERIFIED (ASUS spec page).
- RAM: 24 GB LPDDR5X 7500 MHz, shared with the GPU. VERIFIED (ASUS).
- Battery: 80 Wh. VERIFIED (ASUS, iFixit).
- Display: 7 inch, 1920x1080, 120 Hz, 500 nits, FreeSync Premium, touch. VERIFIED (ASUS).
- Ports: USB 3.2 Gen 2 Type-C (DP 1.4, PD 3.0); USB4 Type-C, Thunderbolt 4 compatible (DP 1.4, PD 3.0); 3.5 mm combo jack; UHS-II microSD. VERIFIED (ASUS).
- Wireless: Wi-Fi 6E; Bluetooth 5.2. VERIFIED (iFixit); ASUS page did not list Bluetooth.
- Storage: PCIe 4.0 M.2 2280 SSD, 1 TB (2 TB variant exists). VERIFIED (iFixit, ASUS SSD guide).
## Which Bazzite image
- Handheld: the `-deck` family. VERIFIED (Bazzite FAQ): `bazzite-deck` (KDE) for AMD, `bazzite-deck-gnome` for GNOME.
- If the Ally X already runs bazzite-deck, keep KDE; do not switch desktop environments later. VERIFIED (Bazzite rebase page warns against it).
- Switching between `bazzite` and `bazzite-deck` (both KDE) is covered by the official rebase guide ("Rebase to other Fedora Atomic Desktop images including other Bazzite images"): `brh rebase bazzite:stable` or `brh rebase bazzite-deck:stable`, then reboot; files are kept. VERIFIED (docs.bazzite.gg rebase guide). The deck/desktop pair is not named there, so back up first.
- Deck image boots into Steam Gaming Mode, includes a Desktop Mode session, updates are manual from Gaming Mode and apply on reboot. VERIFIED (Bazzite FAQ).
- Desktop images have no Steam Gaming Mode. VERIFIED (FAQ).
## Install on the Ally X (only if reinstalling)
- Step 1: Update BIOS and firmware on Windows first, if still possible. COMMUNITY (Discourse Jan 2025: users did this; one got speaker audio fixed by a BIOS update).
- Step 2: Secure Boot. Easiest: leave it off. VERIFIED (Bazzite secure boot page) says if disabled choose "Continue boot" at the blue screen.
- Step 3: If Secure Boot is on: choose Enroll MOK, password `universalblue`, nothing shows while typing. VERIFIED (secure boot page).
- Step 4: After install, enroll later with `ujust enroll-secure-boot-key`, and `ujust bios` reboots to BIOS. VERIFIED (secure boot page, docs.bazzite.gg ujust page). The ujust page lists no handheld, charge-limit or firmware commands; `ujust --choose` shows more.
- A BIOS update can turn Secure Boot back on; "bad shim signature" black screen means redo enrollment. VERIFIED (secure boot page).
- BIOS entry key and exact BIOS menu names for Ally X: UNVERIFIED here (the SSD guide says hold volume down and press power to reach BIOS, VERIFIED ASUS SSD guide).
- Dual boot is supported per the official dual-boot guide. COMMUNITY (maintainer, Discourse).
## BIOS setting worth checking
- UMA / VRAM: set to 4 GB or 8 GB if some games crash with "Auto". VERIFIED (Bazzite ASUS page, Discourse 2414). Change only if crashes happen.
- SMT: suspend may break if SMT is disabled. VERIFIED (ASUS page). So leave SMT on.
## Armoury Crate-less controls and buttons
- No Armoury Crate on Linux. InputPlumber handles controller input and remapping in 44. VERIFIED (GamingOnLinux 44).
- Armoury Crate side button: hold it for Mouse Mode. VERIFIED (ASUS Bazzite page, pre-44 text; recheck on 44, UNVERIFIED).
- Armoury Crate button on 44: for ROG Ally devices, single press opens the QAM, long press opens OGUI. VERIFIED (Bazzite Handheld Wiki). The wiki does not name the Ally X or use the words "Command Center".
- Command Center button mapping on 44 in InputPlumber: UNVERIFIED (not on the wiki or the InputPlumber README). The only user report found is a Xbox Ally post on HHD where a Steam Keyboard shortcut on that button did nothing. COMMUNITY (Discourse 12291, pre-44). Ask the reader to test each button in Steam Settings, Controller, one at a time.
- Controller emulation: DualSense gives most functions, Xbox emulation removes some. Paddles: use DualSense Edge or Steam Deck setting. VERIFIED (Bazzite Handheld Wiki).
- Holding Steam or QAM buttons is not supported; Steam chords may fail; swapping Start and Select helps. VERIFIED (ASUS page, pre-44).
- A Sept 6 fix: some devices wrongly emulated Steam Deck and broke Steam+A/B shortcuts; reported resolved. VERIFIED (Discourse Sept 6).
- On-screen keyboard has no default binding: Steam, Settings, Controller, Desktop Layout. VERIFIED (Handheld Wiki).
- Desktop controller layout missing: fix in Steam controller settings. VERIFIED (Handheld Wiki).
- KDE Plasma 6.7 desktop controller feature conflicts with Steam emulation. VERIFIED (Handheld Wiki).
## TDP, fan, CPU boost
- TDP: Steam QAM, lightning bolt icon, enable Advanced options, TDP dropdown or Custom. VERIFIED (Handheld Wiki).
- If sliders are missing: pick the Performance profile, scroll down, enable TDP and GPU Clocks. VERIFIED (Handheld Wiki).
- Use only ONE TDP method (Steam, OGUI, or a Decky plugin). They conflict. VERIFIED (Handheld Wiki).
- OGUI showing "TDP managed by Steam" means Steam is in control. VERIFIED (Handheld Wiki).
- CPU boost is off by default to limit power draw. VERIFIED (ASUS page).
- Stuck TDP after unplugging the charger in standby: plug and unplug while NOT in standby. VERIFIED (ASUS page, pre-44).
- Fan curves: Bazzite devs say fan control is missing on some devices for now and "all handhelds are designed to have sufficient cooling". VERIFIED (GamingOnLinux 44). Ally X specifically: UNVERIFIED. Desktop TDP and fan control are still in progress. VERIFIED (Sept 6 update, GamingOnLinux Sept 2026).
- The Jan 2025 fan algorithm work targeted Ayaneo, OneXPlayer and GPD, not the Ally. VERIFIED (Discourse 6200, pre-44). Decky PowerControl "supports TDP, GPU, and fan control on select devices"; fan curves are not mentioned. VERIFIED (Handheld Wiki). Whether it covers the Ally X: UNVERIFIED.
## Gyro, haptics, RGB
- Gyro not working: set controller emulation target in OGUI to deck-uhid. VERIFIED (Handheld Wiki).
- Haptics/rumble on Ally X on Bazzite 44: UNVERIFIED (not on the Handheld Wiki, Sept 6 update, or InputPlumber README). Hardware side: ASUS MCU V315 fixed an abnormal left vibrator sound, a Windows tool. VERIFIED (ASUS support page).
- RGB after 44: lost lighting control, lights stay on; ASUS Linux team is writing a new driver. VERIFIED (Sept 6 update). HueSync Decky plugin can turn stick LEDs off but not change color. COMMUNITY (one user, same thread).
- LED brightness at max cannot be changed outside Windows. VERIFIED (ASUS page, pre-44).
## Battery charge limit
- Old method was in HHD. VERIFIED (Discourse 2414, pre-44). Gone with HHD on 44.
- Current method on 44 for Ally X: UNVERIFIED. Not on the Handheld Wiki or Bazzite ASUS page.
- On SteamOS, Valve's Steam battery charge limit support for Ally and Ally X was added to steamos-manager; one user reports it works on SteamOS 3.8.16; another set 80 percent in Windows and it persisted. COMMUNITY (ValveSoftware/SteamOS issue 2097, not Bazzite). The Steam QAM limit on Bazzite 44: UNVERIFIED.
- Jan 2025: the Ally's battery preservation was disabled because the asus-wmi driver reset it, fix pending. VERIFIED (Discourse 6200, pre-44).
- COMMUNITY (CachyOS forum, other distro): charge limit vanished from Game Mode after a kernel update and reset to 100% after reboot; cause unconfirmed. Do not assume the same on Bazzite.
- asus-wmi kernel driver as the charge-limit path: UNVERIFIED (no page fetched confirms it).
## Suspend, sleep, wake
- Fixed in 44: Ally X could refuse to sleep if the controller was used during the sleep animation. VERIFIED (Sept 6 update).
- Wake animation on resume can cause erratic behavior; keep it off. VERIFIED (ASUS page, pre-44).
- Stuck after Extreme Standby: reported, no confirmed fix; another user praised standby. COMMUNITY (Discourse Jan 2025).
## Sound and mic
- Two audio devices appear ("Family 17h/19h/1ah HD Audio Controller" and "ROG Ally"); set both to the same volume. VERIFIED (ASUS page).
- Garbled mic: set input volume 10 to 15 percent. VERIFIED (ASUS page, Discord quirk).
- No speaker sound but headphones work: a BIOS update fixed it for one user. COMMUNITY (Discourse Jan 2025).
## Wi-Fi, Bluetooth
- After 44, some users had to re-enter Wi-Fi credentials. COMMUNITY (windowsforum summary of early reports).
## SD card reader issue
- Stutter on games from microSD: reader (Realtek RTS525A) sleeps after ~4 s idle and the 1.8 V switch fails, causing 1 to 2 s pauses. COMMUNITY (ASUS ROG forum post, Bazzite user).
- ASUS says Ally X is only validated on factory Windows, not Linux. VERIFIED (same post, ASUS agent).
- Workaround: a script writing 1 byte every 3 s (GitHub repo Ardetis/ROG-Ally-X-SD-Card-Stutter-Mitigation-Realtek-RTS525A-). COMMUNITY. Not tested by us. Advise: keep games on the internal SSD first.
- PCIe ASPM and runtime power management tweaks did not help. COMMUNITY (same post).
## Display, scaling, VRR
- Panel supports 120 Hz and FreeSync Premium. VERIFIED (ASUS).
- VRR "improved as far as gamescope allows" but imperfect. COMMUNITY (maintainer comment, Jan 2025; may be stale).
- UI scaling can be tuned in Gaming Mode / desktop. Exact steps for Ally X: UNVERIFIED.
## Gaming Mode vs Desktop Mode
- Gaming Mode is Steam Big Picture in gamescope, "gamepadUI". VERIFIED (Bazzite Steam Gaming Mode page).
- Shortcuts: Ctrl or Win +1 Steam menu, +2 QAM. VERIFIED (same page).
- Steam beta client is not supported; use stable. VERIFIED (same page).
- Some games and emulators need Steam Input off. VERIFIED (same page).
- Switching to Desktop Mode: Steam power menu. COMMUNITY (Decky README describes this for Steam Deck; assumed same on Bazzite-Deck, UNVERIFIED for Ally X).
## Docking, external display, eGPU, docked controller
- USB4 and USB-C DP 1.4 ports exist. VERIFIED (ASUS). Dock behaviour on Bazzite 44: UNVERIFIED (Handheld Wiki has no dock section); windowsforum advises testing docks and external displays after update.
- eGPU: follows the same GPU rules as Gaming Mode; Nvidia eGPUs unsupported (experimental `-deck-nvidia` image exists). VERIFIED (Handheld Wiki).
- Docked with an external gamepad: built-in controller can confuse some games. COMMUNITY (Discourse 12437). One user's workaround, resets on reboot: `sudo systemctl stop inputplumber && sudo systemctl disable inputplumber`; undo with `sudo systemctl enable --now inputplumber`. Risky: it also drops Ally button mapping while off. Offer only if the reader asks.
## Decky Loader and plugins
- Install: `ujust setup-decky`; open from QAM. VERIFIED (Handheld Wiki).
- Decky may break after updates; uninstall before reporting Bazzite bugs. VERIFIED (Handheld Wiki).
- TDP plugins named by Bazzite: SimpleDeckyTDP, PowerControl, Panel de Control (pick only one). VERIFIED (Handheld Wiki).
- HueSync (RGB), CSS Loader (controller glyph themes). VERIFIED (Handheld Wiki, Discourse 2414).
- SimpleTDP worked when other plugins first failed for one user. COMMUNITY (Discourse Jan 2025).
- 44 may need plugin updates. VERIFIED (windowsforum).
## BIOS and firmware updates
- ASUS ships BIOS and MCU via Armoury Crate SE or ASUS website; these are Windows tools. VERIFIED (ASUS ROG forum changelog, which listed Xbox Ally X RC73XA; standard Ally X RC72 had no entries there).
- Ways to flash: MyASUS, Armoury Crate SE (2.1.10.0+), ASUS Windows installer, or EZ Flash from FAT32 USB (battery 20 percent+, charger in). COMMUNITY (itechguides, third party).
- Ally X is RC72LA; do not use RC71L (Ally 1) files. COMMUNITY (itechguides).
- Latest on the ASUS RC72LA support page (read 2026-10-21): BIOS 313 (2026/10/14, "New function of Audio"), 312 (2025/06/11). MCU firmware V317 (2026/10/19, adds Xbox Experience Mode, needs latest ACSE and BIOS), V315 (2025/10/03). MCU tool needs Windows 11 64-bit 23H2. VERIFIED (ASUS support page). Versions move; recheck.
- BIOS comes as Windows installer or EZ Flash file. VERIFIED (ASUS support page). EZ Flash from USB avoids a running Windows. MCU from Linux: no supported way today. VERIFIED (fwupd issue 10746): asus-hid reads the MCU version but does not mark it updatable, no MCU firmware is on LVFS, ASUS ships the tool only for Windows. A user flashed an Xbox Ally X over hidraw; this is an unmerged feature request, do not try it.
- fwupd 2.0.2 added community-provided "initial support" for Ally and Ally X. VERIFIED (GamingOnLinux). The article does not say which firmware; BIOS via fwupd/LVFS: UNVERIFIED. One user saw no BIOS listed in fwupd (COMMUNITY, Discourse).
- Safest advice: do BIOS/MCU on Windows or EZ Flash first, then Linux. Bazzite install can turn off Secure Boot issues; BIOS update may re-enable it.
## SSD upgrade and cloning
- Ally X takes M.2 2280 (Ally 1 takes 2230). VERIFIED (ASUS SSD guide).
- Tools: size 0 Phillips, guitar pick. Discharge battery to 25 percent or less, remove microSD. VERIFIED (ASUS SSD guide).
- Six back screws (one captive); a ribbon cable to the back panel can tear, so lift gently. VERIFIED (ASUS SSD guide).
- Disconnect battery connector under the right fan, then remove SSD screw above the battery. VERIFIED (ASUS SSD guide).
- Cloning: guide only mentions an external SSD enclosure can clone; no steps. UNVERIFIED for Bazzite. Simplest: fresh install, then restore Steam library.
## Known issues quick list
- Fingerprint reader does not work; duplicate drives shown are a visual bug, never format. VERIFIED (ASUS page).
## Bazzite deck setup on a desktop PC
- The deck image works on a desktop PC with an AMD GPU; Nvidia and Intel not supported for it. COMMUNITY (Discourse 2809); the official FAQ lists `-nvidia` deck images, so check the image picker. VERIFIED (FAQ).
- Trade-offs: desktop apps close in Gaming Mode, manual updates, weaker multitasking, no multi-user with `-deck` images. COMMUNITY (Discourse 2809).
- For a PC used mainly for desktop and creative apps, prefer the desktop image; use Big Picture instead of Gaming Mode. The reader's call.
## Troubleshooting tree (one step, then test)
1. Odd behavior after an update: reboot, then test. Still wrong: roll back with `rpm-ostree rollback`, reboot.
2. Controls wrong: reset the Steam controller layout; then set emulation to DualSense; then check OGUI (Guide + B).
3. TDP slider missing: Performance profile, enable TDP and GPU Clocks; make sure only one TDP method is active.
4. Gyro dead: OGUI emulation target deck-uhid.
5. No sleep or stuck on wake: wake animation off; leave SMT on; unplug charger, retest.
6. Game crashes at launch: BIOS UMA 4 or 8 GB.
7. Stutter from SD: move the game to internal SSD.
8. No sound: match both audio devices; then consider BIOS update.
9. Decky broken: uninstall Decky, retest, report without it.
10. Still stuck: Bazzite Discourse and docs, with `rpm-ostree status` output.
## Sources (fetched)
- https://github.com/hhd-dev/hhd
- https://www.gamingonlinux.com/2024/07/bazzite-linux-36-out-now-bringing-full-asus-rog-ally-x-support/
- https://www.ifixit.com/Device/Asus_ROG_Ally_X_%282024%29
- https://rog.asus.com/de/gaming-handhelds/rog-ally/rog-ally-x-2024
- https://docs.bazzite.gg/Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/
- https://docs.bazzite.gg/Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/rebase_guide/
- https://docs.bazzite.gg/Handheld_and_HTPC_edition/Handheld_Wiki/ASUS_ROG_Ally/
- https://docs.bazzite.gg/Handheld_and_HTPC_edition/Steam_Gaming_Mode/
- https://docs.bazzite.gg/Handheld_and_HTPC_edition/Handheld_Wiki/
- https://docs.bazzite.gg/General/Installation_Guide/secure_boot/
- https://docs.bazzite.gg/General/FAQ/
- https://rog-forum.asus.com/t5/handheld-gaming/rog-ally-x-sd-card-stutter-issue-investigation-and-temporary-fix/td-p/1128666
- https://rog-forum.asus.com/t5/changelogs/changelog-november-2025-rog-ally-ally-x-xbox-ally-xbox-ally-x/ba-p/1124876
- https://rog.asus.com/au/articles/guides/how-to-upgrade-the-ssd-and-reinstall-windows-on-your-rog-ally
- https://universal-blue.discourse.group/t/latest-rog-ally-status-and-gotchas/6092
- https://universal-blue.discourse.group/t/asus-rog-ally-handheld-compatibility/2414
- https://universal-blue.discourse.group/t/is-there-a-way-to-disable-or-hide-the-integrated-controller-of-the-asus-rog-ally-x-after-bazzite-44/12437
- https://universal-blue.discourse.group/t/bazzite-september-6th-update/12485
- https://universal-blue.discourse.group/t/using-a-deck-image-on-desktop/2809
- https://discuss.cachyos.org/t/bug-rog-ally-x-kernel-linux-cachyos-deckify-7-0-1-1-removes-charging-limit-setting-from-game-mode-asusctl-rgb-control-is-broken/28433
- https://www.itechguides.com/how-to-update-bios-on-asus-rog-ally/
- https://www.gamingonlinux.com/2024/11/linux-firmware-updater-adds-initial-community-support-for-asus-rog-ally-and-rog-ally-x/page=1
- https://gamingonlinux.com/2026/08/bazzite-linux-44-for-handhelds-finally-launches-with-some-massive-upgrades
- https://windowsforum.com/news/bazzite-44-replaces-hhd-moves-tdp-controls-to-steam.443331/
- https://github.com/ShadowBlip/InputPlumber
- https://docs.bazzite.gg/Installing_and_Managing_Software/ujust/
- https://www.asus.com/us/supportonly/rog%20ally%20x%20(2024)%20rc72la/helpdesk_bios/
- https://github.com/fwupd/fwupd/issues/10746
- https://github.com/ValveSoftware/SteamOS/issues/2097
- https://www.gamingonlinux.com/2026/09/bazzite-linux-44-gets-even-more-fixes-for-september-6th/
- https://www.handheldatlas.com/news/bazzite-44-rog-ally-x-sleep-handheld-controls
- https://universal-blue.discourse.group/t/bazzite-update-happy-new-year-sleep-fixes-smoother-updates-bootc-fan-curves-gpd-more-devices/6200
- https://universal-blue.discourse.group/t/remapping-device-buttons-asus-rog-xbox-ally/12291
- https://universal-blue.discourse.group/t/bazzite-44-update/12092
- https://github.com/SteamDeckHomebrew/decky-loader