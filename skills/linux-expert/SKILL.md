---
name: linux-expert
description: Use when a non-programmer needs general Linux system knowledge, command-line help, troubleshooting method or distro comparisons, on Bazzite or any other distro.
---

# Linux expert for a non-programmer (Bazzite first, other distros second)

Labels: VERIFIED (source) = read on a fetched page this session. COMMUNITY = widely repeated, not read on a fetched page. UNVERIFIED = not confirmed, test before trusting.
Some fetches failed (Fedora Docs, Arch Wiki, Debian Wiki, Reddit were blocked; see Not verified). Say so when a question lands there.

Related skills (do not duplicate them):
- `bazzite-kde-linux` for Bazzite install, images, Gaming Mode, updates, rollback, layering costs.
- `linux-security-hardening` for encryption, Secure Boot, firewall policy, backups.
- `linux-audio-production`, `wine-proton-bottles`, `home-network-specialist` for their topics.

## How to teach (assume the reader is not a programmer)
1. Plain words first, then the exact command, then what good output looks like, then how to undo.
2. One command at a time. Ask for the output before the next step.
3. Say which machine a command runs on: host terminal, inside a container, or on another PC.
4. Prefer read-only commands first (list, status, show). Change things only after diagnosis.
5. Never ask for passwords, keys or real public IPs in chat. Use placeholders.
6. Before a risky step: say what could go wrong, and what to back up first.
7. Distro-specific advice needs the distro named first. Ask: `cat /etc/os-release`. COMMUNITY.

## 1. How Linux is organised
- Linux itself is the kernel: it talks to hardware and runs programs. VERIFIED (kernel.org README: "a clone of the operating system Unix, written from scratch by Linus Torvalds"). The kernel docs README does not define "kernel" in its opening lines: UNVERIFIED wording, the split below is COMMUNITY.
- A distribution (distro) = kernel + system tools + package manager + default settings + a support policy. COMMUNITY.
- Desktop environment (DE) = the look and feel: KDE Plasma, GNOME, XFCE. It is a separate layer from the distro. COMMUNITY. Bazzite here uses KDE.
- Display server: Wayland or X11, chosen by the DE and distro. COMMUNITY.
- Sound server: PipeWire on modern distros. COMMUNITY (see `linux-audio-production`).
- Package formats (what an app is shipped as):
  - RPM (`.rpm`): Fedora, RHEL, openSUSE. COMMUNITY.
  - DEB (`.deb`): Debian, Ubuntu, Mint. COMMUNITY.
  - Arch packages via pacman, plus the AUR (user-made build recipes, not vetted). COMMUNITY.
  - Flatpak: sandboxed desktop apps. VERIFIED ("a system for building, distributing, and running sandboxed desktop applications on Linux", docs.flatpak.org).
  - AppImage: one downloadable file you make executable and run. COMMUNITY.
  - Nix and Homebrew: separate package systems that sit beside the distro's own. See section 5.

## 2. Filesystem layout (FHS) and immutable variants
Linux has one tree starting at `/`. There are no drive letters. VERIFIED (mount man page: attaches a filesystem "to the big file tree").
Directory purposes, VERIFIED from the hier(7) man page:
- `/etc`: configuration files local to the machine.
- `/home`: home directories for users.
- `/usr`: shareable, read-only data. `/usr/bin` is the primary directory for programs. `/usr/local` is for programs local to the site.
- `/var`: files that change in size, such as spool and log files. `/var/log` holds log files.
- `/opt`: add-on packages with static files.
- `/srv`: data served by this system.
- `/tmp`: temporary files that may be deleted without notice.
- `/boot`: static files for the boot loader.
- `/dev`: device files. `/proc` and `/sys`: live info about processes and the kernel.
- `/run`: information about the system since boot.
- `/mnt` and `/media`: mount points (temporary and removable media).
- `/root`: usually the root user's home. `/sbin`: commands needed to boot, usually not run by normal users.
Notes:
- The hier page is a man page. The formal FHS 3.0 document (refspecs.linuxfoundation.org) was not fetched: the formal standard text is UNVERIFIED.
- Hidden files start with a dot (`~/.config`, `~/.local/share`). App settings live there. COMMUNITY.
- Immutable (Atomic) variants: `/usr` is replaced as a whole image and is read-only; `/etc` and `/var` stay writable; rpm-ostree keeps two bootable deployments by default. VERIFIED for the two-deployment default and offline, reboot-applied updates (rpm-ostree handbook). The read-only `/usr` and writable `/etc`/`/var` detail comes from the `bazzite-kde-linux` skill (its source: docs.bazzite.gg).
- On Fedora Atomic, `/home` may be a link to `/var/home`. COMMUNITY.
- Consequence: instructions that say "edit a file under /usr" or "sudo dnf install" fail on Bazzite. Use the install order in section 5.

