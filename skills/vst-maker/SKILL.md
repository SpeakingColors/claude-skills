---
name: vst-maker
description: Use when designing, writing, reviewing, packaging or releasing audio plugins (synths, effects, MIDI controllers) in C++/JUCE for VST3 on Linux, macOS and Windows, incl. realtime safety and installers.
---

# VST Maker

Companions: `juce-expert` (JUCE details, builds, licence), `mockup-is-the-plugin` (UI port rule), `plugin-dsp-quality` (aliasing audits, ADAA, level matching, responsiveness) and `plugin-ship-checklist` (old saves, editor checks, installers, releases). Load them together for JUCE plugin work. For GPU UI options (Visage), see juce-expert section 13c.

Unofficial community skill. Not made or endorsed by any plugin, synth or framework vendor named here.

How to read confidence tags:
- (V: source) checked against the named source.
- (R) rule of thumb or taste. A starting value to test by measuring and listening, never a law.

If a fact has no tag, it is standard practice you should still verify before relying on it for a release.

## 0. Ground rules

- Ask before building: plugin type (synth, effect, controller), target OS (Linux, macOS, Windows), formats (VST3 first; CLAP or LV2 optional), colour palette (never assume one; offer a neutral default if the user has none), licence (see 1).
- Free and open-source plugins must work offline: no account, no licence server, no download at install or run time. Everything the plugin needs is bundled.
- Never claim a sound is good by ear. Measure it (see 12) and let the user's ears make the final call.
- Cite or test every number. Say "unverified" when a figure is a rule of thumb.
- Do one step at a time when the user is not a programmer. Short answers first, details on request.

## 1. Project setup and licence

