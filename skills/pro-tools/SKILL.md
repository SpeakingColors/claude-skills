---
name: pro-tools
description: Use when helping with Avid Pro Tools, covering editions, pricing, iLok licensing, Linux/Wine status, AAX plugins (and testing your own), playback engine, sidechain, Atmos and hard dance workflow.
---

# Avid Pro Tools

Labels: VERIFIED (source) = read on a page I fetched. COMMUNITY = forum or blog report. UNVERIFIED = not read, test before relying on it.
Researched 2026-10-23. Prices and versions change. Re-check before quoting.
Rule for Claude: Assume the reader is not a programmer. Plain words first, then one exact step. One change at a time, ask the reader to test, then continue. Say which OS (Mac or Windows) each step is for.

## 1. Version and editions
- Latest release I found: Pro Tools 2026.4 (30 Apr 2026), then 2026.4.1 (about 10 Jul 2026, page date "07.10.26" is ambiguous). VERIFIED ([1][2])
- 2026.4 adds Track Pin, MPEG-H immersive support, Dolby Headphone Personalization, Speech-to-Text updates, Massive X Player. Immersive and Speech-to-Text parts are Studio and Ultimate only. VERIFIED ([1])
- Plans: Intro (free: 8 audio, 8 instrument, 8 MIDI tracks), Artist, Studio, Ultimate. VERIFIED ([3])
- Track counts. Artist: 32 audio, 64 MIDI. Studio: 512 audio, 1,024 MIDI, 1 video, immersive support. Ultimate: 2,048 audio, 1,024 MIDI, 64 video, full post tools. VERIFIED ([3])
- Prices in USD (individuals): Artist 9.99 per month, 99 per year, 199 perpetual, 69 yearly upgrade. Studio 34.99 per month, 299 per year, 599 perpetual, 199 upgrade. Ultimate 99 per month, 599 per year, 1,499 perpetual, 499 upgrade. VERIFIED ([3], a 2026 third-party article, not avid.com)
- Education: Studio 99 per year, Ultimate 299 per year. Artist n/a. VERIFIED ([3])
- Perpetual: sold only through authorised resellers, not the Avid web store. You can keep using your version after the upgrade plan lapses, but get no new versions. VERIFIED ([3][4])
- Flex: a 2022 article called it the top tier ($999 per year or $99.99 per month, 2,000+ tracks, ExpertPlus support, DigiLink license). A reseller page lists Flex 1-year with Ultimate-level counts (2,048 audio, 128 VCA). VERIFIED ([5][6]). Whether Flex is still current in 2026: UNVERIFIED, the 2026 plan table in [3] does not list it.
- avid.com pricing and system-requirements pages return only navigation text to my fetcher (JavaScript pages). Avid's own current price list: UNVERIFIED.

## 1a. Platforms (Windows, macOS, Linux)
| | Windows | macOS | Linux |
|---|---|---|---|
| OS | Windows 11 24H2 and 25H2 (2026.4). VERIFIED [7] | Sonoma 14.8.x, Sequoia 15.7.x, Tahoe 26.3.x; M1 to M5 or Intel i5. VERIFIED [2] | No native version. VERIFIED by absence [2][7][8] |
| Audio driver | ASIO from the interface maker, installed BEFORE Pro Tools. VERIFIED [7]. ASIO4ALL without an interface: COMMUNITY [9][18] | Core Audio. Not on a page I read: UNVERIFIED | None. PipeWire and JACK are not supported by Avid. UNVERIFIED |
| Plugin format | AAX only (section 5). Folder `C:\Program Files\Common Files\Avid\Audio\Plug-ins`. VERIFIED [33] | AAX only. Folder `/Library/Application Support/Avid/Audio/Plug-Ins`. VERIFIED [33][34] | n/a |
| Force plugin rescan | Delete `InstalledAAXPlugins` in `AppData\Avid\Pro Tools`. VERIFIED [33] | Delete `InstalledAAXPlugins` in `Library/Preferences/Avid/Pro Tools`. VERIFIED [33] | n/a |
| Licence | iLok key, iLok Cloud or account login (Intro). iLok on USB3 can fail on some controllers, use USB2. VERIFIED [7][4] | iLok key or iLok Cloud. Same licence rules. VERIFIED [4][12] | iLok route blocked under Wine (section 3) |
| Shortcuts | Ctrl and Alt (section 11) | Cmd and Opt (section 11) | n/a |
- Windows only: with Windows Aero on, playback errors can occur at buffers of 128 or lower. VERIFIED [7]
- Both OSes: a 32-bit plugin in 64-bit Pro Tools gives error -7054. COMMUNITY [31]
- Session files are .ptx on both OSes; whether a session moves between Windows and Mac without changes: UNVERIFIED.
- VST3 and AU are not hosted on either OS (section 5). Your own VST3 builds do not load.

