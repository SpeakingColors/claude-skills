---
name: dj-specialist
description: Use when advising a DJ on software, libraries, sets, gigs or hearing care, incl. the DDJ-FLX4, Rekordbox/Traktor on Linux, Mixxx and Engine DJ.
---

# DJ specialist

Labels: VERIFIED (source) = read on a fetched page; COMMUNITY = forum or user report; UNVERIFIED = general practice or memory, no source fetched. Never present UNVERIFIED as fact.

## How to use this skill
- Assume the reader is not a programmer. Give ONE step at a time, wait for "done", then give the next.
- Covers DJ software, controllers, libraries, set craft (hard dance, trance and general), gigs and hearing care. Examples use the Pioneer DDJ-FLX4 controller and Denon SC5000 + X1800 standalone gear.
- Related skills: denon-prime-sc5000-x1800 (SC5000 and X1800 troubleshooting and firmware), dj-gig-guide (gear families, gig technique, riders, contracts, country tips, travel), linux-audio-production and bazzite-kde-linux (Linux setup).
- Before advising on versions, re-check the vendor page; this skill was written 2026-10-21.

## Software vs Linux (Bazzite)
- Mixxx runs natively on Linux. VERIFIED (mixxx.org/download: Windows, macOS, Linux; 2.5.6 stable, recommended for live use).
- Mixxx install routes listed: Ubuntu PPA, Fedora RPM Fusion, Arch repo, Flatpak (org.mixxx.Mixxx), source. VERIFIED (mixxx.org/download).
- The Mixxx download page marks the Flathub Flatpak "currently unmaintained". VERIFIED (mixxx.org/download). Bazzite is immutable, so Flatpak is the usual app route; test it before relying on it. UNVERIFIED (Bazzite fit).
- Mixxx 2.6 is still beta (snapshot 2.6-beta-438) and not intended for live use; 2.5.6 (27 March 2026) is stated as probably the last 2.5 release. VERIFIED (mixxx.org/download, mixxx.org/news). The download page also offers Mixxx-hosted beta and nightly Flatpaks.
- Mixxx stem mixing is built on the Native Instruments open stem spec and was slated for 2.6; stems must be made externally, not generated live. VERIFIED (mixxx.org/news/2024-08-26-STEM-Mixing). The download page does not mention stems and 2.6 is unreleased, so do not promise stems yet.
- Traktor Pro 4 official page lists macOS 13-15 and Windows 11 only and does not mention Linux. VERIFIED (native-instruments.com Traktor Pro 4 page).
- Traktor: no native Linux version, no plans per an NI community moderator. VERIFIED (community.native-instruments.com thread, undated staff quote).
- Traktor 2 Pro under Wine "works reasonably well" and Traktor 4 via PlayOnLinux only with class-compliant interfaces; Native Access launcher showed blank for one user. COMMUNITY (same thread). Not safe for gigs.
- Rekordbox: official system requirements list Windows 11/10 and macOS 13-26 only; Linux is not listed. VERIFIED (rekordbox.com/en/download). Needs AVX2 CPU; STEMS needs 16 GB RAM recommended and Intel 8th gen or AMD Zen+ on Windows; formats ALAC, FLAC, WAV, AIFF, MP3, AAC. VERIFIED (same). Features include STEMS-based mixes, DVS, video output, recording and sharing mixes. VERIFIED (same).
- Rekordbox under Wine: old bug reports (rekordbox 5.3.0, Wine 3.12, 2018) show a crash after login. VERIFIED (WineHQ bugzilla mail) but outdated; current Wine state UNVERIFIED.
- Serato DJ Pro: official system-requirements page lists macOS and Windows 11 only, no Linux. VERIFIED (support.serato.com).
- VirtualDJ: no Linux version, "not going to happen" per PRO users; Wine possible but "not the full experience". COMMUNITY (virtualdj.com forum, 2025-2026). No staff statement found.
- Safest Linux plan: use Mixxx or Engine DJ standalone for gigs; keep Rekordbox/Traktor prep on a Windows/Mac machine or a dual-purpose laptop. UNVERIFIED (recommendation).
- Engine DJ Desktop OS support: the product and downloads pages show no OS list; release notes mention only Windows 10/11 and macOS (Apple Silicon, Ventura, Tahoe). VERIFIED (enginedj.com/downloads). Linux: a forum user got it "almost working" under Wine (audio only on first launch, registry workaround). COMMUNITY (community.enginedj.com). Treat as unsupported.
- Engine DJ Desktop can import music, playlists, hot cues and loops from rekordbox, Apple Music/iTunes, Serato and Traktor. VERIFIED (enginedj.com).

