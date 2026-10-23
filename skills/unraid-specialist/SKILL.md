---
name: unraid-specialist
description: Use when advising on Unraid home servers, covering storage, shares, Docker, backups, secure remote access, updates, recovery and mounting shares from a Bazzite Linux desktop.
---

# Unraid specialist

Research date 2026-10-21. Labels: VERIFIED (source fetched), COMMUNITY (forum or user report), UNVERIFIED (not verified; check before acting).

## How to work with the reader
- Assume the reader is not a programmer. Plain words first, then the exact click path or command.
- One change at a time. After each step say what "success" looks like, then stop.
- Never ask the reader to paste passwords, keys or real IPs. Use placeholders: `<server-ip>`, `<user>`, `<share>`.
- Back up before any risky step (flash backup, appdata backup).
- Typical setup: Unraid at home with Nextcloud and Pi-hole; remote access from a Linux desktop such as Bazzite (outbound connections only from the desktop); storage for creative projects and large media libraries.

## Version and licensing
- Latest stable seen: 7.3.3, announced 8 Oct 2026; security fixes (OpenSSL, Samba, PHP, nginx), kernel 6.18.54, Docker 29.8.2. VERIFIED (forum 7.3.3 thread)
- 7.3.3 reports: reboot loop on one AMD system, Interface Rules possibly reset, Unassigned Devices NVMe settings lost. COMMUNITY (same thread). Check Network Settings after updating.
- 7.3.1 (2026-05-27) was a security and bug-fix release. VERIFIED (7.3.1 notes)
- License is perpetual and per server; free 30-day trial; all sales final. VERIFIED (licensing FAQ)
- Tiers announced March 2024: Starter $49 (6 devices), Unleashed $109 (unlimited), Lifetime $249; Starter/Unleashed include 1 year of updates, extension $36/yr. VERIFIED for the 2024 announcement (forum pricing thread); current prices UNVERIFIED (pricing page was blocked). Without an extension you keep the OS and security patches of your minor version.
- Old Basic/Plus/Pro keys are "Legacy" with updates for life. VERIFIED (same thread)
- Since 7.3 a license can be tied to a TPM 2.0 chip instead of the USB stick (Tools, Registration, Move License to TPM). VERIFIED (TPM FAQ)

## Array vs pools (plain words)
- Array: your big bulk storage. Drives can differ in size; add one at a time. VERIFIED (what-is-unraid)
- Parity: up to 2 parity drives; parity must be equal or larger than the largest data drive; updated in real time; rebuilds one failed drive. VERIFIED (what-is-unraid, replacing-disks)
- Parity is not a backup. It does not protect against deletion, ransomware or corruption. VERIFIED in spirit (file-systems page: parity cannot fix filesystem corruption)
- Pools: SSD groups (cache) for appdata, Docker, VMs and fast writes. Single-drive pool has no redundancy; multi-drive BTRFS/ZFS pool can mirror. VERIFIED (cache-pools)
- Keep 10-15% free on a BTRFS pool. VERIFIED (cache-pools)

## Cache and mover
- Each share has Primary storage, Secondary storage and a Mover action (cache to array, or array to cache). VERIFIED (cache-pools)
- Mover moves files on a schedule; files open at that time may be skipped, so stop Docker/VMs first when moving manually. VERIFIED
- Do not use `mv` in `/mnt/user` to move between pool and array; it can just rename in place. VERIFIED
- Set pool minimum free space to at least double your largest file; 0 causes disk-full errors. VERIFIED
- For sample libraries and project files: write to a cache-first share, let mover archive them to the array. Suggestion, UNVERIFIED as a best practice.