## 2. OS and hardware
- Windows: 2026.4 Read Me says "Windows 11 (24H2 and 25H2)". VERIFIED ([7]). Older note for 2025.6 listed Windows 10 22H2 too. VERIFIED ([8])
- macOS (2026.4.1): Sonoma 14.8.x, Sequoia 15.7.x, Tahoe 26.3.x. Chips M1 to M5, or Intel Dual Core i5 or faster. M5 is qualified, but Avid is still tuning M5 Pro and Max. VERIFIED ([2])
- Monterey dropped in 2025.6. VERIFIED ([8])
- Windows Read Me: install interface drivers before Pro Tools, or it will not launch. With Windows Aero on, playback errors can occur at buffers of 128 or lower. iLok on USB3 ports can fail (Texas Instruments controllers), use USB2. VERIFIED ([7])

## 3. Linux and Wine
- No native Linux version. No Linux in any requirements source I read. VERIFIED by absence ([2][7][8])
- One user on Ubuntu got Avid Link and Pro Tools Intro to open, then error AAE-6132 (output device could not be initialised). The post does not say Wine was used. COMMUNITY ([10], May 2023)
- Wine bug 55178 (Jul 2023, Wine 8.11): the iLok/PACE license manager installer fails (pnputil.exe). Status unconfirmed. VERIFIED ([11]). This blocks the iLok route.
- WineHQ AppDB rating: UNVERIFIED (search found nothing). Reddit: blocked for my fetcher.
- Plan for Bazzite: do not count on Pro Tools. UNVERIFIED that it can run at all. Section 14 has a test recipe and Linux alternatives.

## 4. Licensing and iLok
- Avid says Pro Tools uses iLok License Manager for activation; most other Avid products use Avid Link. VERIFIED ([12])
- A reseller FAQ says an iLok USB key is needed, or you can use iLok Cloud with a steady internet connection. VERIFIED ([4], Sweetwater, date unknown)
- Number of activations and offline behaviour: UNVERIFIED.
- Subscriptions stop working if payment stops. VERIFIED ([3][4])
- Steps for a new user: 1) Make an iLok account. 2) Install iLok License Manager. 3) Redeem the code in your Avid account. 4) Activate to the key or to iLok Cloud. 5) Install Pro Tools with Avid Link. (my outline, exact Avid steps UNVERIFIED)

## 5. Plugins: AAX only
- Pro Tools uses AAX only since version 11 (2013). RTAS and TDM were dropped. VERIFIED ([13])
- No VST3 or VST2 support. The article does not mention VST at all, so this rests on AAX being the only format. UNVERIFIED as a direct Avid statement. Wrappers (for example from plugin vendors) exist. UNVERIFIED.
- AAX Native: runs on CPU, any system. AAX DSP: runs on HDX cards or Carbon, low latency. AudioSuite: offline rendering. VERIFIED ([13])
- 2024.3 added AAX MIDI plugins. VERIFIED ([14])

### Testing your own plugins (JUCE)
- JUCE only builds the AAX. Signing is separate. VERIFIED ([15])
- Release builds must be signed with PACE tools (wraptool / EDEN) or Pro Tools will not load them. VERIFIED ([15][16], forum posts)
- Avid gives developers a debug build of Pro Tools that loads unsigned plugins. Only for registered developers. VERIFIED ([15])
- Reported route: get an iLok, register as an Avid developer, have Avid assign a free EDEN signing license to the iLok, sign, test in free Pro Tools Intro. COMMUNITY ([16], Jul 2022). Intro uses an account login, no iLok, but plugins must still be signed. COMMUNITY ([16])
- PACE sends an NDA before the toolkit. Replies can be slow. COMMUNITY ([16])
- Sign last. Any change to the bundle after signing breaks it. VERIFIED ([15])
- The AAX SDK needs a developer account. Not read from Avid, UNVERIFIED. If your own JUCE plugins are VST3 first, an AAX build is extra work and cost. Ask before starting.
- AAX test list: scan finds it; opens in Intro; preset recall after save and reopen; automation; sidechain; offline Bounce vs real time; no crash when buffer changes.

