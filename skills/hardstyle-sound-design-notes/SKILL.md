---
name: hardstyle-sound-design-notes
description: Use for hardstyle, rawstyle, hard techno, hardcore, rave and trance sound design: kick layers, pitch envelope, staged distortion, reverse bass, screeches, hoovers, stabs, arrangement, tempos.
---

# Hard dance sound design notes (from tutorials, not from a lab)

Companion to `hard-dance-production`, `hard-dance-synth-recipes`, `plugin-dsp-quality`. Labels: AGREED (several independent tutorials), SINGLE (one source), OPINION. Research date: November 2026; sources were tutorials and vendor blogs, and exact numbers conflict between them, so start from these and tune by ear and by measurement.

## Kick (hardstyle, rawstyle, hard techno)
- AGREED: layers (punch or click, tuned sub and tail, optional reversed tail) bussed, then compressed and driven further. Pitch envelope: fast sweep from a high start (about 200 to 500 Hz) down to the fundamental; click part 10 to 50 ms, longer tail sweeps 200 to 400 ms also quoted. The exact milliseconds conflict (3 to 30 ms in some sources).
- AGREED: EQ before distortion; distort in stages instead of one big smash; clip for loudness instead of compressor pumping.
- Tune the tail to the track's root (or fifth); typical first octave E, F or G with the tail root about 45 to 65 Hz; mono below about 120 Hz; cut 180 to 260 Hz if boxy.
- Gabber and frenchcore: sine with fast pitch drop, hard clip toward a square wave, sustained sub body; short tails at high tempo (180 bpm is 333 ms per beat).
- For our own kick engine: offline render at 4x or 8x the sample rate before the distortion stages, then downsample; check alias energy with a sine test (see `plugin-dsp-quality`).

## Bass and sidechain
- Reverse bass: low pass the distorted bass at about 200 to 400 Hz so harmonics do not mask the kick; sidechain to the kick with fast attack and release about 80 to 120 ms; mono below about 150 Hz; design kick and bass as one unit. SINGLE or two sources.
- Compressor sidechain follows the real kick; a volume shaper gives identical beat precise ducking. Release is the key control. AGREED.
- Rolling bass: sidechain for separation, or trigger the ducking from a copy of the kick delayed by a sixteenth. SINGLE.

## Leads
- Screech: square or saw down octaves, formant mode, scream type filter with high resonance, LFO on oscillator intensity. SINGLE x2. High pass leads so they do not fight the kick mids.
- Euphoric and trance supersaw: 5 to 7 detuned saws, layered per octave, a high passed noise layer for air. Trance: one key (A or D minor typical), shelve reverb returns below about 150 Hz. 128 to 145 bpm.

## Rave and hardcore
- Hoovers: layer two or three in different bands (weight, mid, sizzle), slight pan, glide for riffs, short release for stabs.
- Stabs: classic is a static open filter, modern moves the filter per note; attack 1 to 5 ms; fast riffs across two octaves; offbeat with heavy delay and reverb.
- Happy hardcore about 160 to 175 bpm (median about 170).

## Arrangement for DJs
- Intro 16 to 32 bars at about half energy (drums first), build 8 to 16, drop, breakdown, build, drop, outro mirroring the intro. Risers pair with a snare roll and a filter sweep. Impact and sweep placement: no source found.

## Tempo by style (single guides, approximate)
Euphoric 150 to 155 (others quote 145 to 150); rawstyle 150 to 155; xtra raw 155 to 160; uptempo and frenchcore about 190 to 250 (sources disagree where terrorcore starts); trance 128 to 145; happy hardcore 160 to 175.

## Opinions and marketing (do not treat as rules)
Rawstyle bass louder than the punch; gradually raising the tail pitch as a signature; 5 to 15 percent drum bus drive on the kick; specific plugin chains. Whether gated reverb belongs in trance is disputed.

## Vengeance style polish
No independent information on how Vengeance packs are made was found. Inference only, UNVERIFIED: pre processed, key labelled, loudness matched, phase checked one shots and ready made kick and bass pairs. Do not repeat this as fact.

## Ideas for our tools (from the gaps)
Three layer kick builder with tail to key snap; staged distortion chain with a mud cut; reverse bass mode with kick linked sidechain; compressor vs volume shaper curve switch; screech module; supersaw presets with a band split reverb low shelf at 150 Hz; hoover and stab module; mono below X crossover; riser and sweep generator; tempo and key preset sets per genre.
