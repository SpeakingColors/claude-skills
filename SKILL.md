---
name: korg-logue-sdk-expert
description: Use when writing, porting, debugging, building or loading custom oscillators, synths and effects (units) with the KORG logue SDK for minilogue xd, prologue, NTS-1 (mkI/mkII), NTS-3, drumlogue or microKORG2. Covers per-platform APIs, manifest/header files, Docker and manual builds, logue-cli, memory limits, realtime-safe DSP practice and Linux loading workarounds.
---

# KORG logue SDK Expert

> Unofficial community skill, not made or endorsed by KORG. Facts were checked against the official logue-sdk repo (BSD-3-Clause, https://github.com/korginc/logue-sdk) and korginc.github.io/logue-sdk as of October 2026. The SDK changes over time: when in doubt, read the user's local SDK headers. Do not redistribute `logue-cli`; it has its own EULA from KORG.

Senior embedded DSP engineer mode. Correctness over speed: hardware has no debugger by default and a bad unit can crash or mute the synth.

## 0. Ground rules

1. **Identify the target platform first.** The old and new platforms have different APIs. Never mix them.
2. **Source of truth order:** the user's local SDK checkout headers (`inc/`, `userosc.h`, `unit.h`) > official docs (korginc.github.io/logue-sdk) > this file. If a header disagrees with this file, the header wins; say so.
3. **Never invent API names, struct fields, limits or manifest keys.** If unsure, read the header or say "unverified".
4. Ask for the SDK version if it matters (xd/prologue/NTS-1 mkI: v1.1.0; drumlogue/NTS-1 mkII/NTS-3: v2.0.0; microKORG2: v2.1.0).
5. SDK is BSD-3-Clause, provided as-is, no Korg support. Community: Korg Discord.

## 1. Platform map (verified from the official repo README)

| Product | SDK | Min FW | CPU | Unit format | Extension |
|---|---|---|---|---|---|
| prologue | 1.1.0 | 2.00 | Cortex-M4 | static ARM ELF-like, custom | .prlgunit |
| minilogue xd | 1.1.0 | 2.00 | Cortex-M4 | static, custom | .mnlgxdunit |
| NTS-1 digital kit (mkI) | 1.1.0 | 1.02 | Cortex-M4 | static, custom | .ntkdigunit |
| NTS-1 digital kit mkII | 2.0.0 | 1.0.0 | Cortex-M7 | ELF shared object, dynamic | .nts1mkiiunit |
| NTS-3 kaoss pad kit | 2.0.0 | 1.0.0 | Cortex-M7 | ELF shared object, dynamic | .nts3unit |
| drumlogue | 2.0.0 | 1.0.0 | Cortex-A7 | ELF shared object, dynamic | .drmlgunit |
| microKORG2 | 2.1.0 | 2.0.0 | Cortex-A7 | ELF shared object, dynamic | .mk2unit |

All extensions above are confirmed from the platform READMEs in the SDK repo (snapshot of `main`, checked 2026-10-18). If the SDK may have moved on, ask the user for a fresh copy of the repo and re-verify before relying on these tables.

Unit files are zip archives: binary payload plus metadata.

**Binary compatibility:** prologue, minilogue xd and NTS-1 mkI units are binary compatible with each other if the SDK version matches. Korg still recommends a platform-specific build. mkII, NTS-3, drumlogue and microKORG2 are NOT compatible with those or with each other. Porting is usually easy because the core structure is similar.

**Unit types per platform:**
- prologue, minilogue xd, NTS-1 mkI/mkII: osc, modfx, delfx, revfx.
- NTS-3: generic effects only (4 identical runtimes), plus touch event handler.
- drumlogue: synth, delfx, revfx, masterfx (masterfx has optional sidechain send bus).
- microKORG2: osc, modfx, delfx, revfx (32 slots each). Osc units get up to 13 params across the OSC1/2/3 pages; effects get up to 8 params.

**Slot and routing facts:**
- prologue/NTS-1: 16 osc slots, 16 modfx, 8 delfx, 8 revfx (Korg FAQ). minilogue xd osc slots 0-15 seen in logue-cli usage.
- On xd/prologue/NTS-1 mkI, custom delay and custom reverb share one runtime: only ONE of them can be custom at a time. Internal plus custom mixes are fine.
- On NTS-1 mkII, delay and reverb runtimes are independent.
- Modfx runs after voice and filter, before delay/reverb.

## 2. Old platforms (xd, prologue, NTS-1 mkI): API

Headers: `userosc.h`, `usermodfx.h`, `userdelfx.h`, `userrevfx.h`, `userprg.h`.

**Oscillator (osc):**
- `void OSC_INIT(uint32_t platform, uint32_t api)`
- `void OSC_CYCLE(const user_osc_param_t * const params, int32_t *yn, const uint32_t frames)`: write **Q31 fixed point** into `yn`. Use `f32_to_q31(f)` from `inc/utils/fixed_math.h`.
- `void OSC_NOTEON(const user_osc_param_t * const params)`
- `void OSC_NOTEOFF(const user_osc_param_t * const params)`
- `void OSC_PARAM(uint16_t index, uint16_t value)`

**Modfx:** `MODFX_INIT(platform, api)`, `MODFX_PROCESS(const float *main_xn, float *main_yn, const float *sub_xn, float *sub_yn, uint32_t frames)`, `MODFX_PARAM(uint8_t index, uint32_t value)`. The sub buffers exist for prologue dual timbre: process both identically on prologue, ignore on xd and NTS-1.

**Delfx / Revfx:** `DELFX_INIT/PROCESS/PARAM`, `REVFX_INIT/PROCESS/PARAM`. `PROCESS(float *xn, uint32_t frames)` is in place: you must mix dry and wet yourself (the shift-depth param is the usual mix control).

**Buffers:** support up to 64 frames per call. Never assume a fixed size. Optimize for 16, 32, 64. Splitting into smaller passes is allowed. A local `float buf[64]` is fine, but a cheap `if (frames > 64)` guard is good defensive practice.

**Verified from `userosc.h` / `osc_api.h` (xd, prologue and NTS-1 mkI share these):**
- `user_osc_param_t`: `int32_t shape_lfo` (LFO already applied to shape, Q31), `uint16_t pitch` (**high byte note number, low byte fine 0-255**), `cutoff` and `resonance` (0x0000-0x1fff).
- Param ids in order: `k_user_osc_param_id1` = 0 ... `id6` = 5, then `k_user_osc_param_shape` = 6, `k_user_osc_param_shiftshape` = 7.
- `param_val_to_f32(val)` = 10-bit value times 1/1023, giving 0..1. Use it for shape and shiftshape.
- **Bipolar percent params arrive as 0..200, with 0% at 100 and -100% at 0.** So subtract 100. (For a narrower range like -2..2 the value should be display + 100, so 98..102. That is inferred from the header note, not tested on hardware.)
- Typeless params arrive as the raw number, not offset (the +1 is display only).
- `osc_w0f_for_note(note, mod)`: note 0-151, mod 0-255 fine pitch, returns normalized phase increment (cycles per sample), clipped to a max Hz.
- `osc_sinf(x)` wraps with `x - (uint32_t)x`, so phase above 1 is fine, but **negative input is not safe** (cast of a negative float to unsigned). Keep arguments positive, for example by adding a whole number offset before phase modulation.
- Also available: `osc_cosf`, `osc_softclipf(c, x)`, `osc_rand()`, `osc_white()`, `osc_notehzf(note)`.

## 3. New platforms (mkII, NTS-3, drumlogue, microKORG2): API

Different model. Do not use `OSC_*` or `manifest.json` here.
- Files: `config.mk` (project name, sources), `header.c` (unit name, params, ranges), `unit.cc` (implementation).
- Callbacks: `int8_t unit_init(const unit_runtime_desc_t *desc)`, `void unit_render(const float *in, float *out, uint32_t frames)`, plus param setter `unit_set_param_value(...)` and others. **Read `platform/<name>/common/unit.h` for exact signatures and the full list.**
- Oscillator-type units get a runtime context (`unit_runtime_osc_context_t`) with voice info. Read the header for fields.
- NTS-1 mkII modfx has no second buffer; effect API is uniform with other effects.
- Known quirk (issue #106 on the official repo): on NTS-1 mkII, `unit_set_param_value()` can be called right after `unit_init()` with zeros before the first `unit_render()`. Do not trust that early parameter state; set defaults carefully and consider ignoring param calls until the first render.
- drumlogue default param values are used when the module is first selected; do not assume the same on mkII.

**Verified from the drumlogue README (the new-platform READMEs share this structure):**
- `header.c` fields: `.header_size`, `.target`, `.api`, `.dev_id` (32-bit, unique; 0x00000000, 0x4B4F5247 "KORG" and 0x6B6F7267 "korg" are reserved, in any case mix), `.unit_id` (unique per developer), `.version` (major in upper 16 bits, then minor, then patch: v1.2.3 = 0x00010203), `.name`, `.num_presets`, `.num_params`, `.params`.
- Unit name: max **13** ASCII chars. Param name: max **12** chars. Allowed characters: letters, digits, space and `!?#$%&'()*+,-.:;<=>@`.
- drumlogue: up to **24 params**, shown 4 per page. Every one of the 24 descriptors must be filled; unused ones use `{0,0,0,0,k_unit_param_type_none,0,0,0,{""}}`. A blank descriptor pushes the next param to the next page.
- Param descriptor: `min`, `max`, `center` (set equal to `min` for unipolar), `init`, `type`, `frac`, `frac_mode`, `name`. Types include none, percent, db, cents, semi, oct, hertz, khertz, bpm, msec, sec, enum, strings, bitmaps (bitmaps need drumlogue FW 1.1.0+), drywet, pan, spread, onoff, midi_note.
- Other limits: NTS-3 exposes **8 params**; mkII and microKORG2 limits depend on module (`UNIT_XXX_MAX_PARAM_COUNT` in the common headers).
- Callbacks: `unit_init`, `unit_teardown`, `unit_reset` (clear notes, envelopes, phases; do NOT reset param values), `unit_resume`, `unit_suspend`, `unit_render`, `unit_set_param_value(uint8_t, int32_t)` (bound-check against header min/max), `unit_get_param_value`, preset callbacks, `unit_set_tempo` (BPM integer in upper 16 bits, fraction in lower 16; keep it cheap). Synths add `unit_note_on/off`, optional `unit_gate_on/off`, `unit_all_note_off`, `unit_pitch_bend`, `unit_channel_pressure`, `unit_aftertouch`.
- `unit_runtime_desc_t` gives `samplerate` (drumlogue: always 48000, but check it), `frames_per_buffer` (max frames; smaller must work), channel counts, and sample-bank access functions.
- drumlogue builds are **Docker only**. Units load in alphabetical order after restart; prefix files with `01_`, `02_` to force order.

## 4. Project files (old platforms)

Copy a template (`dummy-osc`, `dummy-modfx`, `dummy-delfx`, `dummy-revfx`). Set `PLATFORMDIR` at top of `Makefile` to the SDK `platform/` dir.

**project.mk variables:** `PROJECT`, `UCSRC`, `UCXXSRC`, `UINCDIR`, `UDEFS`, `ULIB`, `ULIBDIR`.

**manifest.json** (header object):
```json
{
  "header": {
    "platform": "minilogue-xd",
    "module": "osc",
    "api": "1.0-0",
    "dev_id": 0,
    "prg_id": 0,
    "version": "1.0-0",
    "name": "waves",
    "num_param": 6,
    "params": [
      ["Wave A", 0, 45, ""],
      ["Sub Mix", 0, 100, "%"]
    ]
  }
}
```
- `module`: `osc`, `modfx`, `delfx` or `revfx`.
- Max **6 custom params**, and only for osc. For effects use `num_param: 0` and `params: []`.
- Param descriptor: `[name, min, max, type]`. Name about 10 chars visible. Values in -100..100, max > min. Type `"%"` for percent, `""` for typeless.
- Typeless values should be positive, and the display is offset by +1 (0-9 shows as 1-10).
- Doc quirk: the README bullet says `num_params`, the example JSON says `num_param`. The JSON key `num_param` is the one in real units (a real xd unit using it passes `logue-cli check`). Still copy from the template in the user's checkout.
- Negative ranges: typeless params should be positive, so developers use type `"%"` for bipolar params (for example -2..2). Downside: the xd then shows a percent sign. The value should arrive as display + 100 (see section 2, inferred, not hardware-tested).
- `dev_id` is currently unused on xd (use 0). Repo has `developer_ids.md` and `factory_unit_ids.md`.
- Platform strings: xd `minilogue-xd`. For others copy the template, do not guess.

## 5. Memory and size limits (be precise)

- Korg FAQ (prologue/NTS-1): oscillator **code and variables must fit in 32KB RAM**. Custom effects get additional RAM for delay lines **up to 2MB**. That 2MB is working RAM, not code size.
- Real device probe (NTS-1 mkI, FW 1.20, from an official repo issue), `logue-cli probe`:
  - Osc: 16 slots, max_load_size 32768
  - Modfx: 16 slots, max_load_size 6144
  - Delfx: 8 slots, max_load_size 12288
  - Revfx: 8 slots, max_load_size 12288
  So **effect code is far smaller than osc code**. Treat these as per-firmware, re-probe the user's device.
- **Limits for the new platforms (from each platform README):**

  | Platform | Module | Slots | Max unit size / RAM load | Allocatable external memory |
  |---|---|---|---|---|
  | NTS-1 mkII | osc | 16 | ~48KB | none |
  | NTS-1 mkII | modfx | 16 | ~16KB | 256KB |
  | NTS-1 mkII | delfx, revfx | 8 each | ~24KB | 3MB |
  | NTS-3 | genericfx | 50 | ~32KB | 3MB per runtime |
  | microKORG2 | osc | 32 | ~48KB | 8KB |
  | microKORG2 | modfx | 32 | ~16KB | 64KB |
  | microKORG2 | delfx, revfx | 32 each | ~24KB | 1MB |

- drumlogue: the README has no size table, and Korg's drumlogue page says units are not bound to specific size or memory limits. Still be frugal.
- Check size after build: the `size` line in build output (text, data, bss). Example waves osc: about 2KB text.
- **Old platforms (xd, prologue, NTS-1 mkI): no malloc/new/heap, no exceptions, no RTTI, no static constructors with side effects, no printf.** Use static buffers sized at compile time.
- **New platforms:** the drumlogue README says `unit_init` may perform dynamic allocations and `unit_teardown` should free them. That is the only place. Never allocate in `unit_render`. On mkII, NTS-3 and microKORG2 the "allocatable external memory" in the table is where big delay lines go (check the platform's runtime header for the allocation call, do not guess it).

## 6. Build

**Docker (recommended, host-OS agnostic):**
```
git clone https://github.com/korginc/logue-sdk.git
cd logue-sdk && git submodule update --init
docker/run_interactive.sh
build -l --minilogue-xd         # list projects
build minilogue-xd/waves        # build and package
```
Output lands next to the project as `<name>.mnlgxdunit` (or platform equivalent).

**Manual:** `git submodule update --init`, install GNU Arm Embedded Toolchain (scripts in `tools/gcc`), GNU Make, Info-ZIP, optionally logue-cli. Then `make`, then `make install` to package.

**Build flags seen for Cortex-M4 targets:** `-mcpu=cortex-m4 -mthumb -mfloat-abi=hard -mfpu=fpv4-sp-d16 -fsingle-precision-constant -Os -std=c11`, defines `STM32F401xC`, `ARM_MATH_CM4`. Note `-fsingle-precision-constant`: write float literals deliberately, avoid accidental double math.

**Common build failures:**
- Missing `arm_math.h`: CMSIS submodule not initialized. Run `git submodule update --init`.
- Wrong `PLATFORMDIR`, or wrong project copied for target.
- Linker overflow: you blew the RAM budget. Cut tables, use smaller types, compute instead of store.
- Warning `-mstructure-size-boundary deprecated` under Docker is harmless (seen in official output).

## 7. Loading units

**logue-cli** (in `tools/logue-cli`): commands `check`, `probe`, `load`, `clear`. Use `-h` after a command for detailed help.
- **Supported devices per its README: prologue, minilogue xd, NTS-1 digital kit (mkI) only** (.prlgunit, .mnlgxdunit, .ntkdigunit). It is NOT for mkII, NTS-3, drumlogue or microKORG2.
- Install scripts in `tools/logue-cli` (all fetch version 0.07-2b, checked by reading the scripts):
  - `get_logue_cli_linux.sh`: downloads `logue-cli-linux64-0.07-2b.tar.gz` (**64-bit Linux only**), needs `curl`, `tar`, `sha1sum`, `awk`. Exits if `$OSTYPE` is not `linux-gnu*`.
  - `get_logue_cli_osx.sh`: `logue-cli-osx-0.07-2b.zip`, needs `curl`, `unzip`, `shasum`.
  - `get_logue_cli_msys.sh` (win32 zip) and `get_logue_cli_msys64.sh` (win64 zip): MSYS2 only, need `curl`, `unzip`, `sha1sum`.
  - All download from `http://cdn.storage.korg.com/korg_SDK/...` (plain HTTP, not HTTPS) and compare a SHA1 hardcoded in the script. That catches corruption, not tampering, since the hash ships with the script from the same repo.
  - Run the script from its own folder. It extracts the archive in place and deletes the download afterwards.
  - On immutable distros (Bazzite) or non-glibc systems the prebuilt binary may not run; run it inside a distrobox (untested).
```
logue-cli check -u my.mnlgxdunit
logue-cli probe -l                      # list MIDI ports
logue-cli probe -i 1 -o 2               # explicit ports (indexes from -l)
logue-cli probe -m osc                  # list oscillators loaded on device
logue-cli load -u my.mnlgxdunit         # first free slot
logue-cli load -u my.mnlgxdunit -s 2    # specific slot, overwrites
```
Slot `-s`, ports `-i`/`-o`, unit `-u`. Always run `check` before `load`.

**Port gotcha (xd and prologue):** if auto-detect fails, pick the ports ending in **KBD/KNOB** (input) and **SOUND** (output). The other ports are the legacy MIDI DIN connectors and will not work for unit loading.

**Alternatives:** KORG Librarian (Win/Mac), Korg Sound Librarian for xd.

**drumlogue:** no CLI. Power on holding the record button, it mounts as USB mass storage "drumlogue". Copy `.drmlgunit` into `Units/Synths/`, `Units/DelayFXs/`, `Units/ReverbFXs/` or `Units/MasterFXs/`. Press YES to boot with the new units.

**microKORG2:** USB Mass Storage mode, or the microKORG2 Editor / Librarian app. The README marks the Editor and a new loguecli as "pending release", so check what exists now before promising either.

**NTS-1 mkII and NTS-3:** the READMEs say units load via the KORG Kontrol Editor or a new loguecli, both marked "pending release" in the repo. The old logue-cli 0.07-2b does not target them. Check Korg's current downloads before telling the user how to load.

**Linux:** an official Linux install script exists (`get_logue_cli_linux.sh`), but users report `load` problems on Linux (official issue #37). First check you picked the KBD/KNOB and SOUND ports. If load still fails, community workaround: run `logue-cli load -d ...` to dump the SysEx, extract the last line, then send it with `amidi -p hw:X,0,0 -S "<hex>"`. Treat that as a workaround, test on a spare slot, and do not promise it works until tested on the user's machine. The CLI is a prebuilt binary, so on an immutable distro like Bazzite run it in a distrobox or container if it will not start (untested suggestion).

### Checking an existing unit (do this myself, no user help needed)

1. `unzip` the `.mnlgxdunit` (or other unit) into a fresh empty folder. Expected layout for xd units: a `<name>/` folder holding `manifest.json` and `payload.bin` (seen in a real third-party xd unit; payload starts with the `UOSC` marker).
2. Read `manifest.json` against section 4 rules: platform, module, param count vs descriptors, ranges, name length.
3. If the logue-cli binary is available in the workspace, run `logue-cli check -u <unit>`. **Verified output on a good unit:** "Parsing minilogue xd unit archive / Parsing manifest / Parsing unit binary payload / Looks okay." Exit code 0. It needs no synth connected.
4. A sandboxed workspace may be unable to download the CLI from Korg's CDN. If so, ask the user to attach `logue-cli-linux64-0.07-2b.tar.gz` (a 64-bit glibc Linux ELF). Do not try to work around a blocked network.
5. If the source is available, review it against the section 10 checklist and cross-check manifest params against the `OSC_PARAM` handler (indices, ranges, the minus-100 rule for bipolar percent).
6. Packaging passing `check` does NOT prove the DSP is correct or fast enough. CPU load can only be judged on the device.

## 8. Realtime DSP best practices

- **Audio thread rules:** no allocation, no locks, no blocking, no unbounded loops, no `printf`, no libm calls you have not costed. Branch-light inner loops.
- **Numerics:** wrap phase with subtraction or fractional masks, not `fmod`. Avoid division in the sample loop; precompute reciprocals in the param handler. Guard every divisor and every table index (clamp, mask or power-of-two wrap).
- **Denormals and NaN:** a NaN in feedback kills the sound until reload. Clamp feedback gain below 1.0, flush tiny values, add a final sanity clamp on output.
- **Params:** treat `OSC_PARAM`/`*_PARAM` as async. Store raw value, convert once, smooth per sample or per block to avoid zipper noise. Validate `index` (ignore unknown).
- **State:** reset phase and envelopes in `NOTEON` deliberately, not by accident. Reinitialize everything in `INIT`; assume units get re-instantiated.
- **Polyphony (xd/prologue):** each analog voice has its own osc runtime instance, so per-voice state is yours alone. Do not build global shared state across voices.
- **Output level:** osc output is Q31. Leave headroom: summed voices and the analog path add up. Test at full resonance and all params at extremes.
- **Alias control:** naive saw/square alias hard at high notes. Use PolyBLEP/minBLEP or band-limited tables. Detuned stacks (supersaw style): fixed small voice count, per-voice phase accumulators, cheap randomized start phases, then sum and scale by `1/N` constant.
- **CPU budget:** unknown and platform specific. Do not quote cycle counts you have not measured. Prefer measuring on device, start light, add voices until it glitches, then back off with margin.
- **Prefer** SDK utilities: `inc/utils` (fixed_math, float_math, osc_api) and `dsp` namespace helpers (see API reference), they are tuned for these cores.

## 9. Test strategy (do this before hardware)

1. Desktop harness: compile the DSP core as plain C++ with a thin wrapper, render to WAV, inspect level, DC, aliasing, NaN checks. Build the harness against stub headers, since the real ones need hardware lookup tables, and say so when reporting results.
2. For NTS-1 mkII and NTS-3, use the official **websim** (browser simulator in repo `websim/`).
3. Run `logue-cli check` on the package.
4. Load into a spare slot, volume low, test notes across the range, param extremes, fast note retrigger, patch change while a note is held.
5. Soak test: hold a note and sweep params for several minutes.

## 10. Code review checklist (run on every unit)

- [ ] Correct callbacks for the target platform and SDK version
- [ ] Right header included, right `platform`/`module` in manifest (old) or `header.c` (new)
- [ ] Param count, ranges, names match between manifest/header and `*_PARAM` handler
- [ ] No heap, no exceptions, no large stack arrays, no recursion
- [ ] Every divide, array index, loop bound guarded
- [ ] Handles any `frames` value up to 64
- [ ] NaN/inf impossible or clamped; output bounded
- [ ] Size under limit (check `size` output and probe limits)
- [ ] Packaged, `check` passes, loaded to spare slot
- [ ] Float constants single precision where intended

## 11. Response style for this skill

- Lead with the answer or the code, then explain only if asked.
- State the target platform and SDK version assumption up front.
- Mark anything unverified as "unverified" and say how to verify (header path, `logue-cli probe`, official doc URL).
- Prefer minimal diffs to existing user code over rewrites.
- Do not claim code was compiled or tested on hardware unless it actually was.

## 12. References

- Docs: https://korginc.github.io/logue-sdk/
- Repo: https://github.com/korginc/logue-sdk (platform READMEs, docker/, tools/, websim/, developer_ids.md, factory_unit_ids.md)
- Unit index: https://korginc.github.io/logue-sdk/unit-index/
- drumlogue SDK page on korg.com (loading steps)
