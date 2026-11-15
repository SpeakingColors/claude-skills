---
name: loudness-and-lowend-delivery
description: Use when mastering or checking hard dance for streaming and club: LUFS and true peak targets, clipper and limiter chain, mono bass, kick and bass phase, room acoustics basics, DJ mixing basics.
---

# Loudness, low end and delivery for hard dance

Companion to `hard-dance-production`, `sound-engineer-acoustics`, `dj-specialist`, `dj-gig-guide`. Labels: COMMUNITY (blogs, vendor guides, single source), UNVERIFIED (not found by research or only background knowledge). Research date: November 2026. Platform rules change: check the platform's own page before you rely on a number.

## Loudness targets
- Spotify: about -14 LUFS integrated, true peak at or below -1 dBTP (some guides say -2 dBTP if louder than -14). COMMUNITY. Apple Music is usually quoted at about -16 LUFS but one 2026 review found no published target: UNVERIFIED. YouTube sources conflict (-12, -13, -14): UNVERIFIED. An old -15 LUFS figure for Deezer is outdated. COMMUNITY.
- True peak at or below -1 dBTP guards against lossy codec overshoot. COMMUNITY.
- Platforms turn loud tracks DOWN and do not penalise them. Background knowledge, UNVERIFIED.
- Club and DJ delivery: WAV, 24 bit (or 16 bit), 44.1 or 48 kHz, no normalisation, and a separate streaming safe version. UNVERIFIED.
- Hard dance loudness: about -6 LUFS short term in the loudest section is treated as club loud and louder usually adds distortion (COMMUNITY); -8 to -6 integrated is quoted for aggressive styles from a non hardstyle guide (low quality). No hardstyle mastering engineer figures were found. LRA: no source.

## Chain
- Typical: compressor, then clipper, then true peak limiter last. A hard clipper around -1 dB ahead of the limiter is cited as a route toward about -7 LUFS and warns about harsh transients if overdone. COMMUNITY.
- If the final limiter works more than about 1 dB, back off the earlier stages. COMMUNITY (low).
- Distortion on every kick hit usually means the kick body overloads the limiter; cymbals and sibilance distort first. COMMUNITY. Real practice (clip the kick separately, parallel saturation, multiple clipper stages) is UNVERIFIED.
- Dither once, at the final bit depth reduction. Export 24 bit masters. UNVERIFIED.

## Low end, stereo, phase
- Keep the sub mono; crossover advice runs 80 to 120 Hz, 100 Hz is the conservative choice. Large clubs use distributed sub arrays so stereo content below 120 Hz cancels. COMMUNITY.
- Mono check: if the sub vanishes or turns hollow, or the correlation meter goes below 0, you have a phase problem. Keep the true sub clean below 80 to 100 Hz and distort the mid bass layer from about 120 Hz up. COMMUNITY.
- Kick and bass not tuned to each other cause a vanishing low end. COMMUNITY.
- Multiband compression on the master is a last resort; pumping, kick and bass modulation and crossover phase smear are the pitfalls (UNVERIFIED); linear phase costs latency.
- Not found: EQ moves per instrument, M/S detail, K weighting, reference level matching, headphone correction, sub integration.

## Room and monitoring (small studio)
- Treatment order: corner bass traps, first reflection points (mirror trick), rear wall. Axial mode `f = c / (2L)`; the Schroeder frequency is about 100 to 300 Hz in small rooms. Speakers 2 to 3 feet from the rear wall. RT60 about 0.3 to 0.4 s, one source says balance matters more than the number. COMMUNITY.
- Measure with REW and a calibrated mic (UMIK-1 class), treat, measure again. Room correction cannot fix strong modes. COMMUNITY.
- A bass that vanishes on club systems usually points to phase and low end alignment. COMMUNITY.

## DJing basics
- Mix on phrase boundaries; EQ mix (cut the incoming bass, swap lows, one band at a time); a bass swap does not fix a key clash (harmonic mixing, Camelot wheel); set gain before EQ because overlapping tracks sum louder; a master limiter catches peaks but must not hide bad gain staging. COMMUNITY.
- Loud masters leave no headroom: trim about 3 to 6 dB down. UNVERIFIED. Hearing safety limits were not found: keep monitoring low and use ear protection.

## Tools our plugins could provide
Loudness meter (short term, integrated, LRA, true peak) with streaming and club presets; streaming translation preview (gain change and codec overshoot); low end mono checker with correlation and mono collapse delta; clipper plus limiter chain with a gain reduction budget warning; kick and bass alignment assistant; level matched A/B reference; REW import for room checks; club translation simulator; DJ export checker (true peak, headroom, intro and outro length, bpm and key tags, bit depth).
