---
name: linux-security-hardening
description: Use when hardening an immutable Fedora Atomic desktop (Bazzite KDE/Deck) or learning home security basics, from encryption and Secure Boot to IDS, updates, backups.
---

# Linux security hardening (Bazzite / Fedora Atomic + home basics)

Labels: VERIFIED (source) = read in a fetched page; COMMUNITY = widely repeated, not confirmed in a fetched page; UNVERIFIED = unconfirmed, test before trusting.

## How to teach (assume the reader is not a programmer)
- One change at a time. Plain-words explanation first, then the exact command, then how to check it worked, then how to undo it.
- Never paste several commands at once. Ask for the output before the next step.
- Never ask for passwords, keys or real IPs in chat. Use placeholders.
- Check the current docs before stating a Bazzite-specific fact; Bazzite changes fast.

## Threat model by tier (plain words)
- Tier 1, stolen PC or drive: someone has the hardware. Defence: full disk encryption plus a secret needed at boot.
- Tier 2, malware: a bad download or app runs as you. Defence: trusted sources only, sandboxing, updates, backups.
- Tier 3, network attacker: someone on the internet or Wi-Fi. Defence: nothing listening (no SSH), firewall on, router basics.
- Tier 4, account takeover: someone logs in as you on a website. Defence: password manager, unique passwords, 2FA, phishing awareness. This is the most likely tier.

## What immutability already gives (and does not)
- System files are replaced as a whole image and you can roll back: VERIFIED (docs.bazzite.gg rolling back page: `rpm-ostree rollback`, two deployments kept by default).
- Updates are image builds that apply on reboot: VERIFIED (docs.bazzite.gg updating guide).
- Flatpak apps run in a sandbox (seccomp, private namespaces, filtered session bus): VERIFIED (Flatpak wiki, page last edited 2019, may be dated).
- Flatpak permissions can weaken the sandbox (home access, host sockets, host network): VERIFIED (Flatpak wiki).
- Immutability does NOT stop malware running as your user in your home folder or in a Flatpak with broad permissions: COMMUNITY.
- Immutability does NOT protect a stolen powered-off PC; only encryption does: COMMUNITY.

## Design option: no login password but protected at rest
- Plain words: the disk is locked until a secret is given at boot. After that, autologin skips the second password.
- Recommended: LUKS passphrase typed at every boot, then autologin. COMMUNITY (standard design).
- Not recommended alone: TPM auto-unlock plus autologin. A thief powers on and lands on your desktop. Reason (VERIFIED, Fedora Discussion thread): with PCR 7 only, a Fedora live ISO can get the key, and "obviously not secure" per a Fedora developer quoted there.
- Better TPM option: TPM plus PIN (systemd-cryptenroll `--tpm2-with-pin`). VERIFIED (systemd-cryptenroll man page). Wrong PIN attempts count toward a TPM lockout: VERIFIED (same page).
- On Fedora Atomic with GRUB, PCR sets are fragile across updates (PCR 4, 8, 9 change often): VERIFIED (Fedora Discussion thread, may be dated).
- A recovery key or passphrase must always stay enrolled: VERIFIED (man page recommends keeping one).
- Bazzite helper `ujust setup-luks-tpm-unlock` exists: COMMUNITY (Universal Blue forum thread; thread shows users hit errors and does not say which PCRs it uses). Its PCR choice: UNVERIFIED.
- Typing the passphrase on a Steam Deck style boot with only a controller: UNVERIFIED; plan on a keyboard attached at boot.
- The Bazzite installer offering an encrypt option: UNVERIFIED (not found in fetched docs). Adding encryption later without reinstall is generally not possible: COMMUNITY.
- Several NVMe drives: each data drive needs its own LUKS; extra drives can auto-unlock with a keyfile stored on the encrypted root: COMMUNITY.
- Bazzite docs have a page on enabling TRIM on LUKS drives (title seen on docs.bazzite.gg; content not fetched): UNVERIFIED details. TRIM on encrypted drives leaks which blocks are used: COMMUNITY.
- Gaming Mode autologin uses SDDM config files in `/etc/sddm.conf.d/`: VERIFIED (rollback page warns Deck 44 to 43 rollback breaks autologin, fix is deleting `zz-` prefixed files there).
- Bazzite has a "Reset Forgotten User Password" page: VERIFIED (docs index). Meaning: without disk encryption, anyone with the PC can reset the password. Encryption is the real lock.

