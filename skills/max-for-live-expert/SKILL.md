---
name: max-for-live-expert
description: Use when helping a non-programmer build, debug, freeze or share Max for Live devices (audio effect, instrument, MIDI effect), or Max 9 licensing, the Live Object Model and Live/Max on Linux.
---

# Max for Live (Max 9 era)

Labels: VERIFIED (source) = read on a page I fetched. COMMUNITY = forum or user report. UNVERIFIED = not confirmed; do not rely on it.
Rules for Claude: assume the reader is not a programmer. Plain words first, then one exact step. One change at a time, ask the reader to test, then continue. Never invent object names, attributes or version numbers; if unsure, say UNVERIFIED and point to the reference page.

## 1. Editions and licensing
- Max for Live is included with Live Suite. Live Standard can buy it as an add-on. VERIFIED (ableton.com Live manual 12, Max for Live chapter; support.cycling74.com Common questions about Max for Live)
- Live Lite and Intro cannot use the add-on. VERIFIED (help.ableton.com 206407124; Cycling '74 support article)
- Add-on price: not stated on the pages I read. Check the Ableton shop. UNVERIFIED
- Live 12 comes bundled with Max 9. Max 9 does not work with Live 11 or earlier (use Max 8 there). VERIFIED (help.ableton.com 209772305)
- The bundled Max is a different product from standalone Max. M4L lacks some features, e.g. multichannel devices and saving Gen patchers. VERIFIED (Cycling '74 support, Common questions)
- Saving devices that use Gen, MC or Jitter Geometry objects needs a standalone Max license. VERIFIED (same article). So gen~ and mc. work needs standalone Max 9.
- Max for Live and standalone Max are authorized separately. A standalone serial will not unlock M4L. VERIFIED (same; help.ableton.com 206407124)
- "Unauthorized" in Max usually means you opened standalone Max. Fix: sign out of Max, quit Max and Live, reopen Live, add an M4L device, choose Edit in Max. VERIFIED (Cycling '74 support)
- Max 9 (cycling74.com/shop/max): permanent license $399 (Max 9 and 9.x.x updates; major upgrades extra), or subscription $120/year or $12.99/month. VERIFIED (cycling74.com/shop/max, fetched 2026-10-23, prices can change)
- Max has a free trial, fully unlocked during the trial. VERIFIED (cycling74.com/products/max). Trial: 30 days after download and a free account. VERIFIED (cycling74.com/products/max, fetched 2026-10-23).
- Max for Live owners get an Ableton-customer discount on standalone Max. VERIFIED (Cycling '74 support)
- To use a newer or standalone Max inside Live: Live Settings, File & Folder, Max Application, pick it, restart Live. VERIFIED (Live manual; forum.ableton.com p=1829321 as COMMUNITY detail)
- Max 9 standalone requirements: macOS 11.0 or later (Intel Core 2 Duo minimum, or Apple silicon), Windows 10 22H2 or Windows 11 22H2 or later (64-bit); 4 GB RAM minimum, 8 GB advised. No Linux. VERIFIED (cycling74.com/downloads). The 9.1.3 release page lists only macOS and Windows. VERIFIED

## 1a. Platforms (Windows, macOS, Linux)
| | Windows | macOS | Linux |
|---|---|---|---|
| Live 12 needs | Windows 10 22H2 or 11 22H2+, Intel i5 5th gen or Ryzen with AVX2, 8 GB RAM, about 6 GB disk. VERIFIED (help.ableton.com 115001663530) | Apple silicon on Big Sur 11.7.10+, or Intel up to Tahoe 26; 8 GB RAM, 8 to 10 GB disk. VERIFIED (same) | No official version (section 14) |
| Audio driver | ASIO-compatible hardware needed for Link, advised for best audio. VERIFIED (same) | Core Audio-compatible interface advised. VERIFIED (same) | Unofficial Wine project: ASIO driver PipeASIO. VERIFIED (shibco README) |
| Plugin formats in Live | VST2 (64-bit), VST3. Not AAX, RTAS, DirectX. VERIFIED (help.ableton.com 5937501570460) | VST2, VST3, AUv2, AUv3 (Live 11.2+). VERIFIED (same; Live manual) | Only Windows plugins inside the Wine prefix (section 14) |
| Plugin folders | Set a VST Custom Folder in Settings > Plug-ins; Live may find a path in the registry. VERIFIED (Live manual). VST3 default folder: UNVERIFIED | `/Library/Audio/Plug-Ins/VST` plus a custom folder; AU needs "Use Audio Units" on. VERIFIED (Live manual) | `~/.wine-ableton/drive_c/Program Files/Common Files/VST3/`. VERIFIED (shibco README) |
| Max for Live | Same .amxd; Max 9 with Live 12 | same | Experimental. VERIFIED (cdm.link) |
| Licence | Online or offline authorization (hardware code, .auz file); offline disables Pack updates and downloads in the Browser. VERIFIED (help.ableton.com 360000573444) | same | Own licence needed; the project does not change it. VERIFIED (README) |
- Frozen devices carry externals only for platforms in your search path, so a device with an external can be Windows-only or Mac-only. VERIFIED (live_freezing)
- Max packages folder: `Documents\Max 9\Packages` (Windows) or `~/Documents/Max 9/Packages` (macOS). VERIFIED (userguide/packages)
- MIDI Tools folder `~/Music/Ableton/User Library/MIDI Tools/...` is the macOS style path in the manual. Windows equivalent: UNVERIFIED.
- Skip plug-in scan at launch: hold Alt (Win) or Option (Mac). VERIFIED (Live manual)
- Splice in Live 12 needs macOS 12 or later. VERIFIED (help.ableton.com 115001663530)

## 2. Device types and the .amxd file
- Three device types: Max Audio Effect, Max Instrument, Max MIDI Effect. Also Modulators and MIDI Tools (Transformations, Generators). VERIFIED (Live manual 12)
- Devices are saved as .amxd files, separate from the Live Set. VERIFIED (Live manual; docs.cycling74.com m4l overview)
- A .amxd can hold patchers, abstractions, media and anything a Max collective can hold. VERIFIED (docs overview)
- Every new device starts from a template with the audio or MIDI in and out already wired. VERIFIED (live_creatingdevices)
- Default save folder: your User Library folder for the device type. MIDI Tools go to `~/Music/Ableton/User Library/MIDI Tools/Max Transformations` or `Max Generators`. VERIFIED (Live manual)
- Moving or renaming a .amxd can break paths. Use Live's File Manager to repair. VERIFIED (Live manual)
- MIDI Tools saved outside the default folders or Places are not indexed. VERIFIED (Live manual)
- Open the editor: device context menu or Show Options, Edit in Max. Before Live 12.2 there was an Edit button; the Options.txt line `-MaxForLiveDeveloperMode` brings it back. VERIFIED (Live manual)
- Save updates every instance of the device. Save As asks if the change applies to all instances or only the edited preset. VERIFIED (Live manual)
- Make a copy first: File, Save As, new name. VERIFIED (live_creatingdevices)
- Preview mode keeps the device audible in Live while you edit. VERIFIED (live_creatingdevices; plugin~ page)
- Device height is fixed at 169 pixels. Width is set with View, Set Device Width (Clear Device Width undoes it). VERIFIED (live_userinterfaces)
- Presentation mode: select objects, Add to Presentation, then turn on Open in Presentation in the Patcher Inspector. Only presentation objects show in Live. VERIFIED (live_userinterfaces)

## 3. Freeze, unfreeze, share
- Freezing packs everything the device needs: subpatchers, audio, images, JavaScript, third-party externals. It is NOT Live's Freeze Track. VERIFIED (live_freezing, Live manual)
- Steps: click Freeze in the device toolbar, then File, Save. It is frozen only once saved. Click Freeze again before saving to undo. VERIFIED (live_freezing)
- Files the device opens at runtime (a sample folder) must be added as dependencies before freezing. VERIFIED (live_sharing)
- Bundled files win over same-named files on disk. VERIFIED (live_freezing)
- Externals are bundled only for platforms you have in your search path. VERIFIED (live_freezing)
- A frozen device cannot be edited. Unfreeze first. A conflict icon in the toolbar means frozen files differ from disk; resolve it, then unfreeze. VERIFIED (live_sharing, live_unfreezing)
- Unfreeze writes new files to a folder named after the device inside "Unfrozen Max Device Files" on the Desktop. Choices on conflict: Use Device Version or Use Disk Version. VERIFIED (live_unfreezing)
- Sharing: freeze, save, send the single .amxd. Beyond that the pages gave no distribution steps. VERIFIED (live_sharing)

## 4. Live Object Model (LOM) and live.* objects
- LOM = Live's object classes with properties, functions and parent-child links. Docs cover Live 12.4.5. VERIFIED (docs.cycling74.com/apiref/lom)
- Root paths: `live_app`, `live_set`, `control_surfaces N`, `this_device`. VERIFIED (LOM page, live.path page)
- `live.path`: navigates. Messages `goto`, `path`, `getid`, `getpath`, `getchildren`, `getcount`. Left outlet id on request; middle outlet id whenever it changes. VERIFIED (live.path reference)
- A nonexistent path gives `id 0`, not an error. Cannot `goto` a list itself (`live_set scenes` fails, `live_set scenes 3` works). VERIFIED (live.path)
- `live.object`: `get`, `set`, `call`, `getid`, `id nn` (right inlet). Not all properties can be set. VERIFIED (live.object reference)
- `live.observer`: `property <name>` then outputs on every change. Not all properties are observable; check the LOM page. VERIFIED (live.observer reference)
- `live.remote~`: realtime parameter control that does not touch undo or automation. VERIFIED (Live API overview)
- Do not change the Live Set from inside a notification (observer or middle outlet); put `deferlow` between. VERIFIED (Live API overview, live.observer)
- Ids are valid only inside the device and are not saved. Re-navigate after load. Use `live.thisdevice`, not `loadbang`, to start. VERIFIED (Live API overview)
- Example path: `path live_set tracks 1 mixer_device volume`. Lists count from 0. VERIFIED (Live API overview)
- `live.thisdevice`: left outlet bang on open/preset load/save; middle 1 if enabled; right 1 if preview mode; `setwidth`. VERIFIED (live.thisdevice reference)
- UI objects: `live.dial` (also `live.numbox`, `live.menu` and similar). Only `live.dial` was read: Type (Float, Int, Enum, Blob), Range/Enum, Unit Style, Long Name, Short Name. VERIFIED (live.dial reference). `live.numbox`, `live.menu` pages: UNVERIFIED (not fetched).
- Live stores parameters as floats. Int parameters default to 0 to 255; for a wider whole-number range use Type Float with Unit Style Int. VERIFIED (live.dial)

## 5. Parameters, automation, presets
- A control shows in Live's automation list only if Parameter Visibility is "Automated and Stored". VERIFIED (live_automation)
- "Stored Only" keeps preset values but disables automation. "Hidden" is not stored or recalled. VERIFIED (live.dial)
- Give every control a clear Long Name and Short Name. That is what you see in Live. VERIFIED (live.dial attributes)
- Clip modulation needs Type Int or Float plus a Clip Modulation Mode. VERIFIED (live_automation)
- `live.param~` gives a sample-accurate signal from a parameter. VERIFIED (live_automation, live.param~ reference)
- Presets: `preset`, `pattr`, `pattrstorage`, `autopattr`. VERIFIED (presets_and_interpolation). How these combine with Live's own preset system in a device: UNVERIFIED (the page did not cover it).
- Max 9.1.3 added parameter visibility "Visible" and "Visible (Not Stored)". VERIFIED (9.1.3 release page). Check which Max your Live uses (section 1).

## 6. Max patch basics
- Messages (control) run on events. Signal objects end in `~` and run at audio rate. Gen is another system, see below. UNVERIFIED as one page; standard Max teaching, see Max tutorials.
- Audio in a device: `plugin~` in, `plugout~` out. Default 2 channels. VERIFIED (plugin~ reference)
- MIDI: `midiin` into `midiparse` splits note, CC, pitch bend and more. VERIFIED (midiparse reference)
- `gen~`: compiled single-sample patcher; use for filters, feedback, per-sample work. Uses `in`, `out`, `param`, `history`, `delay`; codebox uses GenExpr. VERIFIED (gen overview)
- `mc.`: multichannel; `mc.cycle~` is the MC version of `cycle~`. VERIFIED (docs.cycling74.com/userguide/mc)
- `abl.device.*~` and `abl.dsp.*~` wrap Live devices and DSP parts (Max package "Ableton DSP"). Whether Suite is required: UNVERIFIED. VERIFIED (userguide/abl); What's New in Max 9 says they expose "some of Ableton Live Suite's most popular devices".

## 7. JavaScript and Node
- `js` is the old engine (1.8.5), kept for compatibility. For new code use `v8` and `v8ui`. VERIFIED (userguide/javascript)
- JavaScript runs in the low priority thread; MIDI-triggered work is deferred, so tight timing may slip. VERIFIED (userguide/javascript)
- No DOM, no `document`. A function named `compile` cannot be reached from Max. VERIFIED (userguide/javascript)
- `node.script` runs Node in a separate process (can use another core; npm supported via `script npm install`). VERIFIED (node.script reference). The node.script page does not mention Max for Live.
- Node for Max inside M4L devices (support, freezing node folders): UNVERIFIED. Test with a tiny device before building on it.

## 8. Sync, transport, timing
- Unnamed `transport` objects in devices follow Live's transport. VERIFIED (live_timing)
- The `transport` object reflects Live's state on `bang` but cannot control Live. Control Live via the API. VERIFIED (userguide/transport)
- Named transports: live_timing says set `clocksource live`; the transport page says other named transports are not supported. The pages disagree. UNVERIFIED which is right; avoid named transports.
- Transport resolution is 480 PPQ. VERIFIED (userguide/transport)
- `plugsync~`, latency and plugin delay compensation: not covered on fetched pages. UNVERIFIED.

## 9. Performance and CPU
- Devices run in Live's low priority queue, unlike plain Max. COMMUNITY (cycling74.com forum, Max Device terribly slow inside Live)
- Biggest wins reported: hardwire routing instead of dynamic send~/receive~ networks; remove meter~ debug objects. COMMUNITY (same thread; 160% down to about 20% CPU in one case)
- `delay~ 0` costs as much CPU as a long delay. COMMUNITY (same thread)
- Many fast GUI objects cost CPU, even in hidden subpatchers. Slow down polling. COMMUNITY (forum Reducing CPU load)
- Downsample modulation signals when many use `live.remote~`. COMMUNITY (same thread)
- Jitter in M4L runs on the UI thread; frame rate depends on Live's audio buffer. VERIFIED (m4l overview)

## 10. Packs, examples, where to look
- Official docs: docs.cycling74.com (User Guide, Object Reference at /reference/, LOM at /apiref/lom/, Learn at /learn/). VERIFIED (docs home)
- The "Building Max Devices" pack teaches device building. VERIFIED (Live manual, m4l overview). Also see Max sidebar clippings and snippets. VERIFIED (m4l overview)
- Max packages: `~/Documents/Max 9/Packages` (macOS) or `Documents\Max 9\Packages` (Windows); Package Manager installs them; each can have an `examples` folder. VERIFIED (userguide/packages)
- Community devices: maxforlive.com lists free and paid devices; operator and terms not stated on the page. VERIFIED (maxforlive.com home). Check each device's Live version note.
- Reddit (r/ableton, r/maxmsp): BLOCKED, not read. Ableton forum: partly read (threads cited).

## 11. Beginner traps
- Opening standalone Max by mistake, then seeing "unauthorized". See section 1.
- Editing a frozen device. Unfreeze, or keep an unfrozen master.
- Using `loadbang` for Live API setup. Use `live.thisdevice`.
- Ids not saved: path objects must re-navigate on load.
- Control not automatable: check Parameter Visibility and Type.
- Files outside the device not frozen: add dependencies.
- Max 9 devices fail on Live 11. VERIFIED (help.ableton.com 209772305)

## 12. Recipe: simple device (a gain trim, audio effect)
1. In Live, drag a Max Audio Effect template onto a track. Choose Edit in Max.
2. File, Save As: name it (e.g. `Gain Trim`). Keep it in the User Library folder.
3. The template has `plugin~` and `plugout~`. Click the lock (bottom left) to unlock edit mode.
4. Add a `live.dial` and one `*~` per channel. Wire `plugin~` outlet to `*~` left inlet, `*~` to `plugout~`.
5. In the dial Inspector set Long Name `Trim`, Type Float, Range 0 to 1, Parameter Visibility Automated and Stored.
6. Dial left outlet to the right inlet of each `*~`. Save.
7. Select the dial, Add to Presentation, turn on Open in Presentation.
8. Test (section 13). Only then freeze, save, and keep a copy of the unfrozen version.
For an instrument: same, but audio comes from your own synth objects into `plugout~`. For a MIDI effect: `midiin` and `midiparse` in, `midiout` out. UNVERIFIED for `midiout` details (not fetched).

## 13. How to test
- Does it make sound in the track? Bypass it and compare.
- Open the Max Console for red errors. Right-click a cord to add a Print watchpoint. VERIFIED (debugging_and_probing)
- Save a Live Set, close Live, reopen: does the dial value return?
- Automate the dial in Arrangement: does it move?
- Make a second instance: does it behave the same?
- Watch the CPU meter in Live with the device on and off.

## 14. Run it on Linux (Wine, Bottles, Proton) or alternatives
Status: unofficial and unsupported. VERIFIED (cdm.link). M4L is "Experimental". VERIFIED (cdm.link)
- Max for Live devices only run in Ableton Live; there is no standalone M4L. VERIFIED (m4l overview)
- Live has no official Linux version. VERIFIED by absence (Live manual, Max 9.1.3 page, requirements page lists Windows and macOS only)
- Wine bug 57109 (Aug 2024): Live 12 Max for Live hangs at "Starting Max..." on a git Wine build; unconfirmed. COMMUNITY (WineHQ list)
- 2012 report: M4L editor did not work in Wine (copy protection drivers). COMMUNITY (forum.ableton.com p=1443237, very old)
- WineHQ AppDB: Access Denied (Anubis), not read. UNVERIFIED
- Project: github.com/shibco/ableton-linux (LGPL-2.1, not affiliated with Ableton). Supports Live 11 and 12 (Intro to Suite, Lite, Trial), Max 8 and 9, M4L (Live 11 and 12), Push 1 and 2. Push 3 is claimed in the README but the troubleshooting page says Push 3 and Move are not supported yet. Pages disagree: UNVERIFIED. VERIFIED (README, TROUBLESHOOTING.md)
- Needs: x86-64, glibc 2.35+, PipeWire 1.4.2+, Linux 6.14+ with NTSync active, GStreamer base and good, coreutils, tar, zstd, flock. VERIFIED (README). Whether Bazzite's kernel, PipeWire and NTSync meet this: UNVERIFIED. Check first: `uname -r` and `pipewire --version`.
- Native Linux VST and CLAP do not load; an experimental Carla bridge exists (steps in the project's notes file, not read). VERIFIED (README, TROUBLESHOOTING.md)

### Recipe A: the project installer (best sourced)
Do one step, then test. Rule: nothing here was run on Bazzite for the reader.
1. Check the numbers: `uname -r` (need 6.14 or newer), `pipewire --version` (need 1.4.2 or newer). If lower, stop; run Bazzite updates first (skill bazzite-kde-linux).
2. Download your Ableton Live installer ZIP from your Ableton account (you need your own licence). VERIFIED (README)
3. Download `install-ableton-latest.run` from the project page. Exact release URL: UNVERIFIED, use the README link.
4. Run: `sh ~/Downloads/install-ableton-latest.run install`. For a chosen ZIP add `--live-installer "$HOME/Downloads/Ableton Live 12 Installer.zip"`. If the ZIP was renamed add `--live-major 12`. VERIFIED (README)
5. First run downloads extra files, so stay online. VERIFIED (README) Files go under your home (`~/.local/...`, `~/.wine-ableton`). VERIFIED (README paths)
6. Start with `ableton-live`. Settings > Audio: Driver Type ASIO, Audio Device PipeASIO. VERIFIED (README)
7. Authorize Live with your account. Offline route: hardware code, then .auz file. VERIFIED (help.ableton.com 360000573444)
8. Buffer: test `env PIPEASIO_PREFERRED_BUFFERSIZE=512 ableton-live`; settings file `~/.config/pipeasio/config.ini`. VERIFIED (TROUBLESHOOTING.md). Start at 256 or 512.
9. Turn on Enable GPU Renderer. If grey: `env WINE_D3D_FORCE_GPU_RENDERING=1 ableton-live`. VERIFIED (TROUBLESHOOTING.md)
10. Max for Live: use Live 12 with its bundled Max 9. Build the Gain Trim device (section 12). Live 11 needs a one-time repair: `sh ~/Downloads/install-ableton-latest.run --extract /tmp/ableton-kit` then `bash /tmp/ableton-kit/scripts/installer.sh prefix repair-live11`. VERIFIED (TROUBLESHOOTING.md)
11. Windows plugins: run their installer with the project's Wine: `env WINEPREFIX="$HOME/.wine-ableton" "$HOME/.local/opt/wine-d2d1-nspa-11.13/bin/wine" "/path/to/PluginInstaller.exe"`. VERIFIED (README). The Wine folder name may change with releases; use `ls ~/.local/opt`.
12. Link: UDP port 20808 must be open; guest Wi-Fi and VPNs block it. VERIFIED (TROUBLESHOOTING.md)
13. Updates are manual: `sh ~/Downloads/install-ableton-latest.run update`; read the changelog first. VERIFIED (README)
yabridge: not mentioned by the project. Using it with this Wine: UNVERIFIED. Generic yabridge facts are in skill wine-proton-bottles section 8 (not for Flatpak hosts).

### Recipe B: Bottles and WineASIO by hand (weaker)
1. Follow skill wine-proton-bottles sections 3 to 7: Bottles Flatpak, Software bottle, runner Caffe, one bottle for Live.
2. Install all Visual C++ runtimes first; this stopped crashes for one Debian user on Live 12 Suite in a Win10 prefix with wine-staging. COMMUNITY (KVR p=8884394)
3. Audio: WineASIO needs JACK (PipeWire's JACK layer). The only written recipe is for native Bottles on Fedora, building WineASIO and registering it in the bottle. COMMUNITY (ewpratten blog). A Bottles Flatpak recipe is UNVERIFIED. Wine's PulseAudio path gave 5 ms at 256 samples and was called high. COMMUNITY (forum.winehq.org p=141770)
4. If WineASIO fails, ASIO4ALL was used instead. COMMUNITY (KVR). WineASIO settings are env vars; see skill wine-proton-bottles section 7.
5. M4L in this route: likely to hang (bug 57109). UNVERIFIED outcome.

TEST checklist (both recipes):
1. Live opens without a crash 5 times. 2. Authorization survives a restart. 3. Audio plays 10 minutes, no crackle at 256 or 512. 4. Interface hot-plug. 5. MIDI keyboard plays a synth. 6. A Max Audio Effect loads and the editor opens (Edit in Max). 7. Save the device, save a Set, reopen: dial value returns. 8. Freeze the device and reopen. 9. CPU meter steady. 10. A Windows VST3 appears and opens. 11. Sleep and wake. 12. Link if used.
Known problems: installer hangs while the Ableton USB Driver tray icon is open (fixed after 2026.08.04.1); WMA or video import can crash Live 11; plugin window scaling (turn off Auto-Scale Plugin Window); GNOME shortcut clashes (`ABLETON_SHORTCUTS=take`); display scaling via `ABLETON_DPI_MODE`. VERIFIED (TROUBLESHOOTING.md)
Backup: `uninstall --keep-prefix` keeps prefix, Live and authorization; `--delete-prefix` removes them. VERIFIED (README). Copy the folder `~/.wine-ableton` before each update (path VERIFIED, copying it is my advice). Bottles route: Duplicate and Full backup (skill wine-proton-bottles section 11). Back up Sets and the User Library yourself; their location in the prefix: UNVERIFIED.
Do NOT rely on it for: gigs, deadlines, copy-protected plugins (iZotope and D16 plugins fail authorization under Wine, VERIFIED yabridge README), unsupported hardware, or Push 3 without testing.
Alternatives on Linux:
- Bitwig Studio (skill bitwig-studio) for native work. Rebuild the idea as a Bitwig device or a JUCE plugin (skill vst-maker). M4L devices in Bitwig or Studio One: UNVERIFIED, widely said to be impossible.
- Keep a Windows or Mac PC for Live and M4L.

## Not verified
- M4L add-on price.
- Live system requirements page (failed to fetch); native Linux status beyond absence.
- Pages for live.numbox, live.menu, live.gain~, midiout, plugsync~ (not fetched).
- Node for Max inside M4L; named transport behaviour; Suite requirement for abl.* objects.
- Reddit (blocked). Ableton Live 12.x current patch and bundled Max sub-version.
- Shibco Wine project on Bazzite; any real M4L test on Linux; Push 3 support in that project (pages disagree); Windows VST3 default folder; NTSync check command; WineHQ AppDB (blocked); Carla bridge steps.

## Sources (fetched)
- ableton.com/en/live-manual/12/max-for-live/
- ableton.com/en/live/max-for-live/ ; ableton.com/en/live-manual/12/live-concepts/
- help.ableton.com/hc/en-us/articles/209772305 ; 206407124
- support.cycling74.com/hc/articles/360049845974 (Common questions about Max for Live)
- cycling74.com/shop/max ; cycling74.com/products/max ; cycling74.com/products/maxforlive ; cycling74.com/shop
- cycling74.com/releases/max/9.1.3
- docs.cycling74.com: home, userguide, userguide/new_in_max9, userguide/m4l (overview, live_creatingdevices, live_userinterfaces, live_automation, live_sharing, live_freezing, live_unfreezing, live_timing), userguide/javascript, mc, abl, transport, packages, presets_and_interpolation, debugging_and_probing, gen/_gen_overview
- docs.cycling74.com: apiref/lom, apiref/nodeformax, legacy/max8/vignettes/live_api_overview
- docs.cycling74.com/reference: live.path, live.object, live.observer, live.thisdevice, live.dial, live.param~, plugin~, midiparse, node.script
- cycling74.com/forums: max-device-terribly-slow-inside-live ; reducing-cpu-load ; confusion-full-max9-cycling74-license-and-livesuite12-bundled-max-installation ; max-on-linux
- forum.ableton.com viewtopic p=1829321, p=1443237
- list.winehq.org wine-bugs thread (Bug 57109)
- cdm.link/ableton-live-on-linux/ ; github.com/shibco/ableton-linux
- maxforlive.com
- help.ableton.com 115001663530, 5937501570460, 360000573444; cycling74.com/downloads; Live manual plug-in chapter (via Ableton knowledge search); github.com/shibco/ableton-linux README and TROUBLESHOOTING.md; wineasio README; ewpratten.com blog; forum.winehq.org p=141770; kvraudio.com p=8884394; yabridge README
- Failed or blocked: docs.cycling74.com/userguide/m4l/ (index), ableton.com/live/system-requirements, appdb.winehq.org (Access Denied), reddit.com (blocked)
