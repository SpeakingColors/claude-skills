---
name: plugin-aliasing-measurement
description: Use to measure how much a distortion effect aliases from outside the plugin: two sample rates, sines that avoid integer ratios, why a one rate non-harmonic count fails, self test, CI report.
---

# Measuring aliasing of a built plugin

Companion to `plugin-dsp-quality` (what to fix) and `plugin-fleet-audit`. Labels: MEASURED (a JUCE console tool loading VST3 effects, Linux, JUCE 8.0.16), UNVERIFIED.

## Method that worked
- Load the built VST3 in a small JUCE host (`AudioPluginFormatManager` with `VST3PluginFormat`, `JUCE_PLUGINHOST_VST3=1`, run under `xvfb-run`). Skip instruments: a synth is inharmonic by design (detune, unison).
- Turn the drive-like parameters to maximum by NAME (drive, fuzz, dist, crush, fold, clip, sat, warm, tube, tape, boost, mix, wet, gain). Skip names with bypass, mute, power, output, ceiling, threshold. It is a worst case, not normal use.
- Play a sine of amplitude 0.5. Use coherent sampling: pick the FFT size so the sine fits a whole number of bins, then a plain FFT has no leakage and harmonics sit exactly on bins `k * f`.
- Run it at 48 kHz and again at 192 kHz with the SAME bin spacing (FFT 65536 at 48 kHz, 262144 at 192 kHz) and normalise every bin by the FFT size, or the two rates are not comparable. Measure only below 20 kHz.
- aliasing = (energy not on a harmonic at 48 kHz) minus (the same at 192 kHz), in dB relative to the band energy. What remains at 192 kHz is modulation sidebands and noise; report it separately.

## Why not the simple version
- Counting every non-harmonic component at one rate looked plausible and was wrong: a plugin with modulation read about -6 dB "aliasing" at every frequency. The second rate removes what is not aliasing.
- Test frequencies must not divide the sample rate. At 3 kHz and 48 kHz (ratio 16) folded harmonics land exactly on other harmonics and a naive clipper looked perfectly clean (-390 dB). Use 1.1, 3.1, 7.3, 9.1 and 11.3 kHz.
- Forgetting to normalise by the FFT size gave a 6 dB phantom difference between the rates.

## Positive control (build it first)
A `--selftest` that runs `tanh(12x)` naively and through a 4x oversampled version (polyphase IIR) at 3.1 and 9.1 kHz and fails unless the oversampled one is at least 10 dB cleaner. Measured: naive -29.1 and -14.7 dB, 4x oversampled -106 and -47 dB. If the control does not separate them, the metric is broken.

## Reading results
- Compare a plugin with its own earlier numbers; the absolute value depends on the extreme settings. Example: an effect with 2x oversampled drive stages and every drive-like knob at maximum measured -29.8 dB at 1.1 kHz rising to -13.7 dB at 11.3 kHz, close to a naive clipper, so 2x was not enough for that setting. Whether that matters at normal settings was not measured.
- Even 4x oversampled tanh(12x) still showed -47 dB at 9.1 kHz: heavy drive needs ADAA as well (see `plugin-dsp-quality`).
- Run it as a report only in CI (never fail the build on it) and keep the number in the job summary.
