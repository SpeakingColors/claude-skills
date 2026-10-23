---
name: plugin-dsp-quality
description: Use when a synth or effect plugin must sound smooth, clean and loud without harshness: aliasing audits, oversampling and ADAA, level-matched drive, output stages, responsiveness, synth design lessons.
---

# Plugin DSP quality: smooth sound, no harshness, no lag

Companion to `vst-maker` (rules) and `juce-expert` (JUCE code). This skill holds hard-won lessons from building and measuring synth and effect plugins. Numbers are from small offline test harnesses on hand-copied maths, not from compiled plugins, so treat them as strong leads and re-measure your own code.

Labels: VERIFIED (read on a source page), MEASURED (our own harness result, re-check on your build), COMMUNITY, UNVERIFIED.

## 1. Harshness is mostly aliasing
- Any non-linear stage (distortion, fuzz, exciter, wavefolder, hard clip, rectifier, saturator, even a "small" one) creates harmonics. Above half the sample rate they fold back as inharmonic noise, the "digital" sound. VERIFIED (Vicanek, "Anti-aliasing for tanh and soft clippers", vicanek.de/articles/AADistortion.pdf).
- Oversampling alone gains about 6 dB per doubling on a hard-driven spectrum. VERIFIED (same). ADAA (antiderivative anti-aliasing) plus 4x oversampling makes aliasing practically negligible. VERIFIED (same).
- ADAA form: `y = (F(x[n]) - F(x[n-1])) / (x[n] - x[n-1])` with F the antiderivative of the shaper. It adds half a sample of latency and a gentle low-pass, and needs a fallback when two samples are nearly equal. VERIFIED (same).
- A cheap tanh-like shaper: `x / sqrt(1 + x*x)`. VERIFIED (same).
- Oversampling does NOT fix a slope kink at zero (rectifiers, diodes, asymmetric shapers with an abs). Those plateau near -50 dB alias level even at 4x and 8x. Smooth the zero crossing or use ADAA. MEASURED.
- Oversample every non-linear stage, including side stages such as exciters and fuzz after a high-pass. In one audit the worst alias numbers (about -18 dB at 9 to 12 kHz) came from an un-oversampled exciter; 2x oversampling plus ADAA brought it to about -75 to -80 dB. MEASURED.
- Hot settings matter: stages that are fine at normal level can alias only when pushed. Test at the maximum knob positions.
- Applying ADAA everywhere low-passes the signal (about -2.4 dB at 10 kHz at 44.1 kHz in one test), so it is not transparent without compensation. Switching it on only when clipping makes a step. MEASURED, compensation filters not built.

## 2. How to run an aliasing audit (simple, repeatable)
1. Feed a pure sine (try 1, 3, 9 and 12 kHz, amplitudes 0.3 and 0.5, drive at 30%, 75% and 100%).
2. Apply the stage, take an FFT of a whole number of cycles.
3. Sum the energy NOT on a harmonic of the input. That is alias energy. Report it in dB below total power.
4. Repeat with oversampling off, 2x, 4x, 8x. Keep a table in the repo.
5. Re-run after every DSP change. The final proof needs the real compiled code (and the real JUCE oversampler) in CI, not hand-copied maths.
- Harness trap: do not divide RMS by a fixed sample count when sample rates differ; use the real length, or 96 kHz looks 3 dB louder.
- Mix-level de-harsh tips (gain staging, dynamic EQ, de-essing, tape saturation) are a separate topic from code-level aliasing; do not mix them up.

## 3. Oscillators and supersaws
- Naive saw and square alias. Use PolyBLEP-family correction, differentiated polynomial waveforms or band-limited wavetables per octave, then measure. See `vst-maker` section 6.
- Tutorials' basic table oscillators are not band-limited (JUCE dsp::Oscillator is a plain table; VERIFIED in the JUCE DSP tutorial). Do not ship a supersaw on it.
- Sub oscillator: lock its phase to oscillator A (flip on each A wrap) and follow A's pitch modulation. A free-running sub drifts against A and sounds odd in the blend. With hard sync it free-runs. COMMUNITY (project experience).
- Thickness: layering, unison, detune and a sub. Tiny slow pitch drift (about 0.1 to 1%) stops a sound sounding static; 1% is about 17 cents, which is clearly audible, so prefer the low end and judge by measurement and ear. 0.1% is about 1.7 cents. UNVERIFIED as taste.
- Smoothness often comes from the filter: ladder-style behaviour and saturation inside the feedback loop. Study, then measure; do not copy another product's code or presets.
- Filter input stage idea: `tanh(x*g)/g` with `g = 0.5 + 3*drive` gives unity small-signal gain and gentler curvature at zero drive. MEASURED in one engine.
- Oversample the filter drive and the hard distortion stage; that is where hard distortion lives.

