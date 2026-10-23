---
name: fx-plugin-design
description: Use when designing effect plugins: multiband compressors, EQs with dynamics and saturation, exciters, reverbs, spectral ducking, analysers, with UI, preset and test patterns.
---

# FX plugin design: feature sets and patterns

Companion to `vst-maker`, `plugin-dsp-quality` and `plugin-ship-checklist`. Study products for feature ideas only; never copy code, presets, names, layout or look. Labels: VERIFIED, MEASURED, COMMUNITY, UNVERIFIED.

## 1. Multiband compressor feature set (what users expect)
From one vendor's page (COMMUNITY): 1 to 4 bands; crossover slopes 6 to 96 dB/oct; per band a compressor (hard or soft knee, auto gain, auto release) plus a limiter; master limiter on the sum; a Mix knob for parallel compression; a dynamic pattern compressor; anti-distortion filters for very short releases; per-band scopes and an FFT overlay of input versus output.
- Dance-music style default: low band off or gentle, dry/wet about 50%. Starting values only.
- Nobody publishes exact producer settings; any "famous artist's multiband settings" claim is a guess. What is checkable is the tools they say they use. COMMUNITY.

## 2. Console and tube EQ idea sets (COMMUNITY)
- Pultec EQP-1A style: low shelf choices 20, 30, 60, 100 Hz with separate Boost and Atten knobs (0 to 10); high boost at 3, 5, 8, 10, 12, 16 kHz with bandwidth; high atten shelf at 5, 10, 20 kHz. Boosting and cutting at the same frequency gives a bump with a dip just above it: fuller bass, less mud. One preset idea: 60 Hz, boost about 7, atten about 4, by ear.
- Neve 1073 style: high shelf 12 kHz ±16 dB; mid peak 0.36, 0.7, 1.6, 3.2, 4.8, 7.2 kHz ±18 dB fixed Q; low shelf 35, 60, 110, 220 Hz ±16 dB; high-pass 50, 80, 160, 300 Hz at 18 dB/oct; add soft transformer-style saturation with a Drive knob.
- BBE-style phase/dynamic enhancer: three bands, the low band delayed about 2.5 ms, the mid about 0.5 ms, the high undelayed and dynamically processed; Lo Contour rebalances bass; Definition sets the high-band processing. Different from Aphex-style exciters that create new harmonics from a high-passed sidechain (can add hiss or sibilance). Offer both as "Maximize" and "Excite".
- All numbers above come from vendor or review pages; confirm against the manual before claiming a model is faithful.

## 3. Psychoacoustic bass
- Original design, not any vendor's code: generate harmonics from the low band so small speakers imply bass. Provide a frequency display with original bass and generated harmonics, three faders and an Audio / Harmonics / Original monitor switch.
- Add a Drive control, a bipolar dynamics knob (negative evens out, positive expands, 0 exactly off) and wide harmonic level ranges (about -36 to +18 dB); retune presets after changing a range.

## 4. Exciters and saturation
- Stages: input gain, optional oversampled saturator (several characters: soft, tape, tube, transistor, fuzz), tone filter, mix, level-matched output. See `plugin-dsp-quality` sections 1, 5 and 10 for aliasing and loudness rules.
- Drive characters as a mixable chain (six 0 to 100 knobs in series, level-matched) are easier to dial than one type menu. Test with an LA-2A-style opto and a hidden soft clipper before the limiter for loudness.
- A "stereo turbo" (right channel delayed up to about 12 ms after mix and output) gives width; show the mono-sum comb (first notch at `1/(2*tau)`), L/R correlation and the mono-versus-stereo level; mono compatibility is the cost. MEASURED in a lab model.

## 5. Spectral ducker (sidechain by frequency)
- 64-band STFT ducker: cut only where the sidechain has energy; amount 0 is a bit-exact bypass; blend with a broadband pump for audibility; show what the ducking removes from the original (pink = removed, band colour = remaining). Our own guess at how commercial "spacer" tools behave; internals unverified.
- Latency choice (STFT 6 to 43 ms) must be reported to the host and documented.
- Crossover display: draw level per band in that band's frequency range, crossover lines with arrows that reset on double click, value chips for the frequencies.