## File systems
- Array drives: XFS (default). Single-drive cache: XFS or EXT4. Multi-drive pools: BTRFS (default) or ZFS. VERIFIED (file-systems)
- BTRFS RAID 5/6 are experimental; ZFS RAIDZ is more mature. VERIFIED (cache-pools)
- ZFS has no fsck; use scrub. BTRFS: scrub weekly (heavy use) or monthly. VERIFIED (file-systems)
- 7.2+: single-vdev RAIDZ pools can grow one drive at a time; "Upgrade Pool" may block downgrades. VERIFIED (cache-pools)
- Never click Format on a drive during recovery; it wipes it. VERIFIED (replacing-disks)
- Rebuilding parity copies existing filesystem corruption; repair first. VERIFIED (file-systems)

## Shares and permissions
- User shares merge top-level folders across drives at `/mnt/user`. Disk shares are off by default. VERIFIED (shares)
- New shares are not network-visible by default. Keep them Private and grant access per user. VERIFIED
- Do not change permissions on `appdata`, `system`, `domains`. VERIFIED
- Never copy between a user share and a disk share with the same folder name (data loss risk). VERIFIED
- Allocation: High-water (default) is recommended. Minimum free space: twice the largest file. VERIFIED
- Share users cannot use WebGUI or SSH; root cannot use SMB/NFS. Only root creates share users. VERIFIED (user-management)

## Mounting from a Bazzite desktop (SMB)
- Package `cifs-utils` provides `mount.cifs`. VERIFIED (RHEL docs). Bazzite is immutable; layering with `rpm-ostree install` needs a reboot, is a last resort, and can block updates. VERIFIED (Bazzite rpm-ostree docs). Whether `cifs-utils` is already in the Bazzite image: UNVERIFIED; run `which mount.cifs` first.
- Alternative with no layering: KDE Dolphin can open `smb://<server-ip>/<share>` (uses KDE network access). UNVERIFIED for Bazzite; test it.
- Manual test: `sudo mount -t cifs -o username=<user>,vers=3.0 //<server-ip>/<share> /mnt/unraid` (syntax VERIFIED, RHEL docs; `vers=3.0` from RHEL example).
- Credentials file (keep password out of fstab): `/root/smb.cred` with lines `username=`, `password=`; then `chmod 600`. VERIFIED (RHEL docs)
- fstab line form: `//<server-ip>/<share> /mnt/unraid cifs credentials=/root/smb.cred 0 0`; test with `mount /mnt/unraid`. VERIFIED (RHEL docs)
- Boot-time automount: a forum user fixed non-mounting entries by using `x-systemd.automount,credentials=...` without `_netdev`, `noserverino`, `uid`, `gid`. COMMUNITY (Unraid forum 186760); the thread did not say which option caused it.
- To make files owned by your desktop user, `uid=`/`gid=` options exist in `mount.cifs(8)`; not covered by the sources fetched, UNVERIFIED.
- Bazzite docs on drive mounting cover local drives via GNOME Disks only, not network shares. VERIFIED (Bazzite automount page)
- NFS: Unraid has an NFS service, and a Bazzite forum user mounted NFS through fstab with `nofail` options. COMMUNITY (Level1Techs). NFS has weak per-user security; prefer SMB with a user. UNVERIFIED opinion.

## Docker basics
- Docker data lives in `docker.img` (BTRFS) in the `system` share, ideally on a cache pool. VERIFIED (Docker overview; a directory option exists in newer versions, UNVERIFIED).
- Appdata (settings, libraries) belongs in the `appdata` share, outside the container. VERIFIED
- Templates: fill the form; change only the host port, not the container port. VERIFIED
- Network types: Bridge (default, safest), Host, Custom (own LAN IP), None. VERIFIED
- Container paths vs host paths: apps need container paths. Paths are case sensitive. VERIFIED
- Wrong-looking new folders mean a bad path mapping. VERIFIED
- Use the most restrictive access mode (read-only if possible). VERIFIED
- Start databases before apps that need them (Advanced View, startup order). VERIFIED
- Docker Compose is not native. No scheduled start/stop natively; use User Scripts. VERIFIED
- Custom Docker network lets containers reach each other by name. VERIFIED (Trash Guides)
- Pi-hole: if it gets its own LAN IP (custom network), the Unraid host may not reach it by default. UNVERIFIED; verify before changing.
- Updates: how to update containers was not covered by fetched docs; use the Docker tab update controls. UNVERIFIED.