- JUCE is dual licensed: the JUCE licence and AGPLv3. Without a paid JUCE plan you must use it under AGPLv3, and AGPLv3 asks for more than publishing source (V: JUCE forum, staff reply). Read the current JUCE licence for the version you use before choosing, and tell the user which one applies. Do not state tier prices or revenue limits from memory.
- Use CMake. Keep DSP code free of JUCE GUI types so it can be unit tested without a window.
- Build VST3 first. CLAP and LV2 are optional: check the current JUCE docs and clap-juce-extensions before promising either.
- Where hosts scan for VST3 (V: Steinberg VST 3 Developer Portal, Plug-in Locations):
  - Linux: `$HOME/.vst3/` first, then `/usr/lib64/vst3/`, `/usr/lib/vst3/`, `/usr/local/lib64/vst3/`, `/usr/local/lib/vst3/`.
  - macOS: `~/Library/Audio/Plug-ins/VST3/` (user), `/Library/Audio/Plug-ins/VST3/` (global).
  - Windows: `C:\Program Files\Common Files\VST3\` (global), `%LOCALAPPDATA%\Programs\Common\VST3\` (user, mainly for development).
  - Hosts use the first plugin found for a given Processor UID, scanning in priority order.

## 2. Realtime safety

`processBlock` runs on a high-priority audio thread with a hard deadline. The JUCE docs say any interaction with the UI there is out of the question, and the code must cope with variable block sizes (V: JUCE AudioProcessor docs).

Never on the audio thread:
- allocate or free memory (new, delete, malloc, growing vectors or strings, building juce::String)
- take a lock another thread can hold (std::mutex, CriticalSection)
- file, network or console I/O
- call the UI or MessageManager
- throw exceptions or call anything with unknown realtime behaviour

Instead:
- Allocate in `prepareToPlay` (the sample rate stays constant until playback stops; the block size is only a hint and the docs say to program defensively in case a host exceeds it) (V: JUCE docs). Free in `releaseResources` or the destructor.
- Talk to other threads with lock-free queues (`juce::AbstractFifo`) or atomics. The UI polls atomics with a Timer; or trigger AsyncUpdater from the audio thread.
- Put `juce::ScopedNoDenormals` at the top of `processBlock`; it stays active until the function returns, so helpers do not repeat it (V: JUCE forum consensus, not official docs). Also design feedback paths so they cannot decay into denormals.
- Recommended reading: Ross Bencina, "Real-time audio programming 101: time waits for nothing" (not quoted here, could not be fetched when this skill was written).

## 3. Parameters and state

- Use `AudioProcessorValueTreeState`: host automation, undo and state save come with it.
- Smooth every parameter that reaches a gain, frequency, mix or delay time (`juce::SmoothedValue`), or you get zipper noise and clicks.
- Read values once per block into locals unless the value is smoothed per sample.
- Give every parameter a stable string ID. Never rename or reorder IDs after release: it breaks saved projects and automation. Add new parameters with new IDs and keep a state version number.
- Validate everything loaded from state or presets: clamp ranges, ignore unknown keys, never trust sizes or counts.
- Keep the processor (DSP and state) strictly separate from the editor (UI). The processor must run perfectly with the editor window closed. VST3 itself splits a plug-in into a processor and a controller (V: Steinberg VST 3 tutorial, "Code your first plug-in").
- VST3 facts worth knowing even when JUCE wraps them (V: same tutorial): parameters are always normalized to 0.0 to 1.0; set the automatable flag so hosts can automate; one processing block can contain more than one change for the same parameter, so a hand-written processor must handle the queue correctly (the tutorial applies only the last change, which is a simplification); if the input is silent, set and honour the silence flags and clear the output buffers; reject unsupported bus layouts instead of guessing; when there are no inputs or no samples, still apply pending parameter changes.

More VST3 architecture facts (V: Steinberg VST 3 Developer Portal, API documentation):
- The processor must work with no controller loaded, so DSP state never depends on the editor.
- `process()` and `setProcessing()` may run on the audio thread: no allocation. Initialize and terminate run on the UI thread.
- Bus and speaker arrangements can change only while the plug-in is inactive. Provide buffers for all busses, even inactive ones. Input and output buffers may share memory, so do not blindly clear outputs.
- Notes arrive as events in `process()`. Parameter changes arrive sample-accurately through parameter queues. Tempo and transport arrive in the process context.
- GUI-to-host edits use beginEdit, performEdit, endEdit in that order, on the UI thread only.
- On state restore the processor is restored first; the controller then receives the component state and must not fire handler callbacks.
- Do not send private processor-to-controller messages from `process()`; use the UI thread or the Data Exchange API.
- Units group parameters; the MIDI mapping interface maps MIDI CCs to parameters.
- Portal pages to read when needed: Parameters and Automation, Workflow Diagrams, Multiple Dynamic IO (sidechain), VST 3 Units, Data Exchange.

## 4. Performance: CPU, RAM, GPU

- Measure before optimising (see 12).
- CPU (R): process in blocks, precompute coefficients when a parameter changes, avoid per-sample branches and virtual calls in inner loops, avoid `std::pow`, `std::exp`, `std::sin` per sample where a recurrence or table works and measures faster.
- RAM: preallocate once, share wavetables and tables between voices, free big buffers in `releaseResources`.
- GPU and UI: draw only while the editor is visible and in front. Pause timers, meters and canvas animation when hidden; audio, automation and MIDI keep running. Cap the repaint rate and repaint only dirty regions (R). Use GPU rendering only if clearly needed and tested on Linux.
- A hidden or closed editor must not keep running per-frame work.

## 5. Latency

- Report real latency with `setLatencySamples` ("the number of samples delay that it introduces", V: JUCE docs) whenever the plugin delays audio: lookahead limiters or compressors, linear-phase filters, oversampling filters. Verify in a host that the report is applied.
- Instruments add zero latency from note-on to sound.
- Linear-phase oversampling filters add latency; minimum-phase ones do not but change phase. Choose on purpose and document it. `juce::dsp::Oversampling` reports its latency; report it.
- Keep `getTailLengthSeconds` correct for reverbs and delays so hosts do not cut tails.

## 6. Sound quality

Aliasing
- Naive sawtooth and square waves have harmonics above Nyquist that fold back as inharmonic noise. Fixes: band-limited step methods (BLEP family), differentiated polynomial waveforms, band-limited wavetables per octave, or oversampling.
- A published method: differentiated polynomial waveforms; the authors' listening-model evaluation found a fourth-order method perceptually alias-free across the whole range of a grand piano (V: Välimäki, Nam, Smith, Abel, IEEE TASLP vol. 18 no. 4, 2010).
- Any nonlinearity (distortion, saturation, wavefolding, hard clip) creates new harmonics that alias. Oversample around nonlinear stages, or use antiderivative-based anti-aliasing. Zavalishin covers antialiasing of waveshaping (V: "The Art of VA Filter Design", section 6.13).
- Test aliasing by measurement (see 12), not by eye on the oscillator code.

Filters
- For modelled analog filters use zero-delay-feedback (topology-preserving transform) structures. The book covers them in chapter 3 (section 3.9, zero-delay feedback), the Moog-style ladder in chapter 5, and feedback-loop saturation in chapter 6 (V: Zavalishin, "The Art of VA Filter Design", rev. 2.1.0, table of contents).
- For plain EQ and utility filters use biquads. The Audio EQ Cookbook (R. Bristow-Johnson, W3C Working Group Note 2021) gives low-pass, high-pass, band-pass, notch, all-pass, peaking EQ and shelves (V).
- Smooth cutoff and resonance changes, clamp cutoff below Nyquist, keep resonance stable at extremes, and compensate level so high resonance does not jump the volume.

Smooth rather than harsh (R, from producers' practice; test each)
- Harshness usually comes from aliasing, hard clipping, strong resonance peaks in the upper mids, and too much unfiltered top end.
- A lead with the lowpass left fully open can sound too bright. A starting cutoff around 12 kHz for bright leads is a user-reported taste value, not a rule.
- Saturation inside the filter feedback loop is a common reason analog-style filters sound smooth (V: Zavalishin covers feedback-loop saturation; the perceptual claim is R).
- Very small, slow modulation keeps static tones alive, for example a pitch drift of a few cents. Convert before choosing: 0.1 percent is about 1.7 cents, 1 percent is about 17 cents, and 17 cents is clearly audible detune. Stay at the low end unless detune is the goal.
- Thick sounds come from layering, unison with detune spread, a sub oscillator and stereo width. Check mono compatibility (sum L and R, listen for hollow or cancelling sounds).

Gain staging and DC
- Run the internal chain in float with generous headroom. Never clip inside the chain. Put the only clipper or limiter at the output, on purpose.
- Remove DC after asymmetric nonlinearities with a gentle high-pass in the low single-digit to tens of Hz range (R); verify with the DC measurement in 12.
- Match preset loudness (see 9) so switching presets does not jump the level.

## 7. Synth design

- Voices: preallocate every voice, never allocate on note-on. Make polyphony a constant or a user setting. Steal voices with a short fade, never a hard cut.
- Envelopes: use a minimum attack and release of a few milliseconds to avoid clicks; on retrigger start from the current level, not from zero.
- Unison: random or spread start phases, a detune spread curve, stereo spread, and a level compensation that does not grow with voice count.
- Supersaw: the Roland JP-8000 Super Saw is described as resembling seven sawtooth oscillators detuned against each other (V: Wikipedia, Roland JP-8000). Detailed analyses exist: Adam Szabo, "How to Emulate the Super Saw" (KTH, 2010) and Alex Shore (2013), both cited on that page. Read them for detune curves and mixing instead of guessing numbers.
- Drift and analog feel: slow random modulation of pitch and cutoff, per voice, small and uncorrelated.
- Ideas seen in commercial supersaw synths, for study only; write your own code and design, never copy a product's code, look, name or presets (R, verify by ear and measurement):
  - One slow LFO per oscillator, with frequencies spaced by irrational ratios such as the golden ratio, so the combined movement does not repeat audibly.
  - One "drift" macro that scales detune and drift depth together, with fine controls on a second page.
  - A keytracked high-pass as its own control (the JP-8000-style supersaw sound uses one).
  - An optional 2x or 4x oversampled filter; report the oversampling latency to the host.
  - Check dB scales on meters, per-voice stereo spread, and sidechain-capable effects: gaps some products leave that users notice.
- MIDI: use the sample position of each MIDI event inside the block so notes start sample-accurately. Handle pitch bend (default range of two semitones, configurable), sustain pedal, all-notes-off, and note-off with release. Offer mono, legato and portamento if the instrument is lead or bass oriented.
- Wavetables: band-limit per octave or per pitch range; cross-fade between frames to avoid zipper noise; interpolate (linear is cheap, higher order costs CPU, measure the aliasing).

## 8. FX design

- Compressor and limiter: detect in the log domain with smoothed attack and release, apply gain smoothing, add auto or manual makeup, report latency if you look ahead. A limiter at the end of a chain needs a true-peak or oversampled ceiling if it promises inter-sample safety.
- Multiband: split with Linkwitz-Riley crossovers so the bands sum back flat; process each band; recombine. Keep crossovers phase-consistent and report any added latency.
- Delay: fractional-delay interpolation, damping filters in the feedback path, tempo sync, ping-pong, ducking, and a feedback limit so it cannot run away.
- Reverb: feedback delay networks or the Dattorro plate topology (J. Dattorro, "Effect Design Part 1", JAES 1997); damp the highs in the tail; modulate delay lines slightly to avoid metallic ringing; expose pre-delay, decay, damping, size and mix.
- Common starting practice for leads, test by ear (R): keep the reverb return out of the low end with a high-pass around 200 to 300 Hz, roll off the tail's highs, and use a moderate mix.
- Chorus, ensemble, phaser, flanger: modulated delays with proper interpolation and LFO phase offsets between voices.
- Distortion: oversample, filter before and after, and offer a tone control. Always include dry/wet.
- Every effect: bypass without clicks (cross-fade), mix control, input and output gain, and a sane default that sounds good on first load.

## 9. Presets

- A factory bank is the product's first impression. Plan categories (lead, bass, pad, pluck, FX, arp, and so on), consistent naming, and tags.
- Embed factory presets in the plugin binary or its bundle; never require files outside the bundle on first run.
- Include an init preset, and macro controls for the three to eight things users reach for most.
- Level-match every preset. Render each one with a standard note and chord set and measure short-term loudness (ITU-R BS.1770 / EBU R128 style) and peak; aim for a consistent target and no clipping.
- Audit script for every preset (see 12): no NaN or infinity, no DC, no clipping, no silence, no runaway tail, CPU within budget, and a note on aliasing level.
- Study references the right way: analyse reference patches parameter by parameter (oscillator waves, detune, filter cutoff and resonance, envelopes, FX chain), then build your own sounds from what you learn. Never copy another maker's presets or sample content into a product.
- Version the preset format. Keep old presets loading in new versions.

## 10. UI standards

- Ask the user for a palette first. If none, use a neutral, high-contrast default with an accent colour. Keep contrast readable in dim studios.
- Mockups are interactive by default: every display, meter and curve reacts to the controls, and controls react to the displays (drag a point on a curve, the knob moves). Never ship a static picture of a control.
- Put each control directly under the display it affects. Put input and output meters on the far right.
- Meters and level displays show dB numbers and a dB scale (ticks with labels). Input and output meters follow the real audio.
- Hover info bubbles after about one second explain each control, with a setting to turn them off.
- Pause drawing when the window is hidden or not in front (see 4).
- Support HiDPI and resizing, keyboard focus, and double-click to reset a control.
- Back up before editing designs and keep versions (v1, v2, v2.1) so changes can be rolled back.

## 11. Gear controller plugins (hardware editors and librarians)

- Source order for the MIDI map: official manufacturer documents first, then captures from the user's own hardware, then third-party documents (label those unverified). See the hardware-protocol-capture skill.
- Write the MIDI implementation document before the UI. Add a "verified on hardware" column.
- Back up the device's patches before sending any unknown SysEx. Never send firmware or flash-write commands you do not fully understand.
- Guard against MIDI feedback loops: do not echo received messages back to the device; add a loop guard and a switch to disable pass-through.
- Handle the device being absent, slow or reconnecting without blocking the audio or UI thread. Chunk big SysEx dumps, show progress, and allow cancel.
- Show device state truthfully: if a value cannot be read back, mark it unknown instead of guessing.

## 12. Testing and measuring

- Unit-test DSP with an offline render harness: render known input to a buffer and assert on peak, RMS, DC, NaN, spectrum.
- Aliasing: render a sweep or high notes, take a spectrum, and measure energy at frequencies that should be empty. Compare with and without oversampling.
- Harshness: measure spectral energy in the 2 to 6 kHz region against the rest, and resonance peak height.
- CPU: render many seconds at several sample rates and block sizes, and compare time to real time. Test worst-case presets and full polyphony.
- Denormals: render silence after a loud note and watch CPU.
- State: save, reload, and compare parameters. Test automation and random parameter changes.
- Run `pluginval` in CI (V: Tracktion pluginval README): `pluginval --strictness-level 5 <plugin>`; level 5 is described as the lowest generally recognised for host compatibility; exit code 0 means pass, 1 means fail; formats VST, AU, VST3; macOS, Windows, Linux.
- Other validators named by experienced developers (V: JUCE forum thread "Development cycle of a audio plugin", 2023, forum not official): Apple's auval for AU, the Steinberg VST3 validator, and AVID's DSH tool for AAX. Also A/B null testing with a scriptable host, and Ryan Avery's ADC'17 talk "Test-driven development for audio plugins".
- Wire pluginval and the DSP unit tests into CTest or CI so they run on every change. A CI machine is also where code signing, notarisation and installer building belong.
- Test in real hosts on each OS (for example Bitwig, Reaper, Ardour on Linux), including a sandboxed Flatpak host.
- Use sanitizers (AddressSanitizer, UndefinedBehaviorSanitizer, ThreadSanitizer) in debug builds.

## 13. Security

- Treat every external input as hostile: preset files, state blobs, SysEx, MIDI, and any imported audio or wavetable. Bounds-check sizes and indexes, clamp values, reject unknown versions.
- Fuzz parsers (libFuzzer or similar) for presets, SysEx and state.
- No network access, telemetry, auto-update or code download inside the plugin. Offline is also a security feature.
- No embedded secrets or tokens. No evaluating scripts from presets.
- Pin and checksum third-party dependencies, keep a list of licences, and update on known vulnerabilities.
- Sign releases where possible and publish SHA-256 checksums (see 14).
- In a Flatpak, request the minimum permissions.

## 14. Packaging and release (offline, beginner friendly)

Every release is one zip containing: an installer for each platform, a short PDF manual (what each control does, plus recommendations), plain install instructions, and a LICENSE. It works offline. Nothing is fetched at install or run time. Users are surprised and annoyed by online-only or badly packaged plugins.

### Linux
- Offer a Flatpak. Audio plugins ship as extensions of `org.freedesktop.LinuxAudio.Plugins`, mounted at `/app/extensions/Plugins`; VST3 goes in `.../vst3`, LV2 in `.../lv2`. Listed formats: LV2, LADSPA, VST, VST3, DSSI, CLAP. The extension version must match the host's Freedesktop runtime; the README showed 23.08 when checked, so check the current branch (V: Flathub LinuxAudio BaseExtension README).
- Cautions from forum threads (single-user reports): a Flatpak Bitwig could not see plugins in `/usr/lib/vst3` or the home directory (2023); plugins in sandboxed hosts could not read presets from `~/.local/share/<vendor>` (2024).
- So embed factory presets and assets in the plugin, never depend on files outside it for first run, write user data only where the host sandbox allows, and test inside a Flatpak host.
- Also provide a plain tarball with the `.vst3` and a one-paragraph copy to `~/.vst3` instruction for non-Flatpak users.

### Windows
- Ship a real installer (.exe, for example built with Inno Setup or NSIS) that installs to `C:\Program Files\Common Files\VST3\`, plus an uninstaller.
- Signing (V: Microsoft docs, code signing options): unsigned installers get a strong SmartScreen block. Options: Azure Artifact Signing (about $9.99 per month; organisations in USA, Canada, EU, UK; individuals USA and Canada), an OV certificate ($150 to $300 per year, key on hardware token), SignPath Foundation (free OV-level signing for qualifying open-source projects). EV certificates no longer bypass SmartScreen since 2024. No option gives instant trust; reputation builds across releases signed consistently. If unsigned, tell users what warning to expect.

### macOS
- Ship a signed and notarized .pkg or .dmg that installs the `.vst3` to `/Library/Audio/Plug-ins/VST3/`.
- Apple docs: since macOS 10.15, plug-ins downloaded from the internet are only loaded without manual approval if notarized; otherwise the user must approve them in System Settings (V). Notarization needs Developer ID certificates (Application for binaries, Installer for the pkg), hardened runtime and a secure timestamp. Use `notarytool` (`altool` has not been accepted since Nov 1, 2023), then `stapler`. Notarizable: apps, non-app bundles, disk images, flat installer packages (V: Apple docs).
- Check Apple's site for the current Developer Program fee before quoting a price.
- Without an Apple Developer account, say so in the README and give the manual approval steps. Never tell users to disable Gatekeeper.

### Always
- LICENSE, README (what it is, how to install, how to uninstall), manual PDF, SHA-256 checksums in the release notes.
- Test install and uninstall on a clean machine or VM with the network disabled.
- GitHub release limits: each file under 2 GiB, up to 1000 assets, no total size limit (V: GitHub docs, About releases).

## 15. Review checklist

- [ ] No allocation, locks or I/O on the audio thread
- [ ] Parameters smoothed; IDs stable; state versioned and validated
- [ ] ScopedNoDenormals set; silence-tail CPU checked
- [ ] Latency reported; tail length correct
- [ ] Aliasing measured, nonlinearities oversampled
- [ ] No DC, no clipping inside the chain, presets level-matched
- [ ] Editor pauses when hidden; meters have dB scales; info bubbles can be turned off
- [ ] pluginval level 5 passes; tested in real hosts and a Flatpak host
- [ ] Parsers validated or fuzzed; no network code
- [ ] Offline installer per OS, manual PDF, install instructions, checksums, LICENSE
- [ ] Licence of every dependency checked, JUCE licence choice stated

## 16. Development workflow and learning resources

Fast iteration (V: JUCE forum thread "Development cycle of a audio plugin", 2023; these are experienced developers' practices, not official rules):
- Do not reload the plugin into a DAW by hand after every change. Configure the IDE to launch the host with a saved project that already contains the plugin, then debug normally. Attach the debugger to the host or validator process to hit breakpoints in the plugin; some hosts do not allow attaching.
- Use the standalone build or JUCE's AudioPluginHost for most DSP and UI work, and unit tests for DSP. Standalone lacks sidechain inputs, a playhead and effect-chain setups, so test automation, offline rendering, bus layouts and sidechains in a real host before release.
- A user reported that Bitwig's plugin sandboxing allows near hot-swapping of builds (single report, check yourself).

Avoid these claims even when they appear in popular advice (checked while writing this skill):
- "Add a tiny offset like 1e-30f or use fast-math to flush denormals." Prefer `juce::ScopedNoDenormals`; fast-math flags change floating-point semantics for the whole program and can break NaN and infinity checks. Do not quote CPU-spike multipliers without measuring.
- Beginner posts that say plugins are written in C# or Objective-C. JUCE is C++.

JUCE DSP module (V: JUCE tutorial "Introduction to the DSP module"):
- Each processor has `prepare(ProcessSpec)`, `process(context)` and `reset()`. ProcessSpec holds sample rate, maximum block size and channel count.
- `juce::dsp::ProcessorChain<...>` runs processors in series; access members with `get<index>()` and name the indices with an enum.
- Wrap an AudioBuffer in `dsp::AudioBlock`, slice with `getSubBlock()`, process with `ProcessContextReplacing`.
- `dsp::Oscillator` takes a function and a lookup-table size. The tutorial oscillator is a plain table oscillator, not band-limited: for supersaws use PolyBLEP or mip-mapped wavetables and measure aliasing yourself (see 12).
- `dsp::LadderFilter` is a Moog-style ladder (12 dB low-pass by default). Update low-rate LFOs every N samples outside the chain to save CPU.
- The name is `juce::SmoothedValue` (not "SmoothValue" as some popular summaries write).

Frameworks besides JUCE named in forum threads: iPlug2, NIH-plug (Rust), Faust (functional DSP prototyping), HISE (built on JUCE), JSFX for prototyping inside Reaper. Check licence and format support of each before choosing. For a synth or an effect where the user wants VST3 on three desktop systems, JUCE is a sound default.

Reading list for DSP and plugin design (recommendations from the forum threads and a learning-path page, treat as opinion; the third item is a free web book):
- Will Pirkle, books on designing audio effect plugins and software synthesizer plug-ins in C++.
- Udo Zölzer, DAFX.
- Richard Lyons, Understanding Digital Signal Processing.
- Steven Smith, The Scientist and Engineer's Guide to Digital Signal Processing (free online).
- Vadim Zavalishin, The Art of VA Filter Design (free from Native Instruments).
- A suggested learning order: audio basics, C++ in the JUCE context, enough maths for filters, DSP fundamentals (FFT, filters, delays, nonlinear effects), then the framework.
- Real code to study: open-source synths and effects on GitHub. Read their licence first; copying code from a copyleft project into a project with a different licence is not allowed.

Architecture tip from a commercial developer interview: separate code into DSP, view and controller layers, and use assertions so errors break early; most bugs come from data exchange between threads.

## Sources

- JUCE forum, "Development cycle of a audio plugin": https://forum.juce.com/t/development-cycle-of-a-audio-plugin/57180
- Steinberg VST 3 Developer Portal, "Code your first plug-in": https://steinbergmedia.github.io/vst3_dev_portal/pages/Tutorials/Code+your+first+plug-in.html
- Lars Lentz Audio, "Creating and Programming Synths, Samplers, and VSTs": https://larslentzaudio.com/2020/05/03/creating-and-programming-synths-samplers-and-vsts/
- JUCE AudioProcessor docs: https://docs.juce.com/master/classAudioProcessor.html
- JUCE tutorial, Introduction to the DSP module: https://juce.com/tutorials/tutorial_dsp_introduction/
- Steinberg VST 3 Developer Portal, API documentation: https://steinbergmedia.github.io/vst3_dev_portal/
- JUCE forum threads on licensing and ScopedNoDenormals (forum, not official)
- Steinberg VST 3 Developer Portal, Plug-in Locations: https://steinbergmedia.github.io/vst3_dev_portal/pages/Technical+Documentation/Locations+Format/Plugin+Locations.html
- Flathub LinuxAudio BaseExtension: https://github.com/flathub/org.freedesktop.LinuxAudio.BaseExtension
- Apple, Notarizing macOS software before distribution: https://developer.apple.com/documentation/security/notarizing-macos-software-before-distribution
- Microsoft, Code signing options: https://learn.microsoft.com/en-us/windows/apps/package-and-deploy/code-signing-options
- GitHub, About releases: https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases
- Tracktion pluginval: https://github.com/Tracktion/pluginval
- Välimäki, Nam, Smith, Abel, "Alias-suppressed oscillators based on differentiated polynomial waveforms", IEEE TASLP 18(4), 2010
- Zavalishin, "The Art of VA Filter Design", rev. 2.1.0, Native Instruments
- R. Bristow-Johnson, Audio EQ Cookbook (W3C Working Group Note): https://www.w3.org/TR/audio-eq-cookbook
- Roland JP-8000 (Wikipedia) and its cited analyses by A. Szabo (2010) and A. Shore (2013)
