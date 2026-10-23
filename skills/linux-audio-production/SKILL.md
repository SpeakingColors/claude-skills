---
name: linux-audio-production
description: Use for professional Linux audio setup and debugging on Bazzite or Fedora Atomic, covering PipeWire, WirePlumber, JACK, ALSA, realtime, interfaces, routing, xruns, plugin paths and yabridge.
---

# Linux audio production on Bazzite (Fedora Atomic)

Verify against current docs before acting on anything marked UNVERIFIED.
Labels: VERIFIED = read in official or primary docs this session. COMMUNITY = forum or blog report. UNVERIFIED = general knowledge, not checked; test before trusting.
Scope: system audio only. Genre, MIDI creative work and room acoustics are other skills.

## 1. The stack

- ALSA is the kernel driver layer. PipeWire sits on it and replaces the old sound servers. [UNVERIFIED as a statement about Bazzite defaults, but Bazzite uses PipeWire: `ujust restart-pipewire` exists, VERIFIED]
- Pulse layer (pipewire-pulse): browsers, Steam, games.
- JACK layer (pipewire-jack): pro apps. `pw-jack <cmd>` only sets LD_LIBRARY_PATH so a JACK client loads PipeWire's JACK libraries; it has no effect if those are already the system JACK. [VERIFIED, pw-jack man page]
- Native PipeWire: Bitwig 4.3 and later has a PipeWire driver. [VERIFIED, Bitwig support page]
- Do not run a second JACK server (jackd, QjackCtl start) on top of PipeWire. [UNVERIFIED rule of thumb]
- WirePlumber is the session manager: it decides device profiles, defaults, suspend, routing policy. [UNVERIFIED, general]

## 2. Tool cheat sheet

```
wpctl status                       # devices, sinks, sources, streams, defaults
wpctl set-default <id>             # choose default output/input
wpctl inspect <id>                 # properties of a node
pw-cli list-objects                # raw object list [VERIFIED command]
pw-cli info <id|all>               # details [VERIFIED]
pw-cli enum-params <id>            # parameters [VERIFIED]
pw-top                             # load, QUANT, RATE, ERR (xruns) [COMMUNITY for ERR meaning]
pw-metadata -n settings            # show runtime clock settings
pw-jack <app>                      # run a JACK app via PipeWire [VERIFIED]
aconnect -l ; amidi -l             # ALSA MIDI ports (alsa-utils) [UNVERIFIED availability on Bazzite]
ujust restart-pipewire             # [VERIFIED]
systemctl --user restart pipewire pipewire-pulse wireplumber
journalctl --user -u pipewire -u wireplumber -b
```

## 3. Buffer size and latency

- Latency in ms is roughly buffer / rate x 1000 (256 at 48 kHz is 5.3 ms one way). Round trip is about double plus converter and USB overhead.
- Starting points (COMMUNITY): tracking 128 or 256; mixing 512 or 1024; heavy sessions 1024 or 2048. Keep one sample rate (48 kHz) project-wide.
- Runtime force and release [VERIFIED, pipewire(1) man page]:

```
pw-metadata -n settings 0 clock.force-quantum 256
pw-metadata -n settings 0 clock.force-quantum 0
pw-metadata -n settings 0 clock.quantum 256
```

- Per-app hint: env var PIPEWIRE_LATENCY="256/48000" (also PIPEWIRE_QUANTUM, PIPEWIRE_RATE). It is only a suggestion. [VERIFIED names; "256/48000" format UNVERIFIED]
- Permanent defaults: a drop-in `~/.config/pipewire/pipewire.conf.d/10-audio.conf` with `context.properties = { default.clock.rate = 48000 default.clock.quantum = 256 default.clock.min-quantum = 32 default.clock.max-quantum = 8192 }`. Restart the three user services. [COMMUNITY: blog; drop-in directory also VERIFIED by the loopback docs]
- A DAW using the PipeWire or JACK layer follows the graph quantum. A DAW that opens ALSA directly bypasses PipeWire (device is then locked). [UNVERIFIED]

