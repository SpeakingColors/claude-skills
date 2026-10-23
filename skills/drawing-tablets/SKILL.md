---
name: drawing-tablets
description: Use when helping a non-programmer choose, set up or troubleshoot a drawing tablet or pen display (Wacom, Huion, XP-Pen, Gaomon, Xencelabs, iPad) on Bazzite KDE, Windows or macOS.
---

# Drawing tablets for a beginner on Bazzite (also Windows and macOS)

Research date: 2026-10-23. Prices: none read on any page, so none are quoted. Check the shop.
Labels: VERIFIED (source), COMMUNITY (wiki, forum, retailer), UNVERIFIED (not read on a fetched page).
Fetch limits: vendor sites (wacom.com, huion.com, xp-pen.com, gaomon, xencelabs, parblo, samsung.com), opentabletdriver.net, wiki.archlinux.org and Reddit were not readable here. Hardware numbers below come from driver source files, which are what the Linux stack actually uses.

## 0. How to work with the reader
1. Assume the reader is not a programmer. Plain words first, then one exact step. One change at a time, ask the reader to test, then continue.
2. Test with a quick circle and line drawing before the next change.
3. Ask first: which tablet (exact model code on the back), which desktop session (Wayland or X11), which app.
4. Never run `curl ... | bash` from a web page. On Bazzite use `ujust` (section 6).
5. Colour, palettes, layout: hand off (section 14). This skill is only the pen and the tablet.

## 1. Tablet types
- Pen tablet, no screen (Intuos, Inspiroy, Deco, Wacom One Pen). You look at the monitor while the hand moves elsewhere. Cheapest. Takes about a week to feel natural (UNVERIFIED, common teaching).
- Pen display (Cintiq, Kamvas, Artist, Wacom One Pen Display). A screen you draw on. Wikipedia: "draw directly on the screen" (COMMUNITY). It is a second monitor, so mapping matters (section 8).
- Standalone / tablet PC: a full computer with a pen screen. libwacom lists Cintiq Companion and MobileStudio-era pens, and Wacom Movink 13 (DTH-135K0C, touch, Pro Pen 3E) as a display device (VERIFIED, libwacom data). Prices and current availability: UNVERIFIED.
- iPad + Apple Pencil. VERIFIED, apple.com compare page: current iPad Pro 11 and 13 inch (M5), iPad Air 11 and 13 inch (M4), iPad (A16), iPad mini (A17 Pro).
  - Pencil Pro works with iPad Pro (M4, M5), iPad Air (M2 to M4), iPad mini (A17 Pro). Pencil (USB-C) also works with iPad (A16) (VERIFIED, support.apple.com HT211029).
  - Apple's feature table: Pencil Pro has pressure, tilt, hover, squeeze, barrel roll, double tap. Pencil (USB-C) has tilt and hover but pressure sensitivity is "No" (VERIFIED, apple.com/apple-pencil). For drawing buy Pencil Pro or an older pressure-capable Pencil.
  - iPad Pro M5: 2420 x 1668 (11 inch) and 2752 x 2064 (13 inch) at 264 ppi, optional nano-texture glass on 1TB and 2TB only (VERIFIED, apple.com specs). iPad Air M4: 2360 x 1640 and 2732 x 2048 (VERIFIED).
  - It runs iPadOS, not Linux. Use it as a separate sketch device and move files over (Nextcloud, USB). Procreate details: UNVERIFIED (page blocked).
- Android (Samsung Galaxy Tab): Galaxy Tab S11 (released 2025-09-19) includes the S Pen; screen 1600 x 2560, 120 Hz (COMMUNITY, Wikipedia). Wikipedia's box shows a discontinued date of 2026-09-30, so ask Samsung for the current model. Pressure levels: UNVERIFIED.
- Krita runs on Android and has special Xiaomi stylus workarounds (VERIFIED, Krita Tablet Settings page). Other Android drawing apps: UNVERIFIED.