## 6. Playback Engine, buffer, I/O
- Open Setup > Playback Engine. Pick the interface. Set H/W Buffer Size. VERIFIED ([17][18])
- Avid starting point: 128 or 256 samples. Tracking: 64 or 128. Mixing big sessions: 512 or 1024. VERIFIED ([19])
- Playback Engine options (read): Ignore Errors During Playback/Recording (turn off for final mix), Dynamic Plugin Processing, Optimize Performance at Low Buffer Sizes (Mac, default on, may hang some plugins), Limit Number of Real-Time Threads (Intel Mac only), Disk Playback Cache Size. VERIFIED ([17])
- Intel Mac with Sonoma to Tahoe and a 1024 buffer: DSP instantiation error fixed by lowering buffer or limiting threads. VERIFIED ([20])
- I/O Setup: Input, Output, Bus tabs. Rename paths. Export your I/O settings to a file for recall. COMMUNITY ([18]). Shortcut Ctrl+Shift+I (Windows) or Cmd+Shift+I (Mac). COMMUNITY ([18])
- Sample rate and bit depth are set when the session is created. 24-bit is standard; 32-bit float gives headroom. COMMUNITY ([18])
- Windows needs ASIO. A generic ASIO4ALL is an option without a proper interface. COMMUNITY ([9][18])

## 7. Editing and mixing tools
- Elastic Audio: pick timebase (Tick for music, Sample for post). Algorithms: Polyphonic (full mixes), Rhythmic (drums), Monophonic (single notes, vocals), Varispeed, X-Form (best, needs rendering), élastique Pro. Views: Warp and Analysis. VERIFIED ([21])
- Clip Gain: select clip, click the clip gain icon, drag the fader. For changes over time: View > Clip > Clip Gain Line, then click with Grabber to add breakpoints. VERIFIED ([22])
- Do clip gain before compression to feed it an even level. VERIFIED ([22])
- AudioSuite is offline and destructive: Window > AudioSuite, pick effect, Preview, Render. The original stays in the Clip List. VERIFIED ([23])
- Real-time plugins sit on track inserts and process live. VERIFIED ([23])
- Aux inputs and routing folders sum tracks for group processing. Master Faders have no audio input, meter post-fader, and are not created by default. VCA faders control a Mix Group and pass no audio. VERIFIED ([24])
- Common bus layout: tracks to a bus, bus into an aux, aux to main out, Master Fader for metering. VERIFIED ([24])

## 8. Sidechain how-to (Avid)
1. Put a sidechain-capable compressor (for example Dyn3 Compressor/Limiter) on the track to duck, such as the bass. VERIFIED ([25])
2. On the trigger track (kick), add a Send to a free bus, e.g. Bus 1. Start the send at 0 dB. VERIFIED ([25])
3. In the compressor, set Key Input to that bus. VERIFIED ([25])
4. Click the Key button. VERIFIED ([25])
5. Lower the threshold until the bass ducks. Fast attack, medium release. VERIFIED ([25])
- No ducking: check Key is on and the send is not muted. The compressor must be on the track you want to duck. VERIFIED ([25])
- Pre-fader send so the kick can be muted and still trigger: UNVERIFIED, test it.

## 9. Dolby Atmos basics
- The integrated Atmos renderer is included in Studio and Ultimate. An external renderer is still supported. VERIFIED ([26])
- I/O Setup has a tab for beds, objects, groups, trim and downmix, saved with the session. VERIFIED ([26])
- Binaural headphone monitoring works. Speaker monitoring needs at least 12 outputs. VERIFIED ([26])
- Known issue: intermittent Aux I/O errors with the external renderer on macOS Sonoma to Tahoe. VERIFIED ([20])

