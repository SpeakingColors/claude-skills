---
name: couch-pc-cec-gaming-mode
description: Use when setting up a console-like living room PC on Bazzite-deck with HDMI-CEC, receiver audio, controller wake and autologin into Steam Gaming Mode.
---

# Couch PC: CEC, wake, Gaming Mode (Bazzite-deck)

Target: a living room PC (AMD or Nvidia GPU, desktop motherboard, TV plus an optional 5.1 receiver on HDMI, Xbox and PS5 pads) running Bazzite-deck. Hardware examples below come from public reports, not from one machine; always test on yours.
Researched 2026-10-21. Labels: VERIFIED (source), COMMUNITY (forum/user report), UNVERIFIED (not confirmed).
Rule: one step at a time. Ask the reader to do ONE step, report the result, then log it. Never guess.

## 1. What is verified

- Bazzite docs DO have a CEC section: Portal, Troubleshoot, Change CEC mode. VERIFIED (docs.bazzite.gg issues_and_resolutions). The "no CEC page" idea is only half true: no dedicated page.
- Two modes: Native (new, Valve linux-cec/cecd) and dGPU (legacy, libcec + cec-ctl). Docs say cecd can interfere with wakeup on HTPCs using dongles; dGPU may be steadier with Pulse-Eight and UGREEN. VERIFIED (same page).
- ujust names cec-mode, cec-sleep, configure-amd-hdmi21 appear in a user post. COMMUNITY (forum 12543). Not seen in official docs.
- Services cec-onboot, cec-onpoweroff, cec-onsleep exist, inactive by default on one install. COMMUNITY (forum 7064, answeroverflow).
- HDMI 2.1 (FRL, VRR, ALLM) ships in Bazzite 44 but is OFF by default; enable with `ujust configure-amd-hdmi21` or the Portal switch. COMMUNITY (pcgameshardware.de article, a news site).
- Deck images boot straight into Gaming Mode; Desktop Mode is reached from the power menu in Gaming Mode. VERIFIED (docs.bazzite.gg HTPC install page, FAQ). That page is marked legacy.
- Bazzite-deck: Steam beta client is not supported. VERIFIED (docs.bazzite.gg Steam Gaming Mode page).
- Pulse-Eight adapter: TV on/off, input switch, volume, remote buttons; PC sleep/wake can drive the TV. VERIFIED (Pulse-Eight support). It does NOT say the adapter can wake the PC. VERIFIED (absence).
- libcec commands: `cec-client -l` (list), `echo "scan" | cec-client -s -d 1`, `echo "on 0" | cec-client -s -d 1`, `echo "standby 0" | cec-client -s -d 1`. VERIFIED (Pulse-Eight libcec Linux article).
- steamos-cec-toolkit (Twsts): controller button wakes TV/AVR and switches input; tested on an AMD GPU with a UGREEN DP-to-HDMI adapter on SteamOS; Bazzite is NOT mentioned. VERIFIED (GitHub README). Community report says it does not work on Bazzite. COMMUNITY (forum 12543).
- Kernel CEC docs and Arch wiki HDMI-CEC: fetch blocked. UNVERIFIED (not read).

## 2. Hard truths (set expectations first)

- AMD GPUs usually have no usable CEC on the HDMI port. Pulse-Eight USB adapter or a DP-to-HDMI adapter with CEC (UGREEN) is the common route. COMMUNITY (forum 7064, 12543, toolkit README). Whether your GPU's HDMI port does native CEC: UNVERIFIED, test it (Step 4).
- Waking the PC from a controller button: possible only through a USB or Bluetooth wake path. Support is mixed:
  - Xbox controller via Xbox Wireless Adapter woke a ROG Ally. COMMUNITY (bazzite issue 4873). Same dongle on other boards: stops working after sleep unless replugged. COMMUNITY (issue 2367, forum 10917).
  - Bluetooth "can't wake the system": one user. COMMUNITY (issue 2367). Toolkit README claims Bluetooth pad wake works "when the adapter allows it". Mixed, so test.
  - PS5 (DualSense) wake on your board: UNVERIFIED. Toolkit lists DualSense as tested for wake on its setup only.
  - Wake from full power-off (S5) by a pad: UNVERIFIED. Sleep (S3) wake is the realistic target.
- Wake is hardware, firmware and kernel dependent; some desktop AMD systems need BIOS power changes. VERIFIED (toolkit README).
- Known bug family: after wake, PC re-suspends because the CEC dongle sends KEY_POWER (issues 5200, 5240). COMMUNITY, unresolved. Pending PR adds a 3 second delay in /usr/bin/cec-control. COMMUNITY.
- Sleep sync can power the TV off about every minute and drop controllers. COMMUNITY (forum 12543, one user).
- Some TVs cold-boot after CEC Standby; toolkit offers "inactive-source" instead. VERIFIED (README).