## Hardening ladder (do in order, one per session)
1. Full disk encryption with a long passphrase, written on paper kept at home. Check: `lsblk -f` shows crypto_LUKS; `sudo cryptsetup status <name>`. COMMUNITY.
2. Updates on and rebooted weekly. Bazzite desktop images auto-check daily and apply on reboot; Bazzite-Deck images have auto updates OFF by default and update from Steam menu, Settings, System, Check for Updates: VERIFIED (updating guide). So Deck image users must update by hand.
3. Keep 3% or more free space on the system drive or updates fail: VERIFIED (updating guide).
4. Secure Boot on with the Universal Blue key enrolled. Steps in docs: `ujust enroll-secure-boot-key`, then MokManager at next boot: VERIFIED (docs.bazzite.gg secure boot page; the page lists the enrollment password, read it there). Warnings VERIFIED: password prompt uses English QWERTY, typed characters are invisible, a BIOS update may re-enable Secure Boot and cause a boot failure. Check: `mokutil --sb-state`. COMMUNITY.
5. Firmware/BIOS password and boot order locked to the internal drive. COMMUNITY.
6. Remote access fully off: no SSH, no VNC, no KDE Connect if unused. Check: `systemctl is-active sshd` (expect inactive), `sudo ss -tulpn` (listening ports). COMMUNITY. Whether Bazzite ships sshd enabled: UNVERIFIED; verify with the command, do not assume.
7. Firewall on, default zone checked. `firewall-cmd --state` prints running: VERIFIED (firewalld.org). Default zone applies to anything not assigned elsewhere: VERIFIED (firewalld.org). Command to show it, `firewall-cmd --get-default-zone`: COMMUNITY. Whether firewalld runs by default on Bazzite: UNVERIFIED.
8. SELinux stays enforcing. Check: `getenforce` (expect Enforcing). COMMUNITY.
9. Password manager plus unique passwords plus 2FA (hardware key or app) on email, cloud storage, GitHub, music or sample services, Steam. COMMUNITY. Email account is the master key: secure it first.
10. Flatpak permission review with Flatseal (Flathub app). VERIFIED it reviews and changes permissions, needs app restart after change, has a reset button (Flatseal README). Remove `filesystem=host` / `home` where not needed. Test the app after each change.
11. Backups, 3-2-1: 3 copies, 2 kinds of media, 1 offsite and encrypted. COMMUNITY. Test a restore. Keep one copy disconnected from the PC (ransomware).
12. Browser: uBlock Origin, no password saving in the browser if using a manager, separate profile for banking, updates on. COMMUNITY.
13. Optional: USBGuard. VERIFIED it is a USB allowlisting tool; starting it without a rules file can lock you out (keyboard, mouse): create rules first with `usbguard generate-policy` (USBGuard README). High risk for a music setup with many USB devices (interfaces, MIDI gear); not recommended unless asked.
14. Optional: file integrity check (AIDE). VERIFIED it monitors file changes; README says an attacker can still replace the binary or database (AIDE README). On an Atomic system `/usr` is already image-managed, so value is lower: COMMUNITY. Packaging on Bazzite: UNVERIFIED.

## What NOT to do
- Do not disable SELinux "to fix" something; read the denial instead (`sudo ausearch -m avc -ts recent`). COMMUNITY.
- Do not add random COPR repos or layer many packages with `rpm-ostree install`; each adds third-party code run as root and complicates updates. COMMUNITY.
- Do not run `curl ... | bash` or random install scripts; download, read, then run, or prefer Flathub/Bazaar. COMMUNITY.
- Do not give Flatpaks `--filesystem=host` or `--device=all` casually. VERIFIED these weaken isolation (Flatpak wiki).
- Do not trust AppImages from unknown sites: no sandbox by default. COMMUNITY.
- Do not enable SSH "just in case". If ever needed: keys only, no password login, non-root, firewall limited to your LAN, never exposed to the internet. COMMUNITY.
- Do not use metered-connection mode to stop updates; docs call it unsupported and it pauses auto updates: VERIFIED (updating guide).
- Do not run an AV "real-time" scanner expecting protection; ClamAV is an open-source engine for detecting malware (README) and on-demand scanning use is COMMUNITY. It mostly finds Windows malware in files you share.

