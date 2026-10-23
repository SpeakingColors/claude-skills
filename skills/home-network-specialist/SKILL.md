---
name: home-network-specialist
description: Use when explaining, hardening, tuning or troubleshooting a home network (Pi-hole, Unraid, Nextcloud, Wi-Fi, VLANs, remote access) for a non-programmer.
---

# Home network specialist

## Rules of engagement
- Plain words first, then the term. One change at a time, then test, then next.
- Before any change: note how to undo it, and keep one wired PC that can reach the router.
- Never ask the reader to paste passwords, keys or public IPs. Use placeholders like `<pihole-ip>`.
- Labels: VERIFIED (source) = read in a fetched page; COMMUNITY = common practice, not checked here; UNVERIFIED = recall, check before relying.
- If unsure, say so and give a test the reader can run instead of guessing.

## 1. How it works in plain words
- Modem/ONT: turns the ISP line (cable, fibre) into Ethernet. Often combined with the router. COMMUNITY
- Router: connects home to the internet, hands out addresses (DHCP), does NAT, runs the firewall. COMMUNITY
- Switch: a patch panel that passes wired traffic between devices. AP: Wi-Fi radio on a wire. COMMUNITY
- DHCP: gives each device an address, gateway and DNS server. A "reservation" always gives the same address to the same device. COMMUNITY
- DNS: the phone book that turns names into addresses. Whoever answers DNS sees every site name you visit. COMMUNITY
- NAT: many home devices share one public address; unsolicited incoming traffic is dropped unless you forward a port. COMMUNITY
- CGNAT: the ISP shares one public address among many customers, so port forwarding cannot work. Test: compare router WAN address with a "what is my IP" site; if different, suspect CGNAT. COMMUNITY
- IPv6: every device can have a public address; the router firewall (not NAT) is the protection, so check it is on. COMMUNITY
- Pi-hole docs say it needs a fixed address (a DHCP reservation works). VERIFIED (Pi-hole prerequisites)

## 2. Improvement ladder (do in order, one per session)
1. Write down what you have: router model, firmware, every device on the network. Fing or the router client list help. COMMUNITY
2. Change defaults: router admin password, Wi-Fi password, admin username if allowed. Use a password manager. COMMUNITY
3. Update firmware on router, APs, switch, NAS. Turn on auto-update where offered. COMMUNITY
4. Disable UPnP and WPS in the router. UPnP lets devices open holes in the firewall unasked. COMMUNITY
5. Guest network for visitors, with "client isolation" on. COMMUNITY
6. IoT separation: TV, receiver, speakers, cameras on their own network that cannot start connections to the main one. VERIFIED (OPNsense guest guide: block guest to LAN, block guest to firewall, then allow internet; block rules go before the pass rule)
7. VLANs (only if router, switch and AP all support them): one wire carries several separate networks. Risk: wrong settings lock you out, so keep one port untouched as a safety door. COMMUNITY
8. DNS filtering with Pi-hole (see section 3).
9. Firewall rules: default deny incoming; between networks, allow only what is needed (for example main LAN to Unraid, IoT to internet only). COMMUNITY
10. Outbound blocking for IoT: block IoT from reaching the main LAN, allow DNS to Pi-hole only; consider blocking their direct DNS to the internet. COMMUNITY
11. Remote access with WireGuard (section 4) instead of port forwarding.
12. Nextcloud: reverse proxy with HTTPS (section 5), only if it must be reachable from outside.

## 3. DNS: Pi-hole + Unbound, DoH/DoT
- Unbound lets Pi-hole ask the internet's root servers itself, so no third party sees all your lookups. COMMUNITY
- Setup steps, VERIFIED (Pi-hole Unbound guide):
  - Install Unbound (`sudo apt install unbound`), root hints usually come with the package.
  - Config file `pi-hole.conf` makes Unbound listen on localhost port 5335, UDP and TCP.
  - Pi-hole: Settings > DNS, set custom upstream `127.0.0.1#5335`, untick all other upstreams, Save.
- Test, VERIFIED (same guide): `dig fail01.dnssec.works @127.0.0.1 -p 5335` should say SERVFAIL; `dig +ad dnssec.works @127.0.0.1 -p 5335` should say NOERROR with the `ad` flag.
- Before installing, check your ISP or router is not blocking or hijacking DNS on port 53; guide gives a test. VERIFIED (same guide)
- First lookup of a new domain ending is slow, later ones fast. VERIFIED (same guide)
- Switch Pi-hole to another upstream before uninstalling Unbound. VERIFIED (same guide)
- Pi-hole's DNS is a dnsmasq fork with a default cache of 150 names. VERIFIED (Pi-hole DNS resolver page)
- Pi-hole ports: 53 TCP/UDP DNS, 80/443 web UI, 67/547 only if it is your DHCP server. Firewall it so only the local network reaches it. VERIFIED (Pi-hole prerequisites)
- Make clients use Pi-hole: set the router's DHCP "DNS server" to `<pihole-ip>`. Router-specific; check your router manual. UNVERIFIED (Pi-hole router page failed to load)
- Single point of failure: if the Pi-hole is off, the house has no internet by name. Consider a second resolver or a quick way to revert. COMMUNITY
- DoT (port 853) and DoH (port 443) encrypt the hop to a public resolver (Cloudflare, Quad9). COMMUNITY
  - Pro: ISP cannot read your lookups. Con: the resolver company sees them instead.
  - Unbound recursion: no single company sees everything, but the ISP can see which servers you contact. COMMUNITY
  - DoH inside apps/browsers/TVs can bypass Pi-hole; block or redirect it at the firewall. COMMUNITY
