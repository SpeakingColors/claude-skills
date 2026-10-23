---
name: hard-dance-production
description: Use when mixing, mastering or sound designing hardstyle, UK and happy hardcore, trance and rave: frequency plan, buses, master chain, build-ups, lead, bass, pluck and FX recipes with starting values.
---

# Hard dance production: mix, master and synth recipes

All numbers below are AI-written starting values (UNVERIFIED), not measurements. Test by ear and with meters, change one thing at a time, and level-match before judging. Never present a recipe as proven. Labels: VERIFIED (read on a source page), COMMUNITY, UNVERIFIED.

## How to use
1. Name the target: genre, role (lead, bass, pluck, riser, impact), tempo.
2. Pick the closest recipe, then translate it to the synth at hand (Serum, Vital, Surge XT, hardware). Parameter names differ; keep the intent (oscillator mix, filter cutoff and envelope amount, FX order).
3. Level-match each change against the previous version so louder never reads as better.
4. Check mono sum and aliasing.
5. Write down final values and what was heard.
6. Do not copy third-party presets or sample content. Recipes are ideas; sounds should be your own.

## Typical tempos
- Hardstyle roughly 135 to 160 BPM, modern often near 150. VERIFIED (Wikipedia: Hardstyle).
- Trance commonly 125 to 150 BPM. VERIFIED (Wikipedia: Trance music).
- English happy hardcore around 170 BPM. VERIFIED (Wikipedia: Happy hardcore). Wider UK hardcore range: UNVERIFIED.

## Frequency plan (UNVERIFIED)
- 20 to 150 Hz: kick and sub only. High-pass everything else near 180 to 220 Hz. Sub 100% mono.
- 200 to 500 Hz mud: narrow cut of 2 to 4 dB near 350 to 450 Hz on synth buses; high-pass reverb returns near 250 Hz.
- 2 to 5 kHz harshness: dynamic EQ or de-esser near 3.2 kHz so it only dips when a lead screams. Saturation before the filter smooths peaks.
- 8 kHz and up: high-pass the noise layer, add air, pan delays wide.
- Hardstyle kick EQ start: +3 dB narrow at 45 Hz, -6 dB wide at 350 Hz, +4 dB at 2.2 kHz.

## Buses (UNVERIFIED)
- Drums: VCA-style compressor, attack 30 ms, release auto or 100 ms, 2 to 3 dB reduction. Parallel smash: very high ratio, about 10 dB reduction, blended about 15 dB under the clean bus.
- Bass: split at 120 Hz, linear phase. Low band mono with fast flat compression and full duck from the kick (attack 0, release 80 to 120 ms). High band gets chorus, wideners, distortion, and a 3 to 4 dB dynamic dip near 250 Hz keyed by the kick.
- Synths: dynamic EQ at 400 Hz and 3.2 kHz; chords sidechained to the kick; leads wide above 8 kHz.
- Pads: sidechain a high-pass moving 150 to 400 Hz on each kick instead of volume ducking.
- Vocal pocket: dip the lead mid 2 to 3 dB at 2 kHz. Reverb on an aux, then a compressor keyed by the dry vocal (attack 2 to 5 ms, release 150 to 250 ms, 3:1 to 4:1, 4 to 6 dB).
- Reverb and delay returns: high-pass the side channel near 350 Hz.

## Layering and phase
- Lock centre oscillators to phase 0 (retrigger). Flip polarity on a side layer if it thickens in mono. Use linear-phase EQ when splitting one sound into layers.
- Three-layer stack: sub anchor (sine or triangle, mono, below 120 Hz); mid body (2-voice saw or square, 120 Hz to 3.5 kHz, narrow); high shimmer (9 to 16 voice saw, high-passed at 3.5 kHz, width about 130%).

## Master chain order (starting point, UNVERIFIED)
Linear-phase EQ (high-pass 20 Hz, narrow cut near 350 Hz) > spectral resonance suppression > multiband imager (mono below about 120 Hz) > M/S multiband saturation (mid clean 10 to 15%, side 40 to 60% above about 3 kHz) > multiband compressor > soft clipper (+2 to +4 dB) > true-peak limiter (ceiling -1.0 dBTP).
- Glue crossovers 100 Hz, 2.5 kHz, 8 kHz, linear phase, at most 1 to 1.5 dB reduction per band. Low: attack 15 ms, release 80 ms, 2:1. Mid: attack 35 to 50 ms, release 150 ms or auto, about 1.7:1. High-mid: attack 8 ms, 2:1.
- Transient and sustain split: transient path clean, sustain path clipped and limited; blend transients in at -12 to -8 dB.
- Loudness: club about -6 to -8 LUFS integrated (hardstyle -6.5 to -7.5 with healthy crest factor), streaming about -14. Ceiling -1.0 dBTP.
- Stereo correlation target for a rave track: +0.2 to +0.7. Check mono loss.

