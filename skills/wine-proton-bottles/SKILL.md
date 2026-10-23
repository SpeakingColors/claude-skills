---
name: wine-proton-bottles
description: Use when running Windows music software or games on Bazzite or Linux with Bottles, Wine, Proton or ProtonPlus, covering prefixes, runners, dependencies, wineasio, yabridge, crashes and backups.
---

# Wine, Proton and Bottles on Bazzite

Verify against current docs before acting on anything marked UNVERIFIED.
Labels: VERIFIED = read in docs this session. COMMUNITY = forum/blog. UNVERIFIED = general knowledge.
Bottles docs: https://docs.usebottles.com/ . Bazzite docs: https://docs.bazzite.gg/ .

## 1. Pick the right tool

- Steam games: Steam with Proton (built in). Add GE-Proton with ProtonPlus (Flatpak id `com.vysp3r.ProtonPlus`; manages Steam, Lutris, Bottles, Heroic). [VERIFIED]
- Non-Steam games: Lutris (preinstalled), Heroic (Epic, GOG, Amazon), Faugus. [VERIFIED, Bazzite]
- Windows music software (Ableton Live, FL Studio, Studio One): Bottles Flatpak, one bottle per program. [UNVERIFIED that each runs well; test installers]
- Bitwig is native Linux: do not run it under Wine.
- Windows plugins inside Bitwig: yabridge (section 8). Realistically optional; native Linux plugins first.
- Bazzite lists Bazaar (Flatpak) as primary install source; Bottles comes from there or Flathub. [VERIFIED]

## 2. Prefix basics (what a "bottle" is)

- A prefix is a fake Windows folder (C: drive plus registry). Each program should get its own so one break does not spread.
- Steam prefixes: `~/.steam/root/steamapps/compatdata/<AppID>/pfx/drive_c`. Do not delete the whole compatdata folder, it holds every game's saves. [VERIFIED]
- Reset a Steam game prefix: ProtonPlus, Games tab, Open prefix directory; or Protontricks, "Select the default wineprefix", delete all data. [VERIFIED]
- Bottles stores bottles inside its sandbox: `~/.var/app/com.usebottles.bottles/data/bottles`. [VERIFIED for the migration path]

## 3. Bottles install and permissions (Flatpak)

- Flatpak is the most supported, only fully sandboxed version. [VERIFIED]
- Give access to one folder, not your whole home: [VERIFIED]

```
flatpak override --user --filesystem="/path/to/folder" com.usebottles.bottles
flatpak override --user com.usebottles.bottles --filesystem=xdg-data/applications
flatpak override --user com.usebottles.bottles --filesystem=xdg-data/Steam
flatpak override --user com.usebottles.bottles --filesystem=~/.var/app/com.valvesoftware.Steam/data/Steam
```

- Restart Bottles after overrides. Flatseal is the GUI alternative.
- Installers kept in `~/Downloads` need a filesystem override or a copy into the bottle's C: drive. [VERIFIED approach]
- Sample libraries and project folders: grant only those paths.

## 4. Runners

Bottles has two runner kinds: Wine and Proton. [VERIFIED]

- Caffe: official, patched for gaming and software. Default choice for music apps. [VERIFIED]
- Soda: a Bottles runner; docs fetched do not describe it. Treat as general-purpose alternative. [UNVERIFIED]
- Vaniglia: clean, only wine-staging patches. Good for isolating whether patches cause a bug. [VERIFIED]
- Wine-GE: GloriousEggroll Wine; not described in the Bottles docs fetched. [UNVERIFIED]
- Proton / Proton-GE (Proton-GE is custom Proton): recommended only for games that need Proton patches; switchable per bottle. [VERIFIED]
- Install runners: Bottles, Preferences, Runners. Tick Pre-release for release candidates only to test. [VERIFIED]
- Rule: change one thing at a time (runner, then dependency, then component) and keep notes.

## 5. Environments, components, dependencies

