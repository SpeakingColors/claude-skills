---
name: bazzite-kde-linux
description: Use when helping a new Linux user install, update, harden, roll back or troubleshoot Bazzite (immutable Fedora Atomic, KDE) including Gaming Mode, Steam, encryption and the macOS-style layout.
---

# Bazzite KDE for a first-time Linux user who also games

Verify against current docs before acting on anything marked UNVERIFIED.
Docs home: https://docs.bazzite.gg/ . Commands below were checked against it unless marked.

## Rules of engagement

1. Explain in plain words first, then give the command. Assume the reader is not a programmer. Plain words first, then one exact step. One change at a time, ask the reader to test, then continue.
2. Prefer the least invasive method (see install order). Never suggest layering as a first answer.
3. One change at a time, then reboot and test. Say what rollback undoes.
4. Never tell the reader to disable SELinux, enable the root account, or edit /usr (read-only).

## What "immutable" means

- The base system (/usr) is read-only and replaced as a whole image on update. You do not patch it package by package.
- Your home folder, /etc and /var stay writable and are kept across updates.
- The previous system image stays on disk, so a bad update can be undone (rollback).
- Apps live outside the base image: Flatpak, Homebrew, Distrobox containers.

## Image choice

- The desktop KDE edition does NOT include Steam Gaming Mode (FAQ: "Steam Gaming Mode is not on these specific images").
- Gaming Mode lives on the `-deck` images (bazzite-deck). Deck images boot into Gaming Mode and offer a KDE Desktop Mode from the power menu.
- So for "boot straight into Gaming Mode", install a `-deck` image variant that matches the GPU (AMD/Intel or NVIDIA).
- Switching between `bazzite` and `bazzite-deck` (both KDE): VERIFIED. The official rebase guide lists "Rebase to other Fedora Atomic Desktop images including other Bazzite images" and gives `brh rebase bazzite-deck:stable` / `brh rebase bazzite:stable` (or `rpm-ostree rebase ostree-image-signed:docker://ghcr.io/ublue-os/bazzite-deck:stable`), then reboot. Personal files and app data stay. The pair is not named as an example, so test it on a spare disk or keep a backup first.
- Official warning: do not rebase between different desktop environments (KDE to GNOME), "may cause issues and is not officially supported". Deck and desktop images are both KDE here.
- Both are official images from the same project; the README describes `bazzite` as the common desktop variant and `bazzite-deck` as the console-like HTPC/handheld variant that boots into Game mode. No source found saying either is sub-par or going away (absence of evidence, not a promise).
- Rollback: README says any build from the last 90 days; GRUB lists the previous deployment.
- GPU needs: Gaming Mode wants Vulkan 1.3 capable hardware. AMD RX 4xx and up is the baseline; Intel Arc works with caveats; NVIDIA works "with major caveats" (hardware compatibility page).
- NVIDIA images: `-nvidia` (legacy) covers Pascal, Maxwell, Volta; `-nvidia-open` covers Turing and newer (GTX 16 and RTX). Drivers ship in the image; you cannot update them separately. AMD/Intel drivers come with the kernel in the image.
- NVIDIA Flatpak apps without GPU acceleration: update all Flatpaks, or Bazzite Portal, Manage Bazzite, "Update Nvidia Flatpak Runtime".

## Install software: order of preference

1. Bazaar app store (Flatpak): main source for graphical apps.
2. Homebrew `brew install <pkg>`: command-line tools only.
3. Distrobox: for Linux apps not in Flatpak or Homebrew.
4. AppImage: trusted sources only; Gear Lever (in Bazaar) integrates it.
5. rpm-ostree layering: last resort.

### Distrobox

```
ujust distrobox-assemble        # create a container from a menu
distrobox enter <container>
distrobox-export --app <package>   # run inside container: makes a menu shortcut
distrobox stop <container> && distrobox rm -f <container>
```

Containers are disposable, not virtual machines. Test in a throwaway one first.

### rpm-ostree layering and its costs

```
rpm-ostree install <package>     # needs reboot
rpm-ostree uninstall <package>
rpm-ostree status                # see what is layered
rpm-ostree reset                 # removes ALL layered packages
```

Costs documented: reboot required; slower, bigger updates; can block updates and rebasing; dependency conflicts can break upgrades; local RPMs never auto-update; third-party COPRs can break updates. Docs: "not recommended, use as a last resort."

## Updates and rollback

