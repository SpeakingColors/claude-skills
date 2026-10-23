---
name: synth-engine-design
description: Use when designing a synth plugin engine: supersaw, hoover, acid 303, mono analog style, filters, mod matrix, FM/AM, unison, FX chain, presets and banks, voices and CPU, with measurable tests.
---

# Synth engine design: patterns that worked

Companion to `vst-maker` (rules), `plugin-dsp-quality` (sound quality) and `hard-dance-production` (recipes). Study other products' feature lists for ideas only; never copy their code, presets, samples, names or look. Labels: VERIFIED (read on a source page), MEASURED (own test), COMMUNITY, UNVERIFIED (ideas to test by ear).

## 1. Classic sounds, what the sources say
- JP-8000-style supersaw: 7 saws (1 centre in tune, 6 detuned sides), free-running phase, internal high-pass, oversampled around 88.2 kHz; detune curve non-linear (slow then steep); mix = side level against centre. COMMUNITY (musicproductionwiki; the Szabo thesis "How to Emulate the Super Saw" has the curves, not re-read here).
- Hoover (Alpha Juno "What The?"): PWM sawtooth(s), fast LFO on pulse width, resonant low-pass, thick chorus; chorus off is just buzzy saws; a pitch dive at note start (starts slightly sharp, falls into pitch in a fraction of a second). Sources disagree on the exact layout (three saws an octave apart versus saw plus pulse with a sub), and the dive has no published numbers; tune by ear. COMMUNITY.
- TB-303 acid: one oscillator (saw or square; the square's duty is not 50%, roughly 45% at high notes to 71% at low notes per one source); 4-pole diode-ladder low-pass that behaves like about 18 dB over much of its range and is resonant but not self-oscillating; two envelopes (filter, amp); accent shortens the filter decay, boosts level and raises cutoff, with an accent sweep that builds on consecutive accents; slide is portamento with the gate extended into the next note. COMMUNITY (olney.ai, Wikipedia). Step-level sequencer details were not in the sources read.
- Two-oscillator analog mono (Pro-One class, from the original operation manual): osc A saw/pulse always keyboard-tracked; osc B saw/tri/pulse with a low-frequency range and keyboard on/off; hard sync A follows B; noise; 4-pole 24 dB low-pass that self-oscillates at high resonance; two ADSRs; LFO 0.1 to 30 Hz; modulation sources (filter envelope, osc B, LFO) routed to destinations (osc A/B frequency and pulse width, filter) with a wheel/direct/off switch; low-note priority single trigger versus last-note retrigger; repeat gates envelopes at LFO rate; drone holds the gate. VERIFIED (original manual, read by OCR). Facts about other makers' newer reissues differ; read their own documents.
- Moog-style ladder: resonance lowers passband level (bass gets thinner), so add makeup; self-oscillates at high resonance. COMMUNITY.
- Filter circuit study (CEM3320-class four-stage 24 dB filter): resonance is a current-controlled stage; exponential cutoff control; the resonance feedback is taken after a buffer; used here only as rules of thumb: resonance taper like `k = 4.4 * reso^1.5`, soft tanh clipping before and inside the filter, exponential cutoff with key tracking, a tiny noise floor so the filter can self-start. UNVERIFIED by ear; do not copy schematics or code.

## 2. Oscillator and layer architecture
- Layers (for example A, B, C): each an oscillator or a loaded sample; plus sub and noise.
- Multisaw: 1 to 9 saws, optionally with an equal number of sub saws an octave down; Detune and Mix as two separate knobs.
- Third oscillator "slave" mode that copies another oscillator's wave and pitch with inverted detune; phase control (0 = free-run, otherwise fixed offsets); noise colour and a "punch" click on key press. COMMUNITY (feature lists of two commercial synths, ideas only).
- Sub and noise can also have Voices (1 to 5), Detune and Width. Defaults must be neutral so old presets sound the same (see `plugin-ship-checklist` section 1).
- FM and AM per layer: source choices (off, layers, sub, noise) with amount 0 to 1. FM scales oscillator frequency (up to about 3x deviation in one engine); AM is `1 - amt + amt*src` (1 = ring mod). A layer at level 0 must still run when used as a modulator. Sources use the previous sample (one sample delay). An FM-depth destination in the mod matrix would allow a decaying FM index for e-piano and bell sounds.
- Screech-lead set: feedback oscillator (harmonics, feedback), osc 2 sync with pitch sweep from an LFO or pitch envelope, cross-modulation, ring mod, 24 dB filter at full resonance. COMMUNITY (from one synth manual, not verified on hardware).
- Drift: independent slow LFOs per oscillator with golden-ratio spaced frequencies so the movement never repeats, plus one "drift" macro that scales detune and drift together. A keytracked high-pass (JP-8000 style) as its own control. Write these fresh in your own code. UNVERIFIED as quality.
- Wave import rules that worked: a file up to 8192 samples is one cycle; a multiple of 2048 samples is a wavetable with a frame slider; otherwise autocorrelation finds one period near the middle. Store the cycle in the preset as base64 Int16. Offer find-cycle and seam-fix tools.
- Never bundle third-party waveform packs; see `plugin-ship-checklist` 9c.

## 3. Filters
- Offer a filter list with honest names (your own models, style nicknames): off, LP 6/12/18/24, ladder-style, jupiter-style, MS-20-style, SEM-style, acid, HP, BP, notch, comb +/-, formant. Make every type finite and stable (test).
- Up to three filters with their own envelopes; Series or Parallel (and Split with pan spread) routing; cutoff link with offset.
- The extra knob follows the type: LP and BP show a low cut, HP shows a high cut. Side slope menu 6, 12, 18, 24, 48, 96 dB (48 and 96 as Butterworth biquad cascades of 8 and 16 poles) and verify with the same test in JS and C++.
- Filter drive: adaptive makeup so raising drive does not make the sound quieter (worst case measured -1.7 dB in one engine).
- Oversampled filter option (2x or 4x); report the latency.
- Comb filter display: show teeth every `fs/delay` Hz.

## 4. Modulation
- Matrix of sources by destinations, values -1 to 1, default 0, with explicit scales (for example 12 semitones for pitch, 5 octaves for cutoff). One engine used 15 sources and 23 destinations, with global destinations (reverb mix, delay mix, EQ, width) following the newest held note.
- Slots with three targets each, and amounts that can themselves be targets, are more powerful than one source per slot. Unison voice index and arp step values are useful sources.
- Test: every matrix cell must change the sound and stay finite (one suite did 126 cells automatically).
- LFOs: sine, triangle, square, saw up/down, random square (sample and hold), random smooth (cosine glide); retrigger or free-run; tempo sync; fade-in on one LFO; key-follow of rate.
- Drawn envelope: 64 samples as a hex string, time 0.02 to 20 s or tempo-synced, loop, invert, per-segment curves; shape presets (pluck, ramp, swell, sidechain, random). A drawn "sidechain" curve (low after the beat, exponential rise, hold, drop) on volume gives pumping without a compressor.
- Amp envelope link: linked = envelope 1 shapes all; unlinked = envelope n shapes layer n, envelope 1 also shapes sub and noise.

## 5. Voices, polyphony and CPU
- Mono / Poly / Stack modes; polyphony 1 to 32, default around 12; steal releasing voices first. A chord of 5 notes with release tails exceeds 8 voices; do not default too low.
- A browser (JavaScript) port of a heavy engine runs hot (one test: 8 voices about 67% of a core, 16 voices 120%, 24 voices 200%); the C++ plugin is far lighter. Use the browser build for sound design only.
- Cache per-voice tables (for example supersaw pan and gain) instead of recomputing; one such change took 8 voices from 106% to 67% of a core. MEASURED.
- Keep a JS and C++ copy of the engine in parity: compare renders (worst RMS difference about 2e-7 achieved) and run the same presets through both.
- Drum kit mode: each slot is its own small engine with choke groups and per-slot gain.
- Capture the last played phrase as an audio file (offline render, 24-bit) for drag-out; native drag needs the host window's external drag API (JUCE `performExternalDragDropOfFiles`).

## 6. FX chain order that worked
Voices > chorus/delay/reverb > opto/OTT/squeeze > bass mono > dance master (mix, drive, clip; dry path allpass-aligned) > sub bus > limiter > soft clip. Another synth used: filter FX, distortion, character, phaser, chorus, delay, reverb, EQ, limiter. UNVERIFIED as best; choose and measure.
- Per-effect preset menus with factory lists plus "save current"; stored per user.
- Display ideas: live scrolling wet waveform per effect, impulse response, comb teeth, dynamic-EQ curve with a ring marker, gain-reduction history.

## 7. Presets and banks
- Preset has a stable id, category, tags and a note; level it by measurement: set master so a single held note peaks near 0.6 before the clipper (bass notes an octave lower), and record the old master if you re-level.
- Freeze factory order: banks A to D with new presets only appended, so program changes never move. Provide Restore factory and verify that import reproduces the bank exactly.
- Favourites and re-order stored in user data; arrows step through the same visible order as the browser.
- Delay shows tempo-sync divisions (14 in one engine); verify, for example, 1/8 at 140 BPM is 214 ms.
- Presets are starting points; say clearly they were level-measured, not heard.

## 8. Test checklist for a new engine
- [ ] Every filter type and every mod cell finite and stable.
- [ ] Output linear under the clipper knee; bounded with four notes at master 2.
- [ ] No NaN, no DC, no runaway tail.
- [ ] Alias audit (see `plugin-dsp-quality` section 2).
- [ ] Old presets render the same after adding parameters.
- [ ] CPU at full polyphony on the slowest target machine.
- [ ] JS versus C++ parity if both exist.