## Arrangement and build-up
- Pre-drop bar: roll and uplifter, stutter, bass cut, reverse reverb, silence, one shout. Mute reverb and delay returns in the gap so tails do not soften the kick.
- Sub inversion trick: on bar 4 beat 4 mute everything below 120 Hz, then snap back on the downbeat.
- Width: squeeze 100 to 70% over bars 1 to 3, hold in the gap, snap to 130 to 135% at the drop; always mono below 120 Hz.
- One-knob build-up macro idea: 0 to 100% drives high-pass 150 Hz to 2.5 kHz, reverb and delay mix 15% to 65%, drum clipper drive up to about +5 dB, gain down to about -2.5 dB; snap to 0 at the drop.

## Synth recipes (starting values, UNVERIFIED)
**Leads**
- Hands-up hyper-saw: saw 8 voices detune 22%, random phase 100%, plus square 2 voices +12 st, sine sub 20%; low-pass 12 dB cutoff 35%; filter envelope decay 420 ms, sustain 30%, amount +55%; OTT-style compression 40%; chorus 0.2 Hz 12 ms; high-pass 220 Hz.
- Trance mainliner: saw 9 voices detune 28% plus saw 9 voices +12 st hard L/R plus square sub 20%; dotted 1/8 ping-pong; hall mix 35%, 4 s.
- Rawstyle screamer: mono square, sync ratio about 1.45, phase retrigger, plus saw 7 voices +12 st; comb filter or static phaser with resonance 80% swept to the "yelling" spot; compression 50% then distortion or wavefolder +6 dB; high-pass 250 Hz.
- Organ-style lead: square 7 voices detune 10% plus sine +31 st with FM 35%; compression 45% plus overdrive; high-pass 250 Hz.

**Basses**
- Kick sub ("tok"): mono sine, pitch envelope decay 80 ms, +12 st; distortion 80%; cut above 180 Hz.
- Rumble tail: mono sine two octaves down; asymmetric waveshaper for even harmonics; linear-phase low-pass near 90 Hz.
- Sidechain distortion: distort only the band above 120 to 150 Hz, never the sub; envelope follower on the kick, attack 0, release 45 to 60 ms.

**Plucks and stabs**
- Dream-trance pluck: triangle plus narrow pulse 20% +12 st; low-pass 25%; envelope decay 320 ms, amount +50%; stereo delay 1/4 feedback 45%; hall 4.5 s, high-passed.
- Anchor oscillator for stabs: single-voice saw or square with phase retrigger 0%, so the transient is the same every note while wide unison swims around it.

**FX**
- Risers: pitch-scream uplifter, laser roll, Shepherd tone, sub-suck sweep, stereo noise uplifter.
- Downlifters and impacts: noise-wash downlifter; sub-drop impact (sine, pitch envelope +24 st, low-pass 100 Hz); glass-shrapnel impact.

**Chords (A minor examples)**
- Trance and hard house: Am F G Em. Uplifting trance: F G Am C. Hardstyle, UK hardcore: Am Em F C Dm G. Progressive: Am Dm G F.
- Voicings: eurodance minor 9th (A3 bass, A4 C5 E5 G5); future bass minor 11th (A4 C5 D5 F5 A5); melodic techno sus2 (D3, D4 E4 A4).

## Rules that always apply
- Avoid digital harshness: oversample distortion, exciters and wavefolders; check with a spectrum view.
- Sub 100% mono below about 120 to 130 Hz. Phase retrigger centre layers; start-phase randomisation 40 to 60% keeps wide leads mono safe.
- Keep raw synth peaks around -18 dBFS before analog-modelled stages.
- After any drive stage that loses gain, level-match by RMS.
- Know your synth's gaps (comb filter, formant filter, bitcrusher, wavetables, arp) before promising a sound; offer the closest approximation.

## Fact-check flags
- A source saying "low-pass at 20 Hz" meant a high-pass at 20 Hz.
- Mid high-pass 150 Hz plus Side high-pass 250 Hz leaves no bass on a master; it is valid only on a synth bus. For mono bass, high-pass the Side only.
- A Haas delay of 14 to 18 ms on one side comb-filters in mono; check correlation first.
- Loudness gain claims (for example a soft clipper adding "up to 3 dB") are unmeasured.
- Unison curve names ("Exponential", "Super") are synth-specific and not verified.
- Commercial limiter internals are not public; use the idea, not the claim.

## Process
1. Reference a commercial track in the same genre at matched loudness.
2. Change one thing at a time; level-match.
3. Measure with a spectrum, LUFS and correlation meter; do not trust numbers alone.
4. Write down what worked.
