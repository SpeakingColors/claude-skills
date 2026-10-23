---
name: av-receiver-specialist
description: Use when choosing, connecting, calibrating or troubleshooting an AV receiver (Yamaha, Sony, Denon, Marantz, Onkyo, Pioneer), HDMI ARC/eARC/CEC, speakers and wire, or explaining AV terms plainly.
---

# AV receiver specialist

Researched 2026-10-23. Labels: VERIFIED (source) = read on a page I fetched. COMMUNITY = owner or third party report, not official. UNVERIFIED = not confirmed, do not rely on it.
Lines without a label are standard industry know-how, not fetched. Check the manual before acting.
Rules: TLDR first. Then one step at a time: ask for ONE action, wait for the result. Never advise opening a powered unit. Explain every term in one plain sentence. Assume the reader is not a programmer. Plain words first, then one exact step. One change at a time, ask the reader to test, then continue.

## 1. Ask first: preference checklist
Fill this in with the person you help before recommending anything. Ask two or three at a time, not all at once.
1. Room: size, open or closed, distance from seat to speakers.
2. Speakers: brand, model, impedance (ohm) on the rear label, count, subwoofer yes or no.
3. Channels wanted: 2.1, 5.1, 7.1, or height speakers. Is height wanted at all?
4. Sound taste: neutral and uncolored, or processed? Any dislike of upmixing or virtual surround?
5. Listening mode: one automatic mode, or switching by hand? Remote use often or rarely?
6. Sources: TV, game console, PC, turntable, streamer. How many HDMI inputs needed?
7. Video: 4K120 gaming, VRR, 8K, HDR or Dolby Vision, dark room?
8. Control: HDMI CEC wanted so one remote runs everything?
9. Music or movies first? Night listening at low volume?
10. Budget, currency, country, retailer rules, financing, warranty length wanted.
Then restate the answers in 5 lines and ask "correct?" before advising.

## 2. How to choose a receiver
- Match the receiver to the speakers first, then to the sources.
- Power: compare ratings only at the same ohm, frequency range and distortion. Example: Yamaha RX300A is 70 W at 8 ohm, 20 Hz to 20 kHz, 0.09% THD, 2 channels driven. VERIFIED (usa.yamaha.com RX300A specs).
- Many receivers rate less per channel when all channels play at once. Denon lists a "70% guarantee at 5ch driven" on the AVR-X2900H. VERIFIED (denon.com X2900H). Ask for this when a seller quotes big watts.
- Impedance: Onkyo NR and RZ pages list speaker impedance 4 to 16 ohm. VERIFIED (onkyo.com NR5100, NR6100, RZ50). Yamaha pages list no separate minimum. VERIFIED (absence). Read the manual line "speaker impedance".
- HDMI count: count every source, plus one for the TV output. Note which ports are full speed (8K, 4K120). Denon X1800H: 6 inputs, 3 of them 8K. VERIFIED (denon.com X1800H).
- eARC wanted for lossless TV audio. Check both TV and receiver, and which port is the eARC one.
- Phono input only if a turntable is used. Zone 2 only if a second room is wanted. Both are missing on small models, see the table.
- Network features (HEOS, MusicCast, AirPlay) are not on every model. RX300A lists none. VERIFIED (specs page shows "-").
- Check warranty length and who sells it (section 7).
- One solid recommendation with the reason, one backup, and what would change the answer. No experiments.

