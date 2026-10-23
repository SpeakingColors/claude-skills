---
name: grapheneos
description: Use when advising a Linux desktop user, such as a musician or developer, on installing and using GrapheneOS on a Pixel, covering devices, safe install, privacy, apps, banking, USB audio and MIDI.
---

# GrapheneOS on a Pixel (Linux desktop user, musician or developer)

Labels: VERIFIED (source tag), COMMUNITY (forum/reports, not official), UNVERIFIED (not confirmed, test it).
Source tags: [FAQ] [USAGE] [FEATURES] [WEB] [CLI] [REL] = grapheneos.org pages (see Sources).
Research date 2026-10-21. Re-check devices and install steps on grapheneos.org before acting; pages change.

## Devices
- VERIFIED [FAQ]: official production support: Pixel 6, 6 Pro, 6a, 7, 7 Pro, 7a, Fold, Tablet, 8, 8 Pro, 8a, 9, 9 Pro, 9 Pro XL, 9 Pro Fold, 9a, 10, 10 Pro, 10 Pro XL, 10 Pro Fold, 10a.
- VERIFIED [FAQ]: "strongly recommended" are Pixel 8 and later (7 years minimum support, hardware memory tagging).
- VERIFIED [FAQ]: OEM support ends: Pixel 6/6 Pro Oct 2026 (now), 6a Jul 2027, 7/7 Pro Oct 2027, 8/8 Pro Oct 2030, 9 series Aug 2031, 10/10 Pro/XL Aug 2032, 10 Pro Fold Oct 2032, 10a Mar 2033.
- VERIFIED [FAQ]: avoid carrier-variant Pixels (US carriers mainly): bootloader may be locked. Buy carrier-unlocked/unbranded.
- VERIFIED [FAQ]: Pixel 10 series is listed as production support. COMMUNITY (Privacy Guides, Nov 2025): it started as "experimental" then moved to production.
- Pick: Pixel 8a or newer new/unlocked; 10-series for the longest support.

## Install overview (from Linux)
- VERIFIED [WEB]: web installer (WebUSB) is "recommended for most users"; CLI is the traditional alternative.
- VERIFIED [WEB]: officially supported install hosts: Arch, Debian 12/13, Ubuntu 22.04/24.04/25.04, Mint 21/22, LMDE 6, Windows 10/11, macOS 14-26, ChromeOS, GrapheneOS, Android 14-17. Fedora/Bazzite is NOT listed.
- VERIFIED [WEB]: browsers: Chromium (not Ubuntu snap), Vanadium, Chrome, Edge, Brave (Shields off). Avoid Flatpak and Snap browsers, and private/incognito mode.
- VERIFIED [WEB]: needs 2GB free RAM, 32GB free disk; bare metal not a VM; direct rear/laptop USB port, no hub; use the Pixel's own USB-C cable.
- VERIFIED [WEB][CLI]: on non-root Linux you need udev rules (Arch: android-udev; Debian/Ubuntu: android-sdk-platform-tools-common).
- VERIFIED [WEB][CLI]: fwupd can claim the fastboot device; run `sudo systemctl stop fwupd.service` (restarts on reboot).
- VERIFIED [CLI]: fastboot must be 35.0.1 or newer; distro packages are often bad. Debian/Ubuntu: use standalone Google platform-tools (r35.0.2 in the guide, sha256 listed). Arch: android-tools.
- VERIFIED [CLI]: verify the factory zip with `ssh-keygen -Y verify` against `allowed_signers` (contact@grapheneos.org, ed25519).
- VERIFIED [CLI]: if /tmp is a small tmpfs, flashing fails; use `mkdir tmp && TMPDIR="$PWD/tmp" ./flash-all.sh`.
- UNVERIFIED: Bazzite/Fedora Atomic path. No official Fedora or distrobox guidance found. Safest: boot a Debian/Ubuntu/Arch live USB and use the web installer there (VERIFIED supported), or use a laptop or Android phone with Chrome/Vanadium.
- UNVERIFIED: running fastboot/adb inside toolbox/distrobox. USB passthrough into containers needs host udev rules and `--privileged` or device mounts; test `fastboot devices` before flashing.

