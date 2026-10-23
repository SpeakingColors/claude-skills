---
name: arduino-electronics-soldering
description: Use when helping a non-programmer with Arduino or Teensy projects, MIDI hardware, soldering, or safely fixing and de-humming audio gear, on Bazzite Linux.
---

# Arduino, electronics and soldering

Labels: VERIFIED (source) = read on a page fetched this session; COMMUNITY = widely repeated practice, not checked here; UNVERIFIED = recall, check before relying on it. Never present UNVERIFIED as fact.

## How to work with the reader
- Assume the reader is not a programmer. Plain words first, then one exact step. One change at a time, ask the reader to test, then continue.
- One change at a time. After each step, say what the reader should see.
- Safety first: state the danger before the step, not after.

## Safety rules (read before anything else)
- Mains voltage can kill. Never open a mixer, amp or PSU that is plugged in. UNVERIFIED as a rule list; COMMUNITY as universal advice.
- Unplug, wait, then touch. Big capacitors in power supplies can hold charge after unplugging. COMMUNITY.
- Do not work on mains-powered internals (power supply, transformer, mains wiring) unless trained. Stop and send to a technician. COMMUNITY.
- Low-voltage work (Arduino, Teensy on USB 5 V, MIDI, audio signal paths) is the safe zone for learning. COMMUNITY.
- Wash hands after soldering, especially with leaded solder; no food or drink at the bench. VERIFIED (Adafruit soldering guide) says lead builds up in the body through inhalation, ingestion or skin contact.
- Ventilate: open window, or a fan with a filter if you do more than a few joints. VERIFIED (Adafruit soldering guide).

## Safe-work checklist
1. Device unplugged from mains and USB; battery out if any.
2. Photos taken of the inside before touching anything.
3. Work area clear, well lit, ventilated; iron stand ready.
4. Eye protection on; no loose sleeves or dangling jewelry.
5. Wrist strap or touch a grounded metal object before handling chips (ESD). COMMUNITY.
6. Change one thing, then test. Write down what you changed.
7. Power up only after a visual check for solder bridges and loose strands.
8. If unsure about anything with mains, stop.

## Choosing a board (all COMMUNITY unless marked)
- Arduino Uno: easiest first board, many tutorials, 5 V logic. No built-in USB MIDI (its USB chip is separate). UNVERIFIED on the exact USB chip.
- ESP32: Wi-Fi and Bluetooth, 3.3 V logic. More to learn. Not a first board.
- RP2040 (Raspberry Pi Pico): cheap, 3.3 V logic, can act as USB MIDI. UNVERIFIED on library details.
- Teensy 4.1: fast, 3.3 V logic, strong audio and MIDI support. If the reader already owns one that runs an M8 headless rig, do not erase it casually. Back up the M8 firmware setup first. UNVERIFIED on the exact M8 restore steps; ask the reader before flashing anything.
- Buy a second, cheap board for experiments rather than risking a Teensy that runs an M8 headless.
- 5 V signals into a 3.3 V board can damage it. Check the logic level before wiring. COMMUNITY.

## Toolchain on Bazzite (immutable Fedora; Flatpak and Distrobox)
Do not layer packages with rpm-ostree unless nothing else works. COMMUNITY.

Option A, arduino-cli (works in a Distrobox or the host home folder):
- VERIFIED (arduino-cli 1.5 install page): install script
  `curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh` installs to `$PWD/bin` by default.
- VERIFIED (same page): `BINDIR=~/local/bin` before `sh` installs to another folder; the folder must be in PATH to run it from anywhere.
- VERIFIED (same page): Homebrew install is `brew install arduino-cli`.
- Typical flow: `arduino-cli core update-index`, then `arduino-cli core install <package>`, `arduino-cli compile`, `arduino-cli upload`. UNVERIFIED on exact flags; check `arduino-cli --help`.

Option B, Arduino IDE 2 as a Flatpak:
- UNVERIFIED that an official Flathub build exists and how it handles serial access; the Flathub page could not be fetched. Check Flathub in the Discover app before promising it.
- Flatpak apps may need device access permission for serial. UNVERIFIED; check with Flatseal.

Option C, PlatformIO (in Distrobox or VS Code): COMMUNITY. Good for Teensy. PlatformIO's udev page below is VERIFIED but does not mention Teensy.