## 2. Spec glossary (plain words)
- Active area: the part of the tablet the pen reads. Wikipedia calls it the usable drawing zone (COMMUNITY). Bigger area means bigger arm movements.
- Pressure levels: how many steps between light and hard. Driver configs show max values 2047, 4095, 8191, 16383. Levels are that number plus one: 2048, 4096, 8192, 16384 (VERIFIED values, OpenTabletDriver configs; plus one is my reading). Above 4096 you will not feel the difference in a beginner brush (UNVERIFIED opinion).
- Tilt: the pen angle, used for shading and calligraphy brushes. libwacom marks Pro Pen 3 with axes Tilt, Pressure, Distance and 3 buttons (VERIFIED).
- Resolution (LPI, lines per inch): how finely the pen position is read. OpenTabletDriver says LPI is "commonly 5080 or 2540" (VERIFIED, OTD General FAQ). Compute it: LPI = MaxX / width in mm x 25.4. Example Wacom PTK-670: 52600 / 263 x 25.4 = about 5080. Wacom CTL-6100: 21600 / 216 x 25.4 = 2540. Both are fine for drawing.
- Report rate (points per second), latency (delay pen to screen), parallax (gap between pen tip and the drawn line on a pen display), laminated display (glass and panel fused, less gap), colour gamut (sRGB, AdobeRGB, P3 coverage), ExpressKeys (Wacom name for the buttons on the tablet frame). No page was fetched with numbers for these. Treat any figure as UNVERIFIED until read on the vendor page.
- Pad = the buttons, rings, dials on the tablet. Stylus = the pen. KDE and libwacom use these words (VERIFIED).
- Active pen needs a battery; passive pen (electromagnetic) does not (COMMUNITY, Wikipedia). Wacom-style pens in this list need no battery (UNVERIFIED for each model).

## 3. Verified hardware table (driver data, not vendor pages)
Source: OpenTabletDriver configuration files (digitizer size in mm, max pressure) and libwacom data (name, features). Digitizer size can differ a little from the marketed active area. "OTD status" is from OpenTabletDriver TABLETS.md. Check the real active area on the vendor page (UNVERIFIED here).
| Model (code) | Digitizer mm | Pressure levels | Notes |
|---|---|---|---|
| Wacom Intuos S (CTL-4100) | 152 x 95 | 4096 | OTD Supported |
| Wacom Intuos M (CTL-6100) | 216 x 135 | 4096 | OTD Supported |
| Wacom One Pen tablet S / M (CTC-4110WL / CTC-6110WL) | 152 x 95 / 216 x 135 | 4096 | OTD Supported |
| Wacom Intuos Pro S 3rd gen (PTK-470) | 187 x 105 | 8192 | OTD Supported; libwacom 178 x 102 |
| Wacom Intuos Pro M 3rd gen (PTK-670) | 263 x 148 | 8192 | OTD Supported; libwacom: 254 x 152, 2 dials, buttons both sides, no touch |
| Wacom Intuos Pro L 3rd gen (PTK-870) | 349 x 195 | 8192 | OTD Supported |
| Wacom Intuos Pro M 2nd gen (PTH-660) | 224 x 148 | 8192 | OTD "Has Quirks": wheel reports backwards |
| Wacom One Pen Display 13 (DTC-133) | 294 x 166 | 4096 | OTD Supported |
| Wacom Cintiq 16 (DTK-1660) | 348 x 198 | 8192 | OTD Supported |
| Wacom Movink 13 (DTH-135) | 298 x 169 | 8192 | OTD "Missing Features": touch |
| Huion Inspiroy H640P (small) | 160 x 100 | 8192 | OTD Supported |
| Huion Inspiroy 2 M (H951P) | 221 x 138 | 8192 | OTD Supported; 11 buttons |
| Huion Inspiroy 2 L (H1061P) | 267 x 167 | 8192 | OTD "Has Quirks": group keys act as aux buttons |
| Huion Kamvas 13 (Gen 3) | 294 x 165 | 16384 | OTD "Has Quirks": function-switch buttons act as normal keys |
| Huion Kamvas 16 (Gen 3) | 350 x 197 | 16384 | OTD Supported |
| Huion Kamvas Pro 24 (Gen 3) | 527 x 296 | 16384 | OTD "Missing Features": touch |
| XP-Pen Deco 01 V3 | 254 x 159 | 16384 | OTD Supported |
| XP-Pen Deco Pro MW Gen2 / LW Gen2 | 229 x 143 / 279 x 174 | 16384 | OTD Supported |
| XP-Pen Deco mini7 V2 | 178 x 111 | 16384 | OTD Supported |
| XP-Pen Artist Pro 16 (Gen2) | 345 x 215 | 16384 | OTD Supported |
| XP-Pen Innovator 16 | 344 x 194 | 8192 | OTD Supported |
| Gaomon S620 (16K variant) | 165 x 102 | 16384 | OTD Supported |
| Gaomon M5 V2 | 178 x 110 | 16384 | OTD Supported |
| Xencelabs Pen Tablet S / M | 178 x 101 / 262 x 148 | 8192 | OTD Supported; 3 aux buttons |
| Xencelabs Pen Display 16 (LPH1612U-A) | 344 x 194 (libwacom) | not read | libwacom 2.19.0 lists it; no OTD config found |
| Parblo Intangbo SW / Ninos N7B | 183 x 103 / 178 x 114 | 16384 / 8192 | OTD: SW "Missing Features" (wheel, wireless); N7B "Has Quirks" (size unconfirmed) |
- OpenTabletDriver status words: Supported, Has Quirks, Missing Features (VERIFIED, TABLETS.md).
- libwacom 2.15 to 2.20 added many of these names: Innovator 16, Deco01 v3, Cintiq 16/24 (DTK168), Wacom One 14, Kamvas 13/16 Gen 3, Deco Pro LW Gen 2, Xencelabs Pen Display 16, Gaomon M5 V2, Kamvas Pro 27, Inspiroy Frego S, Deco SE, Gaomon S620 (VERIFIED, libwacom NEWS). A libwacom entry only says the tablet is described. It does not make it work (VERIFIED, README).
- Not in the data I could read: Intuos Pro pressure on the vendor page, Cintiq Pro and Movink screen specs, any Parblo or Gaomon pen display specs, any colour gamut. UNVERIFIED.