## 4. Output stage: master is not drive
- If the master gain feeds a `tanh`, master becomes both volume and drive and presets sit in constant saturation (peaks pinned, RMS far too high). Use: clean linear gain, then a slow peak limiter, then a smooth-knee clipper that is idle at normal level.
- Smooth knee example: identity below knee T (default 0.72); above it `T + w*tanh((|x|-T)/w)` with `w = 1 - T`; C2-continuous at the knee and never exceeds 1. MEASURED. When hard-driven it is not clearly better than tanh, because clipping is clipping; the limiter's job is to keep the clipper nearly idle.
- Separate goals: a limiter keeps level in range; a distortion curve changes the sound. Thresholds below about 0.5 on some threshold-curve shapers cause an expansion effect. COMMUNITY (KVR thread).
- Level presets so a single held note peaks near 0.6 before the clipper, and test four notes at master 2 for bounded, NaN-free output.
- Any EQ boost needs a safety limiter in the real plugin. Auto-level or loudness-follow needs a peak ceiling (about -0.3 dBFS used).

## 5. Level-matched drive (louder is not better)
- A static per-stage RMS match using one test sine is not enough: bass-heavy material came out 1.5 to 2.3 dB quieter at full drive while kick, lead and mix were fine. MEASURED.
- Fix: closed-loop RMS gain around the whole drive section. Measure mean-square in and out with a slow one-pole (about 250 ms); makeup `= sqrt(in/out)` clamped 0.5 to 2.5; glide about 100 ms; exactly 1.0 and bit-exact when every drive knob is 0. Time constants from 60 to 500 ms changed the result by under 0.1 dB. MEASURED.
- Test with bass-heavy, drums, lead and full-mix sources, each knob at 25, 50, 75 and 100%, compare output RMS with INPUT RMS (tolerance 0.5 dB), no NaN. If you also have a web or script prototype, it must use the same loop as the C++.

## 6. Responsiveness: no lag between knob and sound
- A knob change must reach the audio within one buffer.
- Smoothing time 5 to 20 ms (`juce::SmoothedValue`); never over 20 ms for level, mix or drive. Reading parameters once per block with no smoothing risks zipper noise.
- No locks, waits or allocations on the audio thread.
- Report exact latency with `setLatencySamples` and update it when a latency setting changes. Add latency only where sound quality needs it (STFT effects, limiter lookahead, oversampling) and document it in the manual.
- Write a test per plugin that measures knob-to-sound time.
- A test page that renders a loop offline and swaps it in will lag 0.3 to 0.8 s; a live audio-worklet engine fixes that. That lag is a page limit, not a plugin issue.

## 7. Reverb and effect taste notes (UNVERIFIED, test by ear)
- Long dark reverb on a lead, with the tail high-passed near 290 Hz and 20 to 25% mix, is a common hard-dance lead treatment (taken from analysing a few third-party reverb presets; the parameters were: mix 23%, pre-delay about 200 ms, time about 8.5 s, high-cut about 5 kHz).
- A lowpass left wide open sounds bright or harsh; around 12 kHz is a lead starting point. A starting value, not a rule.

## 8. Analysers and measurement tools
- An analyser that feeds a match EQ must tap BEFORE the EQ, or the EQ feeds back into the measurement.
- Loudness meters: BS.1770 momentary, short-term and integrated LUFS; a stereo -23 dBFS sine should read about -23.0 LUFS (sanity check). COMMUNITY.
- Masking finder idea: 1/3-octave bands where two signals are both above -70 dBFS and within 3, 6 or 10 dB; smooth the result; rule of thumb only.
- A default spectrum slope of 4.5 dB/octave around a 1 kHz pivot matches a well-known EQ's default tilt. COMMUNITY (vendor help page).
- Drawing helpers: set colour and line width inside each loop pass (a helper that drew arrow glyphs left a dark stroke on the next line). Draw dB ranges with headroom (0 to -100 rather than clipping the top).

## 9. Prototype fast, then port
- A browser lab (Web Audio) is a quick way to let the owner listen and A/B before installing. Keep the DSP in a small portable core with shared constants so the lab and the C++ plugin match, and write a test that compares their output levels.