## 10. Sessions, saving, sharing
- A session is a folder. The .ptx file is a list of references to audio, plus mixer, plugin and MIDI settings. VERIFIED ([27])
- Save = overwrite. Save As = new .ptx. Save Copy In = new self-contained folder. Save As Template = .ptxt. Session File Backups = .bak.001 files; opening one makes .recovered.ptx. VERIFIED ([27])
- To share: File > Save Copy In, never just copy the folder, because media can sit outside it. Use Copy not Add on import. VERIFIED ([28])
- Older versions: latest saves .ptx, PT 7 to 9 saves .ptf, 5.1 to 6.9 saves .pts. Newer features are lost. VERIFIED ([28], older article)
- Round trip 2026.4 to 2025.10.x can reset track outputs to none. Hidden tracks may reappear if saved with the Edit window closed. VERIFIED ([7])
- To another DAW: send stems from offline bounce, all from the same start point. VERIFIED ([28]). Pro Tools 2023.9 and later has Export Selected Range. VERIFIED ([14])
- Cloud collaboration: Avid Cloud Collaboration launched in 2016 (Pro Tools 12.5). Whether it is still offered in 2026: UNVERIFIED. VERIFIED only for 2016 ([29])

## 11. Keyboard shortcuts (Mac / Windows). VERIFIED ([30], Avid shortcuts PDF 2025.10)
- Play/stop: Space. Half speed: Shift+Space. Record: Cmd/Ctrl+Space, F12, or keypad 3.
- Loop playback: Cmd/Ctrl+Shift+L. Pre/post roll: Cmd/Ctrl+K.
- Edit modes: F1 Shuffle, F2 Slip, F3 Spot, F4 Grid.
- Tools: F5 Zoomer, F6 Trimmer, F7 Selector, F8 Grabber, Cmd/Ctrl+7 Smart Tool.
- Mix/Edit window: Cmd/Ctrl+=. New Track: Cmd/Ctrl+Shift+N. Duplicate Tracks: Opt/Alt+Shift+D.
- Separate clip: Cmd/Ctrl+E. Trim to selection: Cmd/Ctrl+T. Fades dialog: Cmd/Ctrl+F. Consolidate: Opt/Alt+Shift+3.
- Bounce Mix: Cmd+Opt+B (Mac), Ctrl+Alt+B (Win). Commit Track: Opt/Alt+Shift+C.
- Clip gain line: Ctrl+Shift+- (Mac), Start+Shift+- (Win). Shortcut search: Ctrl+Shift+K (Mac), Start+Shift+K (Win).
- AudioSuite shortcuts are not in that PDF. Use Setup > Keyboard Shortcuts.

## 12. Hard dance workflow (my recommendation, not sourced)
- Render the distorted kick to audio, then edit with Clip Gain and fades.
- Sidechain: use section 8. Duck bass and pads from the kick bus, not the kick itself.
- Use Elastic Audio Rhythmic on loops. Use Tick timebase so they follow tempo.
- Put drums, bass, leads on aux busses. Master Fader at the end for metering.
- Template: save a .ptxt with I/O, busses and sidechain send pre-built.
- Master: leave headroom, bounce 24-bit, limit in a mastering session.
- Pro Tools has no built-in stock hard dance synths in what I read. Kick design belongs in a synth plugin or in sampled kicks (for example Splice samples). UNVERIFIED which instruments ship.

## 13. Common errors (older sources: Pro Tools 11 and 12 era, check they still apply)
- -6101 / -6106 family (also -6085, -6086, -6031, -6080, -6093, -6097, -9128): H/W buffer or CPU overload. Raise the buffer, check the CPU meter, reduce plugins, turn off Wi-Fi and Bluetooth, update interface drivers, try another USB port. COMMUNITY ([31])
- -9073: disk too slow. Faster drive, bigger disk cache. COMMUNITY ([31][32])
- -9171: Host Processors too high at low buffers. Set to physical core count. COMMUNITY ([31])
- -6117: device missing. Install the interface driver. COMMUNITY ([31])
- -55: incompatible plugin, even unused in the folder. COMMUNITY ([31])
- -7054: 32-bit plugin in 64-bit Pro Tools. COMMUNITY ([31])
- -20007: bad I/O setup. Reset Input and Output tabs to Default. COMMUNITY ([31])
- Assertion errors: trash Pro Tools preferences first. COMMUNITY ([31][32])
- Plugin crash on launch: 2026.4 asks you to move the plugin to "Plugins (Unused)". VERIFIED ([7])
- Avid's official error list: not found. Avid publishes none, per one author. COMMUNITY ([32])