## 4. WirePlumber rules (device behaviour)

The WirePlumber ALSA configuration page could not be fetched; syntax below is UNVERIFIED. Look at the current WirePlumber docs (pipewire.pages.freedesktop.org/wireplumber) before writing.

- Typical fixes: stop USB interface suspending between sessions (session.suspend-timeout-seconds = 0), pin a device profile (e.g. "pro-audio"), set period size, set priority.session so the interface is default.
- Files go in `~/.config/wireplumber/wireplumber.conf.d/` as `.conf` drop-ins. [UNVERIFIED for the Fedora/Bazzite version in use; check `wireplumber --version`]
- Pro-audio profile: in KDE System Settings, Audio, Configure devices, set Profile "Pro Audio" for the interface to expose all channels raw. Digiface multi-channel use needs it. [COMMUNITY]
- Debug after each change: `systemctl --user restart wireplumber` then `wpctl status`.

## 5. Realtime: groups, limits, rtkit

- Symptoms: yabridge warns about low RLIMIT_RTTIME (rtkit limiting) or low memlock (no privileges). [VERIFIED, yabridge README]
- Fix per yabridge docs: user in group `realtime` (Fedora, Arch) or `audio` (Debian, Ubuntu); log out and in. Test with `chrt -f 10 whoami`. [VERIFIED]
- On GNOME 45 and later yabridge suggests masking rtkit after privileges are set; this is not KDE advice. [VERIFIED statement, applicability UNVERIFIED]
- Bazzite ships neither confirmed: check before changing.

```
groups ; getent group realtime audio
ulimit -r -l
chrt -f 10 whoami
rpm -q realtime-setup 2>/dev/null ; ls /etc/security/limits.d/
```

- Adding a group on Atomic: system groups live in /usr/lib/group and must be copied into /etc/group first. Follow https://docs.bazzite.gg/Advanced/add-user-to-group/ exactly (backup /etc/group, use `tee -a`, never `>>`, then `usermod -aG`, reboot). [VERIFIED]
- /etc/security/limits.d/ is on writable /etc. Lines like `@audio - rtprio 95` and `@audio - memlock unlimited` are the usual form. [COMMUNITY]
- PipeWire's own rt module and rtkit/portal keys are blog-sourced only; do not paste them without checking `man libpipewire-module-rt`. [UNVERIFIED]

## 6. Kernel, threadirqs, PREEMPT_RT, CPU governor

- Atomic way to add boot options: `rpm-ostree kargs --append=threadirqs` then reboot. The kargs docs page could not be fetched this session, so exact flags are UNVERIFIED; check `rpm-ostree kargs --help` and confirm in `/proc/cmdline`.
- `threadirqs` makes interrupt handlers schedulable threads (helps RT tuning). Gain is small on modern kernels; try it only if you can measure an improvement. [COMMUNITY]
- PREEMPT_RT was merged into mainline in Linux 6.12 (KVR thread title; exact Bazzite build option UNVERIFIED). Bazzite ships its own kernel; do not swap kernels or layer a kernel to chase RT. Rollback exists but costs time.
- CPU governor: use the Performance profile (KDE power menu) while recording. Check `cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor`. [UNVERIFIED path]
- Disable CPU sleep tweaks only if xruns correlate with load swings. Turn off Wi-Fi power saving if USB/network stalls: NetworkManager `wifi.powersave = 2` [VERIFIED, Bazzite Issues page].
- Never use gamemode in Bazzite. [VERIFIED: not installed]

## 7. Audio interfaces

- Class-compliant USB audio and MIDI (most synths and basic interfaces) use the kernel `snd-usb-audio` driver with no install. Check: `lsusb`, `aplay -l`, `wpctl status`. [UNVERIFIED commands, standard]
- Plug into a rear motherboard USB port, avoid unpowered hubs for audio. [COMMUNITY]
- Clock: one device master, others slaved, or you get clicks. 
- Flatpak DAWs need device access; Bitwig Flatpak has `--device=all` and `--filesystem=xdg-run/pipewire-0`. [VERIFIED, Flathub manifest]