## 10. Limiters, ceilings and loudness (measured and read in source)
- `juce::dsp::Limiter` is not a ceiling limiter. Its header says "two compressors and a hard clipper at 0 dB". The threshold is set only on the second compressor; the output gain then includes `dB2gain(-threshold)` plus a fixed makeup of about 3.7 dB (VERIFIED, JUCE source juce_Limiter.cpp and .h, read 2026-10-23). The shown code has no lookahead and reports no latency. So lowering the "ceiling" makes the output LOUDER and then hard-clips at 0 dB. In a lab test on a full mix, a -6 dB setting clipped about 14% of samples, and the peak always landed at 0 dBFS (MEASURED, on a lab port of the same maths).
- If you need a true ceiling, write a lookahead brick-wall limiter: about 1.5 ms lookahead, boxcar-smoothed attack, one-pole release (about 80 ms worked), and delay the dry path by the lookahead. At 44.1 kHz that is about 66 samples of latency; report it with `setLatencySamples`. Output must never exceed the ceiling (tested exact at -0.3, -3, -6 and -12 dB). It is sample-peak only; true-peak needs a 4x check. MEASURED.
- Use JUCE's limiter only as a safety net, not as a mastering ceiling.
- A maximizer did not get louder at equal peak until a light peak clipper was added. Shipped chain without clipper: about 0 LU gain; with a clipper and push: about +4 to +8 LU, crest falling to 3 to 4 dB. The clipper delivers loudness. MEASURED. Put the clipper before the limiter (post position recommended), smooth knee, oversampled.
- Squeeze or upward-compression styles can lose 7 to 17 dB LUFS without makeup (band gain reduction averaging about -20 dB). Fix: closed-loop slow RMS follower (about 250 ms power window, attack 50 ms, release 400 ms) before clip and limiter, target = input RMS plus a few dB, upward-only gain. Sparse bass-heavy material still ends up near -1 LU at equal peak because the kick is already near full scale. MEASURED.
- A fixed "contour" low shelf (for example 70 Hz) also lifts DC and infrasound; contour 8 raised DC about 4x. Add an always-on 20 Hz high-pass. MEASURED.
- An "air" control that is a tanh of a high-passed band mixed at about 12% is barely audible. A smooth high shelf (about 9 kHz, up to +4.5 dB) plus an oversampled exciter reads better. Judge by ear. COMMUNITY.
- An unclamped "process" or high-band lift can add up to +70 dB of gain when the mids are quiet; clamp it and check for noise pumping.
- Nasty ranges (drive to 300%, push to 36 dB) need 4x or 8x oversampling; at 2x one fuzz setting measured about -13 dB alias at 8 kHz. Offer an HQ switch if CPU is a worry. MEASURED.
- When 0% and 100% mix should read the same dB, report loudness (LUFS, K-weighted, ungated is fine for a lab) and "LU gained at equal peak" so makeup is not mistaken for quality.

## 11. Other effect lessons
- Spectral (STFT) sidechain ducker: amount 0 must reconstruct the input bit-exactly (tested about -150 dB). Blending a broadband pump with the spectral carve gives audible attack and release. A coloured sidechain widens the cut (about -3 LU), so level-match with a closed-loop RMS gain and test a "colour only what was not ducked" mode.
- Bipolar dynamics knob (negative evens out, positive expands) with exactly 0 = off is clearer than a ratio knob. Document the harmonic-versus-level slope you measure.
- Reverb size maps to decay time nonlinearly; measure it with an impulse (one engine: size 0.2 gave 0.7 s, 0.6 gave 1.4 s, 0.8 gave 2.2 s, 1.0 gave 6.4 s). Do not promise long tails (8 s) until you measure them. MEASURED.
- Reverb reference settings read off a commercial plugin's screen (decay 2.41 s, damping at 3.5 kHz with strong high shelf cut, bass multiplier 1.25x at 700 Hz, mod 1 Hz at 38%, early diffusion 96%, late 100%, high cut 7.5 kHz, pre-delay 10 ms) are a design target, not a clone. What the controls mean exactly is UNVERIFIED until you read the vendor manual.
- Dynamic EQ with per-band saturation: oversample the saturation, and keep the detector separate from the audio path.
- Every effect in a chain that can lose level needs a level check on at least four material types (see section 5).

## Not verified / next reading
- Parker, Esqueda, Bilbao (DAFx 2016) on continuous-time convolution, Esqueda et al. (2017), Chowdhury's ADAA notebook: found by search, not read here. Zavalishin, "The Art of VA Filter Design": cited in `vst-maker`, not re-read here.
- Real compiled-plugin alias measurements and the JUCE oversampler's exact response: UNVERIFIED, measure in CI.