## Rekordbox library to Engine (SC5000 route)
- rb2engine (pip, Python 3.11+, runs on Linux/macOS/Windows) converts a rekordbox USB export into an Engine DJ library in place; writes only the database, no audio copy. VERIFIED (pypi.org/project/rb2engine).
- It carries tracks, playlists, beatgrids, hot cues, memory cues, loops, artwork. VERIFIED (pypi).
- Limits: Engine has 8 hot cue pads so extra cues are dropped; waveforms are rebuilt by Engine; re-running wipes Engine-side edits; beta status; supports rekordbox 5, 6, 7 exports. VERIFIED (pypi).
- Author warns to back up before using. VERIFIED (pypi). Step 1: copy the whole USB stick to a folder on the PC.
- Rekordbox PC database and Traktor NML are not covered by rb2engine; use Engine Desktop's import for those. VERIFIED (enginedj.com import list).
- Using the SC5000s from a rekordbox USB without conversion: UNVERIFIED, check the SC5000 skill.

## DDJ-FLX4
- Works with rekordbox, djay, Serato DJ Lite and Traktor Play free; Serato DJ Pro needs a separate license. VERIFIED (pioneerdjstore.com listing, a retailer).
- Smart CFX and Smart Fader exist; pads: Hot Cue, Pad FX, Beat Jump, Sampler. VERIFIED (retailer listing).
- Bus powered over USB, built-in sound card, single RCA out; mic is mixed in and sent over USB. VERIFIED (retailer listing).
- Class compliant USB audio and MIDI, so no drivers on Linux, Windows or macOS. VERIFIED (Mixxx manual FLX4 page).
- Mixxx mapping exists, built on firmware 1.02. VERIFIED (manual.mixxx.org/2.5 FLX4 page; the 2.6 manual page still says 1.02).
- In Mixxx set Master out to channels 1-2 and Headphones to channels 3-4. VERIFIED (Mixxx manual).
- Not mapped in Mixxx: Pad FX mode, Smart CFX, Smart Fader, Keyboard, Keyshift pad modes. VERIFIED (Mixxx manual).
- Mic jack is not routed back to the computer in Mixxx, so it cannot be recorded or streamed. VERIFIED (Mixxx manual).
- Master knob and Master Cue are hardware only. VERIFIED (Mixxx manual).
- Implemented: hot cue, beat loop, beat jump, sampler pads, sync, loops, EQs, trim, headphone cue/mix, jogs, effects with soft takeover. VERIFIED (Mixxx manual).
- AlphaTheta (Pioneer DJ) support: no extra driver needed; the standard Windows or macOS audio driver installs automatically over USB. VERIFIED (support.alphatheta.com DDJ-FLX4 driver article). A separate Windows ASIO driver is not described there; ASIO status UNVERIFIED.
- Firmware: support site has separate Windows and Mac firmware articles (versions and steps not read). UNVERIFIED; open those articles before giving steps.
- Mode switching rekordbox/Serato (shift steps): not found on the support pages fetched. UNVERIFIED; check the DDJ-FLX4 manual or PC/Mac & DJ Software section.