## 3. Step plan with test points (do one, then log)

Step 0. Baseline, no CEC.
- Install Bazzite-deck (not the desktop image), sign in to Steam, reboot. Expect Gaming Mode on boot.
- TEST: boots into Gaming Mode without a keyboard? Power menu, Switch to Desktop, then icon "Return to Gaming Mode". Log it.
- If Return to Gaming Mode fails on an external display: restart works; SDDM autologin may be the cause. COMMUNITY (forum 9892, 8265). Check `systemctl status bazzite-autologin` and `systemctl status sddm`.

Step 1. Audio to receiver.
- Gaming Mode: Settings, Sound, pick the HDMI output for the receiver. Desktop Mode: check the same device.
- TEST: stereo sound from all speakers; then Steam surround setting.
- 5.1 caution: one user could not keep Steam at 5.1/7.1 on a Denon (reverted to stereo, options vanished after mode switch). COMMUNITY (forum 11328, no answer). Expect to test and log. 5.1 passthrough limits: UNVERIFIED.

Step 2. HDMI 2.1 (only if you want 4K120/VRR).
- `ujust configure-amd-hdmi21`, reboot. COMMUNITY/article.
- TEST: picture stable, receiver in the chain passes video. If black screen or dropouts, undo and log. RDNA4 specific Mesa issues: UNVERIFIED (no source read).
- Receiver in the chain: some receivers have HDMI 2.1 bugs. UNVERIFIED for yours.

Step 3. Turn on CEC in the TV and receiver menus (names differ by brand: Bravia Sync, Anynet+, Simplink, EasyLink, HDMI Control, Viera Link, Aquos Link; receivers often "HDMI Control"). COMMUNITY (generic CEC trade names, Wikipedia result not fetched). Also enable the TV's "wake on CEC / power on link" option.
- TEST: use the TV remote on the receiver volume. Log.

Step 4. Find a CEC path.
- Portal, Troubleshoot, Change CEC mode. Try Native first with the GPU HDMI port.
- If no `/dev/cec*` appears, you need a Pulse-Eight USB-CEC adapter or UGREEN DP-to-HDMI CEC adapter. Install either only after the reader decides. Buying advice beyond the sources: UNVERIFIED.
- TEST: `ls /dev/cec*`; `lsusb` for Pulse-Eight; `cec-client -l`. If libcec is missing on Bazzite it can be installed via Homebrew. COMMUNITY (forum 7064).
- With a dongle, switch mode to dGPU. Try the other mode if flaky.

Step 5. Power on TV and receiver at boot.
- Services cec-onboot and cec-onpoweroff: enable via `systemctl`. COMMUNITY (forum 7064). Skip cec-onsleep at first.
- TEST: cold boot; TV on, input switches, receiver on. Log.

Step 6. Sleep and wake.
- `ujust cec-sleep` toggle is optional. COMMUNITY. Test with it ON and OFF, one at a time.
- TEST: press the Steam menu, Power, Sleep. TV off? Then press the pad. Does PC wake? Does TV come on? Does PC immediately re-suspend (issue 5200 symptom)?

Step 7. Pad wake (hardest). Try in order, log each:
- 7a. Xbox Wireless Adapter on a rear motherboard USB port; enable USB wakeup via udev rule. COMMUNITY (issue 4873 shows a udev rule setting power/wakeup to enabled for a given USB ID; copy their pattern for your dongle ID from `lsusb`).
- 7b. Wired USB pad or PS5 pad via USB cable.
- 7c. Bluetooth pad (see BIOS list).
- 7d. Give up pad wake; use fallback in section 4.

Step 8. Lock it in: reboot, sleep, wake five times; update Bazzite once and re-test (updates can reset settings, per toolkit README on SteamOS, so expect re-test). 

## 4. Fallbacks, ranked (best first)

1. Wake-on-LAN from phone (Steam Link app or a WoL app); wired Ethernet only. COMMUNITY (overkill.wtf, Steam Deck). Works for sleep; from full off depends on BIOS. UNVERIFIED on your board.
2. Press the case power button (or a keyboard/mouse wake); pad takes over after boot. UNVERIFIED (no source read), but zero-risk to try.
3. Smart plug on PC power with BIOS "Restore AC Power Loss: Power On". Setting name on your board: UNVERIFIED. Plug on = PC boots = TV on via cec-onboot.
4. Home Assistant or IR blaster to power TV and receiver; CEC then not needed. UNVERIFIED (no source read).
5. Remote Play / Steam Link wake from another device: UNVERIFIED for desktop Bazzite.
6. Pulse-Eight "Standby Monitor" type syncing is Windows oriented. UNVERIFIED on Linux.

## 5. BIOS checklist (ASUS examples; names differ per board and brand, confirm on screen)

