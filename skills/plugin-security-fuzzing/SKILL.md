---
name: plugin-security-fuzzing
description: Use when auditing or hardening an audio plugin: hostile preset and file input, libFuzzer on setStateInformation, sanitizer CI, decoder CVEs, host sandboxing facts, hardening flags, signing.
---

# Audio plugin security and robustness

Companion to `vst-maker` section 11, `plugin-ship-checklist` and `gha-supply-chain-hardening`. Labels: VERIFIED (source page), COMMUNITY (forum or secondary source), UNVERIFIED (background knowledge, test first). Research date: November 2026.

## What a plugin is
- Native code with the full rights of the user. Host sandboxing is crash isolation, not a security boundary. COMMUNITY. Bitwig hosts plugins out of process by default (crash protection). VERIFIED (bitwig.com). REAPER can isolate per plugin (forum sources). Ardour deliberately does not sandbox. VERIFIED (ardour.org). Ableton and Logic load plugins in process. UNVERIFIED.

## Hostile input classes (treat all as parsers of untrusted data)
- `setStateInformation`, presets, imported files: out of bounds reads, trusted size fields, XML and JSON parsing, path traversal in sample or preset loading. Real world example class: a plugin state restore crashing Logic on Apple silicon. COMMUNITY (JUCE forum).
- Audio decoders: libsndfile has a long CVE history (FLAC, Vorbis, AIFF, RF64, PCM and MS-ADPCM overflows, WAV writer). COMMUNITY (Arch security tracker data). Pin current versions; JUCE's bundled FLAC and Ogg code only updates when you upgrade JUCE. UNVERIFIED for libFLAC and libvorbis CVE lists.
- Rules: version tag in every state blob; clamp every parameter; length check before every read; never trust a size field; refuse `..` and symlinks in user supplied paths; use `File::createTempFile` in a private folder; never write next to the user's audio. UNVERIFIED practice.

## Fuzzing recipe (no public JUCE plugin harness was found)
1. A libFuzzer target that feeds arbitrary bytes to `setStateInformation`, preset load and file import: `-fsanitize=fuzzer,address,undefined`.
2. Run it as a short CI job (a few minutes) on the pure C++ engine first (no JUCE needed), then on the processor.
3. Seed with real states and presets. Keep crashing inputs as regression tests.
4. Separate job: ThreadSanitizer for message thread vs audio thread races. pluginval for state round trips.
5. Our pure C++ engine tests already run headless; add `-fsanitize=address,undefined` to them first. UNVERIFIED that every repo does.

## Build hardening
- Linux: `-fstack-protector-strong`, `-D_FORTIFY_SOURCE=2`, `-fPIE`, `-Wl,-z,relro,-z,now`. MSVC: `/GS /guard:cf /DYNAMICBASE /sdl`. Clang CFI with LTO is awkward with dlopen. UNVERIFIED.
- Pin dependencies to commit SHAs (see `gha-supply-chain-hardening`).

## Signing and licences
- Windows: SignPath Foundation signs OSI licensed projects for free (MFA required, credit line, approval not guaranteed). COMMUNITY (signpath.org). Azure Artifact Signing: individuals only in the US and Canada, organizations in the US, Canada, EU, UK. COMMUNITY.
- macOS: paid Developer ID plus notarization. Never tell users to disable Gatekeeper.
- JUCE is AGPLv3 or commercial; a free open source plugin under AGPLv3 is fine. COMMUNITY. The VST3 SDK reportedly became MIT (3.8.0); check your JUCE version. COMMUNITY, partly conflicting.

## Privacy and updates
- Collect nothing: no telemetry, usernames, host names, paths, audio, fingerprints. No auto updater; at most a link to a signed release page. Never download and run code. UNVERIFIED practice, our policy.

## Repo side
- Fork only policy and renewal: see `github-repo-lockdown`. Private vulnerability reporting invites reports and spam; GitHub added rate limits for them in October 2026. COMMUNITY (changelog summary).