## Safe-install step list
1. Buy an unlocked, non-carrier Pixel; update stock OS first (WEB suggests it). VERIFIED [WEB].
2. Back up everything; unlock and flash wipe all data. VERIFIED [WEB].
3. Settings > About > tap Build number 7 times; Developer options > enable OEM unlocking (needs internet on some SKUs). VERIFIED [WEB].
4. On the PC: udev rules in place, stop fwupd, use a good cable on a direct port. VERIFIED [WEB].
5. Hold Volume Down while booting; must show red triangle "Fastboot Mode"; do not press Start. VERIFIED [WEB].
6. Unlock bootloader (confirm on phone, wipes). Download and flash the release; do not touch the phone while flashing. VERIFIED [WEB].
7. LOCK the bootloader (confirm on phone, wipes again) BEFORE daily use. VERIFIED [WEB]: locking enables full verified boot.
8. Boot, first setup, leave "disable OEM unlocking" ticked. VERIFIED [WEB].
9. Verify with the Auditor app on a second Android device (optional but recommended). VERIFIED [WEB].
10. Settings > Security: check USB-C port mode, auto reboot, PIN scrambling. VERIFIED [USAGE][FEATURES].

## What can go wrong
- Carrier-locked unit: OEM unlocking greyed out. VERIFIED [WEB].
- Pixel 6a on old factory stock: needs June 2022+ OTA and a factory reset for OEM unlock. VERIFIED [WEB].
- "USB device already claimed" error: fwupd. VERIFIED [WEB].
- Flash fails or stalls: bad cable/hub, VM, low /tmp, old fastboot. VERIFIED [WEB][CLI].
- Flashing but leaving the bootloader unlocked: no full verified boot. VERIFIED [WEB].
- Brave/Snap/Flatpak browser or incognito breaks the web installer. VERIFIED [WEB].
- Forgetting the lock PIN with Duress PIN armed means the phone wipes; no recovery. VERIFIED [FEATURES].
- Forgetting an eSIM PIN with eSIM toggle off: locked out unless you have the PUK. VERIFIED [USAGE].
- Reverting to stock later: use Google's web flasher plus a clean-state step (erase avb_custom_key). VERIFIED [WEB][CLI].

## Updates and releases
- VERIFIED [USAGE]: automatic background updates, checks about every 6 hours, delta updates, A/B with rollback; reboot when prompted.
- VERIFIED [USAGE]: Stable (default) and Beta channels; optional automatic reboot after update.
- VERIFIED [REL]: releases come every few days to weeks; latest seen 2026101600 (2026-10-16), after 2026100600 and 2026100200.
- VERIFIED [REL]: Alpha, then Beta, then Stable after user testing.

## Security and privacy features
- VERIFIED [FEATURES][USAGE]: USB-C port control modes: Off, Charging-only, Charging-only when locked (default), Charging-only when locked except before first unlock, On. Path: Settings > Security > Exploit protection.
- VERIFIED [FEATURES]: PIN scrambling toggle (lock screen and SIM PIN); passwords up to 128 chars.
- VERIFIED [FEATURES]: Auto reboot when locked: default 18h, range 10 min to 72h, or off.
- VERIFIED [FEATURES]: Duress PIN/Password wipes device (and eSIMs) when entered; set in Owner profile; needs both PIN and password set.
- VERIFIED [FEATURES]: per-app Network permission and Sensors permission toggles (default on; can default sensors off for new apps).
- VERIFIED [USAGE]: Storage Scopes and Contact Scopes give apps fake "all permission" with only chosen files/contacts exposed.
- VERIFIED [FEATURES]: up to 31 secondary users plus guest; End session purges keys; each profile has own encryption keys and VPN config.
- VERIFIED [USAGE][REL]: Private Space exists and sandboxed Play can be set up inside it; the hide feature is only superficial (REL warning).
- VERIFIED [FEATURES]: Seedvault encrypted backup (local or storage-provider app); must be enabled explicitly [FAQ]. Project plans to replace it.
- VERIFIED [FEATURES]: Vanadium is the bundled hardened Chromium browser/WebView; payments and DRM off by default.