### Serial and USB permissions
- VERIFIED (PlatformIO udev page): Linux needs udev rules for supported boards; rules go in `/etc/udev/rules.d/99-platformio-udev.rules`; run `pio device list` to see the board's VID and PID.
- VERIFIED (same page): after installing rules reload with `sudo udevadm control --reload-rules` then `sudo udevadm trigger`, then unplug and reconnect.
- VERIFIED (same page): alternative is group membership; find the port's group with `ls -l /dev/ttyACM0` (dialout, plugdev or uucp are typical), then `sudo usermod -a -G dialout $USERNAME`, then log out and back in; check with `id`.
- VERIFIED (same page): `sudo chmod a+rw` on the port only lasts while the device stays plugged in.
- Fedora usually names the serial group dialout. COMMUNITY. On Bazzite, group changes can need a `/etc/group` quirk. UNVERIFIED; check Bazzite docs.

### Teensy specifics
- VERIFIED (PJRC Linux loader page): by default udev makes the Teensy read-only, so uploads fail until the PJRC rules file is installed to `/etc/udev/rules.d/00-teensy.rules`, e.g. `sudo cp 00-teensy.rules /etc/udev/rules.d/`.
- The rules file is at https://www.pjrc.com/teensy/00-teensy.rules. It would not display here (binary); download it with a browser. UNVERIFIED on its contents.
- On Bazzite /etc is writable (it is a layered config area). COMMUNITY.
- VERIFIED (PJRC Linux loader page): the Teensy Loader runs automatically on Verify/Upload from Arduino software once Teensyduino is installed; pressing the board's pushbutton starts HalfKay (bootloader mode).
- Teensyduino on Linux is an installer run against an Arduino IDE 1.8.x folder. UNVERIFIED for IDE 2; use arduino-cli or PlatformIO for Teensy 4.1 and check PJRC's current install page first.

## First-sketch workflow (Uno or similar)
1. Plug in via USB. Check `ls /dev/ttyACM* /dev/ttyUSB*` shows a port.
2. If no permission: fix groups or udev (above), replug.
3. Open the Blink example, select the right board and port.
4. Upload. Built-in LED blinks = toolchain works.
5. Change only the delay number, upload again, see the change.
6. Then add one thing at a time (button, then LED, then MIDI).
- If upload fails: wrong port, wrong board, cable is charge-only, or permissions. COMMUNITY.

## MIDI projects
USB MIDI on Teensy:
- VERIFIED (PJRC USB MIDI page): choose Tools > USB Type > MIDI; MIDIx4 or MIDIx16 add virtual cables.
- VERIFIED (same page): send with `usbMIDI.sendNoteOn(note, velocity, channel)` and `sendNoteOff`; also `sendControlChange`, `sendProgramChange`, `sendPitchBend`, `sendSysEx`.
- VERIFIED (same page): call `usbMIDI.read()` in `loop()` to receive; incoming messages must be read or discarded or buffers fill.
- VERIFIED (same page): outgoing messages are batched for up to 1 ms; `send_now()` sends at once. Pace big SysEx sends.
- VERIFIED (same page): example idea is buttons on INPUT_PULLUP pins with the Bounce library for debouncing.
- Warning: a Teensy set to MIDI USB type will no longer be the M8's Serial/Audio mode. Keep a Teensy that runs an M8 separate. UNVERIFIED on M8 USB type needs.

DIN MIDI (5-pin):
- PJRC page does not describe the DIN circuit (VERIFIED absent). It points to the Arduino MIDI Library for serial MIDI.
- Baud rate 31250 and current-loop design with an optocoupler on the input are standard. COMMUNITY. I could not fetch the MIDI spec this session, so exact resistor values: UNVERIFIED; copy a published schematic (midi.org spec or a well-known open design) and do not invent values.

## Debugging
- Multimeter: continuity beep (power OFF) finds shorts and broken joints; DC volts checks 5 V and 3.3 V rails. COMMUNITY.
- Logic analyzer: cheap USB 8-channel plus the free sigrok/PulseView software can read MIDI at 31250 baud. COMMUNITY; UNVERIFIED on Bazzite packaging (try a Flatpak or Distrobox).
- Common culprits: no shared ground, wrong pin number, swapped TX/RX, missing pull-up, power from a weak USB port. COMMUNITY.

## Power, grounding, ESD