## 4. How to choose
- Budget tiers (no prices read): tier 1 small pen tablet; tier 2 medium pen tablet with 8192 levels; tier 3 pen display about 13 to 16 inch; tier 4 large Cintiq-class display. Ask the reader their budget, then check shop prices.
- Size: a medium pen tablet (about 220 to 260 mm wide) suits a 24 inch monitor and arm-sized strokes. Small (about 150 to 180 mm) is good for pixel art and travel. This is common advice (UNVERIFIED).
- Aspect ratio: most monitors are 16:9. Many tablets are 3:2 or 16:10 (254 x 152 is 5:3). Map with "lock aspect ratio" or circles turn into ovals (section 8).
- Left-handed: libwacom says PTK-670 has pad buttons on both sides and is not reversible; the 2nd gen PTH-660 is reversible (VERIFIED). KDE's left-handed option "often reverses the pad buttons so the tablet can be used upside-down" (VERIFIED, KCM text). Ask which hand first.
- Linux risk rank (see section 5): Wacom lowest risk, then models marked OTD Supported, then anything Has Quirks or Missing Features.
- Pen display extras to check on the vendor page before buying (UNVERIFIED here): laminated glass, parallax, matte surface, colour gamut, cable type (one USB-C or three cables), stand, and whether the pen needs a battery.
### Recommendation (from verified specs only)
- Start with one medium pen tablet: Wacom Intuos Pro M 3rd gen (PTK-670). Why: 8192 levels (OTD), tilt pen Pro Pen 3 (libwacom), two dials and buttons on both sides (libwacom), no touch to disturb the hand (libwacom), OTD Supported, Wacom kernel driver and libwacom maintained upstream (VERIFIED, linuxwacom READMEs). Confirm the model is still sold and its price on wacom.com (UNVERIFIED).
- Lower-cost equal-spec options: Huion Inspiroy 2 M (H951P) or XP-Pen Deco 01 V3. Both are OTD Supported with 8192 and 16384 levels. Tilt on these pens: UNVERIFIED.
- By use case:
  - Logos and vector (Inkscape): the PTK-670 above. Vector work is mostly clicking and dragging nodes, so pressure barely matters. Do not spend on a pen display for this.
  - Pixel art (Aseprite, LibreSprite, Pixelorama): the same tablet, or a small one (Intuos Pro S, Deco mini7 V2, Gaomon S620). Pressure is rarely used for pixel pencils.
  - Painting and album art: first choice is the same tablet. If drawing on screen is wanted, Wacom Cintiq 16 (DTK-1660, 8192 levels, 348 x 198 mm, OTD Supported) or Huion Kamvas 16 (Gen 3, 16384 levels, 350 x 197 mm, OTD Supported). Compare parallax and glass on the vendor pages first.
  - Photo retouch: the pen tablet plus a calibrated monitor. I found no verified gamut numbers for any pen display, so do not pay extra for colour accuracy on a pen display unless the vendor page shows it. See photo-editing-color-grading.

