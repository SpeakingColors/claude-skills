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

## Not verified / next reading
- Parker, Esqueda, Bilbao (DAFx 2016) on continuous-time convolution, Esqueda et al. (2017), Chowdhury's ADAA notebook: found by search, not read here. Zavalishin, "The Art of VA Filter Design": cited in `vst-maker`, not re-read here.
- Real compiled-plugin alias measurements and the JUCE oversampler's exact response: UNVERIFIED, measure in CI.
