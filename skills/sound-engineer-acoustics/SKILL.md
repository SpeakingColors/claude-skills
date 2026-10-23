---
name: sound-engineer-acoustics
description: Use for studio audio troubleshooting and room acoustics, covering routing problems, noise, latency, gain staging, monitor placement, room modes, treatment, measurement and listening position.
---

# Sound engineer and room acoustics

Basis: standard audio engineering and acoustics (physics below is exact; product claims are not made). Mark anything uncertain. For Linux-specific audio daemons use linux-audio-production.

## Troubleshooting method (one step at a time)
1. Define: no sound / crackle / latency / noise / hum / level / one channel / feedback.
2. Isolate the chain: source > cable > interface input > driver > DAW track > bus > output > cable > monitors.
3. Change one thing, test, record result. Swap cable, then port, then device.
4. Reproduce with a simple test (sine, pink noise, a known file).
Give the next single step, not the whole list.

## Common problems
- Clicks/pops/dropouts: buffer too small, CPU or USB issues, wrong sample rate on the device vs DAW, power saving on USB, plugin overload; raise buffer to 256 or 512 to test, check xruns.
- Latency: round-trip = buffer plus converter plus driver. Monitor through the interface direct-monitor for tracking. Typical targets: tracking 64 to 128 samples at 48 kHz, mixing 512 to 1024.
- Hum (50/60 Hz): ground loop; use balanced cables, same power strip, DI box or isolator, lift ground only if it is safe (never remove a safety earth).
- Hiss: too low a source level raised later; gain stage hotter at the source, check the noisy cable/preamp.
- Distortion: clipping at the preamp, converter or plugin; target peaks around -12 to -6 dBFS while tracking (24-bit), mix with headroom.
- One channel only: mono/stereo cable (TS vs TRS), pan, routing, mono sum, phase cancellation.
- Phase issues: polarity flip, align time, check mono compatibility; low end must hold in mono.
- Feedback: monitors and mic open; reduce gain, mute mic, distance.
- Level mismatch: consumer (-10 dBV) vs pro (+4 dBu) outputs; pad or trim.
- Digital sync: one clock master (word clock or ADAT/SPDIF auto), mismatch gives clicks.

## Gain staging
Digital 0 dBFS is a ceiling, not a target. Set the monitor volume once, then adjust sources rather than the speaker. Common calibration (UNVERIFIED this session, widely cited): pink noise at -20 dBFS RMS per speaker reads 85 dB SPL(C) in film practice (SMPTE RP 200) and about 83 dB in small rooms (K-20 style). Check with an SPL meter before relying on it.

## Monitoring
- Equilateral triangle: monitors and head form 60 degrees; tweeters at ear height, toe-in aimed at ears.
- Place the listening position about 38 percent of room length from the front wall (common starting point; avoid the exact center of the room).
- Keep monitors at least 30 to 60 cm from walls; if close, use the speaker's boundary/room-compensation switch.
- Use decouplers (foam pads or stands) to reduce desk vibration; subwoofer needs measurement for crossover, level and phase.
- Check mixes on headphones, earbuds, a phone, the car; use references at matched loudness.

## Room acoustics: key physics (exact)
- Speed of sound c ≈ 343 m/s at 20 C.
- Axial room modes: f = c / (2 L) for each dimension; harmonics at n times that. Example: 4 m wall gives about 43 Hz, 86 Hz, 129 Hz.
- Wavelength = c / f. A porous absorber works best when its depth is a good fraction (about 1/4) of the wavelength, so 100 Hz needs about 86 cm of material in free air (less with an air gap behind it; the gap adds effective depth).
- Schroeder frequency Fs ≈ 2000 sqrt(RT60 / V) (V in m3): below it the room is modal (use bass traps/EQ), above it diffusion/absorption.
- RT60 target for a small control room: about 0.2 to 0.4 s, fairly flat across frequency (typical guidance; room size matters).
- Rule of thumb for early reflections: treat the first reflection points on side walls, ceiling and front wall behind the monitors.

## Treatment priority (cheapest impact first)
1. Speaker/listener placement and symmetry.
2. Corner bass traps (thick porous, e.g. mineral wool/rigid fiberglass, or membrane traps for deep targets).
3. First reflection points: side walls, ceiling cloud, front wall.
4. Rear wall: diffusion or absorption depending on distance (at least about 1 to 2 m is better for diffusion).
5. Floor/rug and desk reflection control.
6. Then EQ/measurement-based room correction (use it for peaks, do not boost nulls).
Avoid: egg-crate foam as treatment (thin, low-frequency ineffective), fully dead rooms, covering only high-mid.
Soundproofing (stopping sound leaving the room) is different from treatment: needs mass, decoupling and sealing (gaps, doors, HVAC); absorption does not block sound.

## Measurement
- Software like REW (Room EQ Wizard) with a measurement mic (e.g. calibrated USB/XLR omni) gives frequency response, waterfall/decay, RT60 and modal peaks. Take several positions around the head and average.
- Read: dips from boundary cancellation cannot be fixed by EQ; fix by moving speakers/listener or adding absorption. Peaks can be reduced by EQ.
- Re-measure after each change; keep a log.

## Hardware routing basics
Balanced XLR/TRS for monitors; keep unbalanced short; analog and digital cables away from mains; interface to speakers direct, no daisy chain; use a power conditioner only as a convenience (it does not fix grounding). USB: avoid hubs, use the rear ports; check cable and device sample rate agree. For hardware synths: each stereo pair to its own input or via mixer; MIDI over USB or DIN; clock master set once.

## Style
Ask room size (L x W x H) and speaker/desk setup only when needed. Give one step at a time; give formulas with the numbers worked out. Say what is a rule of thumb vs physics. Recommend measuring rather than guessing.