### RME Digiface USB

- Supported by the kernel since 6.12 (forum title); the ALSA patch adds sync, output format, input status mixer controls: sync source, current sync source, system rate, current rate. It does not add the matrix mixer, output gain or level meters. [VERIFIED, LKML patch]
- So there is no TotalMix. Route in DAW or patchbay; set sync source in `alsamixer` (ADAT or internal; no word clock input). [COMMUNITY]
- Reports of random crackle after minutes or days, on PipeWire and JACK. What helped varied: different buffers (64 or 1024), disabling then re-enabling the device in PipeWire, 96 kHz, a new cable. Nothing confirmed. [COMMUNITY]
- Do not blame Bazzite first. Test: ALSA-direct recording (`arecord -D hw:... -f S32_LE -r 48000 -c 4 test.wav`, UNVERIFIED flags) to see if the fault is in the driver or the graph.
- Never promise full-feature parity with Windows.

## 8. Routing and virtual devices

- Patchbays: qpwgraph (Qt) or Helvum (GTK); both Flatpak on Flathub. [UNVERIFIED availability on Bazaar]
- Virtual sink via the loopback module [VERIFIED, PipeWire loopback docs]: drop a file in `~/.config/pipewire/pipewire.conf.d/` containing a `context.modules` entry with `libpipewire-module-loopback`; set capture.props `media.class = "Audio/Sink"` and `node.name`, playback.props `target.object` to a real sink node name, `node.passive = true`.
- Use cases: stream to OBS from a DAW, separate game and music paths. Find node names with `wpctl inspect` or `pw-cli info`.
- MIDI: ALSA seq ports through `aconnect`, or PipeWire MIDI bridge shown in qpwgraph. `pw-cli create-link` can connect ports from a script. [VERIFIED command existence]
- Save patchbay layouts in qpwgraph and autostart it only if you need a fixed routing.

## 9. Plugins and paths

- User paths: `~/.vst3`, `~/.clap`, `~/.vst`, `~/.lv2`, `~/.ladspa`. [COMMUNITY, Fedora forum]
- /usr is read-only on Bazzite; system paths are not writable. Install to home.
- Bitwig Flatpak: plugins in `/usr/lib` are invisible; home folder works; Bitwig recommends installing plugins as Flatpaks when possible. [VERIFIED, Bitwig page]
- Flatpak plugin extension point `org.freedesktop.LinuxAudio.Plugins`, mounted `/app/extensions/Plugins` with subfolders vst, vst3, clap, lv2, ladspa. Extension version must match the app runtime (Bitwig manifest: 25.08). [VERIFIED]
- Your own JUCE plugins: ship `.vst3` and `.clap` as plain copies into `~/.vst3` and `~/.clap`; Flatpak-extension packaging is optional extra work.

## 10. yabridge (Windows plugins)