## 5. Linux support status per brand
- Wacom: kernel driver input-wacom and X driver xf86-input-wacom are "included in most major Linux distributions" and give "out-of-the box support for a wide variety of Wacom tablets". You only need to build them for very new devices or old systems (VERIFIED, linuxwacom READMEs). Whether Bazzite's kernel includes every new model: UNVERIFIED.
- libwacom: a database of tablet features (size, buttons, left-handed, built-in screens). Used by GNOME, KDE and libinput. "libwacom does not make a tablet work." Tools: `libwacom-list-local-devices` (devices it recognises) and `libwacom-list-devices` (all known). If your tablet is missing there, it is missing from the database (VERIFIED, libwacom README).
- libinput: handles the pen on Wayland and X11. By default it reports pen position and pressure (VERIFIED for X11, DIGImend README). Pressure curves and button maps on Plasma are handled by the KDE Drawing Tablet page (section 8).
- Huion, Gaomon, XP-Pen, Parblo: tablets from UC-Logic-style makers use the kernel driver `hid_uclogic`. DIGImend kernel drivers are the out-of-tree version for old kernels and testing; install needs kernel headers and DKMS, and Secure Boot blocks unsigned modules ("Required key not available") (VERIFIED, DIGImend README). Not a good fit for an immutable system (section 6).
- OpenTabletDriver (OTD): open source user-mode driver for Windows, Linux, macOS (macOS marked Experimental). Needs its daemon running. Supports many Huion, XP-Pen, Gaomon, Parblo, Xencelabs and Wacom models (VERIFIED, README, TABLETS.md). No Bluetooth support, USB only; partial wireless dongle support (VERIFIED, OTD General FAQ).
- Vendor Linux drivers (Huion, XP-Pen, Gaomon): not read, UNVERIFIED. Avoid them on Bazzite until a source is read.
- Reports from users (Reddit r/wacom, r/linux_gaming, r/DigitalArt): not fetched. No COMMUNITY claims made.

## 6. Bazzite specifics (immutable Fedora Atomic)
- Bazzite includes OpenTabletDriver udev rules, and the full OTD app installs from Bazzite Portal or `ujust install-opentabletdriver` (VERIFIED, Bazzite README and OTD install page, section Bazzite).
- Install order for apps: Bazaar (Flatpak), Homebrew (command line), Distrobox, rpm-ostree layering last (VERIFIED, docs.bazzite.gg Installing and Managing Software). See bazzite-kde-linux for details and rollback.
- Rule: never layer vendor .rpm or .deb tablet drivers. Layering adds update cost and can block rollback (UNVERIFIED for tablets). DKMS drivers on an immutable system: UNVERIFIED, do not try first.
- The Flatpak build of OTD is unofficial. It needs system-wide udev rules and kernel module blacklist, and "updating associated files must be manually repeated" on updates (VERIFIED, OTD install page and flathub README). On Bazzite use `ujust` instead.
- Autostart OTD on a systemd desktop: `systemctl --user enable opentabletdriver.service --now`. If that is not enough, `otd-daemon` runs as a normal user, never root (VERIFIED, OTD Linux FAQ). Whether the ujust recipe does this for you: UNVERIFIED, so check with `systemctl --user status opentabletdriver`.
- OTD keeps two kernel modules out of the way: `wacom` and `hid_uclogic`. Test unload with `sudo rmmod wacom hid_uclogic` (VERIFIED, OTD Required Permissions). A tablet then works only while OTD runs. Reversing: `sudo modprobe wacom hid_uclogic` (VERIFIED, flathub README).
- Plasma: if OTD manages the tablet, KDE shows "This device is managed by a user-space driver that you installed. Use that driver to configure the tablet" (VERIFIED, plasma-desktop source).
- Do NOT use OTD and the kernel driver for the same tablet at once: "two moving cursors" is the symptom (VERIFIED, OTD General FAQ).
- Krita Flatpak (org.kde.krita): permissions are network, x11, pulseaudio, dri, host filesystem. It uses the x11 socket, so it runs through XWayland on a Wayland session (VERIFIED manifest; XWayland is my reading). Pen buttons through XWayland: UNVERIFIED.
- Changing Flatpak permissions with Flatseal: UNVERIFIED.

## 7. Windows and macOS driver setup
- Windows, Wacom: install the Wacom driver from wacom.com (UNVERIFIED, page not read). Windows allows only one WinTab-style driver at a time. Uninstall the old one before a new one, and reboot after (VERIFIED, Krita manual). Windows updates can break tablet drivers; reinstalling usually fixes it (VERIFIED).
- Windows, Huion, XP-Pen, Gaomon: vendor driver from the maker site (UNVERIFIED). Never install two vendors' drivers together.
- Windows, OpenTabletDriver: install .NET Desktop Runtime x64, extract the zip into its own folder, run the app. Most tablets do not need WinUSB; only install it (Zadig) if the supported-tablets Notes column says so. Do not run as Administrator (VERIFIED, OTD wiki). Pressure needs the VMulti driver plus the WindowsInk plugin (VERIFIED, OTD Windows FAQ). Clean other drivers with TabletDriverCleanup first (VERIFIED).
- macOS, OTD: drag the app into Applications. Grant Accessibility (move the cursor) and Input Monitoring (relative mode). If the cursor does not move, remove the entry and add it again (VERIFIED, OTD wiki). "Apple could not verify" is fixed with Apple's open-from-unknown-developer steps (VERIFIED).
- macOS vendor drivers and Sequoia/Tahoe permission names: UNVERIFIED.
- Windows Ink vs WinTab: Windows Ink is the modern Microsoft pen API; WinTab is the old Wacom API. Pick one per app (section 9).