- Desktop images check daily and update when idle. Deck images do NOT auto-update by default: use Steam Menu, Settings, System, Check for Updates, or Bazzite Updater. Reboot to apply.
- Keep at least 3 percent free space on the install drive before updating.
- Terminal: `ujust update` (system, Flatpaks, containers together). `ujust --choose` lists all ujust commands.
- See changes: `rpm-ostree db diff`.
- Roll back: `rpm-ostree rollback`, then reboot. Or at the GRUB menu choose the `ostree:1` entry, then make it permanent via Bazzite Updater rollback menu or the command. Personal files are untouched.
- Pin a good deployment so it is not cleaned up (default keeps 2):

```
rpm-ostree status -v
sudo ostree admin pin <index>
sudo ostree admin pin -u <index>   # unpin
```

- Bazzite Rollback Helper: `brh current`, `brh list`, `brh rebase stable`.
- Stay on the `stable` tag. `testing` and `unstable` are for testers.
- Deck 43 to 44 rollback breaks autologin; fix is deleting `zz-*` files in /etc/sddm.conf.d/ (rolling back docs).

## Gaming Mode, Desktop Mode, autologin

- Switch to Desktop Mode: Steam power menu. From a TTY (Ctrl+Alt+F4, needs a physical keyboard): `steamosctl switch-to-desktop-mode`.
- Back to Gaming Mode: the "Return to Gaming Mode" desktop shortcut (`ujust restore-gamemode-shortcut` restores it).
- Autologin on deck images is done by `bazzite-autologin.service` plus SDDM (community forum log). Exact config keys are UNVERIFIED in the official docs. Do not hand-edit; test with a reboot.
- If the system falls back to Desktop Mode, community reports blame a desktop SDDM autologin setting; reinstalling Decky Loader (`ujust setup-decky`) fixed one case. UNVERIFIED as a general fix.
- Gaming Mode shortcuts: Ctrl/Win+1 Steam menu, Ctrl/Win+2 Quick Access.
- Set Gaming Mode monitor or keyboard layout:

```
mkdir -p ~/.config/environment.d
echo "OUTPUT_CONNECTOR=DP-1" >> ~/.config/environment.d/10-gamescope-session.conf
echo "XKB_DEFAULT_LAYOUT=us" >> ~/.config/environment.d/10-gamescope-session.conf
kscreen-doctor -o      # lists output names
```

## Steam, Proton, Proton-GE

- Steam is preinstalled and is the recommended way to play. Lutris, Heroic, Faugus are alternatives (Bazaar).
- Force a Proton version: game Properties, Compatibility, force a specific tool.
- Bazzite docs point to ProtonPlus (Flathub id `com.vysp3r.ProtonPlus`) to install GE-Proton. ProtonUp-Qt is not mentioned in Bazzite docs (UNVERIFIED for Bazzite; it works similarly).
- Do not use gamemoderun (not installed, can hurt performance). Do not run Counter-Strike 2 through Proton (ban risk). Keep games off NTFS.
- Proton log: launch option `PROTON_LOG=1 %command%`, log at `~/steam-<AppID>.log`.

## Disk encryption

- Optional LUKS, chosen at install. A physical (wired USB) keyboard is needed to unlock. Forgotten passphrase means data is gone.
- Bazzite supports Secure Boot only after enrolling the Universal Blue key: password `universalblue` at the blue MOK screen, or later `ujust enroll-secure-boot-key`.
- TRIM on LUKS is optional and at your own risk (docs/Advanced/trim-on-luks).
- `ujust setup-luks-tpm-unlock` exists (auto-unlock via TPM). Security effect is UNVERIFIED in docs. Tradeoff to explain: with TPM unlock plus autologin, anyone holding the whole PC gets in. A typed LUKS passphrase at boot plus autologin matches "no local login password, protected at rest".

## Hardening for a locked down desktop

Example profile: no local login password, remote access off, outbound connections only.

1. Encrypt at install (above). This is the real protection for a stolen drive.
2. Autologin only on the console; do not run any remote login service.
3. SSH off: do not enable sshd. Check: `systemctl is-enabled sshd` (default state on Bazzite UNVERIFIED). If enabled: `sudo systemctl disable --now sshd`.
4. Firewall: Fedora ships firewalld; Bazzite default and active zone are UNVERIFIED. Check with `sudo firewall-cmd --state` and `sudo firewall-cmd --list-all`. Outbound is not filtered by default; inbound closed services are fine for this use.
5. Do not enable: `ujust setup-sunshine`, `ujust enable-tailscale`, Waydroid, Looking-Glass unless needed (they open or add network paths).
6. Outbound-only needs (Nextcloud, browsing, online games, online sample services, printing, remoting to a home server or DNS filter) need no open inbound ports. Printing: use CUPS network printers; mDNS discovery is outbound-initiated (UNVERIFIED on Bazzite firewall defaults).
7. Keep the account password for sudo; it is not asked at login with autologin. Do not enable the root account.
8. Keep Secure Boot on with the enrolled key. Keep `stable` updates on.