## 6. Reverb
- Design targets: smooth (late diffusion near 100%), slow modulation (about 1 Hz), high-pass on the return (about 250 to 400 Hz), low-pass on the tail, pre-delay, damping split (high frequency and bass multiplier), size to decay nonlinear and measured.
- Shimmer: two voices each with own pitch and amount, LP/HP on the wet, "warm" option, vowel/formant colouring of the tail, tempo-synced pre-delay.
- Ducked reverb: attenuate the wet with the dry signal's envelope so tails come back between notes.
- Check that reverb and delay returns can be muted in a pre-drop gap.

## 7. Analysers and meters (UI patterns that worked)
- Spectrum: fft 16384 or more, interpolate in dB between bins at low frequencies, power-average many bins per pixel at high frequencies, fast attack and slow fall per pixel, 3-point smoothing, quadratic curve through midpoints. Show peak labels (dB, Hz, note) and a hover readout; 1/3-octave band option; waterfall; peak hold with reset.
- Scope: sync modes (free, trigger, frequency, pitch by autocorrelation, beat, transient); freeze.
- Stereo field: goniometer with persistence, correlation meter (-1 antiphase, 0 stereo, +1 mono), width, balance, mono loss, verdict text (mono safe, check mono, phase problem; thresholds are rules of thumb).
- Meters: always dB numbers and ticks; stereo meters with warning colour from about -12 dB and clip colour near 0 dB with a latched clip cap; modes Peak, RMS, Peak+RMS, LUFS (momentary, short-term, integrated; BS.1770; -23 dBFS stereo sine reads -23.0 LUFS).
- Shape matching: capture reference and own shapes (60 bands at 1/6 octave from 20 Hz; keep Mid and Side apart), EQ curve = (reference minus own, each normalised to its average), smoothed, times Strength, limited to a max move; auto-level needs a peak ceiling and any EQ boost needs a safety limiter. Analysers tap before the matching EQ.
- A Panic button (stop test signal, cancel capture, reset peaks) and a Cancel next to long captures prevent confused users.
- Reference tools: do not display a "highest peak" without saying which channel mode.
- Cross-track masking finder: 1/3-octave bands where two signals are both above -70 dBFS and within 3, 6 or 10 dB; better with Bark or ERB bands and loudness-aware rules. Instance linking is UNVERIFIED (see `plugin-ship-checklist` 9d).

## 8. UI conventions that users asked for repeatedly
- Interactive display above the controls it affects; dB scales; hover info bubbles (about 1 s) with an off switch; in/out meters on the right; version backups (v1, v2) of the design.
- Dry/wet bars in contrasting colours (dry pink versus wet green in one design).
- Two views of one parameter stay in sync (see `plugin-ship-checklist` section 3).
- Fixed design size scaled as one piece; eight resize handles keep aspect ratio; save the size.
- Power-saving option (about 16 fps) for slow machines; pause drawing when hidden.

## 9. Plugin ideas still open (UNVERIFIED value)
- Parametric EQ with dynamic EQ and per-band saturation, linear versus minimum phase option, instance linking.
- Freeze-and-transform grain plugin that works as instrument or FX (freeze, hold, capture to sample, riser).
- Edison-style recorder/editor plugin: record from a slot, waveform and spectral view, process menu, repeat-last-operation shortcut, drag back to a track. Avoid a competitor's name in the product name.
- Shared "fx" DSP module so every plugin gets the same multiband, EQ styles, maximize/excite and filter blocks.

## 10. Test checklist for an effect
- [ ] Alias audit at maximum settings (4x for nasty ranges).
- [ ] Level match on bass-heavy, drums, lead and full-mix sources.
- [ ] Amount 0 and mix 0 are bit-exact bypass (or documented).
- [ ] Latency reported and compensated; tail length set.
- [ ] No NaN, DC or runaway feedback.
- [ ] Knob-to-sound under one buffer plus smoothing.