- Environments: Gaming, Software (apps), Custom. Software installs base set (vcrun, corefonts and more). [VERIFIED]
- DXVK (Direct3D 9/10/11 to Vulkan): on by default in Gaming and Software. VKD3D (Direct3D 12): on by default only in Application environment. Toggle in bottle preferences. [VERIFIED]
- DXVK-NVAPI and LatencyFleX: Preferences, DLL components. [VERIFIED]
- Music apps rarely need DXVK; if a GUI is glitchy try toggling DXVK off. [UNVERIFIED]
- Dependencies: Bottles uses its own manager, not winetricks. Installers pull dependencies automatically; reinstall one from the three-dot menu. Avoid multiselect install. [VERIFIED]
- .NET and vcruntime: add the matching entries under Dependencies (names like dotnet48, vcredist/vcrun2019 or later). Exact names in your Bottles version: look in the list, do not guess. [UNVERIFIED names]
- Programs: Bottles scans Start Menu for .lnk; Refresh to rescan; set launch options with `%command%`; Add Desktop Entry and Add to Steam exist. [VERIFIED]
- Env vars per bottle: Preferences, System, Environment variables. [VERIFIED]

## 6. Winetricks and Protontricks

- Bottles does not use winetricks. [VERIFIED]
- For Steam prefixes use Protontricks, Flatpak id `com.github.Matoking.protontricks`. It can only see the Steam directory unless you add filesystem permissions. [VERIFIED]

```
flatpak run com.github.Matoking.protontricks -l
flatpak run com.github.Matoking.protontricks <APPID> <ACTION>
```

- Plain winetricks for other prefixes needs a Distrobox or Homebrew install; UNVERIFIED on Bazzite.

## 7. WineASIO (low latency audio for Wine DAWs)

- WineASIO is an ASIO driver that talks to JACK. PipeWire's JACK layer can serve it. [VERIFIED README; PipeWire statement COMMUNITY]
- Register in a prefix: `env WINEPREFIX=<prefix> wineasio-register`. [VERIFIED]
- Needs a build that matches Wine (32 or 64 bit) and sits in Wine's library folders, which differ per distro. [VERIFIED]
- Bottles Flatpak caveat: it uses its own runner, not system Wine, so installing into /usr (as one blog does for native Bottles) will not work. A Flatpak recipe is UNVERIFIED; do not invent one. [COMMUNITY blog, native only]
- Blog flow for native Bottles on Fedora: build wineasio, `wineasio-register` with the bottle path (`bottles-cli info bottles-path`), copy the dll.so into the prefix system32. Treat as a lead, not a procedure. [COMMUNITY]
- Settings via env vars: `WINEASIO_PREFERRED_BUFFERSIZE` (power of 2, default 1024), `WINEASIO_NUMBER_INPUTS`/`OUTPUTS` (16), `WINEASIO_CONNECT_TO_HARDWARE`, `WINEASIO_CLIENT_NAME`. A buffer the backend does not support can shut the JACK server down. [VERIFIED]
- Fallback without WineASIO: Wine's own audio via PulseAudio driver; latency is worse but it works. [UNVERIFIED]
- Audio system rules (quantum, realtime) are in the linux-audio-production skill.

## 8. Windows VST hosting with yabridge

- Does not work with Flatpak DAWs. Bitwig on Bazzite is Flatpak. [VERIFIED limit]
- Needs Wine Staging, 64-bit prefix; README: Wine 9.22 and 10.x do not work with yabridge 5.1.1 (tested on 9.21). Current status UNVERIFIED. [VERIFIED statement]
- Bottles tie-in: community project `yabridge-bottles-wineloader`. [VERIFIED mention only]
- `yabridgectl add <VST3 folder>`, `yabridgectl sync`, `yabridgectl status`. Bridged plugins appear in `~/.vst3/yabridge`. [VERIFIED]
- Immutable-OS community workaround: a user-space Wine plus running Bitwig's binary from the Flatpak files directory. Fragile; updates may break it. [COMMUNITY]

## 9. DAWs and installers