## 3. Plain-words glossary
- ARC: TV audio sent back to the receiver over the HDMI cable. Compressed sound only.
- eARC: newer ARC with more bandwidth. Carries lossless audio and Atmos from TV apps.
- CEC: devices send each other commands over HDMI (power, volume, input). Brand names: BRAVIA Sync (Sony), HDMI Control (Yamaha, Denon, Marantz, Pioneer), RIHD (Onkyo). Sony and Yamaha names VERIFIED (sony.ca article 00173195 names HDMI Control and BRAVIA Sync); Onkyo and Pioneer names UNVERIFIED.
- HDMI 2.1 passthrough: receiver passes 4K120, VRR (variable refresh rate), ALLM (auto game mode) to the TV.
- Dolby Atmos, DTS:X: object audio. Needs height speakers or a virtual height mode to matter. Sound is placed in 3D, not on fixed channels.
- Dolby Surround, Neural:X, Pro Logic: upmixers. They spread a stereo or 5.1 signal over more speakers. Taste varies; some find it phasey. Can be switched off by choosing a Direct mode.
- Multi Stereo (Sony), Multi Channel Stereo style modes: copy the same stereo sound to all speakers. Yamaha, Denon names UNVERIFIED.
- Pure Direct, Stereo Direct: bypass tone controls and extra DSP (digital sound processing). Exact bypass rules differ by brand; read the manual. RX300A mode list UNVERIFIED.
- Room correction: a microphone measures the room, then the receiver sets distances, levels and EQ. Names: YPAO (Yamaha), Audyssey MultEQ (Denon, Marantz), MCACC (Pioneer), AccuEQ (Onkyo), D.C.A.C. (Sony), Dirac Live (optional on some). Audyssey MultEQ VERIFIED (denon.com, marantz.com); AccuEQ VERIFIED (onkyo.com NR5100); YPAO VERIFIED (Yamaha RX-V385, V4A, V6A); D.C.A.C. IX VERIFIED (sony.ca AN1000); MCACC and Advanced MCACC COMMUNITY (bestbuy.ca blog, henleyaudio.co.uk); Elite LX505 and LX805 add Dirac Live.
- Crossover and bass management: speakers set Small send bass below the crossover (for example 80 or 100 Hz) to the subwoofer. Large keeps full range.
- DAC: converts digital audio to analog. The receiver has one inside.
- Banana plug: a connector on the wire end that pushes into a speaker terminal. Optional.
- Binding post: screw terminal that takes bare wire, spade or banana. RX300A has 5. VERIFIED (specs page).

## 4. Debug order
Each step: one change, then test. Ask for the result.
1. No sound: correct receiver input, volume up, mute off, source audio set to the HDMI device.
2. No sound from TV apps: TV speaker output set to the receiver, ARC or eARC port used, HDMI Control on in both devices.
3. HDMI handshake loss (black screen, flicker, dropouts): power off all devices; unplug HDMI; power reset the TV about 2 minutes; reconnect; power on TV, then receiver, then source.
4. Sony documents this exact HDCP lockup problem; it can switch off Control for HDMI, ARC and BRAVIA Sync. Steps: unplug HDMI, reset TV, reconnect to ARC ports, HDMI Control on, BRAVIA Sync on, check the device list, set TV speaker to audio system, test. VERIFIED (sony.ca article 00173195). Same order is a fair start for any brand, COMMUNITY.
5. Yamaha notice: some emerging video signals such as 4K120 from select sources can lose picture and sound through AV receivers. VERIFIED (ca.yamaha.com support page, notice only). Try 4K60, another port, a certified high speed cable.
6. CEC not working: enable on every device; each brand has a different name (section 3); also test each device alone.
7. Lip sync (voice late): look for "Auto Lip Sync" or audio delay in the receiver menu; RX300A lists Auto Lip Sync. VERIFIED (specs page). Else adjust delay in 5 ms steps.
8. Protection mode: power off, unplug, check speaker wire for stray strands touching, check speaker ohm vs receiver minimum, clear space above vents, reduce volume, power on. If it repeats, stop and contact the brand.
9. Hum or buzz: unplug the antenna or cable TV feed; test one source at a time; plug sources and receiver into the same outlet strip. Do not remove ground pins.
10. Reset: erases calibration and settings. Note settings first. The key combo is model specific, so read the manual. RX300A reset UNVERIFIED.
11. Firmware: update through the receiver menu or brand page. Never power off during an update. RX300A update page returned only an index. UNVERIFIED.