Enter with Delete, Advanced Mode (F7). Change ONE item, test, log.
- Advanced, APM Configuration, "Power On By PCI-E": Enabled (needed for Wake-on-LAN). VERIFIED (ASUS FAQ 1045950, generic ASUS board, not specific to any one model).
- Advanced, APM Configuration, "ErP Ready": Disabled (ErP on cuts standby power; wake may fail). VERIFIED (ASUS FAQ 1042220, generic).
- Advanced, Onboard Devices, "USB power delivery in Soft Off State (S5)": the FAQ shows setting it disabled to cut USB power; for wake you want it enabled. VERIFIED name, direction is inferred. UNVERIFIED on your board.
- "Power On By Keyboard/Mouse" or similar: UNVERIFIED on this board.
- "Restore AC Power Loss": UNVERIFIED name.
- Forum user: BIOS "wake on USB" did not fix pad wake; plus "USB Device Power On" helped one port briefly. COMMUNITY (issue 2367, user report).
- Hidden command for black screen on resume on some Gigabyte boards: `ujust _toggle-gigabyte-wake-fix`. VERIFIED (docs) but Gigabyte only, skip on other brands.
- Wake-on-LAN in Linux: needs NIC wake set to magic packet and persistence through NetworkManager. Exact ethtool and nmcli options: UNVERIFIED (Arch wiki blocked).

## 6. Results log (fill in per test)

| Step | What was done | Date | Result (pass/fail) | Notes (error, mode, BIOS) |
|------|---------------|------|--------------------|---------------------------|
| 0 | Boot to Gaming Mode | | | |
| 0 | Switch to Desktop and back | | | |
| 1 | Audio to receiver | | | |
| 1 | 5.1 in Steam | | | |
| 2 | HDMI 2.1 on/off | | | |
| 3 | TV/receiver CEC menus on | | | |
| 4 | /dev/cec* or dongle seen | | | |
| 5 | TV + receiver on at boot | | | |
| 6 | Sleep with CEC | | | |
| 6 | Wake + re-suspend check | | | |
| 7a | Xbox dongle wake | | | |
| 7b | Wired pad wake | | | |
| 7c | Bluetooth wake | | | |
| BIOS | each setting changed | | | |

## 7. Not found / blocked

- Kernel CEC admin guide and Bazzite forum 12428 (HDMI 2.1 thread): fetch blocked.
- Arch wiki HDMI-CEC and WoL: access denied (bot protection).
- No source found for: RDNA4 + HDMI 2.1 Mesa bugs, receiver 5.1 passthrough in Gaming Mode, PS5 pad wake on Bazzite, board specific BIOS menu text.

## Sources (fetched)

- https://universal-blue.discourse.group/t/pulse-eight-hdmi-cec-support/7064
- https://universal-blue.discourse.group/t/cec-with-the-ugreen-dp-to-hdmi-2-1-adapter/12543
- https://github.com/Twsts/steamos-cec-toolkit
- https://github.com/ublue-os/bazzite/issues/5240
- https://github.com/ublue-os/bazzite/issues/5200
- https://github.com/ublue-os/bazzite/issues/4873
- https://github.com/ublue-os/bazzite/issues/2367
- https://docs.bazzite.gg/General/issues_and_resolutions/
- https://docs.bazzite.gg/General/FAQ/
- https://docs.bazzite.gg/General/Installation_Guide/Installing_Bazzite_for_HTPC_Setups/
- https://docs.bazzite.gg/Handheld_and_HTPC_edition/Steam_Gaming_Mode/
- https://www.answeroverflow.com/m/1349661251709440020
- https://www.pcgameshardware.de/Linux-Software-26761/News/Bazzite-44-HDMI-2-1-VRAM-Overcommit-Kernel-7-2-1551846/
- https://universal-blue.discourse.group/t/xbox-wireless-adapter-newest-version-has-to-be-unplugged-and-reinserted-after-every-boot/10917
- https://universal-blue.discourse.group/t/bazzite-deck-return-to-game-mode-not-working-when-connected-to-external-display/9892
- https://universal-blue.discourse.group/t/bazzite-fails-to-boot-into-gaming-mode-and-falls-back-to-desktop-mode/8265
- https://universal-blue.discourse.group/t/surround-sound-docked-mode-bazzite-gnome/11328
- https://support.pulse-eight.com/support/solutions/articles/30000053023-cec-adapter-setting-up-libcec-on-linux
- https://support.pulse-eight.com/support/solutions/articles/30000053002-what-is-the-pulse-eight-cec-adapter-and-libcec-
- https://www.asus.com/de/support/FAQ/1045950
- https://www.asus.com/latin/support/FAQ/1042220/
- https://overkill.wtf/how-to-turn-on-your-steam-deck-with-your-phone-when-docked