## Apps and Google services
- VERIFIED [USAGE]: Sandboxed Google Play is installed from the GrapheneOS App Store; Play runs as a normal unprivileged app per profile; Play Store works incl. in-app purchases.
- VERIFIED [USAGE]: Android Auto only via App Store plus toggles. Location from Play is rerouted by default.
- VERIFIED [FAQ]: no bundled third-party apps; install from developers or stores. Aurora Store needs an account (USAGE).
- UNVERIFIED: Accrescent, F-Droid and Obtainium specifics were not found on the official pages; they work as normal APK sources (user must allow "install unknown apps" per app). Check each app's signing and update model.
- VERIFIED [USAGE]: eSIM add/manage needs Settings > Network & internet > eSIM support toggle (Google proprietary bits, no Play needed). Some setups need USSD `*#*#4636#*#*` then enable DSDS.
- UNVERIFIED: which carriers/regions work with eSIM, RCS, VoLTE. Check carrier plus GrapheneOS chat.

## Banking and payments
- VERIFIED [USAGE]: banking apps are the hardest class; many work with sandboxed Play in the same profile. GrapheneOS passes basicIntegrity, fails ctsProfileMatch (not Google-certified), and does not spoof.
- VERIFIED [USAGE]: if a banking app fails, try re-enabling Native code debugging protection (Exploit protection).
- VERIFIED [USAGE]: community compatibility list is maintained by PrivSec.dev; GrapheneOS gives no guarantees.
- UNVERIFIED: contactless/NFC tap-to-pay with Google Wallet. Not confirmed on the pages read; plan a card or a second device until you test.
- Tip: test your bank app before selling the old phone; keep the stock device until proven.

## Music and audio use
- VERIFIED [FAQ]: file transfer via MTP/PTP or external drive works; default locked-state USB behavior is charging-only when locked, so unlock first.
- VERIFIED [FEATURES]: USB-C control also blocks USB-C alternate modes (e.g. DisplayPort) when locked. For class-compliant USB audio/MIDI keep mode at the default or "On" and keep the phone unlocked.
- COMMUNITY (discuss.grapheneos.org #1324): one user's Tascam recorder on a Pixel 4a 5G was treated as charging only; no fix posted. Do not assume every interface works.
- UNVERIFIED: USB audio interfaces and class-compliant MIDI on GrapheneOS. Android supports USB audio/MIDI generally, but bus power, hubs and app support vary. Test with your interface before relying on it.
- UNVERIFIED: Bluetooth LE MIDI, Bluetooth latency for monitoring, DAW remote apps (e.g. TouchOSC, OSC/MIDI over Wi-Fi). Normal apps, so likely fine, but test; give them Network permission and local network access only as needed.
- UNVERIFIED: KDE Connect on GrapheneOS (needs local-network, notification, storage via Storage Scopes). GrapheneOS "Network permission" guards localhost between profiles, so keep both ends in one profile.
- Alternatives (UNVERIFIED, test): Syncthing for files, Wi-Fi hotspot or USB tethering for networking, adb over USB for dev.
- Dev: adb needs Developer options > USB debugging; with USB-C port at default, unlock phone first. UNVERIFIED on Bazzite: use `distrobox` with Fedora, install android-tools, ensure host udev rules (android-udev-rules) are present.

## Sources
- https://grapheneos.org/faq (device support, support table, banking, transfers)
- https://grapheneos.org/install/web (web installer, udev, fwupd, relock)
- https://grapheneos.org/install/cli (fastboot version, verification, flash-all)
- https://grapheneos.org/features (USB-C control, PIN scrambling, auto reboot, Duress, Network/Sensors, profiles, Seedvault, Vanadium)
- https://grapheneos.org/usage (updates, Storage/Contact Scopes, sandboxed Play, eSIM, Android Auto, banking)
- https://grapheneos.org/releases (device list, latest release 2026101600)
- Access note: grapheneos.org was blocked in the sandbox, so page text was read from the site's source repo https://github.com/GrapheneOS/grapheneos.org (static/*.html on main).
- https://www.privacyguides.org/news/2025/11/26/grapheneos-now-has-experimental-support-for-pixel-10-series/ (COMMUNITY)
- https://discuss.grapheneos.org/d/1324-connecting-an-audio-interface-to-grapheneos (COMMUNITY)