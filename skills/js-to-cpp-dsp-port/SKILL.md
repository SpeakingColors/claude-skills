---
name: js-to-cpp-dsp-port
description: Use when DSP written in JavaScript (a mockup engine) must be ported to C++ with the same results: function by function, same test cases, rounding and FFT conventions, STFT, phase vocoder, undo steps.
---

# Porting a JavaScript DSP engine to C++ with identical behaviour

Labels: MEASURED (ported spectral editing, phase vocoder stretch, formant preserving pitch shift, warp, YIN note detection and tempo detection; 662 checks pass), UNVERIFIED.

## Method
1. Port ONE function at a time, in a header only file with no JUCE (`MeowDsp.h` style), in the same order as the JS file. Keep the constants and the comments.
2. Port the JS test file to C++ as checks, with the same inputs and tolerances. A port is done when the same cases pass, not when it compiles. Add a second layer: the plugin's editor calls the engine through one undo step (`ed.transform("Label", fn)`).
3. Run the JS tests too, so both sides stay in step. Keep the JS as the reference for the mockup.

## Conventions that bite
- `Math.round(x)` rounds halves UP: use `floor(x + 0.5)`, not `std::round` (which rounds away from zero for negatives).
- JS typed arrays are zero filled and `Float32Array` rounds on store: keep intermediates in `double`, store `float` at the same places.
- Inverse FFT by conjugation: `conj(fft(conj(x))) / n`. Overlap add with a Hann window at 75 percent overlap divides by 1.5.
- Pitch tracks use NaN for "no pitch": test with `isnan`, never `==`. Guard every neighbour index in smoothing windows.
- Use a double precision pi. A float `kPi` already existed in the core and gave small errors in sinc kernels.
- Phase vocoder with peak locking: keep the previous analysis phase and the synthesis phase per bin, assign every bin to its nearest peak, and note the analysis hop is `st - prevSt` (an integer). Time stretch then resample gives pitch shift; formant keeping needs a spectral envelope pass.
- Randomness (grain texture mode) cannot match the JS generator: test length and level only.

## Results that need no reference
- Resample 48k to 44.1k keeps pitch within 1.5 Hz and RMS within 0.01. Stretch by 1.5 gives exactly 1.5 times the frames with the pitch within 3 Hz. Note detection finds 220 Hz as MIDI 57 within 0.1. MEASURED.
- Spectral cut of a box removes the tone inside it by more than 50 dB and leaves tones outside it within 0.2 dB. MEASURED.

## UI notes
- Long jobs (stretch of minutes of audio) block the message thread: say so in the panel, or move them to a thread before shipping.
- Preview = run the process on a copy and play that copy; never touch the real sound until Apply.