## 5. Speakers and wire
- Impedance (ohm): the load. Lower ohm draws more current. Most receivers want 6 to 8 ohm speakers; 4 ohm only if the receiver lists it.
- Wire (know-how, not fetched): 16 AWG for runs under about 10 m at 8 ohm; 14 AWG for longer runs or 4 ohm. Cut clean ends, about 10 mm bare, twist strands, no strand outside the post.
- Banana plugs are optional and make swaps neat. Power OFF and unplugged before changing any wire.
- Polarity: red (+) to red, black (-) to black on every speaker. Wrong polarity gives thin bass.
- Subwoofer: use the sub output (LFE). RX300A has 2 sub outputs ("5.2"). VERIFIED (page).

## 6. Verify claims (how to label)
1. Find the official product page or manual. Read the specs tab, not only the overview. Overview pages often omit power, phono and zones.
2. Quote the line. Note the page name.
3. If two sections disagree, report both. Examples: Marantz Model 40n page says "1x HDMI eARC" in one place and "ARC PCM only" in another. VERIFIED (marantz.com/de-de Model 40n). Denon X3800H says 3 outputs and later "two outputs". VERIFIED (denon.com).
4. Owner reports and forum posts: label COMMUNITY. News and review sites: context only.
5. A missing line is not a "no". Write "not listed on the page", not "unsupported".
6. Reddit r/hometheater and sony.com were blocked from my fetch tool. AVS Forum not read. Owner failure patterns were not gathered, UNVERIFIED.
7. Prices and stock change; give the date read.

## 7. Model map (official pages, read 2026-10-23)
Format: model | HDMI in/out | ARC/eARC | power | calibration | notes | page.

### Yamaha (usa.yamaha.com/products/audio_visual/av_receivers_amps/...)
- RX300A | 4/1 | eARC, ARC | 70 W 8 ohm | "Room Correction" (YPAO not named) | 5.2ch, HDMI 2.1 (8K60, 4K120, VRR, ALLM, QMS), CEC, Zone B, no phono, no network, Bluetooth 5.3, listed "New" | /rx300a/index.html
- RX500A | 4/1 | eARC, ARC | 70 W 8 ohm | "Room Correction" | 7.2ch, Wi-Fi/Ethernet, AirPlay 2, no phono | /rx500a/index.html
- RX-V385 | 4/1 | ARC yes; eARC "via firmware update" | 70 W 8 ohm 2ch | YPAO | 5.1ch, 4K60, Bluetooth, no phono, no network | /rx-v385_u/index.html
- RX-V4A | 4/1 | eARC, ARC | 80 W 6 ohm | YPAO Volume, no multipoint | Wi-Fi, no phono, no Zone 2 | /rx-v4a/index.html
- RX-V6A | 7/1 | eARC, ARC | 100 W 8 ohm | YPAO multipoint | phono, Zone 2 preout, Wi-Fi | /rx-v6a/index.html
- RX-A2A | 7/1 | eARC | 100 W 8 ohm | YPAO with R.S.C. | phono, Zone 2, network | /rx-a2a/index.html
- RX-A4A | 7/3 | eARC | 110 W 8 ohm | YPAO R.S.C., 3D | HDMI 2.1, 8K, phono, Zone 2 | /rx-a4a/index.html
- RX-A6A | 7/3 | eARC | 150 W 8 ohm | YPAO full set | HDMI 2.1, 8K, phono, Zone 2 | /rx-a6a/index.html
- R-N303 | no HDMI listed | none | 100 W x2 (0.2% THD) | not listed | stereo network receiver, phono, DISCONTINUED | usa.yamaha.com/products/audio_visual/hifi_components/r-n303/index.html
- R-N602 | no HDMI listed | none | not listed | not listed | stereo network, MM phono, DISCONTINUED | .../hifi_components/r-n602/index.html
- Name trap: "RX300A" (no dash, 2020s AV receiver) is a different product from R-N303 (stereo) and from RX-V-series names. Always confirm the exact label.
- RX-A8A, R-N600A, R-N800A, R200A listed by name only. Specs UNVERIFIED.

