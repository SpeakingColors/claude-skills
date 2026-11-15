---
name: plugin-performance-profiling
description: Use when a plugin uses too much CPU or RAM: denormal and idle tests, RTSan, SIMD and oversampling costs, FFT library choice, GUI repaint cost, profilers per OS, pluginval, what to measure first.
---

# Plugin CPU and RAM efficiency

Companion to `vst-maker` (sections 2 and 4), `plugin-dsp-quality` and `juce-expert`. Labels: VERIFIED (official docs), COMMUNITY (forum or blog, single source), UNVERIFIED (not found by research, test it yourself). Research date: November 2026; most sources were forum threads, so measure on your own plugin before changing code.

## 1. Measure before you change anything
- Profile a RELEASE build (-O2 or -O3). `juce::dsp::SIMDRegister` and most DSP code is extremely slow in Debug. COMMUNITY (JUCE forum).
- Profile about 20 seconds, filter to the audio thread, root at the plugin entry point. COMMUNITY.
- Tools: `perf record -g` with DWARF call graphs on Linux; Instruments Time Profiler on macOS (filter to the audio I/O thread, hide system libraries); Tracy for timeline views (keep it out of release builds; it showed callback overruns from kernel preemption); Superluminal on Windows (commercial). COMMUNITY. Callgrind details UNVERIFIED.
- Do not trust a DAW CPU meter alone. How each DAW computes it was not found. UNVERIFIED.
- Always compare: editor open vs closed, silence vs signal, 1 voice vs all voices.

## 2. Realtime safety, tested by machine
- No allocation, locks, file or network I/O on the audio thread. VERIFIED (Bencina, rossbencina.com).
- Clang RealtimeSanitizer (LLVM 20 and newer): mark `processBlock` `[[clang::nonblocking]]` and run the standalone or the tests; it reports malloc and mutex calls at runtime with small overhead. VERIFIED (clang.llvm.org/docs/RealtimeSanitizer.html). JUCE specific setup UNVERIFIED.
- Instruments Allocations can also catch audio thread allocations on macOS. COMMUNITY.

## 3. Denormals (silent plugin suddenly burning CPU)
- Subnormal floats can make some CPUs 10x to 100x slower; typical sources are IIR tails, reverbs and feedback loops decaying into silence. COMMUNITY.
- `juce::ScopedNoDenormals` sets flush to zero on x86 (FTZ and DAZ) and ARM. It is PER THREAD: repeat it on any helper thread that runs DSP. COMMUNITY.
- Verify it works in your build: feed a decaying signal, then silence, into every filter, reverb and feedback path; compare CPU with the guard on and off. A tiny DC offset or noise in the feedback path is a belt and braces fix. COMMUNITY.
- Flushing loses only values below about 1e-38. COMMUNITY.

## 4. SIMD and memory layout
- `juce::dsp::SIMDRegister` picks SSE2, AVX2 or NEON at compile time. Gains are not guaranteed; check the compiler's vectorization report first. AVX2 builds need a fallback for older CPUs. COMMUNITY.
- Structure of arrays (SoA) voice data is the usual cache friendly layout. COMMUNITY (low quality source).
- Benchmark scalar vs SoA vs SIMD on your real voice loop. xsimd vs SIMDRegister verdict: UNVERIFIED.

## 5. Oversampling cost
- Oversample only around non linear stages and make it a quality switch (2x, 4x, 8x). Rule of thumb, UNVERIFIED as a number.
- FIR: linear phase, adds latency. Polyphase IIR: low latency, minimum phase, phase distortion near Nyquist, may smear in cascades. Both run at the high rate, so compare real cost. COMMUNITY.
- Report the added latency to the host.

## 6. FFT
- macOS: Accelerate (vDSP) is fastest or tied (about 20 us vs 18 us at order 10 on Apple Silicon, one report). PFFFT is small, permissive and has SSE and NEON. KissFFT is simple but usually slower. FFTW is GPL (fine for open source, not for closed). COMMUNITY.
- Benchmark at YOUR sizes (hayguen/pffft_benchmarks). UNVERIFIED.

## 7. GUI cost
- Repaint frequency and window size dominate. Repaint only the dirty rectangle, pause timers and meters when hidden, lower the timer rate. COMMUNITY.
- JUCE rendering is CPU based. OpenGL results conflict (savings and also a core pinned by continuous repaint). Visage (MIT, GPU, partial redraw) has no benchmarks. COMMUNITY.
- Cache expensive pictures (peaks, spectrogram images) keyed by the data version, view range and size, and rebuild only when the key changes. MEASURED (our editor).

## 8. Idle and memory
- Skip processing when there is no signal and no active voice and tails are below a threshold. Not found in research; UNVERIFIED but cheap to try and measure in Reaper, Bitwig and Ardour.
- Wavetable and sample RAM, scan and load time: nothing found. Measure with the editor open and a typical preset.
- Every edit that copies a whole sound costs time and RAM; say so in the ROADMAP and cap undo memory. MEASURED.

## 9. CI
- pluginval at strictness level 5 or higher, `--validate-in-process`, `--skip-gui-tests` on headless runners; confirm flags against the Tracktion repo. COMMUNITY.