## 3. Users, groups, permissions, sudo
- Every process has user and group IDs, plus supplementary groups used in permission checks. VERIFIED (credentials(7)).
- Superuser is UID 0 (root). The credentials page does not say this: COMMUNITY.
- Read permission output with `ls -l`: first character is the type, then three triplets for owner, group, others. COMMUNITY.
- Numeric modes: read=4, write=2, execute=1, summed per digit for owner, group, others. `755` = owner rwx, group and others r-x. VERIFIED (chmod(1)).
- Symbolic modes: `u+x` adds execute for the owner, `go-w` removes write for group and others. VERIFIED (chmod(1)).
- On a directory, `x` means "search" (you can enter it). VERIFIED (chmod(1)). The sticky bit on a directory stops users removing files they do not own. VERIFIED (chmod(1)).
- Check your IDs: `id`. List who owns a file: `ls -l <file>`. COMMUNITY.
- sudo runs one command as root. What a user may run is decided by the sudoers policy. VERIFIED (sudoers(5): "determines a user's sudo privileges"). Edit with `visudo`, never a plain editor: COMMUNITY (the man page excerpt read did not state it).
- Admin group name differs: `wheel` on Fedora/RHEL, `sudo` on Debian/Ubuntu. COMMUNITY (the sudoers page does not mention it). Red Hat docs have chapters "Managing users and groups" and "Managing sudo access": VERIFIED titles only.
- Rules:
  - Never `sudo chmod -R 777` or `sudo chown -R` on system folders or your whole home. COMMUNITY.
  - Never run a graphical app with sudo; it can leave root-owned files in your home. COMMUNITY.
  - Wrong-permission fix order: look first (`ls -l`), change one file, test. COMMUNITY.
  - Files copied from NTFS or exFAT drives show wide-open permissions. That is normal, see section 6.

## 4. Processes and systemd
- systemd starts and supervises services. Its objects are units: `.service`, `.timer`, `.mount`, `.target`, `.socket`. COMMUNITY for the list; unit files are VERIFIED (systemd.unit).
- Check, then change:
  - `systemctl status <unit>`: runtime state plus recent journal lines. VERIFIED.
  - `systemctl list-units --failed`: failed units. VERIFIED.
  - `systemctl is-active <unit>` and `is-enabled <unit>`. VERIFIED.
  - `sudo systemctl start|stop|restart <unit>`. VERIFIED.
  - `sudo systemctl enable --now <unit>`: enable hooks the unit into boot, it does NOT start it; `--now` also starts it. VERIFIED ("Enabling and starting units is orthogonal").
  - `sudo systemctl mask <unit>`: links to /dev/null so nothing can start it, even by hand. VERIFIED. Undo with `unmask`: COMMUNITY.
  - `sudo systemctl daemon-reload` after editing unit files. VERIFIED.