- Ableton Live, FL Studio, Studio One: start with Caffe, Software environment, install via Bottles' installer if available or run the setup .exe (Add Shortcut).
- Installers needing .NET or vcruntime: install the dependency first, then run the installer.
- Black screen or silent crash in Flatpak: copy the program's whole folder into the bottle's C: drive via Browse C:, then add the exe with the Programs + button. [VERIFIED]
- Online authorization, iLok or copy-protection plugins are likely to fail. [UNVERIFIED]
- Game anticheat: some online games block Linux. [VERIFIED, Bazzite]

## 10. Performance and crash triage (in order)

1. Run Bottles from a terminal and read the INFO/WARNING/ERROR/CRITICAL lines. [VERIFIED]
2. Duplicate the bottle, change one thing in the copy (runner or DXVK).
3. Try Vaniglia, then Caffe, then a Proton runner.
4. Missing video in games: install GStreamer plugins and run `BOTTLES_USE_SYSTEM_GSTREAMER=1 bottles`. Wine builds like Caffe, Soda, Vaniglia ship none. [VERIFIED; system install on immutable base UNVERIFIED]
5. Use "Debug" in the bottle's Utility section for winedbg. [VERIFIED]
6. Stuck processes: `ujust fix-proton-hang` kills all Wine and Proton. [VERIFIED]
7. Steam game: `PROTON_LOG=1 %command%`, log at `~/steam-<AppID>.log`. [VERIFIED]
8. Old GPU without Vulkan 1.3: `PROTON_DXVK_SAREK=1` with Proton-CachyOS; no Vulkan at all: `PROTON_USE_WINED3D=1 %command%`. [VERIFIED]
9. Do not use gamemoderun. [VERIFIED]
10. Keep games and bottles on ext4/btrfs, not NTFS. [VERIFIED]

## 11. Backup, export, versioning

- Config backup: copies bottle.yml (attach it to bug reports). [VERIFIED]
- Full backup archive: whole bottle folder; contains personal files. [VERIFIED]
- Duplicate: clone as a template before experiments. [VERIFIED]
- Versioning: enable "Use versioning" in Custom environment; states are restore points. [VERIFIED]
- Import: Bottles v1, Lutris, PlayOnLinux. [VERIFIED]
- Back up project files and sample libraries separately; do not rely on bottle backups.

## 12. What NOT to do

- Do not share one prefix between unrelated programs.
- Do not install Wine system-wide with `rpm-ostree install wine` as a first move; layering slows updates and can block them. [VERIFIED costs]
- Do not give Bottles your whole home. [VERIFIED advice]
- Do not delete `compatdata` or `~/Games` wholesale.
- Do not install random winetricks verbs or DLL overrides blindly.
- Do not switch Proton versions more than 5 times in 24 hours for Denuvo games. [VERIFIED]
- Do not force Proton on Counter-Strike 2. [VERIFIED]
- Do not use the Steam beta client; Bazzite does not support it. [VERIFIED]
- Do not expect copy-protected Windows plugins to authorise.

## Sources

- https://docs.usebottles.com/
- https://docs.usebottles.com/getting-started/installation
- https://docs.usebottles.com/llms-full.txt
- https://github.com/Vysp3r/protonplus
- https://github.com/Matoking/protontricks
- https://github.com/wineasio/wineasio
- https://git.ewpratten.com/evan/ewpratten.com/raw/branch/gh_ci/content/blog/2024-01-05-wineasio-bottles-ableton.md
- https://cdn.jsdelivr.net/gh/robbert-vdh/yabridge@master/README.md
- https://github.com/robbert-vdh/yabridge
- https://write.as/stack-tracer/running-bitwig-on-steamos-with-native-windows-vsts
- https://docs.bazzite.gg/Gaming/Managing_and_modding_games/
- https://docs.bazzite.gg/Gaming/Common_gaming_issues/
- https://docs.bazzite.gg/Gaming/Hardware_compatibility_for_gaming/
- https://docs.bazzite.gg/Installing_and_Managing_Software/software-intro/
- https://docs.bazzite.gg/Installing_and_Managing_Software/ujust/