### Denon (denon.com/en-us/product/...)
- AVR-S570BT | 4/1 eARC | ARC, eARC | 70 W 8 ohm | mic auto setup, Audyssey not listed | 5.2ch, Bluetooth, no phono, no multiroom | /av-receivers/avr-s570bt/300614.html
- AVR-X1800H | 6 (3 x 8K)/1 eARC | ARC, eARC | 80 W 8 ohm | Audyssey MultEQ XT | 7.2ch, MM phono, Zone 2, HEOS, no QMS | /av-receivers/avr-x1800h/300773.html
- AVR-X2800H | 6 (3 x 8K)/2 (1 eARC) | ARC, eARC | 95 W 8 ohm | MultEQ XT | phono, Zone 2, HEOS, AirPlay 2 | /av-receivers/avr-x2800h/300610.html
- AVR-X3800H | 6 (8K)/3 | ARC, eARC | 105 W 8 ohm | MultEQ XT32, Dirac paid | 9.4ch, phono, Zone 2 | /av-receivers/avr-x3800h/300609.html
- AVR-X4800H | 7 (8K)/3 | ARC, eARC | 125 W 8 ohm | MultEQ XT32, Dirac paid | 9.4ch, phono, 3 zones | /av-receivers/avr-x4800h/300608.html
- AVR-X2900H | 6 (3 x 8K)/2 (1 eARC) | ARC, eARC | 95 W 8 ohm | MultEQ XT, Dirac RC ready | 7.2ch, phono, tagged New | /x-series-av-receivers/avr-x2900h/301131.html
- Listed by name only: AVR-S980H, X3900H, S970H, S770H, S670H, S270BT. Specs UNVERIFIED. No model marked discontinued on the list page.

### Marantz (marantz.com/en-us/product/av-receivers/...)
- NR1510 | 5 back + 1 front / 1 eARC | ARC, eARC | 50 W (8 ohm not given) | Audyssey MultEQ | 5.2ch, 4K only, MM phono, no Zone 2, HEOS | /nr1510/137270.html
- Cinema 70s | 6 (3 x 8K)/1 eARC | ARC, eARC | 50 W 8 ohm | MultEQ | 7.2ch, phono, Zone 2, HEOS, "Out of Stock" | /cinema-70s/300619.html
- Cinema 70s Series 2 | 6 (3 x 8K)/1 | ARC, eARC | 50 W 8 ohm | MultEQ XT, Dirac ready | 7.2ch, phono | /cinema-70s-s2/301134.html
- Cinema 50 | 6/3 | ARC, eARC | 110 W 8 ohm | MultEQ XT32, Dirac ready | 9.4ch, phono, Zone 2 | /cinema-50/300616.html
- Cinema 40 | 7 (8K)/3 | ARC, eARC | 125 W 8 ohm | MultEQ XT32, Dirac ready | 9.4ch, phono, 3 zones | /cinema-40/300615.html
- Model 40n (stereo integrated; marantz.com/de-de/product/amplifiers/model40n) | 1 HDMI, eARC vs ARC conflict | 70 W 8 ohm, 100 W 4 ohm | n/a | MM phono, HEOS
- NR1200, NR1711, Stereo 70s: no page fetched. DROPPED.