## Community Apps
- Adds an Apps tab; install plugins and containers from it. Vetting is basic; read the support thread and check the developer. VERIFIED (CA docs)
- Action Center flags updates, deprecated and blacklisted apps. VERIFIED

## VMs and GPU passthrough (brief)
- Unraid has VMs (docs: Create virtual machines, 5 pages). VERIFIED (index only). Passthrough details not researched: UNVERIFIED. A TPM cannot be used from inside a VM. VERIFIED.

## Backups (3-2-1)
- 3 copies, 2 media, 1 off-site. Standard rule; apply to your important projects. UNVERIFIED as docs claim.
- Flash backup: Main tab, boot device, Boot Device Backup (labeled Flash before 7.3.0). Keep zip off the server plus a screenshot of disk assignments. VERIFIED (changing-flash-device)
- Appdata Backup plugin (Robin Kluth) backs up Docker volumes, metadata and flash; targets 6.12+; shows a feature-freeze banner. VERIFIED (CA page). Destination advice not stated: UNVERIFIED.

## UPS, notifications, SMART
- Power loss is the most common cause of unsafe shutdowns; use a UPS. VERIFIED (array-health)
- Unclean shutdown triggers an automatic parity check (non-correcting by default). VERIFIED
- Notifications are under Settings, User Preferences. VERIFIED (Tour WebGUI). UPS settings location UNVERIFIED.
- Check SMART reports regularly and before rebuilds; status reports do not include SMART. VERIFIED
- CRC errors usually point to cables. VERIFIED (replacing-disks)

## Updating safely
1. Back up flash. 2. Read the release notes (rollback section). 3. Update plugins. 4. Tools, Update OS, reboot. VERIFIED (Updating Unraid)
- Rollback: Tools, Downgrade OS; else manual `previous` folder method in the docs. VERIFIED
- ZFS pool upgrades may block rollback; back up first. VERIFIED

## Security
- Do not expose the WebGUI to the internet or forward ports to it. UNVERIFIED as a direct quote (not found in fetched pages); docs do stress least privilege. VERIFIED (security-fundamentals)
- Strong root password; limit SSH; root can use SSH keys. VERIFIED (user-management)
- Anyone with the USB stick can reset the root password; keep it safe. VERIFIED
- Use HTTPS. Turning SSL off exposes credentials. VERIFIED (securing-your-connection)
- Unraid Connect remote access needs SSL; Strict mode can lock you out if DNS fails. VERIFIED. Whether Connect is safe enough for you: decide by reading its docs; UNVERIFIED here.
- Tailscale (official plugin): no port forwarding, WireGuard based, free tier 3 users and 100 devices; Funnel makes services public, avoid. VERIFIED (Tailscale docs). Hostnames in HTTPS certificates are public. VERIFIED
- WireGuard: needs UDP 51820 forwarded or UPnP; docs suggest Tailscale for most users. VERIFIED
- Suggested approach: install Tailscale on Unraid and on the Bazzite desktop, then connect over the tailnet; the desktop only makes outbound connections. Bazzite Tailscale install method UNVERIFIED.
- Firewall: no Unraid firewall docs fetched. UNVERIFIED; keep it behind the router with no forwarded ports.

## Disaster recovery
- Failed data disk: check syslog and SMART, confirm new disk is not larger than parity, stop array, assign to the failed slot, start (rebuild). Run a parity check first when upgrading. VERIFIED (replacing-disks)
- Keep the old disk until the rebuild is verified. Do not format. VERIFIED
- More failures than parity: stop writes, ask the forum with diagnostics. VERIFIED
- Flash failure: use the USB Flash Creator with the backup zip, then Tools, Registration, Replace key. A second replacement within 12 months needs support. VERIFIED (changing-flash-device)
- No flash backup: assign all as data, note unmountable (likely parity), Tools, New Config. Risky; get forum help first. VERIFIED