## Monitoring / IDS that is not in the way
- Honest view: a single PC with no listening ports needs little IDS. Most value comes from updates, 2FA, backups. COMMUNITY.
- Cheapest: nothing extra, plus a monthly look at `rpm-ostree status` and `sudo ss -tulpn`. Cost: free, zero overhead.
- CrowdSec: VERIFIED open-source IDS/IPS reading logs, blocks via separate remediation components, shares signals with a community blocklist (CrowdSec README). Mostly useful for servers (Unraid, web services), not a desktop with no inbound ports: COMMUNITY. Fit on Bazzite (container/Flatpak/layering): UNVERIFIED.
- Wazuh: VERIFIED it is an agent + server + indexer + dashboard platform (Wazuh README). Heavy for one PC; fits only as a home-lab project on the server: COMMUNITY.
- AIDE / ClamAV / USBGuard: see ladder items 13, 14 and the NOT list.
- Network-side detection (Pi-hole query log review, router logs) catches more than host IDS for a home: COMMUNITY. Routers/VLANs: see the separate network skill.
- auditd and OSSEC on Atomic: UNVERIFIED, not researched here.

## Updates and rollback as a security tool
- Update, reboot, check the apps; if broken, roll back: `rpm-ostree rollback` then reboot. VERIFIED. Personal files are untouched: VERIFIED.
- Pin a good deployment: `rpm-ostree status -v` for the index, `sudo ostree admin pin <id>`; unpin with `-u`. Index numbers shift after every transaction, recheck: VERIFIED.
- Boot failure: pick the `ostree:1` GRUB entry, then make it default or the broken one retries: VERIFIED. An external keyboard may be needed on handhelds/HTPC: VERIFIED.
- Show pending changes and advisories: `rpm-ostree db diff`, `rpm-ostree status -a`: VERIFIED (security advisory info).
- Bazzite images build daily from Fedora; it is volunteer-run; issues in Fedora packages go upstream: VERIFIED (Bazzite SECURITY.md).
- Rollback window: the home page says rebase to a build within the last 90 days: VERIFIED (docs.bazzite.gg home).
- Firmware updates: `fwupdmgr get-updates` then `fwupdmgr update`. COMMUNITY. Bazzite integration: UNVERIFIED.
- Flatpak apps update separately (via Bazaar or `flatpak update`): VERIFIED in part (updating guide says Bazaar-installed apps upgrade without reboot).

## Home basics (short, no router depth)
- Change default router admin password, update router firmware, turn off WPS and remote admin. COMMUNITY.
- Use Pi-hole as DNS and review its logs monthly. COMMUNITY.
- Keep a home server (for example Unraid) and Pi-hole updated and not exposed to the internet; use a VPN to reach them from outside, never port forwards. COMMUNITY.
- Phishing: never log in from an email link; type the address or use a bookmark; check the sender; passkeys/hardware keys resist phishing. COMMUNITY.
- Secure the email account and phone number first (recovery paths). COMMUNITY.

## Monthly checklist (about 15 minutes)
- [ ] Reboot after updates; confirm `rpm-ostree status` shows the newest image.
- [ ] Update Flatpaks and firmware; remove apps not used.
- [ ] `sudo ss -tulpn`: nothing unexpected listening; `systemctl is-active sshd` inactive.
- [ ] `getenforce` Enforcing; `firewall-cmd --state` running; `mokutil --sb-state` enabled.
- [ ] Review Flatseal for new broad permissions.
- [ ] Backup done, one restore test of one file, offsite copy refreshed.
- [ ] Password manager: change any breached or reused passwords; check 2FA codes saved.
- [ ] Router, Pi-hole, home server (for example Unraid), Nextcloud updated, if you run them.
- [ ] Pi-hole log scan for odd domains.

## Sources (pages actually fetched)
- https://docs.bazzite.gg/
- https://docs.bazzite.gg/Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/updating_guide/
- https://docs.bazzite.gg/Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/rolling_back_system_updates/
- https://docs.bazzite.gg/General/Installation_Guide/secure_boot/
- https://docs.bazzite.gg/General/Installation_Guide/
- https://github.com/ublue-os/bazzite/blob/main/SECURITY.md
- https://universal-blue.discourse.group/t/problem-with-ujust-setup-luks-tpm-unlock/3422
- https://man.archlinux.org/man/systemd-cryptenroll.1.en
- https://discussion.fedoraproject.org/t/silverblue-tpm-luks-and-higher-pcrs/160617
- https://gitlab.com/fedora/ostree/sig/-/issues/33
- https://firewalld.org/documentation/
- https://firewalld.org/documentation/howto/get-firewalld-state.html
- https://firewalld.org/documentation/zone/default-zone.html
- https://github.com/flatpak/flatpak/wiki/Sandbox
- https://github.com/tchx84/Flatseal
- https://github.com/USBGuard/usbguard
- https://github.com/crowdsecurity/crowdsec
- https://github.com/wazuh/wazuh
- https://github.com/aide/aide
- https://github.com/Cisco-Talos/clamav