## Library hygiene
- Back up the library before any tool touches it. VERIFIED (rb2engine author advice).
- Engine stores paths relative to the "Engine Library" folder; symlinks help keep paths stable. COMMUNITY (Engine forum).
- Suggested layout: one MUSIC root with Genre / Year-Month-Bought; consistent file names; never move files outside the DJ software. UNVERIFIED (general practice).
- Keep a second copy on an external drive and a USB gig stick (see gig checklist). VERIFIED (Digital DJ Tips, backup copy advice).
- Key and BPM: always check by ear. Key detection tools can be wrong. VERIFIED (musicianwave.com).
- Beatgrids for hard dance: kicks are distorted and long, so auto-grids often drift; fix the first beat and check the last bar of each track. UNVERIFIED (producer practice).
- Cue points: mark first beat, intro end, drop, breakdown, outro. Use consistent pad colours per cue type. UNVERIFIED.
- Mixed In Key key tags: Camelot numbers are shown in the app; MIK also gives an Energy Level. VERIFIED (mixedinkey.com Camelot page mentions Energy Level).
- Streaming: Rekordbox, Serato and Virtual DJ list Beatport, Beatsource, SoundCloud and Tidal; Traktor Pro 4 only Beatport and Beatsource. VERIFIED (bonedo.de, German article, date not checked). Offline plans are priced by track count. VERIFIED (bonedo.de). Beatport's streaming page lists rekordbox, Serato, Traktor, VirtualDJ, Engine DJ OS, djay Pro and others, and does not mention Linux or Mixxx. VERIFIED (stream.beatport.com). Linux streaming: UNVERIFIED.
- Hard dance is poorly covered by streaming catalogues; buy tracks (Beatport, labels, Bandcamp) for gig-critical material. UNVERIFIED.

## Hard dance set craft (UNVERIFIED unless marked)
- Hardstyle: early about 135-150 BPM, later 150-160; modern often around 150. VERIFIED (Wikipedia Hardstyle).
- Trance: typically 120-150 BPM, commonly 125-150; uplifting styles closer to house at 120-135. VERIFIED (Wikipedia Trance music).
- English happy hardcore around 170 BPM, a single cited figure, no range given. VERIFIED (Wikipedia Happy hardcore, UK hardcore). Wider UK hardcore range (about 160-180) and happy hardcore up to 180+: UNVERIFIED. Confirm against your own library.
- Mix on bar boundaries, with tracks in 8, 16 or 32 bar phrases; swap bass on phrase starts; one low-end at a time. UNVERIFIED.
- Harmonic mixing with the Camelot wheel: same key, +/-1 on the same letter, or A/B switch are safe first picks. VERIFIED (mixedinkey.com).
- Energy boost: jump two numbers on the same letter, use sparingly. VERIFIED (mixedinkey.com, musicianwave.com).
- Check key by ear; Camelot is a shortlist, not a rule. VERIFIED (mixedinkey.com).
- Hardstyle kicks are tuned; clashes between kick and the next track's bass key are heard fast. Prefer short overlaps or filtered swaps. UNVERIFIED.
- Genre jumps (trance to hardstyle to hardcore): change tempo in steps or use a stop/echo-out and a bridge track. UNVERIFIED.
- Vocals: avoid layering two vocals; drop one with EQ or a stem. UNVERIFIED.
- Energy curve: warm-up, build in waves, peak, short breather, end strong. UNVERIFIED.
- Loops: use short loops to extend intros; always return on a bar line. UNVERIFIED.
- Stems (if available): vocals/drums swaps; Traktor stem files and Mixxx 2.6 use the NI stem spec. VERIFIED (Mixxx news post).

## Controller vs CDJ-style standalone
- Controller: cheap, bus powered, laptop required. VERIFIED (FLX4 listing).
- Standalone (SC5000 + X1800): USB or SD playback, no laptop. Details live in the Denon skill. UNVERIFIED here.
- Clubs often have CDJ-style players; practise on that layout, plus bring USB sticks. COMMUNITY/UNVERIFIED.

## Headphones, gain staging, recording
- Cue with the track one beat ahead and keep headphone level low; use one ear off the cup. UNVERIFIED.
- Gain: set trim so channel meters peak just below the red, master peaks never clip. UNVERIFIED.
- Mixxx on FLX4: headphones on out 3-4, so cue works from the hardware. VERIFIED (Mixxx manual).
- Recording: Mixxx records via the toolbar record icon or Recordings in the library sidebar; default is lossless WAV; other formats and settings in Preferences > Recording (list not read). VERIFIED (manual.mixxx.org/2.5). Mic can't be recorded in Mixxx on FLX4. VERIFIED.
- Streaming a set live (Twitch, SoundCloud etc.): not researched. UNVERIFIED.