- Does not work with Flatpak DAWs. Community workarounds (running Bitwig's binary from its Flatpak files dir; `yabridge-bottles-wineloader`) are fragile. [VERIFIED limit, COMMUNITY workarounds]
- Needs Wine Staging; README says 9.22 and 10.x did not work with yabridge 5.1.1; testing was on 9.21. Current status UNVERIFIED; check yabridge issues. Newer Wine bugs about GUI offsets exist. [COMMUNITY]
- Core commands [VERIFIED]:

```
yabridgectl add "$HOME/.wine/drive_c/Program Files/Common Files/VST3"
yabridgectl sync
yabridgectl status
wineserver -k
```

- Bridged plugins appear in `~/.vst3/yabridge` and `~/.clap/yabridge`. [VERIFIED]
- On an immutable base prefer a Distrobox with wine-staging; whether a Distrobox yabridge plus Flatpak Bitwig works is UNVERIFIED.

## 11. Xrun debugging, in order

1. `pw-top` while the problem plays. ERR rising means xruns.
2. Raise buffer one step. If gone, it was load; if not, continue.
3. Close browser, Steam, indexers. Check `top` for a busy process.
4. Governor on performance (section 6).
5. Realtime test passes (section 5).
6. USB: other port, other cable, no hub.
7. Same fault in ALSA-direct test? Then driver or hardware.
8. Same fault with only one plugin? Plugin.
9. Logs: `journalctl --user -u pipewire -u wireplumber -b` and `dmesg -T | grep -iE 'usb|xhci|audio'`.
10. After a system update only: `rpm-ostree status`, roll back (`rpm-ostree rollback`) to test. [VERIFIED command]

### Glitch decision tree

- Click at start or stop only: fades, not an xrun.
- Constant crackle with ERR rising: buffer or CPU.
- Crackle after hours then persists: device state; replug, restart PipeWire (`ujust restart-pipewire`).
- Pitch or speed wrong: rate mismatch device vs project.
- Silence: wrong output node or profile; `wpctl status`; pro-audio profile.
- Windows plugin crashes DAW: yabridge/Wine section; clean prefix.
- Only in browser or game: `ujust restart-pipewire`; check Pulse default sink.

## 12. Bazzite and Atomic specifics

- /usr read-only; use Flatpak (Bitwig), Homebrew for CLI, Distrobox for Linux audio tools that are not packaged. [VERIFIED install order]
- Layering audio packages (`rpm-ostree install <pkg>`) is a last resort; it needs a reboot and slows updates. [VERIFIED]
- Kernel args via `rpm-ostree kargs` (section 6, UNVERIFIED flags).
- Distrobox audio tools reach PipeWire through the host socket; JACK/ALSA device passthrough in containers is UNVERIFIED.
- After every system update re-run the first-session checks.

## 13. First session setup checklist

1. `uname -r` is 6.12 or newer for the Digiface (if you own one). Plug it in.
2. `wpctl status`: interface visible; set Pro Audio profile if needed.
3. Realtime checks (section 5); fix groups with the documented Atomic steps.
4. Install Bitwig from Bazaar; sign in.
5. Bitwig Settings, Audio: PipeWire driver, the interface, 48 kHz, 256 samples.
6. Create `~/.vst3`, `~/.clap`; copy plugins; rescan.
7. Add MIDI controllers; verify notes and clock.
8. Play a heavy project with `pw-top` open; ERR should stay 0.
9. Set 512 for mixing; save a template; pin a good system image (`sudo ostree admin pin 0`). [VERIFIED]

## Sources

- https://docs.pipewire.org/page_man_pipewire_1.html
- https://docs.pipewire.org/page_man_pw-cli_1.html
- https://docs.pipewire.org/page_man_pw-jack_1.html
- https://docs.pipewire.org/page_module_loopback.html
- https://github.com/robbert-vdh/yabridge
- https://cdn.jsdelivr.net/gh/robbert-vdh/yabridge@master/README.md
- https://oneuptime.com/blog/post/2026-03-02-configure-pipewire-low-latency-audio-ubuntu/markdown
- https://www.bitwig.com/support/technical_support/52/
- https://raw.githubusercontent.com/flathub/com.bitwig.BitwigStudio/master/com.bitwig.BitwigStudio.yaml
- https://github.com/flathub/org.freedesktop.LinuxAudio.BaseExtension
- https://discussion.fedoraproject.org/t/where-are-the-users-vst-vst3-clap-directories/200321
- https://lkml.iu.edu/hypermail/linux/kernel/2409.0/00332.html
- https://discourse.ardour.org/t/rme-digiface-usb-update/111371
- https://forum.rme-audio.de/viewtopic.php?pid=246046
- https://docs.bazzite.gg/Advanced/add-user-to-group/
- https://docs.bazzite.gg/Installing_and_Managing_Software/ujust/
- https://docs.bazzite.gg/General/issues_and_resolutions/
