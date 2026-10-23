---
name: pihole-raspberry-pi
description: Use when helping a non-programmer run, update, harden, back up or troubleshoot Pi-hole (v6) on a Raspberry Pi at home, including Unbound, groups, whitelisting and a safe fallback plan.
---

# Pi-hole on a Raspberry Pi
Labels: VERIFIED (source) = read on the page listed in Sources. COMMUNITY = widely repeated, not read from an official page. UNVERIFIED = not checked; confirm before relying on it.
## How to work with the reader
- Assume the reader is not a programmer.
- Plain words first, then the command. One change at a time. Wait for "done" before the next step.
- Ask first: which Pi model, which OS, Pi-hole bare metal or Docker, what router. Never guess.
- Before any risky change: say what could break and how to undo it.
- Never put real IPs, passwords or hostnames in notes or files. Use placeholders like <PI_IP>.
- If the reader also runs Unraid or Nextcloud, remember Pi-hole is the home "DNS phone book". Do not mix up the services.
## Plain-words picture
- Every device asks "what is the address of example.com?" That question is DNS.
- Pi-hole answers that question for the whole home. If a name is on a blocklist, it says "no such place", so the ad or tracker never loads. (Blocked answers are 0.0.0.0 by default: VERIFIED, docs.pi-hole.net/ftldns/blockingmode/)
- Gravity = the combined blocklist database Pi-hole builds from your adlists. `pihole -g` rebuilds it. (VERIFIED, domain-database page)
- FTL (pihole-FTL) = the engine that answers DNS, keeps the cache, logs and web server. (VERIFIED, ftldns pages)
- If Pi-hole is off, everything that depends on it loses the internet "by name", so the fallback plan matters most.
## What changed in v6 (vs v5)
- Settings live in one file: /etc/pihole/pihole.toml. (VERIFIED, configfile page)
- Change settings from the web page, API or CLI, not by hand: `sudo pihole-FTL --config <key> <value>`. They check for mistakes; a hand-edit error can stop FTL starting. (VERIFIED, configfile page)
- Any setting forced by an FTLCONF_ environment variable becomes read-only elsewhere. (VERIFIED, configfile page)
- Web server is built into FTL; old lighttpd config is removed or disabled. (VERIFIED, GitHub v6.0 release page)
- Custom list moved to /hosts/custom.list; `restartdns`, `webpage.sh` and chronometer were removed. (VERIFIED, v6.0 release page)
- v6 no longer reads /etc/dnsmasq.d by default (VERIFIED, Docker v5-v6 page; bare-metal toggle is misc.etc_dnsmasq_d, name taken from Docker env var FTLCONF_misc_etc_dnsmasq_d).
- API uses sessions, not static tokens; app passwords exist for scripts and 2FA setups. (VERIFIED, api/auth)
- Live API docs on your own Pi: http://pi.hole/api/docs (VERIFIED, api page).
- Latest release seen on the releases page: v6.4.3, which fixes a high-severity local privilege escalation (pihole user to root). Update to it or newer. (VERIFIED, GitHub releases page; re-check the number, it moves.)
- Read release notes (Core, FTL, Web) before a major jump like v5 to v6. (VERIFIED, main/update)
## Step 1: find the Pi model, version, install type
- Model: `cat /proc/device-tree/model` (COMMUNITY). Ask the reader to paste the output.
- Pi-hole versions: `pihole -v` (VERIFIED, pihole-command page).
- Docker or bare metal: run `docker ps`. If a container named pihole shows, it is Docker; if the command is missing, bare metal. (COMMUNITY)
- Docker: `pihole -up` and `pihole -r` are disabled; update by replacing the container. (VERIFIED, docker/upgrading)
- Minimum needs: 2 GB free (4 GB recommended), 512 MB RAM. (VERIFIED, prerequisites)
- Supported OS includes Raspberry Pi OS, Debian, Ubuntu, Fedora, Alpine, Armbian. Static IP or DHCP reservation required. (VERIFIED, prerequisites)
## Step 2: safe update (bare metal)
1. Read the release notes first. (VERIFIED)
2. Backup: Teleporter export, in the web interface settings menu (look for Teleporter under Settings), or `pihole-FTL --teleporter` on the command line. Save the file on another machine (a home server is fine). (VERIFIED, v6.1 release blog; exact click labels UNVERIFIED.)
3. Also copy /etc/pihole/pihole.toml somewhere safe. (COMMUNITY)
4. Be at the Pi on a keyboard or SSH, not midway through a call or game.
5. Run `sudo apt update && sudo apt full-upgrade` for the OS, then reboot. (COMMUNITY)
6. Run `pihole -up`. (VERIFIED)
7. Check: `pihole status`, `pihole -v`, open the web page, browse one site.
- If apt says the repository "Suite" changed: `sudo apt-get update --allow-releaseinfo-change`. (VERIFIED, FAQ)
- Docker: `docker compose pull`, `docker compose down`, `docker compose up -d`, keep the volumes. (VERIFIED, docker/upgrading)
## Step 3: SD card wear, SSD/USB boot, power
- SD cards wear out from constant writes (logs, query database). (COMMUNITY)
- Reduce writes: lower query logging or privacy level; Pi-hole has a `pihole logging off` command. (VERIFIED command, pihole-command page). Effect on wear: UNVERIFIED.
- Boot EEPROM (updatable bootloader) exists on flagship models since Pi 4B, Compute Modules since CM4, keyboard models since Pi 400. Update: `sudo rpi-eeprom-update -a` then reboot; `raspi-config` > Advanced Options > Bootloader Version offers default or latest. (VERIFIED, raspberrypi.com boot EEPROM docs)
- USB/SSD boot order steps and which models support USB boot: UNVERIFIED (the page body was not readable). Ask the reader to follow the current official Raspberry Pi docs and make a clone first.
- Power: use the official supply for the model. Undervoltage causes random freezes and SD corruption. (COMMUNITY; official supply ratings and the on-screen warning: UNVERIFIED)
- Check for undervoltage or throttling: `vcgencmd get_throttled`; 0x0 means fine. Bits: 0x1 undervoltage now, 0x2 Arm frequency capped, 0x4 throttled now, 0x8 soft temperature limit active; 0x10000, 0x20000, 0x40000, 0x80000 mean the same thing has happened since boot. (VERIFIED, raspberrypi.com os docs) Temperature: `vcgencmd measure_temp`. (COMMUNITY)
## Step 4: fixed address and router setting
- Give the Pi a DHCP reservation in the router (preferred) so it keeps one address. (VERIFIED: reservation is acceptable, prerequisites)
- On the router, set the DNS server handed out by DHCP to <PI_IP>. Devices pick it up on a new lease. (VERIFIED, post-install and fritzbox pages)
- If the router cannot hand out a DNS server, use Pi-hole's own DHCP server and turn the router's DHCP off first. Never run two DHCP servers. (VERIFIED, post-install)
- Making the Pi itself use Pi-hole: if the Pi dies it loses DNS and cannot repair itself with `pihole -r`. (VERIFIED, post-install)
- If clients show as the router in the log, Pi-hole is only the router's upstream, so per-device groups will not work. (VERIFIED, fritzbox page)
## Step 5: if the Pi dies (fallback plan)
- Danger: a second DNS entry such as a public resolver means some queries skip Pi-hole and ads leak, but internet keeps working. Only one entry means the whole house is offline when the Pi is off. (COMMUNITY reasoning; Fritz!Box page enters Pi-hole as both fields, VERIFIED)
- Best plan: a second Pi-hole on another small device, both given out by the router. Keep their lists in sync by exporting from one and importing in the other. (COMMUNITY; sync tools UNVERIFIED)
- Quick rescue: log into the router, put the router's own DNS (or a public resolver) back, reboot clients or renew leases.
## Step 6: Unbound (ask your own resolver, no third party)
- Plain words: Pi-hole normally asks Cloudflare/Google. Unbound asks the internet's root servers directly, so no single company sees all questions. It is slower on the first lookup, then cached. (COMMUNITY plus VERIFIED steps below)
1. `sudo apt install unbound` (VERIFIED, unbound guide)
2. Config file: /etc/unbound/unbound.conf.d/pi-hole.conf with interface 127.0.0.1, port 5335, do-udp and do-tcp yes. Copy the file text from the official guide, do not retype. (VERIFIED)
3. Debian "Bullseye and later": disable unbound-resolvconf service as the guide states. (VERIFIED)
4. `sudo service unbound restart` (VERIFIED)
5. Test: `dig pi-hole.net @127.0.0.1 -p 5335` (VERIFIED)
6. Pi-hole web page > Settings > DNS > custom upstream `127.0.0.1#5335`; untick all other upstreams; Save. (VERIFIED)
7. DNSSEC checks from the guide: `dig fail01.dnssec.works @127.0.0.1 -p 5335` must give SERVFAIL; `dig +ad dnssec.works @127.0.0.1 -p 5335` must give NOERROR plus the ad flag. (VERIFIED)
- Keep TCP port 53 open: Unbound uses it for large replies. (VERIFIED)
- Buffer warning: raise net.core.rmem_max to 1048576 as the guide says. (VERIFIED)
- If Unbound breaks, temporarily untick the custom upstream and pick a normal upstream to get internet back. (COMMUNITY)
## Step 7: blocking vs breakage
- A site, game or app broke? Do not turn Pi-hole off for everyone.
1. Look at the query log (web page > Query Log) while reproducing the problem; find rows marked blocked. (COMMUNITY)
2. Allow one domain: `pihole allow example.com` (command VERIFIED). Allowlist wins over denylist. (VERIFIED, regex page)
3. Test again. Add only what is needed.
4. Need a pause: `pihole disable 5m` then it resumes. (VERIFIED)
5. Which list blocks it? `pihole query <domain>` (VERIFIED).
- Games, consoles and smart TVs often need telemetry or login domains; allow one at a time. (COMMUNITY)
- Per-device groups: clients are identified by IP; new clients go to Default group 0; a domain enabled in some groups and disabled in others can act oddly. (VERIFIED, group_management page)
- Use a DHCP reservation for each device you want in a group, otherwise the IP changes. (COMMUNITY)
- The official example is database commands (SQL) and ends with `pihole reloadlists`. The web UI has Groups, Domains, Lists and Clients pages, each item with a group assignment and an on/off slider, and Settings > Teleporter. (COMMUNITY, 2023 forum thread; exact v6 menu paths UNVERIFIED.) The Default group (id 0) is automatic for new clients and domains. (VERIFIED, group_management page)
- Regex: POSIX Extended; allowlist always beats denylist; reload with `pihole reloadlists`. (VERIFIED, regex page)
## Step 8: adlists and gravity
- Add adlists in the web UI (Lists page), then `pihole -g`. v6 also supports subscribed allowlists, which work like blocklists but permit domains. (VERIFIED command and allowlists, v6 announcement blog; Lists page wording COMMUNITY)
- Fewer lists means fewer breakages. Start small. (COMMUNITY)
- Gravity fails: check internet and DNS from the Pi, then the list URL, then `pihole -g` output. Invalid IDN domains: ask the list maintainer for Punycode. (VERIFIED FAQ)
- Corrupt gravity database: `pihole -g -r recover`, then `pihole -g -r recreate`. (VERIFIED, recovery page)
- pihole-updatelists (third-party tool by jacklul for scheduled list sync): the README requires Pi-hole v6 and prefers a fresh install; install is PHP CLI plus its extensions, then the install.sh from its GitHub, then edit /etc/pihole-updatelists.conf (it does nothing until configured). Read the script before running it. (VERIFIED, github.com/jacklul/pihole-updatelists README) Maintenance status and latest release: UNVERIFIED (page did not show).
## Step 9: IPv6 leaks and apps that bypass Pi-hole
- If the router hands out its own IPv6 DNS, devices may skip Pi-hole. Give out Pi-hole's IPv6 address, or switch IPv6 DNS off at the router. (COMMUNITY; Fritz!Box RA/RDNSS setup VERIFIED)
- Apps, browsers and TVs may use hard-coded DNS or DNS over HTTPS (DoH). (COMMUNITY)
- Force DNS: a router rule blocking outbound port 53 from everything except the Pi; the Fritz!Box guide does this with an access profile, and warns hard-coded devices may break. (VERIFIED)
- Test: `dig google.com @8.8.8.8 +short` from a normal device should fail. (VERIFIED)
- Firefox canary domain: Pi-hole replies NXDOMAIN to use-application-dns.net by default, which tells Firefox to turn off its automatic DoH. Setting dns.specialDomains.mozillaCanary, default true. (VERIFIED, configfile page; Firefox behaviour VERIFIED, Mozilla support page) Only helps users who got DoH by default, not those who switched it on themselves. Blocking other DoH servers by list, or browser policies: UNVERIFIED.
## Step 10: Pi hardening
- Use SSH keys; turn off password login (PasswordAuthentication no in sshd_config, after proving the key works). (COMMUNITY)
- Web admin password: `pihole setpassword`. (VERIFIED)
- Keep apt updates current; unattended-upgrades is an option. (COMMUNITY)
- Firewall: allow SSH, port 53 TCP/UDP, web 80/443 from the home network only. Never forward these ports on the router. (Ports VERIFIED prerequisites; the rest COMMUNITY)
- Do not paste the installer blindly: the docs note piping to bash is "controversial" and offer download-then-run. (VERIFIED, basic-install)
## Step 11: monitoring
- Status: `pihole status`; live log: `pihole tail`. (VERIFIED)
- FTL log: /var/log/pihole/FTL.log. (VERIFIED)
- Cache health: Settings > System, evictions above 0 means raise cache size. (VERIFIED, dns-cache page)
- Disk: `df -h`; temperature and throttling: vcgencmd (COMMUNITY).
- If Docker: `docker logs pihole`. (COMMUNITY)
## Troubleshooting tree
1. No internet after a change? Undo that change first. Test `ping <PI_IP>`. No reply: Pi off or wrong address.
2. Pi answers but names fail: `pihole status`; `sudo systemctl status pihole-FTL`; check upstream (Unbound running? `dig pi-hole.net @127.0.0.1 -p 5335`).
3. DNS slow: Unbound's first lookups are slower (COMMUNITY); check cache; check CPU temperature and throttling.
4. Gravity update fails: see Step 8.
5. Web UI unreachable: ports 80/443 may move to 8080/8443 if taken. (VERIFIED, prerequisites) Check FTL running.
6. Filesystem read-only or odd errors after power loss: suspect SD corruption; back up, run fsck from another machine, reflash if needed. (COMMUNITY)
7. Still stuck: `pihole debug` offers an upload to developers; only share the token after reading what it includes. (VERIFIED command)
8. Repair keeping settings: `pihole repair`. (VERIFIED)
- Pi-hole's own DNS warnings are explained at ftldns/dnsmasq_warn. (VERIFIED)
## Backup and restore
- Teleporter export before every update; restore with Teleporter import on a fresh install, then run `pihole -g` as the web UI prompts. v6 can import old v5 archives. (VERIFIED prompt and export, v6.1 blog; v5 import and file list COMMUNITY, forum: pihole.toml, gravity.db, pihole-FTL.db, dhcp.leases, /etc/hosts; whether groups and clients restore fully: UNVERIFIED, test on a spare system.)
- Also copy /etc/pihole/pihole.toml and note your version. (COMMUNITY)
- Docker: keep the ./etc-pihole volume; back that up. (VERIFIED, docker page)
- Whole-card image of a working Pi is the fastest recovery. (COMMUNITY)
## pihole commands (v6, VERIFIED, pihole-command page)
- `pihole status` / `enable` / `disable 5m`
- `pihole -v` versions; `pihole -up` update; `pihole repair`
- `pihole -g` rebuild gravity; `pihole reloadlists`; `pihole reloaddns`
- `pihole allow <domain>` / `pihole deny <domain>`; `--regex`, `--allow-regex`, `--wild`
- `pihole query <domain>`; `pihole tail`; `pihole flush`; `pihole logging off`
- `pihole setpassword`; `pihole debug`; `pihole uninstall`
- Settings: `sudo pihole-FTL --config <key> <value>` (VERIFIED, configfile)
## Monthly checklist
1. Teleporter export, saved off the Pi.
2. Read release notes, then update OS and `pihole -up`.
3. `vcgencmd get_throttled`, `df -h`, temperature.
4. Skim query log for odd or blocked-by-mistake domains.
5. Confirm the router still lists the right DNS and the fallback plan works.
6. Test restore notes still match reality.
## Not verified (ask or check before stating as fact)
- Teleporter exact click labels and full contents; v6 Groups/Lists exact menu paths; pihole-updatelists maintenance status; Raspberry Pi USB boot order, supported models for USB boot, official power supplies and undervoltage warning; dedicated DNSSEC page (fetch failed).
- Settings keys seen (VERIFIED, configfile): dns.dnssec (default false); dns.revServers is the conditional forwarding setting (its old name) (format: enabled,CIDR,router,domain); dhcp.active (default false), dhcp.start, dhcp.end, dhcp.router. Web screen labels for these: UNVERIFIED.
## Sources (fetched)
- https://docs.pi-hole.net/main/update/
- https://docs.pi-hole.net/main/prerequisites/
- https://docs.pi-hole.net/main/post-install/
- https://docs.pi-hole.net/main/basic-install/
- https://docs.pi-hole.net/main/pihole-command/
- https://docs.pi-hole.net/main/faq/
- https://docs.pi-hole.net/main/
- https://docs.pi-hole.net/guides/dns/unbound/
- https://docs.pi-hole.net/api/
- https://docs.pi-hole.net/api/auth/
- https://docs.pi-hole.net/routers/fritzbox/
- https://docs.pi-hole.net/docker/
- https://docs.pi-hole.net/docker/upgrading/
- https://docs.pi-hole.net/docker/upgrading/v5-v6/
- https://docs.pi-hole.net/ftldns/configfile/
- https://docs.pi-hole.net/ftldns/dnsmasq_warn/
- https://docs.pi-hole.net/ftldns/dns-cache/
- https://docs.pi-hole.net/ftldns/in-depth/
- https://docs.pi-hole.net/ftldns/blockingmode/
- https://docs.pi-hole.net/regex/
- https://docs.pi-hole.net/database/domain-database/
- https://docs.pi-hole.net/database/domain-database/recovery/
- https://docs.pi-hole.net/group_management/
- https://docs.pi-hole.net/group_management/example/
- https://github.com/pi-hole/pi-hole/releases
- https://github.com/pi-hole/pi-hole/releases/tag/v6.0
- https://pi-hole.net/blog/2025/03/30/pi-hole-ftl-v6-1-web-v6-1-and-core-v6-0-6-released/
- https://pi-hole.net/blog/2025/02/18/introducing-pi-hole-v6/
- https://github.com/jacklul/pihole-updatelists
- https://www.raspberrypi.com/documentation/computers/raspberry-pi.html
- https://www.raspberrypi.com/documentation/computers/os.html
- https://support.mozilla.org/en-US/kb/canary-domain-use-application-dnsnet
- https://discourse.pi-hole.net/t/is-teleporter-a-full-replacement-for-that-or-does-it-skip-anything/87095
- https://discourse.pi-hole.net/t/major-overhaul-of-the-domain-adlist-and-client-managment/61013