## 8. First-time setup (Plasma Wayland, step by step)
1. Plug the tablet in with a data USB cable (a charge-only cable fails). Turn the tablet's wired/BT switch to USB if it has one.
2. Run `lsusb`. You should see a line for the tablet. If not, see tree 12.4.
3. Open System Settings and search "tablet". The page is called Drawing Tablet (VERIFIED, kcm_tablet.json). Exact sidebar location: UNVERIFIED.
4. Pick the Device. Tabs: Pen, Pad, Display (VERIFIED, plasma-desktop source).
5. Display tab. "Map to screen:" choose the monitor you draw on. Set Orientation (rotate if needed). Tick "Lock aspect ratio" so circles stay round. "Mapped Area:" shows the tablet part used. Mode "Pen" (point is where the pen is) is correct for drawing; "Mouse" acts like a touchpad.
6. Pen tab. "Pen Pressure:" is a curve between pen pressure and what apps receive. "Pressure Range:" clamps very light or very hard pressure. Start at the default. Change only if a soft line is hard to make (VERIFIED labels).
7. Pen tab, pen buttons: set Button 1 to Right-click and Button 2 to Middle-click or a key you use (Undo is common). Actions offered: Do nothing, Send keyboard key, Send mouse button click, Send pen button, Act as scroll wheel, Defer to application (VERIFIED). Tip: "Defer to application" leaves it to Krita.
8. Pad tab. Give each pad button a key: Undo (Ctrl+Z), Redo (Ctrl+Shift+Z), Brush size - and +, Pan (Space). Dials or rings: Clockwise and Counterclockwise keys, for example brush size (VERIFIED).
9. Left-handed mode and the "Test Tablet..." button are on the same page. The tester prints X, Y, P (pressure), TX, TY (tilt). Press hard and light. P should move from near 0 to near 100 percent (VERIFIED).
10. Pen displays only: Calibrate (tap each target) is in the Display area; "Calibration Not Supported" appears if the device cannot. Touch screens and pen displays get a "Reset Custom Calibration" button (VERIFIED).
11. Draw a circle and a long straight line in Krita. Check: round circle, line under the pen tip, pressure changes the width.
- With OTD instead of KDE settings: open OTD. Set output mode to Artist Mode for pressure, remove the tip binding, set the area, save. Check `libinput list-devices | grep -i OpenTabletDriver` shows "Artist" (VERIFIED, OTD Linux FAQ). Pen buttons and ExpressKeys are set in OTD bindings; "regular mouse buttons" do not work in Artist Mode, use the Artist pen bindings (VERIFIED).
- Save OTD settings: Presets folder and settings.json (VERIFIED, OTD General FAQ). Keep a copy before updates.
- Monitor layout changed (plugged a screen, changed resolution)? Restart the OTD daemon, then recheck the area (VERIFIED, known OTD bug #1143).
- Windows Ink off or on: see section 9 for each app. Tablet mode on Windows (for pen displays used as touch tablets): UNVERIFIED.

## 9. Per-app setup
- Krita (VERIFIED, Krita Tablet Settings page). Settings > Configure Krita > Tablet Settings.
  - "Input Pressure Global Curve": softer or harder feel for every brush.
  - Windows: Tablet Input API. WinTab is recommended for most Wacom tablets. "Windows 8+ Pointer Input" (Windows Ink) is experimental, suggested for N-Trig (some Surface) or tablets that work badly with WinTab. If the setting does not take, restart Krita (my advice).
  - Advanced WinTab: mapping to a screen, the whole virtual screen, or a custom area.
  - "Mouse events for right/middle clicks": use if the side buttons do not reach Krita. Restart Krita.
  - "Maximum Brush Speed" and "Brush Speed Smoothing": for erratic brush speed. Too much smoothing hides subtle speed changes.
  - Tablet Tester: blue lines are tablet events, red lines are mouse events. No blue lines means Krita cannot see the tablet. It ignores Krita's own pressure curve.
  - Reset a broken Krita config by renaming its config file (VERIFIED, Krita drawing tablets page).
  - Stabiliser: Freehand Brush tool has No Smoothing, Basic Smoothing (light, for older tablets), Weighted smoothing (Distance, Stroke Ending, Smooth Pressure, Scalable Distance) and Stabilizer (averages input, finishes the line, a circle shows around the cursor) (VERIFIED, Krita Freehand Brush page).
  - Flatpak Krita: see section 6.
- GIMP (VERIFIED, gimp-help source; version of the page not stated). Edit > Input Devices configures tablets. Set each tablet pen device (stylus, eraser) to Mode "Screen". Mouse usually Disabled. On Windows, Preferences > Input Devices > "Pointer Input API": Windows Ink is preferred, try Wintab if it fails. "Share tool and tool options between input devices" keeps one tool for pen and mouse. OTD's GIMP 2 notes: devices `xwayland-tablet stylus`, `xwayland-tablet eraser`, `OpenTabletDriver Virtual Artist Tablet Pen` to Screen, others Disabled; use a dynamics profile such as "Basic Dynamics" for pressure (VERIFIED, OTD LinuxAppSpecific). GIMP 3 differences: UNVERIFIED.
- Inkscape: UNVERIFIED (page blocked). Know the idea: Pen tool places nodes by clicks and drags; Pencil tool is freehand with smoothing; Calligraphy tool reads pressure and tilt. Confirm menu names in the manual.
- Aseprite (VERIFIED, aseprite docs).
  - Windows: Edit > Preferences > Tablet. Choose "Windows 8/10 Pointer API" (default since v1.2.34), "Wintab", or "Wintab (direct packet processing)". Changes apply at once. If it will not start use `-disable-wintab`.
  - Linux X11: if pressure is missing (v1.2.35 and newer), run `xinput --list`, then add `x11_stylus_id = <device name>` under `[general]` in aseprite.ini.
  - Dynamics: in the context bar. Left column Pressure (pen only), right column Velocity. One option per row. Sensor thresholds and Min/Max set the range. "Stabilizer" draws the stroke some pixels away from the cursor. "Pixel-perfect" mode is a separate toggle in the context bar.
  - Aseprite licence and price: see graphic-design-expert (its own EULA; price not read here).
- LibreSprite: a GPL v2 fork of old Aseprite for Linux, macOS, Windows, Android (VERIFIED, README). Its tablet settings: UNVERIFIED.
- Pixelorama (VERIFIED, translation strings): Preferences > Drivers has "Tablet pressure sensitivity:" and, on Windows, "Tablet driver:". "If you have Windows Ink enabled, select winink." Dynamics menu has Stabilizer, Pressure, Velocity; Pixel Perfect is a tool option.
- MyPaint: README says "Extensive graphic tablet support" (VERIFIED). Details: UNVERIFIED.
- Blender Grease Pencil: UNVERIFIED (page blocked). Pressure and Stabilize Stroke exist in Draw mode as far as I know (UNVERIFIED).
- Photoshop, Affinity, Clip Studio Paint, Procreate: UNVERIFIED (not read). Ask for the app and version. On Windows, Photoshop and Clip Studio can use WinTab or Windows Ink (UNVERIFIED). Use design-software-guide for choosing apps.
- Rule for every app: set the pressure curve in ONE place at a time (driver, app global curve, or brush curve), never stack all three (UNVERIFIED, practical).

## 10. Drawing technique basics (UNVERIFIED teaching practice, no source fetched)
- Posture: hold the pen like a pencil, rest the wrist, draw from the elbow and shoulder for long lines.
- Hand-eye warm-ups, 10 minutes a day, one page each: 1) straight lines edge to edge, 2) circles and ovals, 3) parallel lines at equal spacing, 4) spirals, 5) hatching, 6) trace a simple photo outline.
- Pressure drills: draw one line from light to hard and back. Draw 10 lines with 3 pressure levels.
- Lift the pen between strokes; flick the stroke end for tapered lines.
- Stabiliser: start at the lowest setting that cleans wobble. High smoothing makes lines lag. For clean logo lines use Krita's Stabilizer or weighted smoothing; for sketching use No Smoothing.
- Canvas size and DPI: set pixels first, DPI second. For print, work at the final size at 300 DPI (common practice, UNVERIFIED). For web or album art, follow the target size from graphic-design-expert. Never upscale a small sketch for print.
- Brushes: start with a hard round pen for lines and a soft round for shading. Add textured brushes later.
- Vector pen tool vs drawing: the Bezier pen tool gives exact curves you can resize forever (logos). Freehand drawing gives character but not clean at any size. Workflow: sketch in Krita, import the sketch into Inkscape, trace with the Pen tool, then clean nodes.
- Pixel art: work at a tiny canvas (16, 32 or 64 pixels), zoom in, no anti-aliasing, pixel-perfect on, pressure off for the pencil, stabiliser light. Palette rules: color-palette-expert.
- Sketches: use a rough layer at low opacity, then a clean layer. Keep layers named.