## Soldering
Tools to buy (no prices):
- VERIFIED (Adafruit): at least 25 W; adjustable-temperature 30 W is better; best is temperature-controlled, interchangeable tips, 50 W or more (Adafruit cites the 65 W Hakko FX-888 as an example).
- VERIFIED (Adafruit): avoid butane irons and battery irons except in emergencies; avoid torches and soldering guns for electronics.
- VERIFIED (Adafruit): stand with sponge, diagonal cutters, vise or third hand, solder sucker or wick.
Solder and flux:
- VERIFIED (Adafruit): 60/40 tin/lead rosin-core is easiest; lead-free is generally considered safer but may need more heat and more flux.
- VERIFIED (Adafruit): never use acid-core solder or acid flux (plumbing); it destroys electronics.
- Temperature: Adafruit page gave no degrees. Rough starting points of about 320 C leaded and 350 C lead-free are COMMUNITY; adjust to the solder's datasheet.
Through-hole technique (COMMUNITY):
1. Clean tip, tin it lightly.
2. Touch iron to both pad and lead together for 1 to 2 seconds.
3. Feed solder to the joint (not the iron tip); count 1 to 2 seconds.
4. Remove solder, then iron; do not move the joint until it sets.
5. Good joint is a small shiny cone; dull and blobby means cold joint, redo.
6. Clip lead just above the joint.
SMD technique (COMMUNITY): flux first, tack one corner, check alignment, then solder the other pins; drag soldering needs practice. Start with larger SMD parts (0805 size or bigger) on practice boards. UNVERIFIED on specific sizes; fine pitch ICs are advanced.
Desoldering: solder sucker or wick plus flux; add fresh solder first to help old solder flow. COMMUNITY.
Common mistakes:
- VERIFIED (Adafruit): underpowered iron causes long heating, damage and oxides.
- Too much solder; moving the joint while cooling; dirty tip; lifting pads by overheating. COMMUNITY.

## Component basics (COMMUNITY)
- Resistor: limits current; color bands give value; no polarity.
- Capacitor: ceramic has no polarity; electrolytic has polarity (stripe is negative); wrong way can pop.
- Diode: one-way; stripe is cathode. LED is a diode that glows and needs a resistor.
- Transistor: electronic switch/amplifier; check pinout on the datasheet, pins differ by part.
- Op-amp: audio amplifier chip; pin 1 marked by dot or notch; check the datasheet for supply voltage.
- Connectors: XLR, 1/4 inch TRS, DIN; check pin numbering from the connector datasheet.
- Reading a schematic: lines are wires, triangles are ground symbols, same labels are connected. Follow one signal path at a time.

## Gear repair mindset
- Photograph, label and map every connector before removing.
- Large smoothing capacitors can hold charge. COMMUNITY.
- Separate low-voltage signal boards from mains power board. Leave the mains section to a technician. COMMUNITY.
- Stop and send to a technician when: mains wiring is involved, a smell of burning, blown fuses that keep blowing, swollen caps near the PSU, or you are unsure.
- Use only the correct fuse type and rating; never bypass a fuse. COMMUNITY.

## Hum and noise principles (general, COMMUNITY)
- Hum often comes from a ground loop: several ground paths between devices pick up mains hum. Test by unplugging cables one at a time. COMMUNITY.
- ESD and grounding: touch grounded metal before handling chips; share a common ground in every circuit. COMMUNITY.
- Balanced cables (XLR or TRS) cancel hum picked up on both wires; use them where the gear supports it.
- Unbalanced cables pick up hum more; keep them short and away from power cables.
- Shield (screen) drains interference to ground; one-end grounding is sometimes used to break loops. UNVERIFIED on when it is safe; do not cut shield wires on gear.
- Never lift the safety earth on mains plugs. This is dangerous. Use a proper audio isolator or DI box instead. COMMUNITY.
- For hum in a Denon DJ mixer (written for a reader who owns one): first test outside the mixer (different outlet, remove one cable at a time, laptop on battery, try balanced out). Model-specific cause: UNVERIFIED; do not open it unless the cause is pinned to a known internal fault and the unit is unplugged.

## Starter shopping list (no prices)
- Temperature-controlled soldering iron with stand and spare tips
- Rosin-core solder (leaded 60/40 or lead-free, the reader's choice; see safety notes)
- Flux pen, solder wick, solder sucker
- Flush cutters, tweezers, helping hands, magnifier
- Fume extractor or fan with carbon filter
- Digital multimeter with continuity beep
- Breadboard, jumper wires, assorted resistors and capacitors, LEDs, buttons
- USB cables that carry data (not charge-only)
- Spare cheap Arduino Nano or Uno clone, plus one extra Teensy or Pico for experiments
- 6N138 or similar optocoupler, 5-pin DIN sockets (for a MIDI project; check the circuit you copy)
- 8-channel USB logic analyzer
- Practice soldering kit
- Safety glasses

## Sources (fetched this session)
- https://www.pjrc.com/teensy/td_midi.html
- https://www.pjrc.com/teensy/loader_linux.html
- https://arduino.github.io/arduino-cli/1.5/installation/
- https://learn.adafruit.com/adafruit-guide-excellent-soldering
- https://docs.platformio.org/en/latest/core/installation/udev-rules.html

