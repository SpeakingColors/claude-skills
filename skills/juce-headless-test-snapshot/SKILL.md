---
name: juce-headless-test-snapshot
description: Use to test a JUCE plugin without a DAW or screen: console-app processor tests, parameter and thread gotchas, offscreen editor snapshot to PNG with xvfb, crash backtraces, CI steps.
---

# Headless JUCE plugin tests and editor snapshots

Companion to `juce-expert` and `plugin-ship-checklist`. Labels: MEASURED (a recorder/editor plugin, Linux, JUCE 8.0.16), UNVERIFIED.

## Processor tests (no window)
- Add a `juce_add_console_app` target that compiles the processor `.cpp` with `JUCE_STANDALONE_APPLICATION=1` and a macro such as `MEOW_NO_EDITOR` that makes `hasEditor()` false. Call `prepareToPlay`, then `processBlock` on 10 ms buffers.
- Helper threads need real time: sleep 2 ms per block and 40 ms at the end of a feed, or the worker has not run yet.
- Set parameters with `getParameter(id)->setValueNotifyingHost(convertTo0to1(v))`. Writing through `getRawParameterValue(id)` does not update the ValueTree, so a state save/load round trip loses the value. MEASURED.
- Test: record now, record on input (silence first), pre-roll length, append take, edit then undo, playback output magnitude, WAV round trip, state restore with garbage input ignored, preview then restore, count-in clicks then record.
- Start offsets matter: a take that begins with pre-roll silence has a silent first 10000 samples; start playback checks after it. MEASURED.
- State machines owned by two threads: a worker that recomputes the state after each drain overwrote the "count-in" state with "off". The test caught it. Compute the state from all the flags in one place. MEASURED.
- Use `JUCE_DECLARE_NON_COPYABLE_WITH_LEAK_DETECTOR` and run the test under ASan/UBSan in CI when the engine is pure C++ too.

## Editor snapshot
- A console app with `ScopedJuceInitialiser_GUI`, build the editor, `setVisible(true)`, `MessageManager::getInstance()->runDispatchLoopUntil(400)`, then `createComponentSnapshot(getLocalBounds(), true, 1.0f)` and write a PNG. Run it with `xvfb-run -a`. Pass arguments to open other views and selections.
- Pass an ABSOLUTE output path: `xvfb-run` hid a relative path ("not found") on the first try. MEASURED.
- Crash? `xvfb-run -a gdb -batch -ex run -ex bt --args ./snapshot out.png`. The backtrace pointed straight at a refresh call inside the constructor. MEASURED.
- Compare with a Playwright screenshot of the mockup. Look at the image yourself; do not trust a passing build.

## CI
- Build, run the engine tests, run the processor test, upload the VST3 and standalone as artifacts. Add `pluginval --strictness-level 5` (use `--skip-gui-tests` on headless runners) and sanitizer jobs. See `plugin-ship-checklist`.