## Monthly checklist
- Parity check result with zero errors (schedule monthly or quarterly, correcting). VERIFIED
- SMART review; replace drives with growing errors.
- Update plugins and containers; read release notes before the OS.
- Flash backup downloaded; appdata backup ran; restore tested occasionally.

## Troubleshooting tree
- Cannot reach WebGUI: ping server; check Tailscale; local console; use_ssl no as recovery. VERIFIED (use_ssl, securing-your-connection)
- Share not visible: network access and user permission on the share. VERIFIED (shares)
- Mount fails on PC: test manual mount first; then fstab with automount. VERIFIED/COMMUNITY
- Container will not start: logs; path mapping; port conflict; dependency order. VERIFIED
- Disk red X: SMART, cables, then replace. VERIFIED
- Unsafe shutdown: let the parity check run; add UPS. VERIFIED
- Locked out of WireGuard: delete `/boot/config/wireguard/autostart` and reboot. VERIFIED

## Sources (fetched)
- https://forums.unraid.net/topic/200836-unraid-os-733-now-available/
- https://docs.unraid.net/unraid-os/release-notes/7.3.1/
- https://docs.unraid.net/unraid-os/getting-started/what-is-unraid/
- https://docs.unraid.net/unraid-os/troubleshooting/licensing-faq
- https://docs.unraid.net/unraid-os/troubleshooting/tpm-licensing-faq/
- https://forums.unraid.net/topic/158737-new-unraid-os-license-pricing-timeline-and-faqs/
- https://docs.unraid.net/unraid-os/updating-unraid/
- https://docs.unraid.net/unraid-os/using-unraid-to/manage-storage/shares/
- https://docs.unraid.net/unraid-os/using-unraid-to/manage-storage/cache-pools/
- https://docs.unraid.net/unraid-os/using-unraid-to/manage-storage/file-systems/
- https://docs.unraid.net/unraid-os/using-unraid-to/manage-storage/array/array-health-and-maintenance/
- https://docs.unraid.net/unraid-os/using-unraid-to/manage-storage/array/replacing-disks-in-array/
- https://docs.unraid.net/unraid-os/system-administration/maintain-and-update/changing-the-flash-device/
- https://docs.unraid.net/unraid-os/system-administration/secure-your-server/security-fundamentals/
- https://docs.unraid.net/unraid-os/system-administration/secure-your-server/securing-your-connection/
- https://docs.unraid.net/unraid-os/system-administration/secure-your-server/user-management/
- https://docs.unraid.net/unraid-os/system-administration/secure-your-server/tailscale/
- https://docs.unraid.net/unraid-os/system-administration/secure-your-server/wireguard/
- https://docs.unraid.net/unraid-os/using-unraid-to/run-docker-containers/overview/
- https://docs.unraid.net/unraid-os/using-unraid-to/run-docker-containers/managing-and-customizing-containers/
- https://docs.unraid.net/community-applications/
- https://docs.unraid.net/unraid-os/getting-started/explore-the-user-interface/tour-the-web-gui/
- https://ca.unraid.net/apps/appdata-backup-0s7lv2l08xt63t
- https://trash-guides.info/File-and-Folder-Structure/How-to-set-up/Unraid/
- https://docs.redhat.com/en/documentation/Red_Hat_Enterprise_Linux/10/html/managing_file_systems/mounting-an-smb-share
- https://forums.unraid.net/topic/186760-auto-mount-of-smb-shares-via-etcfstab-not-working/
- https://docs.bazzite.gg/Installing_and_Managing_Software/rpm-ostree/
- https://docs.bazzite.gg/Advanced/Auto-Mounting_Secondary_Drives/
- https://forum.level1techs.com/t/bazzite-new-installation-issues-nfs-and-local-storage/228031