- Quad9 and Cloudflare setup details: UNVERIFIED (docs pages not reachable this session).

## 4. Remote access
- Prefer a VPN to forwarding Nextcloud or Unraid ports to the internet. COMMUNITY
- WireGuard basics, VERIFIED (WireGuard quickstart):
  - Private key stays on the device (`umask 077` before generating); only the public key is shared.
  - Example listen port 51820.
  - Persistent keepalive (suggested 25 s) helps peers behind NAT stay reachable; off by default.
  - `wg show` displays state; `wg-quick` automates up/down.
- WireGuard uses UDP. UNVERIFIED (the quickstart page did not state it in the fetched text)
- Behind CGNAT you cannot forward a port, so home WireGuard will not accept inbound. Options: Tailscale, or a small rented server as a relay. COMMUNITY
- Tailscale caveats, VERIFIED (Tailscale connection types): connections start relayed and try to upgrade to direct; blocked UDP or hard NAT forces slower relays (DERP); enabling NAT-PMP/UPnP or keeping UDP 41641 open helps. The page does not discuss CGNAT.
- Tailscale/NAT-PMP advice conflicts with "disable UPnP"; prefer relays over UPnP unless you accept the risk. COMMUNITY

## 5. Reverse proxy basics for Nextcloud
- A reverse proxy is one front door (ports 80/443) that passes visitors to the right internal service and holds the HTTPS certificate. COMMUNITY
- Only expose what must be public; keep Unraid's web UI and SSH off the internet. COMMUNITY
- Needs: HTTPS certificate (Let's Encrypt), HSTS header, Nextcloud "trusted proxies" and "trusted domains" set, and updates applied. COMMUNITY
- Nextcloud's own hardening page could not be fetched; read it before exposing: https://docs.nextcloud.com/server/latest/admin_manual/installation/harden_server.html UNVERIFIED
- Add fail2ban or crowd-style blocking and 2FA on Nextcloud accounts. COMMUNITY

## 6. Wi-Fi tuning
- Use 5 GHz (or 6 GHz) for fast devices, 2.4 GHz only for far or simple devices. COMMUNITY
- 2.4 GHz: channels 1, 6 or 11 to avoid overlap. 5 GHz: wider channels (80 MHz) are faster but more prone to interference. COMMUNITY
- Use WPA3 or WPA2/WPA3 mixed; turn off WPS; avoid WEP/WPA/TKIP. COMMUNITY
- Place AP high and central; wire APs back to the router rather than using wireless repeaters. COMMUNITY
- Handheld PCs and laptops: Wi-Fi is fine for gaming; for game streaming or big downloads, use a USB-C Ethernet adapter if possible. UNVERIFIED
- Check signal: phone Wi-Fi analyser, or on Linux `nmcli dev wifi list`. COMMUNITY

## 7. Wired for audio, DJ and music gear
- Use Ethernet for the audio PC, Unraid, receiver and TV where cabling allows. Fewer drops, steadier latency. COMMUNITY
- Network audio and MIDI-over-network need wired and low latency; synths with USB do not use the LAN at all, so network trouble never affects USB MIDI. COMMUNITY
- Keep backups and big transfers (Unraid, Nextcloud sync) off Wi-Fi during recording sessions. COMMUNITY
- Put the audio PC and Unraid on the main/trusted network, TV and receiver on IoT; if casting from PC to receiver, expect to need mDNS across networks (section 8). COMMUNITY

## 8. mDNS/Avahi, printing, discovery
- mDNS ("name.local") and casting/printer discovery only work inside one network segment. After VLAN separation they stop. COMMUNITY
- Fix: an mDNS reflector/repeater on the router (names vary by router) or Avahi in reflector mode; open only required ports. UNVERIFIED
- Linux desktops (for example Bazzite): check `avahi-browse -a` (if installed) to see what the PC can see. UNVERIFIED
- Printing: give the printer a DHCP reservation and add it by address instead of relying on discovery. COMMUNITY

## 9. Wake-on-LAN
- Needs wired Ethernet, WoL enabled in the PC BIOS and in the network card settings. Wi-Fi WoL is unreliable. COMMUNITY
- Magic packets are broadcast, so the sender must be on the same network segment (or use VPN plus a relay). COMMUNITY
- Check on Linux: `ethtool <interface>` and look for "Wake-on: g". UNVERIFIED
- Unraid has a WoL option in its settings. UNVERIFIED

## 10. Latency and bufferbloat
- Bufferbloat: internet gets laggy when something else is downloading or uploading, because the router queues too much. COMMUNITY
- Test: run a bufferbloat test while loading a big file (Waveform tool; it needs JavaScript so the fetched page could not show grading). UNVERIFIED
- Fix: enable SQM / smart queue (fq_codel or CAKE) on the router and set speed to about 90 to 95 percent of measured. COMMUNITY
- Many consumer routers lack SQM; OPNsense, OpenWrt and some UniFi models have it. UNVERIFIED

## 11. Diagnostic toolbox (read results like this)
- `ping <host>`: replies and time in ms. Loss over 0 on wired is suspicious; large swings mean congestion or weak Wi-Fi. COMMUNITY
- `traceroute <host>` / `mtr <host>`: shows each hop; loss that starts at one hop and continues to the end is real, loss at one middle hop only is usually harmless. COMMUNITY
- `dig <name>` and `dig <name> @<pihole-ip>`: if the second works and first fails, the problem is your normal DNS path. `NOERROR` good, `NXDOMAIN` name not found, `SERVFAIL` resolver failed. COMMUNITY
- `ss -tulpn` (as root): what is listening on this machine. Anything listening on all addresses that you do not recognise is worth a look. COMMUNITY
- `ip a` and `ip route`: addresses and gateway. COMMUNITY
- `nmap`, only on your own network, VERIFIED (Nmap options reference): `-sn` host discovery only, `-sT` TCP connect scan, `-sV` service versions, `-p` limits ports, `--open` shows only open ports.
  - Example: `nmap -sn <your-subnet>/24` lists live devices. COMMUNITY
  - Port states open/closed/filtered: meaning not confirmed in the fetched page. UNVERIFIED
- `tcpdump -i <interface> port 53`: shows DNS live. Needs root. COMMUNITY
- Wireshark: capture filters limit what is saved; display filters hide packets after capture (for example `dns`). UNVERIFIED (docs page not reachable)

## 12. Troubleshooting decision tree
- Slow: wired PC also slow?
  - Yes: test router direct to modem; run bufferbloat test; call ISP with results.
  - No: it is Wi-Fi. Move closer, change channel, use 5 GHz.
- Drops: all devices or one?
  - All: modem/ISP; check modem light and logs, reboot modem alone.
  - One: that device's Wi-Fi, power-saving, or bad cable.
- DNS fails (sites do not load but `ping <known public IP>` works):
  - `dig example.com @<pihole-ip>` fails: check Pi-hole is running and Unbound is up.
  - Works: client is not using Pi-hole; check DHCP DNS setting and any private DNS/DoH in the client.
- Device A cannot reach device B:
  - Same network? If not, firewall or VLAN rule.
  - `ping` works but app does not: service not running, wrong port, or `ss -tulpn` shows it listening only on localhost.
  - Name fails but address works: DNS or mDNS issue.
  - Check for duplicate addresses (two devices, same IP); fix with reservations.
- After any fix: change one thing, retest, write it down.

## 13. Threat checklist
- Router admin page or Unraid/Nextcloud reachable from the internet unintentionally. Test from phone on mobile data. COMMUNITY
- Port forwards you no longer need; UPnP-made forwards. COMMUNITY
- Default or reused passwords on router, NAS, cameras, printers. COMMUNITY
- Old firmware or unsupported devices. COMMUNITY
- Remote admin turned on; SSH with passwords instead of keys. COMMUNITY
- Pi-hole open to the internet (check section 3 firewall note). VERIFIED (Pi-hole prerequisites advises LAN-only rules)
- Unknown devices in the client list. COMMUNITY
- Backups: 3 copies, one off-site, test a restore. COMMUNITY
- Official guidance from CISA and NCSC: pages could not be fetched this session, so none of their wording is quoted. UNVERIFIED

## 14. Quarterly checklist
- Update firmware: router, APs, switch, Pi-hole, Unraid, Nextcloud, plugins, the desktop OS.
- Review client list; remove unknown devices; update reservations.
- Rotate Wi-Fi password if shared widely; check guest network still isolated.
- Review port forwards and UPnP list; should be empty or known.
- Run bufferbloat test and one speed test; record results.
- Check Pi-hole top blocked and top clients; look for odd devices.
- Test VPN from mobile data; test backup restore of one file.
- Re-run `nmap` from the main network against Unraid and Nextcloud; confirm only expected ports.

## Sources (fetched this session)
- https://docs.pi-hole.net/guides/dns/unbound/
- https://docs.pi-hole.net/main/prerequisites/
- https://docs.pi-hole.net/ftldns/dns-resolver/
- https://www.wireguard.com/quickstart/
- https://tailscale.com/kb/1257/connection-types
- https://docs.opnsense.org/manual/how-tos/guestnet.html
- https://nmap.org/book/man-briefoptions.html
- https://www.waveform.com/tools/bufferbloat (page content limited)