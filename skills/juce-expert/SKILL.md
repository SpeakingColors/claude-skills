---
name: juce-expert
description: Use when developing JUCE audio plugins (VST3, AU, CLAP), covering CMake, realtime safety, quality and CPU, parameters, state, GUI incl. Visage, testing and licensing.
---

# JUCE expert

Research date: 2026-10-23. Written for the reader and the assistant helping them. The reader may not be a programmer, so each topic gives the idea first, then the exact code or setting.

## How to read the labels

- VERIFIED (S#): read on a page that was fetched; the source number points to the Sources list at the end.
- COMMUNITY: forum post, blog or third-party project page; useful, not official.
- UNVERIFIED: not checked in this research. Treat as a lead, test it, never state it as fact.
- Nothing here is copied from a source; facts were learned and rewritten. Always re-check the live page, versions move.

## 1. Licensing (not legal advice, read the licence page yourself)

Idea: JUCE is dual licensed. You pick one licence for your product. Your choice decides whether you must publish your source code.

- VERIFIED (S1, S4): JUCE modules can be used under AGPLv3 (open source) or under the commercial JUCE licence. Using the framework under the commercial option binds you to the JUCE End User Licence Agreement.
- VERIFIED (S4): the linked licence text is the JUCE 9 EULA. The JUCE examples are under the ISC licence. Third-party code inside JUCE has its own licences, listed in a JUCE.spdx.json file in the repo.
- VERIFIED (S4): the JUCE team does not confirm whether your use complies; get your own legal advice.
- AGPLv3 in plain words (UNVERIFIED, general knowledge of the licence): if you distribute a plugin built with it, you must offer the full source of the plugin under AGPLv3 too. A free open source plugin with a public repo fits this well.
- Commercial tiers: names Starter, Indie and Pro, with yearly revenue limits, existed for JUCE 8 (COMMUNITY, S9). Forum figures varied between posts and were not final, so no numbers are given here. JUCE 9 tiers and prices: UNVERIFIED (the juce.com licence and pricing pages could not be fetched). Read https://juce.com/get-juce before choosing.
- COMMUNITY (S9): the forum thread says revenue is counted over the previous 12 months and can include revenue outside JUCE products. Check the exact wording in the EULA.
- Splash screen and "made with JUCE" rules per tier: UNVERIFIED.
- VERIFIED (S6): the Steinberg VST3 SDK is licensed under MIT; the repo page says GPLv3 and the proprietary Steinberg licence are no longer offered. Docs describe SDK 3.8.x.
- VERIFIED (S7): the CLAP project repo is MIT licensed. VERIFIED (S12): clap-juce-extensions is MIT too.
- AAX plugins need Avid signing with PACE tools, free from Avid, and Pro Tools Developer for testing (S1). VST2 needs the old Steinberg SDK; avoid it for new work (S2 says VST2 needs a separate SDK path).
- Rule of thumb for the assistant: when the reader asks about shipping, tell them the licence may require a commercial licence (S1 asks assistants to say this) and point to the licence page.

## 2. Versions and getting JUCE

- VERIFIED (S5, S13, S14): latest release page showed JUCE 9.0.2 (listed as 7 September); JUCE 9.0.0 was listed as 21 July. The page shows no year; the year is UNVERIFIED, assume 2026.
- VERIFIED (S1): `master` carries stable tagged releases, `develop` carries the newest work. The version is in the `JUCE_MAJOR_VERSION`, `JUCE_MINOR_VERSION`, `JUCE_BUILDNUMBER` macros.
- VERIFIED (S1) toolchains: C++17 (C++20 only when `JUCE_USE_WINDOWS_MIDI_SERVICES` is on); macOS and iOS need Xcode 12.4 or newer; Windows needs Visual Studio 2019; Linux needs g++ 7 or Clang 6; CMake 3.22 or newer.
- VERIFIED (S1) deployment targets: macOS 10.11 (Intel and Apple silicon), Windows 10 1607, mainstream Linux on x86_64 and aarch64, iOS 12, Android 7. These numbers are the README's; the README for a newer tag may differ, re-check.
- VERIFIED (S13): JUCE 9.0.0 headline items: new SVG parser, variable fonts, new CoreAudio code, faster software renderer, OpenGL ES on Linux, multi-touch on Linux and Windows, better CMake for headless builds.
- VERIFIED (S14) JUCE 9 breaking changes to watch: Linux needs `libxi-dev` unless `JUCE_USE_XINPUT=0`; `Drawable` no longer inherits from `Component` (wrap in `DrawableComponent`); Linux OpenGL moved from GLX to EGL (may need `libegl-dev`); `Drawable::createFromSVG(const XmlElement&)` removed (use `createFromSVGFile()` or `createFromSVGString()`); OpenGL image cache size now counts bytes.
- Always read BREAKING_CHANGES.md in the repo before upgrading (S1 says so).
- Ways to get JUCE with CMake:
  - VERIFIED (S2): `add_subdirectory(JUCE)` after putting JUCE in your tree, or install JUCE and use `find_package(JUCE CONFIG REQUIRED)`.
  - COMMUNITY (S31): the Pamplejuce template tracks JUCE as a git submodule and uses CPM for other dependencies.
  - FetchContent: the CMake API doc does not cover it (S2). The idea is "let CMake download JUCE at configure time". Snippet below is the common pattern, UNVERIFIED for JUCE 9; pin a tag, never a branch:
```cmake
include(FetchContent)
FetchContent_Declare(JUCE GIT_REPOSITORY https://github.com/juce-framework/JUCE.git GIT_TAG <tag>)
FetchContent_MakeAvailable(JUCE)
```
- Projucer: VERIFIED (S1) there is no prebuilt binary in the repo; you build it from the project files in `extras/Projucer/Builds`. New projects should prefer CMake.
- CLAP in JUCE: see section 11.

## 3. Project setup with CMake

Idea: one `CMakeLists.txt` describes the plugin; CMake then makes one build target per format.

Minimal shape (VERIFIED pattern from S18, written fresh):
```cmake
cmake_minimum_required(VERSION 3.22)
project(MyPlugin VERSION 0.1.0)
add_subdirectory(JUCE)
juce_add_plugin(MyPlugin
    COMPANY_NAME "My Studio"
    PLUGIN_MANUFACTURER_CODE Mystd
    PLUGIN_CODE Mypl
    FORMATS VST3 Standalone
    PRODUCT_NAME "My Plugin"
    IS_SYNTH FALSE
    NEEDS_MIDI_INPUT FALSE
    COPY_PLUGIN_AFTER_BUILD TRUE)
target_sources(MyPlugin PRIVATE PluginProcessor.cpp PluginEditor.cpp)
target_compile_definitions(MyPlugin PUBLIC JUCE_WEB_BROWSER=0 JUCE_USE_CURL=0
    JUCE_VST3_CAN_REPLACE_VST2=0)
target_link_libraries(MyPlugin PRIVATE juce::juce_audio_utils
    PUBLIC juce::juce_recommended_config_flags juce::juce_recommended_lto_flags
           juce::juce_recommended_warning_flags)
```

Key `juce_add_plugin` arguments (all VERIFIED, S2):
- `FORMATS`: space separated list from Standalone, Unity, VST3, AU, AUv3, AAX, VST, LV2. AU and AUv3 only build on macOS; AUv3 needs the Xcode generator; VST needs `juce_set_vst2_sdk_path` first.
- `PLUGIN_MANUFACTURER_CODE`: 4 characters, at least one uppercase letter (AU rule). Default `Manu`.
- `PLUGIN_CODE`: 4 characters, exactly one uppercase letter for AU. Default is random each configure, so set it yourself and never change it after release, hosts use it to find saved projects.
- `IS_SYNTH`: sets sensible category defaults. `NEEDS_MIDI_INPUT` and `NEEDS_MIDI_OUTPUT`: declare MIDI in and out. `IS_MIDI_EFFECT`: for pure MIDI plugins.
- `COPY_PLUGIN_AFTER_BUILD`: installs the built plugin to the default location for the format; on Windows the default folder may need admin rights.
- `VST3_CATEGORIES`: words such as `Fx`, `Instrument`, `Synth`, `Reverb`, `EQ`. `AU_MAIN_TYPE`: for example `kAudioUnitType_Effect` or `kAudioUnitType_MusicDevice`.
- `PLUGIN_NAME` (name in hosts), `PRODUCT_NAME` (output file name), `DESCRIPTION`, `EDITOR_WANTS_KEYBOARD_FOCUS`, `NEEDS_WEB_BROWSER`, `NEEDS_CURL`, per-format `*_COPY_DIR`.
- Header choice: `juce_generate_juce_header(MyPlugin)` makes a `JuceHeader.h` that includes every linked module and may add `using namespace juce`. It is optional; you can include single modules directly, for example `#include <juce_audio_processors/juce_audio_processors.h>` (S2). Direct includes compile faster and are clearer.
- Why turn off web browser and curl: they pull in extra system libraries on Linux (S3, S18). Disable them unless the plugin needs them.
- Why `JUCE_VST3_CAN_REPLACE_VST2=0`: stops the VST3 from posing as an older VST2 with the same ID (S18).

Build commands (generic CMake usage, UNVERIFIED for your exact project but standard):
```
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release -j
```
- Linux: as above with Ninja or Makefiles; Clang or g++.
- macOS: add `-DCMAKE_OSX_ARCHITECTURES="arm64;x86_64"` for a universal build (S2 confirms this option); Xcode generator `-G Xcode` is needed for AUv3 only.
- Windows: `cmake -B build -G "Visual Studio 17 2022"` then `cmake --build build --config Release` (generator name UNVERIFIED, depends on installed Visual Studio). MSVC and Clang-cl are supported (S2).
- Build output sits in `build/<Target>_artefacts/<Config>/<Format>/`.

Linux build dependencies:
- VERIFIED (S3), Ubuntu, from the official list:
```
sudo apt install clang libasound2-dev libjack-jackd2-dev ladspa-sdk libcurl4-openssl-dev \
  libfreetype-dev libfontconfig1-dev libx11-dev libxcomposite-dev libxcursor-dev \
  libxext-dev libxinerama-dev libxrandr-dev libxrender-dev libxi-dev \
  libwebkit2gtk-4.1-dev libegl-dev libglu1-mesa-dev mesa-common-dev
```
- Each package maps to a module (S3); you can skip a package if you set its switch to 0, for example `JUCE_WEB_BROWSER=0`, `JUCE_USE_CURL=0`, `JUCE_JACK=0`, `JUCE_USE_XINERAMA=0`.
- Fedora: the official page covers Ubuntu only (S3). A forum user listed Fedora equivalents by topic (clang, freetype, X11, Xinerama, Xrandr, Xcursor, Mesa GL, ALSA, Xcomposite, libcurl; S28, COMMUNITY). Likely package names, UNVERIFIED: `alsa-lib-devel freetype-devel fontconfig-devel libX11-devel libXcomposite-devel libXcursor-devel libXext-devel libXinerama-devel libXrandr-devel libXrender-devel libXi-devel libcurl-devel mesa-libGL-devel mesa-libEGL-devel libglvnd-devel pipewire-jack-audio-connection-kit-devel`. Check with `dnf search`.
- Bazzite and other immutable distros: the system is read-only, so do not layer dev packages on the host. VERIFIED (S32) that Distrobox gives a mutable container on immutable systems (Fedora Atomic is named; Bazzite is not named on that page). Pattern:
```
distrobox create -n juce-dev -i fedora:latest
distrobox enter juce-dev
```
  Install the packages and build inside. The container shares your home folder, so the plugin lands in `~/.vst3`. Whether a plugin built in a container runs on the host: see GLIBC in section 13.

## 4. Plugin architecture

Idea: two classes. The processor does sound and owns the data; the editor is only the window and can be created and destroyed at any time.

- `AudioProcessor`: your sound engine (VERIFIED, S15). Key virtuals: `prepareToPlay(double sampleRate, int maxBlock)` runs before playback starts; `processBlock(AudioBuffer<float>&, MidiBuffer&)` renders each block; `releaseResources()` runs after stop; `getStateInformation(MemoryBlock&)` and `setStateInformation(const void*, int)` save and restore state; `getTailLengthSeconds()` reports the tail.
- `AudioProcessorEditor`: the GUI. Created in `createEditor()`, tied to its processor by reference (S25). Never keep audio-critical state in the editor.
- Skeleton of `processBlock` (own example):
```cpp
void processBlock (juce::AudioBuffer<float>& buf, juce::MidiBuffer& midi) override
{
    juce::ScopedNoDenormals noDenormals;
    for (auto i = getTotalNumInputChannels(); i < getTotalNumOutputChannels(); ++i)
        buf.clear (i, 0, buf.getNumSamples());   // silence unused outputs
    // read parameters, then process each channel
}
```
- Buses: declare channels in the constructor with `BusesProperties().withInput(...).withOutput(...)`. The docs list `checkBusesLayoutSupported` (S15); the usual override is `isBusesLayoutSupported`, UNVERIFIED on the current page. Typical rule: accept mono or stereo and require input layout equal output layout for effects.
- MIDI: `MidiBuffer` arrives in `processBlock`; iterate with `for (auto m : midi)`, each item has `getMessage()` and `samplePosition`. Remember `NEEDS_MIDI_INPUT TRUE` in CMake (S2) or hosts will not send MIDI.
- Host info: `getPlayHead()` gives tempo and position (UNVERIFIED on exact current API shape, check the header).
- Bypass: `processBlockBypassed` exists (S15); better, expose a bypass parameter so hosts can automate it.
- `suspendProcessing(true)` and `getCallbackLock()` exist (S15) but the lock is for non-audio code; do not lock in the audio path.

## 5. Realtime safety and threads

Idea: the audio thread has a hard deadline of a few milliseconds. If it waits for anything, you hear a click or dropout. So it may only do quick, predictable work.

Rules for `processBlock` (general practice; the Ross Bencina article could not be fetched, so treat as UNVERIFIED but widely accepted):
- No memory allocation or free: no `new`, `std::vector::push_back` or resize, `std::string` building, `juce::String` building, `AudioBuffer` resizing. Allocate in `prepareToPlay`.
- No locks: no `std::mutex`, no `CriticalSection`, no `ScopedLock`. VERIFIED (S19): `copyState` and `replaceState` use internal locks, so never call them from the audio thread.
- No file or network access, no `DBG`/printing/logging, no `Thread::sleep`, no waiting for another thread.
- No exceptions thrown in the audio path; no unbounded loops; avoid virtual calls into unknown code.
- Denormals: put `juce::ScopedNoDenormals noDenormals;` at the top of `processBlock` (VERIFIED, S22: it turns denormals off on entry and restores on exit; works with SSE and ARM NEON). `FloatVectorOperations::disableDenormalisedNumberSupport()` is the global switch.

Safe ways to talk between threads:
- Single numbers: `std::atomic<float>` or `std::atomic<bool>`. VERIFIED (S19): `getRawParameterValue("id")` returns a pointer to an atomic float the audio thread can read without a lock.
- Streams of values (meter data, scope samples, MIDI to the GUI): `juce::AbstractFifo` (VERIFIED, S21). It supports one reader thread and one writer thread, stores no data itself (you own the array), and gives you one or two index ranges via `prepareToWrite/finishedWrite` and `prepareToRead/finishedRead`. Usable capacity is the size minus one.
- Big objects (new impulse response, new wavetable): build on the message thread, then hand over with an atomic pointer swap or a lock-free queue; free the old one off the audio thread (UNVERIFIED pattern, widely used).

Threads in plain words (UNVERIFIED, general JUCE knowledge):
- Message thread: GUI, timers, `AsyncUpdater`, file dialogs, creating components. Never block it long either.
- Audio thread: `processBlock`. Host may also call `setStateInformation` from another thread, so keep it safe.
- GUI refresh from audio data: use a `juce::Timer` in the editor (30 to 60 Hz) that reads atomics or the FIFO. `AsyncUpdater::triggerAsyncUpdate()` can wake the message thread, but do not call it per sample.

## 6. Parameters

Idea: a parameter is a named knob the host can automate and save. `AudioProcessorValueTreeState` (APVTS) stores all of them and connects them to the GUI.

- Build a layout, then pass it to the APVTS (VERIFIED, S19: `ParameterLayout` collects `RangedAudioParameter` objects and groups; the older `createAndAddParameter` overloads are deprecated).
```cpp
static juce::AudioProcessorValueTreeState::ParameterLayout makeLayout()
{
    juce::AudioProcessorValueTreeState::ParameterLayout l;
    l.add (std::make_unique<juce::AudioParameterFloat> (
        juce::ParameterID { "gain", 1 }, "Gain",
        juce::NormalisableRange<float> (-60.0f, 12.0f), 0.0f));
    return l;
}
// member: juce::AudioProcessorValueTreeState apvts { *this, nullptr, "STATE", makeLayout() };
```
- `ParameterID { "gain", 1 }` pairs the text ID with a version number (VERIFIED, S19 shows the pairing; its meaning is not explained there). Meaning, UNVERIFIED but standard: AU hosts need the version hint to keep parameters stable; raise the version number only for parameters added in later releases, and never change an existing ID, or saved projects and automation break.
- Reading in audio code: store `std::atomic<float>* gain = apvts.getRawParameterValue("gain");` once, then `gain->load()` per block (VERIFIED, S19; inside a `parameterChanged` callback the value may not be updated yet).
- GUI link: `SliderAttachment`, `ComboBoxAttachment`, `ButtonAttachment` (VERIFIED, S19). The attachment must be destroyed before the control and before the APVTS, so declare attachment members after the controls.
- Undo: pass an `UndoManager*` instead of `nullptr` if you want undo (S19).
- Smoothing: jumping a value causes zipper noise. VERIFIED (S20): `SmoothedValue` ramps to a target; `reset(sampleRate, seconds)` sets ramp length, `setTargetValue` starts a ramp, `getNextValue` per sample, `skip(n)` jumps ahead. `Linear` suits gain and pan; `Multiplicative` suits frequency, but it can never reach zero.
```cpp
juce::SmoothedValue<float> g;           // in prepareToPlay: g.reset (sampleRate, 0.02);
g.setTargetValue (gainPtr->load());     // once per block
for (int i = 0; i < n; ++i) sample *= g.getNextValue();
```
- Sample rate and buffer size can change: always redo `reset(...)` and re-size internal buffers in `prepareToPlay`, never assume 44100 or a fixed block (UNVERIFIED rule, but `prepareToPlay` is documented as the setup hook, S15).
- Latency: call `setLatencySamples(n)` when your effect delays the signal (VERIFIED, S15). Whole samples only; hosts compensate. Oversampling filters add latency (S24).
- Tail: `getTailLengthSeconds()` tells hosts how long sound continues after input stops (reverb, delay) so they do not cut it off (S15).
- Automation tips (UNVERIFIED): use `beginChangeGesture`/`endChangeGesture` (done for you by attachments) when the GUI moves a knob; avoid heavy work inside parameter callbacks.

## 7. State and presets

Idea: the host saves your plugin state as a blob and gives it back later. Put every setting in the APVTS tree so one save covers it all.

- Save (own example, standard pattern):
```cpp
void getStateInformation (juce::MemoryBlock& dest) override
{
    auto state = apvts.copyState();
    if (auto xml = state.createXml()) copyXmlToBinary (*xml, dest);
}
void setStateInformation (const void* data, int size) override
{
    if (auto xml = getXmlFromBinary (data, size))
        if (xml->hasTagName (apvts.state.getType()))
            apvts.replaceState (juce::ValueTree::fromXml (*xml));
}
```
- VERIFIED (S19): `copyState` and `replaceState` are the thread-safe way to read or swap the whole tree, but they lock, so keep them off the audio thread.
- Versioning: add a `version` property to the tree root when saving. On load, if the number is older, fill in defaults or rename old IDs before calling `replaceState` (pattern, UNVERIFIED). Never reuse an ID for a different meaning.
- Binary vs XML: XML is readable and easy to debug; binary (`ValueTree::writeToStream`) is smaller. Pick one and keep it for compatibility.
- Extra non-parameter data (current preset name, window size, user text): store as properties on `apvts.state`.
- Preset files: use `File::getSpecialLocation(File::userApplicationDataDirectory)` plus a company and product folder. Typical per-OS locations (UNVERIFIED convention, not checked against JUCE docs): Windows `%APPDATA%\Company\Product\Presets`, macOS `~/Library/Application Support/Company/Product/Presets`, Linux `~/.config/Company/Product/Presets`. Offer factory presets inside the binary (see section 9 for BinaryData).
- Do preset loading on the message thread, never on the audio thread.

## 8. DSP module essentials (juce_dsp)

Idea: small building blocks you prepare once and then run on every block.

- `dsp::ProcessSpec` holds sample rate, maximum block size and channel count and is passed to each block's `prepare()` (VERIFIED, S23).
- `ProcessContextReplacing` processes a block in place; `ProcessContextNonReplacing` has separate input and output blocks (VERIFIED, S23). Wrap your buffer with `dsp::AudioBlock<float> block (buffer);`.
- `dsp::ProcessorChain<A, B, ...>` runs several processors in order (name from JUCE docs, details UNVERIFIED in this research; check the header).
- Filters: `dsp::IIR::Filter`, `dsp::StateVariableTPTFilter`, `dsp::Gain`, `dsp::Reverb`, `dsp::Convolution` exist in the module (UNVERIFIED here, check the module header for current class names and signatures).
- Oversampling (VERIFIED, S24): `dsp::Oversampling<float>(channels, factorPowerOfTwo, filterType, isMaxQuality, useIntegerLatency)`. Call `initProcessing(maxBlock)` first, `processSamplesUp(block)` to get the faster-rate block, run your non-linear code at `sampleRate * factor`, then `processSamplesDown(outputBlock)`. `getLatencyInSamples()` can be fractional; round and report it with `setLatencySamples`. Half-band FIR gives linear phase with more latency; polyphase IIR gives lower latency with phase change near Nyquist. Call `reset()` after transport jumps.
- Anti-aliasing: distortion, waveshapers, hard-sync and saw oscillators create harmonics above half the sample rate that fold back as ugly noise. Fixes: oversample (2x to 8x), use band-limited oscillators (PolyBLEP/wavetable), and filter after the non-linear stage (general DSP knowledge, UNVERIFIED here).
- Denormals: tiny numbers near zero (decaying filters and reverbs) make CPU spike. Use `ScopedNoDenormals` (S22) and avoid feedback paths that decay forever; add a tiny offset only if needed.
- Test DSP at 44.1, 48, 88.2, 96 and 192 kHz; many bugs only show at one rate.

## 9. GUI

Idea: everything on screen is a `Component`. You set sizes in `resized()` and draw in `paint()`.

- Layout: use `juce::Rectangle` splitting (`removeFromTop`, `reduced`) or `FlexBox`/`Grid` in `resized()`. Do not hard-code pixel positions for every item.
- Look: subclass `juce::LookAndFeel_V4`, override `drawRotarySlider` etc., and call `setLookAndFeel(&myLnf)` in the editor; set it back to `nullptr` in the destructor, and keep the LookAndFeel object alive longer than components that use it (standard practice, UNVERIFIED here).
- Resizing (VERIFIED, S25): `setResizable(allowHostToResize, useCornerResizer)`; `setResizeLimits(minW, minH, maxW, maxH)` sets min and max and makes the editor host-resizable; `setConstrainer(ptr)` takes your own `ComponentBoundsConstrainer` and does not own it, so keep it alive; `setConstrainer(nullptr)` removes constraints. For fixed aspect ratio, use `ComponentBoundsConstrainer::setFixedAspectRatio` (name known from the JUCE API, header not fetched, UNVERIFIED).
- Save and restore the editor size in the state tree so the window reopens at the same size (pattern, UNVERIFIED).
- HiDPI: JUCE scales components by the display scale; draw with vector paths and `Graphics` instead of fixed-size bitmaps, and provide `@2x` images or SVG. `setScaleFactor` is a hook a host can call (S25). JUCE 9 has a new SVG parser (S13).
- Assets: `juce_add_binary_data(MyAssets SOURCES logo.svg font.ttf)` bundles files into code (VERIFIED as an option, S18). Link the target and read via `BinaryData::logo_svg` and `BinaryData::logo_svgSize` (usual naming, UNVERIFIED).
- OpenGL caution (UNVERIFIED, community experience): `OpenGLContext` inside plugins can fail or flicker on some hosts and drivers, and uses extra resources; start with the software renderer. JUCE 9 moved Linux GL to EGL (S14).
- Linux specifics: the plugin window is an X11 child of the host's window; keyboard focus can be flaky in some hosts (UNVERIFIED). The CMake key `EDITOR_WANTS_KEYBOARD_FOCUS` exists (S2) for plugins that need typing (preset name boxes).
- Never do heavy work in `paint()`; cache images; use `repaint()` regions; timers at 30 Hz are enough for meters.
- Mockup rule: if a design mockup was approved, the real editor should match it, build to the mockup and compare screenshots.

## 10. Formats, hosts and scan paths

- VST3: JUCE builds it natively (S2). A `.vst3` is a folder bundle.
- AU: macOS only (S2). Needs a correct manufacturer code (uppercase letter) and component type (`AU_MAIN_TYPE`).
- Standalone: a normal app with a built-in audio and MIDI settings window; good for quick tests without a host (S2).
- LV2 is available as a format (S2).
- CLAP: the JUCE 9 releases and breaking-changes notes fetched here never mention CLAP (S5, S13, S14). The older JUCE roadmap said JUCE 9 was planned to support CLAP (S8, COMMUNITY-level plan, may have changed). Current native support in JUCE 9.0.2: UNVERIFIED, check the release notes and `juce_add_plugin` docs. Proven route: the unofficial `clap-juce-extensions` (S12): add it with `add_subdirectory`, then call `clap_juce_extensions_plugin(TARGET MyPlugin CLAP_ID "com.me.myplugin" CLAP_FEATURES ...)` to get a `MyPlugin_CLAP` target. Its README names JUCE 6, 7 and 8 only; JUCE 9 compatibility is UNVERIFIED. Known gaps (S12): not supported by the JUCE team, stepped parameters do not translate, CLAP hosting not supported.
- Scan paths (where hosts look):
  - VST3 macOS: `/Library/Audio/Plug-ins/VST3` (VERIFIED, S30); user folder `~/Library/Audio/Plug-Ins/VST3` is rarely used per S30.
  - VST3 Linux: user folder `~/.vst3` (COMMUNITY, S11, S29). System folders such as `/usr/lib/vst3` and `/usr/local/lib/vst3`: UNVERIFIED.
  - VST3 Windows: `C:\Program Files\Common Files\VST3`: UNVERIFIED (the Steinberg portal page could not be fetched).
  - CLAP (VERIFIED, S26, from the CLAP header): Linux `~/.clap` and `/usr/lib/clap`; Windows the Common Files `CLAP` folder and a per-user LocalAppData folder; macOS `/Library/Audio/Plug-Ins/CLAP` and `~/Library/Audio/Plug-Ins/CLAP`. The `CLAP_PATH` environment variable adds more folders, split by colon on Unix and semicolon on Windows, searched recursively.
  - AU: `~/Library/Audio/Plug-Ins/Components` and `/Library/Audio/Plug-Ins/Components` (UNVERIFIED).
- Flatpak hosts (UNVERIFIED): a host installed as a Flatpak runs in a sandbox and may not see `~/.vst3` or `~/.clap`. Check that host's documentation for its own plugin folder or for granting filesystem access; also, a plugin using system libraries absent in the Flatpak runtime may fail to load.
- Host differences: always test in at least two hosts per OS; different hosts differ on editor resizing, parameter flush on state load, and bus layouts (UNVERIFIED general experience).

## 11. Testing

Idea: test with a strict validator, then test sound, then test in real hosts.

- pluginval (VERIFIED, S16, S17, S34): validates VST, VST3 and AU on macOS, Windows, Linux, runs the plugin in a separate process so crashes do not kill the tool; exit code 0 means pass, 1 means fail.
  - Strictness 1 to 10; level 5 is the lowest generally recognised for host compatibility; higher levels run long tests such as parameter fuzzing and repeated state restore.
  - CLI: `pluginval --strictness-level 5 --skip-gui-tests --output-dir logs "path/to/My Plugin.vst3"` (S17 shows the subcommand `validate`, so the full form is likely `pluginval validate --strictness-level 5 <plugin>`; check `pluginval -h`). Other flags from S17: `--junit-xml <file>`, `--json-results <file>`.
  - Downloads (S17): `https://github.com/Tracktion/pluginval/releases/latest/download/pluginval_Linux.zip` (also `_macOS.zip`, `_Windows.zip`). Windows also has `choco install pluginval`.
  - GitHub Action (S17): `Tracktion/pluginval/validate@v2` with plugin paths and a strictness level.
- JUCE `UnitTest` (VERIFIED, S27): subclass `juce::UnitTest`, implement `runTest()`, group checks with `beginTest("name")`, check with `expect` and `expectEquals`; a static instance registers itself; run with `UnitTestRunner`. Good for DSP math and state migration.
- auval on macOS (UNVERIFIED, not fetched): Apple's tool `auval -v aufx Abcd Manu` validates AU plugins (type, plugin code, manufacturer code; match your CMake codes).
- Memory and thread bugs (UNVERIFIED tool names, standard practice): Valgrind on Linux for leaks and bad reads; AddressSanitizer (`-fsanitize=address`) and ThreadSanitizer (`-fsanitize=thread`) in a debug build of the Standalone.
- Audio tests (own checklist): null test (process, invert, sum, expect silence), bypass should equal input exactly, sweep sample rates (44.1 to 192 kHz) and block sizes (1, 7, 64, 512, 4096), odd sizes catch buffer bugs; feed silence, full scale, NaN and Inf and check for no blow-up; render the same audio offline and in realtime and compare (the offline flag is `isNonRealtime()`, UNVERIFIED on exact name).
- CI: the Pamplejuce template (COMMUNITY, S31) builds on Linux, macOS and Windows with GitHub Actions, runs tests and pluginval, and has optional macOS signing and notarisation and Windows signing steps. Read its docs for the exact matrix.

## 12. Packaging, signing and versioning

All items in this section are UNVERIFIED unless a source is given; the Apple page body could not be fetched.

- Version rule: one version number in `project(... VERSION x.y.z)` and in `juce_add_plugin` (default follows the project); tag releases in git with the same number.
- macOS: sign with a Developer ID Application certificate and hardened runtime, then submit with `xcrun notarytool submit file.zip --keychain-profile name --wait`, then `xcrun stapler staple` the app or installer. Sign every plugin bundle (VST3, AU, standalone) and the installer.
- macOS universal binary: `CMAKE_OSX_ARCHITECTURES="arm64;x86_64"` (S2).
- Windows: sign the DLLs and installer with a code-signing certificate (or a cloud signing service, S31 mentions Azure Trusted Signing). Unsigned installers trigger SmartScreen warnings. Installer tools: Inno Setup or WiX; install VST3 to the Common Files VST3 folder.
- Linux: a `.tar.gz` with the `.vst3` folder and a short install note is the simplest; users copy to `~/.vst3`. Flatpak packaging of the plugin is possible but more work (extension runtime layout), check the host app's Flatpak plugin extension docs.
- Always ship a checksum file and a changelog. Free open source projects: keep the AGPLv3 text and source link in the download.

## 13. Common mistakes and debugging

- Host crashes while scanning: the plugin crashes in the constructor or `createEditor`. Fix: no heavy work in constructors, no file or network access at load, run pluginval at level 5 or higher and test in the Standalone first.
- Plugin not found by host: wrong folder, host not rescanning, or build for the wrong CPU. See section 10 and check the file is the bundle, not just a library.
- Duplicate or changing IDs: `PLUGIN_CODE` left random (S2 says default is random per configure) makes each build look like a new plugin.
- GLIBC errors on Linux ("version GLIBC_2.xx not found"): a plugin built on a newer system will not load on an older one, because it needs newer system libraries. Build on the oldest distro you want to support (a container such as S32 helps) and test on that. Source for the concept: UNVERIFIED general knowledge.
- Static linking: ship plugins that link `libstdc++` and libgcc statically on Linux with `-static-libstdc++ -static-libgcc` (UNVERIFIED trick) to reduce clashes with the host; do not statically link GLIBC.
- Missing shared libraries on a user's machine: run `ldd MyPlugin.so` inside `MyPlugin.vst3/Contents/x86_64-linux/` and fix anything marked "not found". Disabling curl and web browser (S18) removes two common ones.
- CPU spikes with silence: denormals (S22); use `ScopedNoDenormals`.
- Clicks when moving knobs: no smoothing (S20).
- Crash on editor close: attachment or LookAndFeel destroyed in the wrong order (section 6, 9).
- Silent plugin in a synth host: forgot `IS_SYNTH` or `NEEDS_MIDI_INPUT` (S2) or did not clear the buffer first.
- Debugging tips (UNVERIFIED but standard): Debug build of the Standalone with a debugger; `jassert` for assumptions; do not use `DBG` in `processBlock`; reproduce host bugs with the smallest project.

## 13b. Quality and performance checklist (JUCE plugins)
Short list; the long version with sources is in `vst-maker` (sections 2, 4, 6, 12), `plugin-dsp-quality` and `plugin-ship-checklist`. Load them together.
- Sound: oversample or band-limit every non-linear stage and oscillator (see section 8), smooth every parameter, check for DC, NaN and clipping, test at 44.1, 48, 96 and 192 kHz.
- CPU: no allocation, locks or file access in `processBlock` (section 5); precompute coefficients when a parameter changes, not per sample; use `ScopedNoDenormals`; measure with an offline render, not by feel.
- Latency: report every delay with `setLatencySamples` and check in two hosts.
- GUI cost: a busy editor must not steal audio time. Repaint only what changed, use timers at 30 to 60 Hz at most, never touch the audio thread from the editor.
- Verify with pluginval (section 11) on every build, and keep a worst-case preset for CPU tests.

## 13c. Visage (GPU UI library) with JUCE
Idea: Visage is an alternative way to draw a plugin window with the GPU instead of JUCE's own Component painting. Treat it as an advanced option; JUCE's own GUI is the safe default.
- What it is (VERIFIED, S35 github.com/VitalAudio/visage README): a GPU-accelerated cross-platform C++ library for native UI and 2D graphics, MIT licence. Backends: Direct3D11 on Windows, Metal on macOS, Vulkan on Linux, WebGL on web. Features listed: event and window normalisation, Unicode text entry, partial redraw of dirty regions, drawing at the monitor refresh rate, automatic shape batching, blend modes, shader transpilation, blur and bloom effects. Modules: visage_app, visage_graphics, visage_ui, visage_utils, visage_widgets, visage_windowing, visage_file_embed. Basic example: `visage::ApplicationWindow` with an `onDraw()` callback that receives a `visage::Canvas&`.
- Origin (COMMUNITY, S36 forum.hise.audio post 97122): the VitalAudio organisation hosts it; developers say adopting it in a JUCE-based framework would be a large change.
- Embedding in a JUCE plugin editor, focus and keyboard handling, destruction order, popups, Linux Vulkan package needs, and host quirks: UNVERIFIED here. The README does not cover plugin use. Before committing, build the repo's examples, then make a tiny test plugin and open it in two hosts on each OS you ship.
- Risks to test (UNVERIFIED, general): extra GPU driver dependency on Linux (Vulkan), behaviour inside sandboxed hosts and Flatpak, window resizing and HiDPI, and keyboard focus inside the host window.
- Plan: keep the audio and parameter code independent of the UI so the UI can change later. Prototype one control (a knob) first and compare CPU and idle GPU use against a plain JUCE editor.
- Licence: MIT requires keeping the copyright notice with copies of the code; read the repo LICENSE file.
- Third-party integration notes for macOS and iOS (COMMUNITY, from a published JUCE+Visage guide; not tested here, treat as leads). JUCE owns the plugin window; Visage runs its own Metal render loop in an embedded view, so mouse, keyboard, clipboard, cursor, focus and resize events must be bridged by hand. Patterns reported: create the Visage window late (start a short timer in the editor constructor and build only once the component is showing, has a native peer and non-zero size); set child bounds in a layout function that runs on every resize, not at creation, because DPI may still read 1.0 then; on destruction stop the render loop first, then destroy overlays, panels and frames, disconnect the bridge, and free the bridge last (the display link holds raw pointers and can fire at 60 to 120 Hz); map Cmd to the right modifier and give the key-combo shortcuts explicit key codes; toggle keyboard focus only while a text field is active; render popups and modals inside the GPU layer instead of using native JUCE popups; on iOS let the GPU view handle touches and do not forward JUCE mouse events (double events), respect safe-area insets, keep touch targets at least 44 pt. Keep a per-project notes file (patches applied, destruction order, popup list, known issues).
- Template idea (COMMUNITY): a starter repo with placeholder names, fixed plugin codes, a settings file for developer identity and signing values (never commit the secret ones), CMake FetchContent for JUCE and CLAP extensions, and an optional GPU-UI switch. Writing your own template once saves repeating the setup in section 3.

## 13d. Extra JUCE habits (from a best-practice guide with no licence found; ideas rewritten, none copied)
- Cross-thread: simple values travel by atomics; audio-to-UI events by `AsyncUpdater` or a FIFO read from an editor timer; never call `repaint()` or any editor method from `processBlock`.
- Always do setup in `prepareToPlay` from the real sample rate (no hard-coded 44100) and call the base class method if you override one that has a base implementation.
- Version the state and migrate old versions in `setStateInformation` (section 7).
- Hoist per-sample maths (coefficients, `exp`, `pow`) out of the loop; recompute only when a parameter changes.
- SIMD: `dsp::SIMDRegister` exists for hand vectorising; measure before using it, and prefer `FloatVectorOperations` and compiler auto-vectorisation first (UNVERIFIED, not benchmarked here).
- Denormals: use `ScopedNoDenormals` (section 5). Adding a tiny constant such as 1e-20 in feedback loops is a common alternative, but it adds a DC offset; prefer the scope guard.
- Disabling C++ exceptions for audio code is sometimes advised; JUCE and the standard library may still throw elsewhere, so just never let an exception cross `processBlock` (UNVERIFIED for your build).

## 14. Not verified, and sources

Not verified (do not state as fact; check first):
- JUCE 9 commercial tiers, prices and revenue limits; splash screen rules (juce.com pages could not be fetched).
- Release year of JUCE 9.x (page showed day and month only).
- Native CLAP support status in JUCE 9.0.2, and clap-juce-extensions compatibility with JUCE 9.
- VST3 folders on Windows and Linux system level; AU folders; Flatpak visibility details.
- Fedora package names; FetchContent snippet for JUCE 9; Windows generator names.
- `ProcessorChain` and filter class details; `ComponentBoundsConstrainer` header; `isBusesLayoutSupported` name; `getPlayHead` shape; `isNonRealtime`.
- macOS codesign and notarisation commands, auval usage, Valgrind/ASan/TSan use, Windows and Linux packaging steps, GLIBC and static-linking advice.
- Realtime rules were not checked against the Ross Bencina article (blocked); they are standard practice.
- ParameterID version number meaning for AU.

Sources fetched (research date 2026-10-23):
- S1 https://github.com/juce-framework/JUCE (README)
- S2 https://github.com/juce-framework/JUCE/blob/master/docs/CMake%20API.md
- S3 https://github.com/juce-framework/JUCE/blob/master/docs/Linux%20Dependencies.md
- S4 https://raw.githubusercontent.com/juce-framework/JUCE/master/LICENSE.md
- S5 https://github.com/juce-framework/JUCE/releases
- S6 https://github.com/steinbergmedia/vst3sdk
- S7 https://github.com/free-audio/clap
- S8 https://juce.com/?p=1627 (JUCE roadmap update, Q3 2024)
- S9 https://forum.juce.com/t/revenue-limits-for-juce-tiers/61058
- S10 https://forum.juce.com/t/fr-support-clap-for-plugins-host-client/51860
- S11 https://discussion.fedoraproject.org/t/where-are-the-users-vst-vst3-clap-directories/200321
- S12 https://github.com/free-audio/clap-juce-extensions
- S13 https://github.com/juce-framework/JUCE/releases/tag/9.0.0
- S14 https://raw.githubusercontent.com/juce-framework/JUCE/master/BREAKING_CHANGES.md
- S15 https://docs.juce.com/master/classAudioProcessor.html
- S16 https://github.com/Tracktion/pluginval
- S17 https://github.com/Tracktion/pluginval/blob/develop/docs/Adding%20pluginval%20to%20CI.md
- S18 https://raw.githubusercontent.com/juce-framework/JUCE/master/examples/CMake/AudioPlugin/CMakeLists.txt
- S19 https://raw.githubusercontent.com/juce-framework/JUCE/master/modules/juce_audio_processors/utilities/juce_AudioProcessorValueTreeState.h
- S20 https://raw.githubusercontent.com/juce-framework/JUCE/master/modules/juce_audio_basics/utilities/juce_SmoothedValue.h
- S21 https://raw.githubusercontent.com/juce-framework/JUCE/master/modules/juce_core/containers/juce_AbstractFifo.h
- S22 https://raw.githubusercontent.com/juce-framework/JUCE/master/modules/juce_audio_basics/buffers/juce_FloatVectorOperations.h
- S23 https://raw.githubusercontent.com/juce-framework/JUCE/master/modules/juce_dsp/processors/juce_ProcessContext.h
- S24 https://raw.githubusercontent.com/juce-framework/JUCE/master/modules/juce_dsp/processors/juce_Oversampling.h
- S25 https://raw.githubusercontent.com/juce-framework/JUCE/master/modules/juce_audio_processors/processors/juce_AudioProcessorEditor.h
- S26 https://raw.githubusercontent.com/free-audio/clap/main/include/clap/entry.h
- S27 https://raw.githubusercontent.com/juce-framework/JUCE/master/modules/juce_core/unit_tests/juce_UnitTest.h
- S28 https://forum.juce.com/t/linuxdependencies-md-debian-based-linux-distros-and-redhat-based-linux-distros/50132 (COMMUNITY)
- S29 https://u-he.com/support/faq/compatibility/install-paths-linux/ (COMMUNITY, vendor page)
- S30 https://www.steinberg.help/r/vst-plug-in-locations-on-mac-os-x-and-macos
- S31 https://github.com/sudara/pamplejuce (COMMUNITY)
- S32 https://github.com/89luca89/distrobox (COMMUNITY)
- S33 https://forum.juce.com/t/how-can-i-install-juce-in-linux-fedora/25304 (COMMUNITY)
- S35 https://github.com/VitalAudio/visage (README, VERIFIED)
- S36 https://forum.hise.audio/post/97122 (COMMUNITY)
- S34 https://raw.githubusercontent.com/Tracktion/pluginval/develop/README.md
- Blocked or empty (not used as facts): juce.com licence, licensing FAQ, tutorials and CMake tutorial pages; Steinberg VST3 portal locations page; Apple notarisation page (no body); Ross Bencina article.