### Sony (sony.ca product pages)
- STR-AN1000 | 8K, 7.2ch | eARC not listed | power not listed | D.C.A.C. IX | /en/audio/audio-components/receivers/p/stran1000. 2023 launch context: 6 HDMI, 2 with 8K/4K120. COMMUNITY (whathifi.com).
- STR-DH590 | 4/1 | not listed | not listed | not listed | 4K60 4:4:4, HDR, Bluetooth; page says "Item no longer available" | /p/strdh590
- STR-DH790 | 4/1 | not listed | not listed | not listed | 4K60 4:4:4; "Out Of Stock" | /p/strdh790
- STR-DH190 | no HDMI listed | none | not listed | not listed | stereo, phono, Bluetooth | /p/strdh190
- STR-AZ ES series: no official page read. Specs from whathifi.com only. COMMUNITY.
- Sony support page for DH590 shows "no downloads" and no discontinuation notice. VERIFIED (sony.ca).

### Onkyo (onkyo.com/receivers/...)
- TX-NR5100 | count not given | eARC (Main Out) | 80 W 8 ohm, 4 to 16 ohm | AccuEQ | 7.2ch, Wi-Fi, AirPlay 2, no phono listed | /tx-nr5100
- TX-NR6100 | 6 + Sub/Zone 2 out | eARC (Main) | 100 W 8 ohm | none named | MM phono, Zone 2, Wi-Fi | /tx-nr6100
- TX-RZ50 | 6 + front, Sub/Zone 2 out | eARC (Main) | 120 W 8 ohm | Dirac Live | MM phono, Zone 2 and 3 | /tx-rz50
- RZ30, RZ70, NR7100 listed by name only. Stock status UNVERIFIED (pages show Add to Cart and Notify Me).

### Pioneer and Pioneer Elite
- Status: Pioneer AV receivers are NOT dropped. The brand is still covered by a current warranty for "AV Receivers" (Pioneer 1 year, Elite 3 years), see section 8. No Pioneer model is listed on the Onkyo AV receiver list page, so whether any is still in production is UNVERIFIED.
- Model table (secondary sources only, no official Pioneer page loaded). Format: model | HDMI in/out | watts | room correction | notes | source.
- VSX-935 | 6/2 | 80 W 8 ohm | MCACC Auto | 7ch (5.2.2 Atmos), eARC, 8K60, VRR, ALLM; Jan 2022 launch | COMMUNITY (blog.bestbuy.ca 2022-01-19)
- Elite VSX-LX105 | 6/2 | 100 W 8 ohm | MCACC Auto | 7ch (5.2.2), eARC, RS-232C | COMMUNITY (bestbuy.ca blog)
- Elite VSX-LX305 | 6/2 | 100 W (blog: 8 ohm; Henley: standard not stated) | Advanced MCACC, Dirac Live (Henley) | 9.2ch (7.2.2 or 5.2.4), 8K60, 4K120, IMAX Enhanced, powered Zone 2 plus Zone B; price and warranty not listed | COMMUNITY (bestbuy.ca blog, henleyaudio.co.uk)
- Elite VSX-LX505 | 7/2 | 120 W 8 ohm, 0.08% THD | Dirac Live | 9.2ch (7.2.2 or 5.2.4; 7.2.4 with external amp), eARC, IMAX Enhanced | COMMUNITY (bestbuy.ca blog)
- Elite VSX-LX805 | audioholics: 6/2; adorama: 7/3, eARC on outputs (conflict, report both) | 150 W; audioholics: 2 channels driven, 0.08% THD | Dirac Live Premium plus MCACC; Bass Control paid ($349 one sub, $499 multi) | 11.2ch / 7.2.4, 8K60, 4K120, Dolby Atmos, DTS:X, IMAX Enhanced, Auro-3D via update; Zone 2 and 3 stereo RCA; launch price $2,999; Adorama: 3 year warranty, "no longer available" | COMMUNITY (audioholics.com news, adorama.com pivsxlx805)
- 2022 Elite pages did not state 4K120 except LX305 and LX805. Not stated means unknown, not "no".
- Older generations (VSX-534, 835, 933, LX302, SC-LX): VSX-835 name only (official warranty page caption). Specs UNVERIFIED.
- Current 2025 to 2026 models: none found. Search and the Onkyo list showed none. UNVERIFIED whether any exist.
- Names seen on official pages: VSX-835 (image caption) and VSX-LX505 (image file name) on onkyo.com/pioneer-home-usa-warranty. Names only; no specs read.
- Candidates NOT read: VSX-534, VSX-933, VSX-LX302, SC-LX lines, any 2025 to 2026 model. All UNVERIFIED.
- Seller listings can lag the brand; check the model page and stock before buying. LX805 is shown as unavailable at Adorama.
- Fetch blocked: pioneer-audiovisual.com (robots), intl and .eu pages (not permitted), pioneerelite.com (domain redirects to a GoDaddy for-sale page), pioneerhomeusa.com (redirects to the Onkyo warranty page). Fetch limit hit before retailer pages. Retry later.

