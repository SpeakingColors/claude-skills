---
name: juce-audio-thread-handoff
description: Use when a JUCE plugin must record, play back edited audio or share big data with the audio thread without allocating or locking: FIFO to a worker, published snapshots, state flags.
---

# Audio thread handoff patterns that held up

Companion to `juce-expert` and `vst-maker` section 2. Labels: MEASURED (a recorder and sample editor plugin with a headless test), VERIFIED (Bencina's realtime audio programming rules), UNVERIFIED.

## Rule
The audio thread never allocates, frees, locks a mutex another thread can hold, or does file I/O. Talk to it with lock-free FIFOs and atomics. VERIFIED (rossbencina.com).

## Pattern 1: record without allocating
- `juce::AbstractFifo` with two preallocated float vectors. `processBlock` copies the input in (drop on overflow) and returns.
- A worker `juce::Thread` drains it into an engine that is allowed to allocate (`push_back` growth). Message thread commands (arm, stop) take a short `std::mutex` shared only with the worker, never with the audio thread.
- Stop = drain once more under the mutex, then take the result.

## Pattern 2: play edited audio
- The editor owns the editable sound. After every change it publishes an immutable `shared_ptr<const Audio>` into a slot guarded by `juce::SpinLock`. The audio thread takes the lock with `ScopedTryLock`; on failure it plays nothing this block.
- The audio thread copies the shared_ptr to a local and releases it at the end of the block. To make sure that release never frees memory on the audio thread, the message thread keeps the last four published snapshots alive in a deque.
- Playback position, range and flags are atomics. Interpolate (linear is enough) when the file rate differs from the host rate.
- Preview = publish a processed COPY into the same slot and play it; restoring means publishing the real sound again.

## Pattern 3: metering and the count-in
- Peaks go out through `std::atomic<float>` with a per block decay. A ring of atomics (512 entries) feeds a live strip.
- A count-in is generated in `processBlock` from atomics (position, beat length, total): a short decaying sine per beat, added after the monitor mute so it stays audible. When it ends, the audio thread sets a flag and the worker arms the recorder.

## Checks
- `ScopedNoDenormals` at the top of `processBlock`; a helper thread that does DSP needs its own.
- Report latency honestly; parameters through APVTS with stable IDs.
- Known limits: the snapshot copies the whole sound on every edit, so minutes of audio edit slowly. Say so in the ROADMAP.