- Unit file locations, highest priority first: `/etc/systemd/system` (admin), `/run/systemd/system`, `/usr/local/lib/systemd/system`, `/usr/lib/systemd/system` (distro packages). VERIFIED (systemd.unit).
- Do not edit files in `/usr/lib/systemd/system`. Use a drop-in: a folder `<unit>.service.d/` with a `.conf` file; drop-ins merge after the main file, and `/etc` beats `/run` beats `/usr/lib`. VERIFIED. Easy way: `sudo systemctl edit <unit>`: COMMUNITY.
- User services run as you, with no sudo. Add `--user` to systemctl and journalctl. VERIFIED (`--user` talks to the user's service manager). Unit files go in `~/.config/systemd/user`. VERIFIED. `systemd-analyze --user unit-paths` shows the real list. VERIFIED.
- User services stopping when you log out, and `loginctl enable-linger`: UNVERIFIED (loginctl page not fetched, rate limit).
- Timers (cron replacement): a `.timer` activates the same-named `.service` by default. VERIFIED (systemd.timer). `OnCalendar=` follows wall-clock time, `OnBootSec=` counts from boot. VERIFIED. `Persistent=true` runs a missed calendar timer after the machine was off; default is false. VERIFIED. List them: `systemctl list-timers`, ordered by next run. VERIFIED. A timer does not start a second copy if the service is still running. VERIFIED.
- Processes: `ps aux`, `top`, `htop` (if installed), `kill <pid>`, `kill -9 <pid>` as last resort. COMMUNITY (ps page not fetched). Try the plain `kill` first.
- Boot slow? `systemd-analyze blame`. COMMUNITY (page not fetched).

## 5. Package managers by family
Pick the tool by distro, not by habit. Confirm with `cat /etc/os-release`.

| Family | Tool | Update | Install |
|---|---|---|---|
| Fedora/RHEL | dnf | `sudo dnf upgrade` | `sudo dnf install x` |
| Fedora Atomic / Bazzite | rpm-ostree | `rpm-ostree upgrade` or `ujust update` | layering, last resort |
| Debian/Ubuntu | apt | `sudo apt update && sudo apt upgrade` | `sudo apt install x` |
| Arch | pacman | `sudo pacman -Syu` | `sudo pacman -S x` |
| openSUSE | zypper | `sudo zypper refresh`, `zypper up` | `sudo zypper in x` |

- The dnf, apt and pacman commands in the table are COMMUNITY (their pages were blocked, see Not verified).
- zypper: VERIFIED (openSUSE SDB). `zypper ref` refreshes metadata, `zypper in`, `zypper rm` (`-u` also removes unneeded dependencies), `zypper se` searches. `zypper up` updates packages; `zypper dup` is a distribution upgrade that can also downgrade packages to match the repositories. Use `dup` on Tumbleweed or when switching release, not as a casual update.
- Arch: never run `pacman -Sy` alone then install (partial upgrade). COMMUNITY (Arch Wiki blocked, unverified here). Always `-Syu`.
- Debian/Ubuntu: do not mix repositories from other releases or random PPAs without need. COMMUNITY (Debian wiki blocked).
- rpm-ostree on Atomic systems, VERIFIED (rpm-ostree handbook):
  - Layered packages persist across upgrades, rebases and deploys.
  - `rpm-ostree status` lists deployments in bootloader order; the first is the default.
  - `rpm-ostree rollback` swaps the default deployment with the other one.
  - Upgrades keep at most two bootable deployments by default.
  - Changes apply after reboot; operations are transactional and offline. `install -yA` can live-apply simple additions.
  - Bazzite costs of layering: see `bazzite-kde-linux`.
- Flatpak: sandboxed apps with a shared runtime. VERIFIED. Typical commands: `flatpak install flathub <app>`, `flatpak run <app>`, `flatpak update`, `flatpak list`. COMMUNITY (docs intro page showed no commands). Permissions review with Flatseal: see `linux-security-hardening`.
- AppImage: download only from the project's own site, `chmod +x file.AppImage`, run. COMMUNITY. Gear Lever manages them on Bazzite (per `bazzite-kde-linux`).
- Homebrew on Linux: installs to `/home/linuxbrew/.linuxbrew`; needs a system compiler and build tools; `brew doctor` troubleshoots; 32-bit x86 unsupported. VERIFIED (docs.brew.sh).
- Distrobox: runs another distro in a container; wraps podman, docker or lilipod. VERIFIED (distrobox.it). It shares your HOME, USB devices, graphics and audio, and "the container will have complete access to your home". VERIFIED. So it is not a security sandbox. Rootless podman is the recommended setup for security. VERIFIED. Commands: `distrobox create -n test`, `distrobox enter test`, `distrobox-export` (inside the container, shows apps on the host). VERIFIED. Host examples listed include Fedora Atomic Desktops and SteamOS 3. VERIFIED.
- Nix (own store at /nix/store, works beside any distro) and Toolbx (Fedora's container tool, `toolbox create`/`enter`): COMMUNITY, pages not fetched.
- Which to use on Bazzite: Bazaar/Flatpak, then Homebrew (CLI), then Distrobox, then AppImage, then layering. See `bazzite-kde-linux` for the reasoning.
- Rules: one package tool per job; never `sudo pip install` or `sudo npm -g` to fix a missing tool (can break system tools, COMMUNITY); use a Distrobox container for dev tools instead.

## 6. Disks, mounts, filesystems
- See disks: `lsblk -f` (name, filesystem type, label, UUID, free space, mount points). VERIFIED (lsblk(8)). `blkid` is the authoritative source for filesystem info. VERIFIED. Never guess a device: re-run `lsblk` right before any write.
- Device names (`/dev/sda`, `/dev/nvme0n1`) can change between boots. Use `UUID=` or `LABEL=` in fstab. VERIFIED (fstab(5) calls it the recommended method).
- `/etc/fstab` has six fields: device, mount point, type, options, dump, fsck pass. VERIFIED (fstab(5)).
  - Options: use at least `defaults`. `nofail` = no error if the device is missing. VERIFIED. For USB or secondary drives, `nofail` avoids a stuck boot. COMMUNITY.
  - fsck pass: root should be 1, others 2, 0 = never checked. VERIFIED.
  - Mount manually: `mount`; override fstab options with `-o`; `-o ro` mounts read-only; `mount --bind a b` shows one folder in two places. VERIFIED (mount(8)).
- Test an fstab edit before reboot: `sudo mount -a` (errors show now). COMMUNITY. Keep a copy: `sudo cp /etc/fstab /etc/fstab.bak`. COMMUNITY.
- On Atomic systems `/etc/fstab` still works and survives updates. COMMUNITY. Do not mount over `/usr`.
- Filesystems:
  - ext4: the long-standing Linux default. Red Hat has "Getting started with an ext4 file system". VERIFIED title. "Default" claim COMMUNITY.
  - XFS: RHEL's default; Red Hat has chapters on creating, backing up, growing XFS. VERIFIED titles. XFS cannot be shrunk: COMMUNITY.
  - btrfs: copy-on-write, snapshots, subvolumes, checksums on data and metadata, compression (ZLIB, LZO, ZSTD), software RAID 0/1/10. VERIFIED. RAID5/6 is "experimental, not production-ready". VERIFIED. Fedora Workstation and Bazzite default to btrfs: UNVERIFIED (Bazzite default root filesystem not fetched; check with `lsblk -f`).
  - NTFS: kernel `ntfs3` driver is read-write, up to NTFS 3.1; mount type `ntfs3`; `force` mounts a dirty volume and is "not recommended"; options `uid=`, `gid=`, `umask=`, `discard`. VERIFIED (kernel.org ntfs3 page). Windows Fast Startup/hibernation leaves NTFS dirty: COMMUNITY. Turn it off in Windows before sharing a drive.
  - exFAT: shared drive for Windows, macOS and Linux with no permissions and no journal. COMMUNITY. Fine for transfer, bad for Linux game libraries or system use.
  - FAT32: 4 GB file limit. COMMUNITY.
- Game libraries on NTFS cause Proton problems. COMMUNITY. Prefer ext4 or btrfs for Steam libraries.
- Health: `sudo smartctl -H /dev/nvme0` (quick verdict), `sudo smartctl -a /dev/nvme0` (full), from the smartmontools package. COMMUNITY (smartmontools site blocked this session).
- fsck: checks and repairs a filesystem. Run it only on UNMOUNTED filesystems and never on the live root. COMMUNITY (fsck(8) fetch hit the rate limit). Use `fsck -n` (read-only dry run): UNVERIFIED flag meaning. Red Hat has the chapter "Checking and repairing a file system": VERIFIED title only.
- Free space: `df -h`, what is big: `du -h --max-depth=1 <path>`. COMMUNITY.
- Disk work rules: back up first; double check the device with `lsblk`; never `dd` or format from memory; unplug unrelated drives before partitioning. COMMUNITY.

## 7. Networking basics
- Desktop distros use NetworkManager. Red Hat docs cover it (nmcli, DNS server order, per-domain DNS, DHCP settings, debugging). VERIFIED chapter titles only.
- Quick checks, in this order (COMMUNITY):
  1. `ip -br addr`: do I have an address?
  2. `ip route`: is there a default gateway?
  3. `ping -c 3 <router IP>`, then `ping -c 3 1.1.1.1`, then `ping -c 3 example.com`.
  4. If IP ping works but the name does not: DNS problem. `resolvectl status` shows DNS servers (when systemd-resolved is used, UNVERIFIED on Bazzite).
  5. `nmcli device status`, `nmcli connection show`, `nmcli device wifi list`.
- Reading the result: no address = link or DHCP; address but no gateway = DHCP or manual config; gateway ok but internet not = router or ISP; IP ok but names fail = DNS. COMMUNITY.
- Firewalls:
  - firewalld (Fedora, Bazzite per `linux-security-hardening`): "a dynamically managed firewall", D-Bus service, zones assign trust levels to networks and interfaces, runtime and permanent configuration are separate. VERIFIED (firewalld.org). Commands such as `firewall-cmd --state` and `--get-default-zone`: see `linux-security-hardening`. Remember `--permanent` for changes that must survive reboot: COMMUNITY.
  - ufw (Ubuntu, Debian): off until you enable it; `sudo ufw enable`, `sudo ufw status verbose`, `sudo ufw allow <port>/tcp`; default is deny incoming, allow outgoing. VERIFIED (help.ubuntu.com).
  - Never run two firewall front-ends at once. COMMUNITY.

## 8. Hardware, drivers, modules, firmware
- Kernel drivers are often modules. `modprobe <name>` loads one with its dependencies; `modprobe -r <name>` removes it; modules live under `/lib/modules/$(uname -r)`. VERIFIED (modprobe(8)). The page says there is "usually no reason to remove modules". VERIFIED.
- Blocking a module: config lives in `modprobe.d` (see modprobe.d(5), not fetched); the boot-line form `modprobe.blacklist=<module>` exists. VERIFIED for the existence of both references; file syntax UNVERIFIED. On Atomic systems prefer kernel arguments (section 9).
- Loaded modules: `lsmod`. Module info: `modinfo <name>`. COMMUNITY.
- Hardware lists (COMMUNITY): `lspci -nnk` (PCI devices, with "Kernel driver in use"), `lsusb`, `lscpu`, `inxi -Fxz` if installed. A device with no "driver in use" line has no driver bound.
- Kernel messages: `dmesg`. VERIFIED options: `-w` follow, `-T` human timestamps (can be wrong after suspend), `--level=err,warn`, `-H` human output. Needs root on some systems. COMMUNITY.
- Same messages through journald: `journalctl -k` (kernel only), `journalctl -b -p err`. VERIFIED.
- GPU drivers:
  - AMD and Intel use the in-kernel open drivers (Mesa for graphics). COMMUNITY.
  - NVIDIA: Bazzite ships the driver in the image (`-nvidia`, `-nvidia-open`). Details per `bazzite-kde-linux`.
  - On other distros the NVIDIA driver is a separate package or module; mismatch after a kernel update is a classic black screen. COMMUNITY.
  - Check: `lspci -nnk | grep -A3 -i vga` and `glxinfo -B` (needs mesa-utils). COMMUNITY.

## 9. Boot: UEFI, bootloaders, initramfs, kernel arguments
Boot order (COMMUNITY summary): firmware (UEFI) reads the EFI System Partition, starts a boot loader, which loads the kernel and initramfs, which mounts the real root, which starts systemd.
- UEFI vs BIOS: modern PCs are UEFI. UEFI keeps boot programs on the EFI System Partition (ESP). COMMUNITY. systemd-boot supports UEFI only. VERIFIED.
- ESP is usually at `/efi`, `/boot` or `/boot/efi`. VERIFIED (systemd-boot page).
- GRUB: the common boot loader on Fedora and Bazzite. Menu at power-on shows the previous deployment on Atomic systems (per `bazzite-kde-linux`). GRUB2 doc page was blocked: commands such as `grub2-mkconfig` are COMMUNITY. Do not run it on Atomic systems without checking: UNVERIFIED.
- systemd-boot: simple UEFI boot manager with a text menu and a built-in kernel command line editor; entries are files in `/loader/entries/` on the ESP; unified kernel images are in `/EFI/Linux/`. VERIFIED.
- Dual boot: install Windows first, then Linux; Windows updates can reset boot order. COMMUNITY.
- initrd/initramfs: a small temporary root loaded with the kernel. The kernel starts with minimal built-in drivers and more modules load from it, then the real root is mounted and `/sbin/init` runs. VERIFIED (kernel.org initrd page, which uses the older term "initrd"). "Initramfs" as the modern name: COMMUNITY. Missing drivers or an encrypted root failing here gives a drop to an emergency shell. COMMUNITY.
- Kernel arguments (command line): the kernel reads them from the boot loader; see them live with `cat /proc/cmdline`. VERIFIED (`/proc/cmdline`). Module parameters can be set as `module.param=value`, for example `usbcore.blinkenlights=1`. Hyphens and underscores are interchangeable; values with spaces go in double quotes; length is limited. VERIFIED (kernel-parameters).
- `nomodeset` and `quiet`: the kernel page excerpt did not show them. `nomodeset` as a black-screen workaround: COMMUNITY. UNVERIFIED on current kernels.
- One-time test: at the GRUB menu press `e`, add the argument to the line starting with `linux`, press Ctrl+X. Nothing is saved, a reboot undoes it. COMMUNITY.
- Permanent change on Bazzite/Fedora Atomic: `rpm-ostree kargs --append=<arg>`. COMMUNITY (the rpm-ostree handbook page read did not cover kargs). Check with `rpm-ostree kargs`. Reboot after.
- Rollback and pinning: see `bazzite-kde-linux`. Secure Boot and TPM: see `linux-security-hardening`.
- Rescue rules: keep a live USB (Bazzite or Fedora ISO) made before you need it; know your firmware key (F2, F12, Del) for boot menu. COMMUNITY.

## 10. Logs: reading them
- journald holds most logs. `journalctl` options, VERIFIED (journalctl(1)):
  - `-b` this boot; `-b -1` the boot before last (previous boot).
  - `-p` priority, single level or range `FROM..TO` (for example `-p err`; also `-p warning..err`).
  - `-u <unit>` one unit (repeatable); `--user` and `--user-unit=` for user services.
  - `-f` follow live; `-n <lines>` last lines.
  - `--since=` and `--until=` (short `-S`, `-U`) for a time window.
  - `-k` kernel messages only.
  - `--disk-usage`, `--vacuum-size=`, `--vacuum-time=` to see and trim log size.
- Previous boot logs only exist if the journal is persistent (`/var/log/journal`). COMMUNITY.
- Reading an error:
  1. Find the first error, not the last. Later errors are often consequences. COMMUNITY.
  2. Look for words: "failed", "denied", "not found", "timeout", "no space". COMMUNITY.
  3. "Permission denied" can be file permissions OR SELinux; check `sudo ausearch -m avc -ts recent` or `journalctl -t setroubleshoot`. COMMUNITY. Never turn SELinux off (see `bazzite-kde-linux`).
  4. "No space left" can also mean out of inodes: `df -h` and `df -i`. COMMUNITY.
  5. Copy exact text into a search, with distro name and version.
- App logs: run the app from a terminal to see its output; for Flatpak, `flatpak run <app>`. COMMUNITY. Flatpak and Steam also keep logs under `~/.var/app` and `~/.steam`: UNVERIFIED paths.

## 11. Troubleshooting method
Ask first (COMMUNITY):
1. Distro, version, image name (`cat /etc/os-release`, `rpm-ostree status` on Atomic).
2. What changed just before: update, new hardware, new app, settings.
3. Exact error text or what happens. Photo of the screen is fine.
4. Does it happen every time? Which user? After reboot?
5. Is there a known-good state (older deployment, other user, live USB)?
Then follow this loop: reproduce, read-only checks, one change, test, undo if no help, note what you did.

Tree: it will not boot to desktop
1. Does the firmware logo show? No: hardware or power; try another boot device.
2. GRUB menu shows? No: ESP or boot order problem. Try the boot menu key.
3. Menu shows, then black screen: try the previous deployment entry (Atomic). COMMUNITY. If that works, the update caused it; rollback per `bazzite-kde-linux`.
4. Still black: one-time add a kernel argument (section 9), try integrated graphics, check GPU cable.
5. Emergency shell: `journalctl -xb -p err`, check disk space and fstab.

Tree: app will not start
1. Start from a terminal; read first error.
2. Flatpak: `flatpak update`; check permissions (Flatseal); try `flatpak run --verbose` (flag UNVERIFIED); reinstall; remove data in `~/.var/app/<app>` only after backup.
3. Native: missing library = wrong package source; try a Distrobox.
4. Windows app: see `wine-proton-bottles`.

Tree: no sound, no network, slow system
- Sound: `linux-audio-production`. Network: section 7 steps in order.
- Slow: `top` (CPU/memory), `df -h` (disk full), `systemctl list-units --failed`, `journalctl -b -p err`, `systemd-analyze blame` for boot time. COMMUNITY.

Tree: update failed on Atomic
1. `df -h` (need space; Bazzite wants 3 percent free per `bazzite-kde-linux`).
2. `rpm-ostree status` and look for layered packages that block.
3. Remove layering one package at a time, retry. See `bazzite-kde-linux`.

When stuck: give the reader a short "what I know / what I tried / next" note to paste into a forum. Forums: Universal Blue and Bazzite Discord/forum for Bazzite; r/linux4noobs and r/linuxquestions are common places (could not be fetched, quality UNVERIFIED). Never run commands from a forum post that you cannot explain.

## 12. Safe-practice rules
1. Back up before any disk, boot or system change: 3-2-1 backups per `linux-security-hardening`. Test a restore.
2. Never `curl ... | bash` or `sudo sh` a script you have not read. Download, read, then run. COMMUNITY. Prefer Flatpak, Homebrew or distro packages over installer scripts.
3. Test on a copy: Distrobox container, a spare disk, or a live USB. Distrobox is not a sandbox, it sees your home. VERIFIED.
4. Check a command before pressing Enter: `rm -rf`, `dd`, `mkfs`, `chmod -R`, `chown -R`, and anything with `sudo` and a wildcard. COMMUNITY.
5. Prefer read-only checks first (`status`, `list`, `show`, `-n` dry-run flags where they exist).
6. Do not copy a Stack Overflow or forum fix for another distro without translating it (section 5 table).
7. Keep one working path to a desktop: do not remove your only kernel, boot entry or user.
8. Update regularly; reboot to apply on Atomic systems. VERIFIED for reboot requirement (rpm-ostree handbook).

## 13. Distro families and which to pick
Use this to answer "other distros I will meet" (all COMMUNITY unless marked; I did not fetch the distro project pages):
- Fedora family: Fedora Workstation/KDE, Fedora Atomic (Silverblue, Kinoite), Bazzite, RHEL, Rocky, Alma. dnf/rpm. Fast release rhythm for Fedora.
- Debian family: Debian, Ubuntu, Linux Mint, Pop!_OS. apt/dpkg. Debian stable moves slowly and is very stable.
- Arch family: Arch, EndeavourOS, Manjaro, CachyOS, SteamOS 3. pacman and AUR. Rolling; needs attention. The `Distrobox` page lists SteamOS 3 as a supported host, VERIFIED.
- openSUSE: Tumbleweed (rolling), Leap, Aeon/Kalpa (immutable). zypper. YaST tools. Aeon/Kalpa named on distrobox.it as immutable hosts. VERIFIED.
- Immutable ones named on distrobox.it: Fedora Atomic Desktops, Vanilla OS, Endless OS, ChromeOS, SteamOS 3, openSUSE Aeon/Kalpa. VERIFIED.
Pick guide:
- PC with easy rollback and gaming: Bazzite (see `bazzite-kde-linux`).
- Server or NAS-like box: stable Debian/Ubuntu LTS or the appliance OS the project recommends (Unraid is its own product, see `unraid-specialist`). COMMUNITY.
- Support policy matters more than looks: how long updates last, who maintains it. COMMUNITY. Check the project's own page before recommending a distro: UNVERIFIED claims about release dates and support periods.

## 14. Common beginner mistakes
1. Following a tutorial for another distro (`apt` on Bazzite). Check the family first.
2. Using `sudo` for everything, including GUI apps.
3. `chmod -R 777` to "fix" a permission error.
4. Piping an install script from the web into a shell without reading it.
5. Layering packages on Atomic systems because it feels like `apt install`.
6. Editing `/etc/fstab` without a backup or without testing `mount -a`.
7. Using `/dev/sdX` names in fstab instead of UUID. VERIFIED as discouraged (fstab(5)).
8. Formatting or partitioning the wrong disk (check `lsblk` twice).
9. Putting game libraries or system data on NTFS or exFAT.
10. Leaving Windows Fast Startup on, then mounting its NTFS drive. COMMUNITY.
11. Partial upgrades on Arch (`-Sy` alone) and mixing releases on Debian.
12. Disabling SELinux or the firewall to "make it work".
13. Ignoring updates for months, then updating with a full disk.
14. Not reading the first error line. Fixing a symptom, not the cause.
15. Making several changes at once, so nothing can be undone cleanly.
16. Skipping backups and a live USB until after something breaks.
17. Assuming a container isolates you: Distrobox shares the home folder. VERIFIED.

## Learning resources
- The Linux Command Line by William Shotts: free PDF download, 596 pages, aimed at new command line users, license BY-NC-ND. VERIFIED (linuxcommand.org). Chapter list not fetched.
- man pages: man7.org online, `man <cmd>` locally; `<cmd> --help` for a short list. COMMUNITY.
- Red Hat Enterprise Linux documentation (docs.redhat.com) is a deep, accurate source for systemd, storage and networking, even for Fedora. Title list VERIFIED, content mostly not read.

## Not verified
- Blocked or failed fetches: docs.fedoraproject.org (dnf, Silverblue, Toolbx, nmcli, GRUB2: Anubis "Access Denied"), wiki.archlinux.org (pacman), wiki.debian.org (Apt, DontBreakDebian: challenge page), reddit.com, smartmontools.org, firewalld.org detail pages (only the overview read), refspecs.linuxfoundation.org (FHS 3.0), linuxfoundation.org, nixos.org manual, fsck(8), loginctl, systemd-analyze, cgroups, ps man pages (hourly fetch limit).
- Therefore UNVERIFIED or COMMUNITY: all dnf, apt, pacman commands; Toolbx; Nix details; GRUB commands; `rpm-ostree kargs`; `nomodeset`; smartctl; fsck options; `enable-linger`; `systemd-analyze blame`; `lspci`, `lsusb`, `lsmod`, `ip`, `ss`, `resolvectl`, `nmcli` command details; SELinux commands; distro family and pick guidance; filesystem defaults for Bazzite and Fedora; community forum quality.

## Sources (fetched 2026-10-23)
- https://man7.org/linux/man-pages/man7/hier.7.html
- https://man7.org/linux/man-pages/man1/chmod.1.html
- https://man7.org/linux/man-pages/man7/credentials.7.html
- https://man7.org/linux/man-pages/man5/sudoers.5.html
- https://man7.org/linux/man-pages/man5/fstab.5.html
- https://man7.org/linux/man-pages/man8/mount.8.html
- https://man7.org/linux/man-pages/man8/lsblk.8.html
- https://man7.org/linux/man-pages/man8/modprobe.8.html
- https://man7.org/linux/man-pages/man1/dmesg.1.html
- https://www.freedesktop.org/software/systemd/man/latest/systemctl.html
- https://www.freedesktop.org/software/systemd/man/latest/journalctl.html
- https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html
- https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html
- https://www.freedesktop.org/software/systemd/man/latest/systemd-boot.html
- https://www.kernel.org/doc/html/latest/admin-guide/README.html
- https://www.kernel.org/doc/html/latest/admin-guide/kernel-parameters.html
- https://www.kernel.org/doc/html/latest/admin-guide/initrd.html
- https://www.kernel.org/doc/html/latest/filesystems/ntfs3.html
- https://btrfs.readthedocs.io/en/latest/Introduction.html
- https://coreos.github.io/rpm-ostree/administrator-handbook/
- https://docs.flatpak.org/en/latest/introduction.html
- https://distrobox.it/
- https://docs.brew.sh/Homebrew-on-Linux
- https://en.opensuse.org/SDB:Zypper_usage
- https://help.ubuntu.com/community/UFW
- https://firewalld.org/documentation/
- https://linuxcommand.org/tlcl.php
- https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_basic_system_settings/index
- https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_managing_networking/index
- https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_file_systems/index