## 11. Pen tips (nibs) and maintenance (UNVERIFIED, no page read)
- Nibs wear down. Replace a nib when it looks flat, sharp, or scratches the surface. Use only nibs made for your pen.
- Felt nibs feel like pencil on paper and wear faster; plastic nibs glide (common description). Textured overlay sheets exist, check compatibility with your tablet.
- Clean the surface with a dry or slightly damp soft cloth. No alcohol or abrasives on coated surfaces unless the manual says so.
- Keep the tablet away from cables, monitors and a laptop keyboard: EMI makes the cursor teleport (VERIFIED, OTD General FAQ).
- Store pens flat or in the holder, not standing on the nib.
- Keep the cable and the model code. Photograph the back label for support.

## 12. Troubleshooting trees
### 12.1 No pressure (cursor moves, lines are always thin or full)
1. Open KDE "Test Tablet...". Press hard and light. Does P change? (VERIFIED)
2. P changes, app does not: check app section 9. Krita: Tablet Tester must show blue lines. GIMP: Mode "Screen". Aseprite on X11: `x11_stylus_id`. Pixelorama: Windows Ink and driver choice.
3. P does not change with OTD: output mode must be Artist Mode, tip binding cleared (VERIFIED).
4. P does not change on Windows: switch the app between Windows Ink and WinTab, restart the app. Only one driver installed (VERIFIED, Krita manual).
5. Some Huion/XP-Pen tablets show 2047 or low-resolution config (OTD lists Huion H610 Pro V3 with "very low resolution"). Report the model to the OTD team (VERIFIED, TABLETS.md).
### 12.2 Offset cursor (line appears away from the pen)
1. Pen display: set "Map to screen" to the display you draw on (VERIFIED). Use calibration if offered.
2. Pen tablet on one of several monitors: map to one monitor, lock aspect ratio.
3. OTD with several monitors: right-click the display area, Set to display > Virtual Display, then set the area in the desktop (VERIFIED, OTD Linux FAQ).
4. Changed monitors recently: restart the OTD daemon (VERIFIED).
5. Windows: the Cintiq must be the first in the Wacom desktop list when Windows Ink is off and the offset grows (VERIFIED, Krita manual). Reset Wacom prefs if needed.
### 12.3 Jittery or wobbly lines
1. Move the tablet away from cables, chargers, powered mouse pads, the monitor and keyboard (EMI) (VERIFIED, OTD).
2. Swap the pen. If it persists the tablet may be faulty (VERIFIED, OTD says "replace the tablet" if all else fails).
3. In Krita: turn on Stabilizer or Weighted smoothing; try "Brush Speed Smoothing" (VERIFIED).
4. With OTD in Artist Mode and slow cursor: libinput smoothing quirk. v0.6.5.0 and newer fix it in packaging. Older: add `[OpenTabletDriver Virtual Tablet]`, `MatchName=OpenTabletDriver*`, `AttrTabletSmoothing=0` to `/etc/libinput/local-overrides.quirks`, restart the daemon (VERIFIED). On Bazzite /etc is writable.
5. Straight line at stroke start (Windows Wacom): lower double-click sensitivity in Wacom settings (VERIFIED, Krita manual).
### 12.4 Pen or tablet not detected (Wayland or any)
1. Different USB port and a data cable. `lsusb` should list it. `dmesg` or `udevadm monitor` while plugging in (VERIFIED, OTD General FAQ).
2. Check libwacom: `libwacom-list-local-devices`. Not listed but present in `/proc/bus/input/devices` means a missing database entry (VERIFIED).
3. KDE shows "No drawing tablets found" or "No buttons or other inputs were detected. This could mean the driver for this device is missing" (VERIFIED strings). Then try OTD.
4. OTD: read its log. "Another tablet driver found" means `wacom` or `hid_uclogic` is loaded: run `sudo rmmod wacom hid_uclogic` (VERIFIED). "Not permitted to open HID class device" means udev rules missing; on Bazzite try `ujust install-opentabletdriver` again and reboot (UNVERIFIED as a fix; the error text is VERIFIED). Failed virtual tablet: ENODEV reboot; ENOENT kernel uinput; EACCES permissions (VERIFIED).
5. Bluetooth: OTD cannot use it. Plug in USB (VERIFIED).
6. Wacom CTL-x100 stuck in Android mode: hold the two outer ExpressKeys 3 to 4 seconds until LED brightness changes (VERIFIED, OTD ModelSpecific).
7. Two cursors: two drivers active (VERIFIED).
8. GIMP or Aseprite on XWayland not seeing the stylus: sections 9 and 6.
### 12.5 Button mapping lost after an update
1. Plasma: the Pad and Pen tabs store per device. If a rebase or kernel change renamed the device, re-open Drawing Tablet and reassign (UNVERIFIED which part persists).
2. OTD: settings are in settings.json (Linux .config, Windows %localappdata%); a Backup folder holds old versions. Restore from a preset or backup (VERIFIED). Flatpak OTD: redo udev rules after each update (VERIFIED).
3. Windows Wacom: reset the driver to defaults and reload settings from a backup (VERIFIED, Krita manual). Export a backup after every good setup.
4. Fix lasting: write your button list on paper (Undo, Redo, Brush size, Pan).