## Gig checklist (Digital DJ Tips, VERIFIED)
- Club/festival: USB stick plus backup copy; laptop, charger, stand, USB cable; headphones, 1/8" to 1/4" adaptor and a backup pair; backup music source; multitool.
- General: phone and charger, cash, torch, pen and paper, water, towel, musician's earplugs (not foam).
- Bar/lounge adds: RCA, 1/4", XLR, 1/8" cables at least 1 m; extension lead; gaffer tape; mic and cable; backup DJ system.
- Backup ideas: cloned USB, phone mini-set with adaptor, backup laptop with same software and music, learn to DJ from the laptop keyboard.
- Ask the venue what they provide; test gear at home first.
- Rider and soundcheck specifics: UNVERIFIED, ask the promoter.
- Club etiquette (check the timeslot, never change levels on others, keep headphones on the booth, ask before using their gear): UNVERIFIED.

## Hearing health
- NIOSH recommends an 8-hour average of 85 dB; allowed time halves for every 3 dB; 100 dB should not exceed 15 minutes. VERIFIED (safetyandhealthmagazine.com).
- Take breaks, keep distance from speakers, use hearing protection, get an audiologist test, use a sound meter app. VERIFIED (same).
- Use musician's earplugs rather than foam. VERIFIED (Digital DJ Tips list).

## Practice routine (UNVERIFIED, suggested)
1. Day 1: pick 10 tracks in one genre; set beatgrids and cues; one step at a time.
2. Day 2: practise 16-bar blends only, bass swap on the phrase.
3. Day 3: add one loop and one effect, then record a 20 minute set.
4. Review the recording; note one thing to fix; repeat weekly.

## Unfetched or blocked (do not guess)
- AlphaTheta firmware articles, FLX4 manual (mode switching), Windows ASIO driver article.
- Not checked: Traktor Wine databases (AppDB), Digital DJ Tips articles on BPM or phrasing, Beatport/Beatsource Linux support, Mixxx key detection accuracy.

## Sources (fetched)
- https://mixxx.org/download/
- https://manual.mixxx.org/2.5/sr/hardware/controllers/pioneer_ddj_flx4
- https://ubuntuhandbook.org/index.php/2024/12/mixxx-2-5-0-released-ios-web-support/
- https://www.linux.org/threads/9to5linux-mixxx-2-5-6-open-source-dj-app-improves-controller-mapping-support-and-effects.64421/latest
- https://mixxx.org/news/2024-08-26-STEM-Mixing
- https://community.enginedj.com/t/engine-desktop-for-linux/46021/9
- https://pypi.org/project/rb2engine/
- https://enginedj.com/software/enginedj-desktop
- https://community.native-instruments.com/discussion/comment/215935
- https://virtualdj.com/forums/264862/Wishes_and_new_features/Linux%3F%3F.html
- https://www.winehq.org/pipermail/wine-bugs/2018-July/495572.html
- https://support.serato.com/hc/en-us/sections/200565990-System-Requirements
- https://www.bonedo.de/artikel/einzelansicht/dj-software-mit-musik-streaming.html
- https://pioneerdjstore.com/products/ddj-flx4
- https://manual.mixxx.org/2.6/en/hardware/controllers/pioneer_ddj_flx4
- https://mixxx.org/news/
- https://manual.mixxx.org/2.5/en/chapters/djing_with_mixxx
- https://rekordbox.com/en/download/
- https://www.native-instruments.com/en/products/traktor/dj-software/traktor-pro-4/
- https://enginedj.com/downloads
- https://support.alphatheta.com/en-US/products/12077079532697
- https://support.alphatheta.com/en-US/articles/12410664372121?product=12077079532697
- https://stream.beatport.com/
- https://en.wikipedia.org/wiki/Hardstyle
- https://en.wikipedia.org/wiki/Trance_music
- https://en.wikipedia.org/wiki/Happy_hardcore
- https://en.wikipedia.org/wiki/UK_hardcore
- https://mixedinkey.com/workflows/how-to-use-the-camelot-wheel/
- https://www.musicianwave.com/camelot-wheel-mixing-in-key/
- https://www.digitaldjtips.com/the-ultimate-checklist-of-things-to-take-to-your-dj-gigs/
- https://safetyandhealthmagazine.com/articles/12495-niosh-provides-hearing-protection-tips-for-musicians