## 14. Run it on Linux (Wine, Bottles) or alternatives
Honest status: no source I read shows Pro Tools running on Linux. Treat this as a test, not a plan. Stop at the first failed step and report what you saw. The Bottles, WineASIO and yabridge facts come from the wine-proton-bottles skill; read it first.
Test target: Pro Tools Intro (free, 8 audio tracks, VERIFIED [3]). It uses an account login and no iLok key. COMMUNITY [16]
Steps (Bazzite, one at a time):
1. Install Bottles (Flatpak, from Bazaar or Flathub). Source: wine-proton-bottles skill, section 3.
2. Let Bottles see only the folder that holds the installer: `flatpak override --user --filesystem="/path/to/folder" com.usebottles.bottles`. Restart Bottles. Same skill, section 3.
3. Create a bottle: environment Software, runner Caffe, name it `ProTools`. One program per bottle. Skill sections 2, 4, 5.
4. Set the bottle Windows version to Windows 11 if the list offers it (Pro Tools 2026.4 lists Windows 11, VERIFIED [7]; whether Bottles offers it: UNVERIFIED).
5. In Dependencies, install the Visual C++ runtimes and .NET entries first. Exact names: look in the list, do not guess. Skill section 5.
6. Run the Avid Link or Pro Tools installer with Run Executable. Exact installer names and order: UNVERIFIED.
7. If the iLok or PACE installer is asked for, it will probably fail: Wine bug 55178 (pnputil.exe), status unconfirmed. VERIFIED [11]. So test Intro only.
8. Audio. Avid wants an ASIO driver on Windows (COMMUNITY [9][18]). Two paths, both UNVERIFIED for Pro Tools: (a) WineASIO with PipeWire's JACK layer; Flatpak Bottles recipe is not sourced, so do not invent one (wine-proton-bottles skill, section 7); (b) Wine's own audio driver, worse latency. One Ubuntu user reached Pro Tools Intro but got AAE-6132, output device not initialised. COMMUNITY [10]
9. yabridge does not help here. It bridges Windows VST2, VST3 and CLAP plugins into a Linux host, and it does not work with Flatpak hosts. VERIFIED (yabridge README). It does not list AAX. VERIFIED (same). So Windows AAX plugins would have to be installed in the same bottle. UNVERIFIED.
10. Set 48 kHz and a 256 sample buffer first (section 6). Realtime and PipeWire rules: skill linux-audio-production.
TEST checklist (stop at the first failure):
1. Installer finishes. 2. Pro Tools Intro opens and signs in. 3. Setup > Playback Engine lists a device, no AAE-6132. 4. New session plays a WAV for 10 minutes with no dropout. 5. Record 10 seconds from an input. 6. Insert one stock plugin. 7. Save, close, reopen. 8. Bounce offline. 9. Quit and open 5 times.
Known problems:
- iLok/PACE installer fails (bug 55178). VERIFIED [11]
- AAE-6132 on Linux. COMMUNITY [10]
- AppDB rating: not readable (Anubis block). UNVERIFIED.
- Bottles Flatpak has its own runner; WineASIO from the host does not carry over. VERIFIED (wine-proton-bottles skill, section 7)
Backup (skill section 11): before each change, Duplicate the bottle. Make a Full backup after a good install. Back up session folders yourself, outside the bottle.
Do NOT rely on it for: paid client work, gigs, deadlines, iLok-locked plugins, Ultimate or Studio features, Atmos. Keep a Windows or Mac machine for those.
Linux alternatives (native):
- Ardour (skill ardour), Reaper (skill reaper), Bitwig Studio (skill bitwig-studio), Waveform (skill waveform).
- Moving a session: send stems from an offline bounce, all from the same start point. VERIFIED [28]. Pro Tools 2023.9 and later has Export Selected Range. VERIFIED [14]
- Windows plugin needs: skill wine-proton-bottles section 8 (yabridge) and linux-audio-production section 10.

