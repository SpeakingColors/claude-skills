---
name: plugin-fleet-audit
description: Use to audit many plugin repos at once: clone shallow, scan for security and sound quality techniques, then read the code to confirm. Includes the false positives that fooled a first pass.
---

# Auditing a whole fleet of plugin repos

Labels: MEASURED (46 repos audited in one session). Companion to `plugin-dsp-quality`, `gha-supply-chain-hardening`, `plugin-security-fuzzing`.

## Pass 1: cheap scan (minutes)
1. Clone every repo with `--depth 1` into a scratch folder, in parallel. Public repos clone without credentials.
2. Per repo, count with grep (exclude `build`, `_deps`, third party): `strcpy|sprintf|gets`, `pull_request_target`, workflows without top level `permissions:`, `uses:` lines not pinned to 40 hex, `curl | sh`, committed binaries (`git ls-files | grep -E '\.(exe|dll|so|vst3|zip)$'`), obvious secret patterns (`ghp_`, `AKIA`, `BEGIN PRIVATE KEY`), `GIT_TAG main`, LICENSE, `.gitignore`.
3. DSP hygiene counts: `ScopedNoDenormals`, `SmoothedValue`, oversampling words, `adaa|antiderivative`, `polyblep|wavetable`, `limiter`, `lookahead`, `true peak`, `LUFS`, `pluginval`, `fsanitize`.

## Pass 2: read the code before reporting
The first pass produced false alarms. Always open the file:
- A "realtime hits" counter that ranges from `processBlock` to the next closing brace swept in whole helper functions (preset I/O with `juce::String`). Three of three samples were false alarms. Nothing was reported from it.
- Searching `fold` matched `folder`; `clip` matched `clipboard`; `saturat` matched UI text. Counts per repo were inflated by editor files. Restrict to the DSP folders and drop comments.
- Zero hits can also mean the DSP lives in a folder with an unexpected name (`src/engine`, `src/core`). List the files first.

## What the audit found (examples of the real kind of result)
- A kick synth rendered each kick offline with plain `tanh` stages (drive, transistor, fuzz, final clip) at the host rate, no oversampling or ADAA. Offline means 4x or 8x internal rendering costs nothing audible. Top candidate fix.
- Shared effect rack without parameter smoothing: fixed with 20 ms and 60 ms glides, test fails before and passes after.
- A sample player applied volume with `applyGain` per block: fixed with `applyGainRamp`.
- Denormal guard flagged for plugins that were hardware units or pure pass throughs: no change needed. Check what the repo IS before "fixing".
- Sanitizers: only 9 of 37 plugin repos ran their engine tests under AddressSanitizer and UBSan. Running all the others locally in isolated copies (`sed` AddressSanitizer and UBSan flags into every `g++` line of `tests/run.sh`) gave 20 clean passes and one failure that was only a speed check (a sanitizer build is slower). Do that dry run before adding a CI job everywhere, so you know what will go red.
- Correction worth remembering: a first count said pluginval was missing in most repos. A `head -12` had truncated the list. It was already in 26 of 37. Never read a count from truncated output.

## Reporting
- Short ranked list: confirmed problems first, then "worth checking", then what you did not review (state loading, installers, DSP itself).
- Say which repos you could not read (private) and that a static scan is not a listening test.

## Rolling a change out to many repos
1. Write the edit as a small script that takes one repo directory, is idempotent, validates every YAML it touched, and prints what it did.
2. Dry run it on two or three different repos and read the diff.
3. A shipper loop per repo: fetch, hard reset to the fetched head, run the script, commit with one message, push. Run it in the background, never at the same time as another command in those clones (a concurrent fetch failed with "shallow file has changed").
4. Afterwards watch CI, not just the push: a changed pin or workflow can go red only on the real runners.
5. Put a weekly sweep in a repo you own (a scheduled workflow with a small Python script): for every public repo, is the latest CI run on the default branch green, are actions pinned, is there a read-only token, is Dependabot present, are issues, wiki, projects, discussions and outside pull requests still off. Its first run caught two of my own mistakes within an hour (the shallow-clone pin, and Dependabot failing where there is nothing to update).