## KDE macOS-style layout (Plasma 6, Desktop Mode)

Steps are from a KDE community thread; exact widget names vary by version (UNVERIFIED on Bazzite's Plasma build).

1. Right-click empty desktop, Enter Edit Mode.
2. Add Panel, choose Application Menu Bar (global menu). Set it to the top edge.
3. On that panel add: Application Dashboard or launcher at the left, window title widget, a spacer, then clock and system tray at the right.
4. Add a second panel at the bottom. Remove everything except an Icons-only Task Manager.
5. Set that panel alignment to center and width to fit content; optionally floating.
6. System Settings, Appearance: pick a macOS-like Global Theme, icons and window decorations. Install themes into `~/.local/share/plasma/` (docs: Desktop Environment Tweaks).
7. Exit Edit Mode. Reboot once and check Gaming Mode still starts.

## Troubleshooting order

1. Reboot once. Check free disk (3 percent minimum).
2. Update: `ujust update`, reboot.
3. Steam problem or blank Gaming Mode: `ujust fix-reset-steam`. Game will not start after crash: `ujust fix-proton-hang`.
4. Crackling audio: `ujust restart-pipewire`.
5. Read logs: `ujust logs-this-boot`, `ujust logs-last-boot`.
6. Bad update: pick `ostree:1` in GRUB, then `rpm-ostree rollback`.
7. Undo experiments: `rpm-ostree reset`.
8. Support info: `ujust device-info`. Ask in Bazzite Discord with it.
9. Locked out: GRUB edit, `init=/bin/bash`, load SELinux policy, then `passwd` (docs: Reset Forgotten User Password; LUKS passphrase still needed first).
10. Secure Boot problems after BIOS update: `ujust enroll-secure-boot-key` again.

## What NOT to do

- Do not run `sudo dnf install` (not the right tool here). Do not add random COPRs.
- Do not rebase between desktop environments or to old builds without a plan to return to `:stable`.
- Do not change `/etc/group` with `>`; use the documented steps (Advanced, Adding User to a Group).
- Do not disable SELinux.

## Sources

- https://docs.bazzite.gg/
- https://docs.bazzite.gg/Installing_and_Managing_Software/software-intro/
- https://docs.bazzite.gg/Installing_and_Managing_Software/rpm-ostree/
- https://docs.bazzite.gg/Installing_and_Managing_Software/Distrobox/
- https://docs.bazzite.gg/Installing_and_Managing_Software/Homebrew/
- https://docs.bazzite.gg/Installing_and_Managing_Software/ujust/
- https://docs.bazzite.gg/Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/updating_guide/
- https://docs.bazzite.gg/Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/rolling_back_system_updates/
- https://docs.bazzite.gg/Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/rebase_guide/
- https://docs.bazzite.gg/General/Installation_Guide/install-guide/
- https://docs.bazzite.gg/General/Installation_Guide/Installing_Bazzite_for_Steam_Deck/
- https://docs.bazzite.gg/General/FAQ/
- https://docs.bazzite.gg/General/Desktop_Environment_Tweaks/
- https://docs.bazzite.gg/Handheld_and_HTPC_edition/quirks/
- https://docs.bazzite.gg/Gaming/Hardware_compatibility_for_gaming/
- https://docs.bazzite.gg/Gaming/Common_gaming_issues/
- https://docs.bazzite.gg/Gaming/Managing_and_modding_games/
- https://docs.bazzite.gg/Advanced/trim-on-luks/
- https://docs.bazzite.gg/Advanced/Reset_Forgotten_User_Password/
- https://docs.bazzite.gg/Advanced/add-user-to-group/
- https://universal-blue.discourse.group/t/bazzite-fails-to-boot-into-gaming-mode-and-falls-back-to-desktop-mode/8265
- https://discuss.kde.org/t/how-can-i-set-the-global-top-bar-like-macbook/19040
- https://github.com/Vysp3r/protonplus
