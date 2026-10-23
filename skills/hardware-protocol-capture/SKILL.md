---
name: hardware-protocol-capture
description: Use when documenting how a music hardware device is controlled over MIDI (CC, NRPN, SysEx) or USB so a controller, editor or librarian can be built, from official docs and own-device captures.
---

# Hardware protocol capture

Unofficial community skill. Not legal advice. Capture only devices the user owns.

## 0. Rules

- The device is the source of truth. Documents can be wrong or outdated; a capture from the real device with the user's firmware is the proof.
- Source order: 1) the manufacturer's official documents, 2) captures from the user's own hardware, 3) third-party documents (mark as unverified until checked on hardware).
- Every entry in the final document carries a status: verified on hardware, from official doc only, or unverified.
- Back up the device's patches and settings before sending anything unknown. Never send firmware, bootloader, flash-write or factory-reset messages until their format is fully understood.
- Give one step at a time to non-programmers. Short answers first.

## 1. Find the official documents

- Look for a "MIDI Implementation" or "MIDI data format" document for the product on the manufacturer's support page, plus the owner's manual's MIDI implementation chart. Example: KORG publishes the minilogue xd MIDI Implementation as a separate text file (download after accepting a personal, non-commercial licence). Link to such documents; do not copy them into public repos unless their licence allows it.
- Check the document's revision and date against the device's firmware version. Firmware updates can change formats. Example: a third-party library for that synth notes that some preset files from newer firmware use 448-byte program blobs, not the 1024-byte format the spec describes (V: oxur/minilogue-xd README). Always test a dump from the user's actual firmware.
- Community lists (such as midi.guide, CC BY-SA 4.0) are useful starting points. Keep their licence and attribution, and verify entries.

## 2. Capture MIDI (class-compliant USB MIDI and DIN MIDI)

Tools by system (check that each is installed or installable):
- Linux: `amidi` and `aseqdump` (ALSA utils) for raw ports and sequencer events; `receivemidi` and `sendmidi` are cross-platform command-line tools.
- Windows: MIDI-OX or a similar monitor.
- macOS: Snoize MIDI Monitor or similar.

Method:
1. Record a baseline: connect the device, start the monitor, touch nothing.
2. Change one control at a time. Record the message, then move the control to its minimum, middle and maximum and record each.
3. Note direction: device to host (knob moved) and host to device (message sent to the device). Test both.
4. Test with the device in different modes (global versus part, layer, sequencer, motion) because the same control may send different messages.
5. Write a table: control, message type, CC or NRPN number or SysEx bytes, min, max, resolution (7-bit or 14-bit), direction, channel handling, status.

Request-and-dump SysEx:
- Use the documented dump request, receive the dump to a file, then change exactly one parameter on the device, dump again, and diff the two files. The changed bytes show where that parameter lives.
- Check the SysEx envelope: starts F0, manufacturer ID, device or model IDs, ends F7. Note the manufacturer ID bytes.
- Many devices pack 8-bit data into 7-bit SysEx bytes. Find the packing rule in the official document (for example, KORG's 7-bit to 8-bit codec is listed in its spec) and decode before diffing.
- Find and verify any checksum by changing one parameter and recomputing. Do not guess; test against dumps from the device.

## 3. Capture USB (non class-compliant devices, vendor apps)

Needed when a device uses a vendor driver or custom USB control messages (for example some audio interfaces' mixers) and no MIDI port carries the data.

- Wireshark records USB URBs, which are transfers as the host stack sees them, not individual USB packets; raw packets need a hardware sniffer (V: Wireshark wiki, USB capture setup).
- Linux: `sudo modprobe usbmon` if there are no `/dev/usbmon*` devices; capture on `usbmonN` for bus N, or `usbmon0` for all buses; the user must be able to read the usbmon devices (group, udev rule or ACL) (V).
- Windows: use USBPcap (V). Past issues included blocked mouse or keyboard input; check the wiki before installing.
- macOS: capture uses interface `XHC20` after `sudo ifconfig XHC20 up`; the wiki says System Integrity Protection apparently has to be disabled on Catalina and later (V). Prefer another system if possible.
- Capture the vendor's own app talking to the user's device, for example from a Windows guest in a virtual machine with the device passed through while a Linux host captures on the matching bus (V: method described on the Wireshark wiki).
- Do the same one-change-at-a-time discipline: perform one action in the vendor app, capture, mark it in the log.
- Decode control transfers (request type, request, value, index, data) into a table. Repeat each action to confirm the bytes are stable.

## 4. Allowed and not allowed

- Observing the messages that a program sends to the user's own device, and reading official documentation, is the normal way to learn a protocol.
- Do not decompile or disassemble someone else's software, and do not copy their code, graphics, data tables or presets. Some laws allow limited reverse engineering for interoperability, but licence agreements can forbid it and rules vary by country. Wire-level capture gives the same facts without that question.
- Do not publish vendor documents, factory patches, firmware or logos. Link to them.
- Do not use captures to bypass copy protection or licensing.

## 5. Write the MIDI implementation document

Use `docs/MIDI-IMPLEMENTATION.md` in the project repo:

- Header: device, firmware version tested, date, sources (official document title, revision and link; capture setup).
- Global conventions: channel, byte order, 7-bit packing, checksum method.
- Table of controls: name, message, range, resolution, direction, notes, status (verified on hardware, official only, unverified).
- SysEx section: request formats, dump formats with byte offsets, how to decode, checksum, examples (short hex) from the user's own device.
- Known quirks and conflicts (for example two documents disagreeing on a CC number), with how each was resolved.
- A test checklist the user can repeat on new firmware.

## 6. Safety checks before the controller sends anything

- Send only messages recorded in the table as verified or documented.
- Throttle and chunk output; some devices drop messages when flooded.
- Never auto-send on startup; read first, send only on user action.
- Keep a "restore from backup" button next to any write feature.

## Sources

- Wireshark wiki, USB capture setup: https://wiki.wireshark.org/CaptureSetup/USB
- KORG, minilogue xd MIDI Implementation (support download page): https://www.korg.com/us/support/download/manual/0/811/4440/
- oxur/minilogue-xd (third-party Rust implementation of that spec): https://github.com/oxur/minilogue-xd