## 8. Vendor facts
- Onkyo.com and the Pioneer home warranty page share the footer "Premium Audio Company, LLC, a wholly owned subsidiary of Gentex Corporation". VERIFIED (both pages).
- Pioneer Home Entertainment U.S.A. distributes Pioneer in the U.S. and Canada and issues the warranty; valid only from authorized dealers. New Pioneer AV receivers 1 year; Elite AV receivers 3 years; refurbished 1 year. VERIFIED (onkyo.com/pioneer-home-usa-warranty).
- Marantz NR1510 page states a 3 year warranty. VERIFIED (marantz.com). Other brands UNVERIFIED.
- Pioneer web presence (read 2026-10-23): pioneerhomeusa.com redirects to the Onkyo-hosted warranty page; pioneerelite.com redirects to a domain for-sale page. VERIFIED (redirect headers). Do not send readers to pioneerelite.com.
- Warranty applies in the country of purchase only; proof of purchase from an authorized U.S. or Canada dealer needed; original owner only; shorter periods may apply to some models. VERIFIED (onkyo.com/pioneer-home-usa-warranty). Warranty issuer named on the page as PHEU.
- Discontinued per brand page: Yamaha R-N303 and R-N602; Sony STR-DH590 "no longer available". No other model marked discontinued.

## Not verified
- Pioneer official spec pages, current price and stock, CEC name, older models before 2022; Marantz NR1200, NR1711, Stereo 70s; Sony AZ series official specs; Denon S-series beyond S570BT.
- RX300A: YPAO name, minimum impedance, mode list, EQ-off option, reset keys, firmware.
- Onkyo and Pioneer CEC names; Multi Stereo equivalents outside Sony.
- Reddit and AVS owner reports; failure patterns; warranty for most brands.

## Sources (fetched)
- usa.yamaha.com: RX300A, RX500A, RX-V385, RX-V4A, RX-V6A, RX-A2A, RX-A4A, RX-A6A, R-N303, R-N602, AV receivers, hifi components and speaker indexes, firmware index
- ca.yamaha.com/en/support/faq/audio_visual/gaa16771.html
- denon.com/en-us: AV receiver list, S570BT, X1800H, X2800H, X3800H, X4800H, X2900H
- marantz.com/en-us: list, NR1510, Cinema 70s, 70s S2, 50, 40; marantz.com/de-de Model 40n
- sony.ca: AV receivers list, STR-AN1000, DH590, DH790, DH190, DH590 downloads, support article 00173195
- Secondary Pioneer: blog.bestbuy.ca new-pioneer-receivers-2022; henleyaudio.co.uk VSX-LX305; audioholics.com news pioneer-vsx-lx805-avr; adorama.com pivsxlx805
- onkyo.com: AV receivers, onkyo.com/receivers/av-receivers, TX-NR5100, TX-NR6100, TX-RZ50, pioneer-home-usa-warranty (pioneerhomeusa.com and pioneerelite.com redirects read)
- Context only: whathifi.com Sony 2023 receivers news; speakerdecision.com RX300A