## Not verified
- Avid's own current price page, Flex status in 2026, activation limits, offline behaviour.
- Avid system requirements numbers (RAM, CPU).
- Any working Pro Tools on Wine or Linux, WineHQ AppDB rating (page blocked by Anubis), Core Audio statement, Avid Link install steps, whether Bottles offers Windows 11, Reddit and Gearspace opinions (Reddit blocked, Gearspace fetch failed).
- Direct Avid statement on VST support, AAX SDK access terms and cost.
- Cloud collaboration in 2026, Pro Tools stock hard dance tools, VCA and aux step-by-step in 2026 UI.
- Dolby Atmos step-by-step, Windows 10 support for 2026 versions.

## Sources (fetched)
1. https://www.avid.com/press-room/2026/04/avid-powers-faster-workflows-and-next-generation-immersive-audio-with-latest-pro-tools-release
2. https://www.production-expert.com/production-expert-1/avid-announces-pro-tools-202641-release-with-support-for-m5-mac-computers
3. https://www.production-expert.com/production-expert-1/avid-pro-tools-how-much-will-it-cost
4. https://www.sweetwater.com/sweetcare/articles/avid-pro-tools-licensing-faq/
5. https://musictech.com/news/gear/avid-announces-three-new-pro-tools-versions-shifts-to-subscription-only
6. https://www.musicmatter.co.uk/avid-pro-tools-flex-1-year-subscription
7. https://resources.avid.com/SupportFiles/PT/Pro_Tools_2026.4_Read_Me-Win.pdf
8. https://www.production-expert.com/production-expert-1/avid-drops-support-for-macos-monterey-with-pro-tools-2025-6
9. https://www.audeobox.com/learn/pro-tools/pro-tools-system-requirements/
10. https://forum.winehq.org/viewtopic.php?p=140751
11. https://list.winehq.org/hyperkitty/list/wine-bugs@list.winehq.org/thread/MTILRBKWNQEH5FQMHIUNWNLBHSNU3QOF/
12. https://www.avid.com/support/license-and-activation
13. https://www.production-expert.com/production-expert-1/pro-tools-aax-plugins-explained
14. https://www.production-expert.com/production-expert-1/every-pro-tools-release-in-the-last-five-years-a-working-professionals-reference
15. https://forum.juce.com/t/aax-codesigning/36700
16. https://forum.hise.audio/post/60686
17. https://www.production-expert.com/production-expert-1/pro-tools-playback-engine-every-setting-explained
18. https://www.audeobox.com/learn/pro-tools/pro-tools-audio-setup/
19. https://www.avid.com/pro-tools/user-guide/change-buffer-size
20. https://www.production-expert.com/production-expert-1/avid-pro-tools-known-issues-with-macos-sonoma-sequoia-and-tahoe
21. https://www.avid.com/pro-tools/user-guide/elastic-audio
22. https://www.avid.com/pro-tools/user-guide/clip-gain
23. https://www.avid.com/pro-tools/user-guide/audiosuite
24. https://www.soundonsound.com/techniques/pro-tools-master-faders?amp
25. https://www.avid.com/pro-tools/user-guide/sidechain-compression
26. https://www.avid.com/pro-tools/dolby-atmos/get-started
27. https://www.production-expert.com/production-expert-1/five-ways-to-save-in-pro-tools-and-when-to-use-them
28. https://www.soundonsound.com/techniques/fair-shares
29. https://www.prosoundweb.com/avid-cloud-collaboration-for-pro-tools-now-available/
30. https://resources.avid.com/SupportFiles/PT/Pro_Tools_Shortcuts_2025.10.pdf
31. https://www.production-expert.com/production-expert-1/more-pro-tools-error-codes-what-they-mean-and-how-to-fix-them
32. https://musictech.com/tutorials/pro-tools-tutorial-error-codes/
33. https://support.izotope.com/hc/en-us/articles/6658276282385-Locating-plug-ins-within-Pro-Tools
34. https://support.spitfireaudio.com/en/articles/11815335-where-are-the-au-vst-aax-plugins-on-mac
35. https://github.com/robbert-vdh/yabridge (README)
- Not fetched: appdb.winehq.org (Access Denied), avid.com/pro-tools/system-requirements (client error), avid.com/pro-tools/pricing and /system-requirements (empty), reddit.com (blocked), gearspace.com (failed), sweetwater DAE 6101 page (empty body).