## 13. Ergonomics (UNVERIFIED, general advice)
- Screen at eye level, tablet flat, elbow at about 90 degrees, forearm supported.
- Micro-break every 20 to 30 minutes. Stretch fingers and wrists.
- Light grip. A white-knuckle grip causes cramps. Use a pen grip if the barrel is thin.
- A pen display needs a stand or the neck bends. Tilt about 20 degrees (common advice).
- Pain, tingling or numbness in the hand: stop and see a clinician.
- Use shortcuts on the pad to avoid reaching to the keyboard.

## 14. Hand off, do not duplicate
- Logo, album cover, poster design, file sizes: graphic-design-expert.
- Choose or install Krita, Inkscape, GIMP, Affinity: design-software-guide.
- Photo retouching and grading: photo-editing-color-grading.
- Palettes: color-palette-expert. Pixel sprites for games: lock the palette first.
- Flatpak, ujust, rollback: bazzite-kde-linux. Terminal help: linux-terminal-expert. Windows apps on Linux: wine-proton-bottles.

## 15. Not verified (do not state as fact)
- Any vendor spec: report rate, latency, parallax, gamut, active area on vendor pages, price, stock, current model status.
- Wacom, Huion, XP-Pen, Gaomon, Xencelabs, Parblo, Samsung, Procreate, Clip Studio, Adobe, Affinity, Inkscape manual, Blender manual pages (blocked or not fetched).
- Huion and XP-Pen Linux vendor drivers, and DIGImend or hid_uclogic on Bazzite's kernel.
- Whether Bazzite's `ujust install-opentabletdriver` autostarts the daemon, and exact System Settings sidebar position of Drawing Tablet.
- Plasma version on a given Bazzite image (the KDE source read was the development branch, version 6.8.80).
- Tilt on non-Wacom pens, Windows tablet mode, macOS vendor driver permissions.
- Technique, nib, maintenance and ergonomics sections are general practice, no source.
- Reddit and review sites (RTINGS, Tom's Guide): not fetched.

## 16. Sources (fetched)
- Driver data, read from source repositories 2026-10-23: github.com/OpenTabletDriver/OpenTabletDriver (README, TABLETS.md, Configurations JSON), github.com/OpenTabletDriver/opentabletdriver.github.io (wiki: Install/Linux, Windows, MacOS; FAQ/General, Linux, LinuxAppSpecific, Windows, MacOS, ModelSpecific; Documentation/RequiredPermissions), github.com/flathub/net.opentabletdriver.OpenTabletDriver (README, docs/Pre-installation.md, manifest).
- github.com/linuxwacom/libwacom (README, NEWS 2.20.0, data/*.tablet, wacom.stylus), linuxwacom/xf86-input-wacom README, linuxwacom/input-wacom README, DIGImend/digimend-kernel-drivers README.
- github.com/KDE/plasma-desktop kcms/tablet (QML strings, kcm_tablet.json), github.com/ublue-os/bazzite README, docs.bazzite.gg/Installing_and_Managing_Software/.
- github.com/flathub/org.kde.krita manifest, docs.krita.org (Tablet Settings, Drawing Tablets, Freehand Brush tool).
- github.com/aseprite/docs (tablet.md, wintab.md, dynamics.md, troubleshooting.md), github.com/Orama-Interactive/Pixelorama (Translations.pot), github.com/GNOME/gimp-help (Input Devices pages), github.com/mypaint/mypaint README, github.com/LibreSprite/LibreSprite README.
- support.apple.com/en-us/HT211029, apple.com/apple-pencil, apple.com/ipad-pro/specs, apple.com/ipad-air/specs, apple.com/ipad/compare.
- en.wikipedia.org/wiki/Graphics_tablet, en.wikipedia.org/wiki/Samsung_Galaxy_Tab_S11 (COMMUNITY).
