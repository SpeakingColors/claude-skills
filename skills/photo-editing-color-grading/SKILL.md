---
name: photo-editing-color-grading
description: Use when helping a non-programmer edit, colour grade, retouch and export photos for album art, posters, merch and websites, on Bazzite (darktable, GIMP, Krita), Windows or macOS.
---

# Photo editing and colour grading (Bazzite first, dark rave look)

Verify anything marked UNVERIFIED against current docs before acting on it.
Palettes go to color-palette-expert. Layout and type go to graphic-design-expert. Web page layout goes to ux-ui-designer. Buying or comparing apps goes to design-software-guide. Pen tablets go to drawing-tablets. This skill covers the photo itself.

## 0. How to work with the reader
1. Assume the reader is not a programmer. Plain words first, then one exact step (the menu path or one command). One change at a time, ask the reader to test, then continue.
2. Ask the reader to look at the result before the next step.
3. Labels: VERIFIED (source), COMMUNITY (common practice or opinion), UNVERIFIED (not read on a fetched page, never guess).
4. Ask first: which app, which version (Help > About), RAW or JPEG, and where it ends up (screen, print, merch).
5. Never edit the original file. Work on a copy or use an app that keeps edits in a sidecar.
6. Reddit, Adobe, Affinity, Capture One, Cambridge in Colour, ICC.org, Bandcamp and the app sites were blocked in my fetch tool. Only Wikipedia pages and GitHub repos could be read. Claims from blocked sites are UNVERIFIED.
7. Most facts below come from official doc source repositories that I cloned and read (dtdocs, gimp-help, digiKam docs, Krita source, flathub manifests). Sources list at the end.

## 1. Pick the tool (decision list)
- RAW photo, want the best quality and free: darktable (VERIFIED, reads RAW, JPEG, PNG, TIFF, see section 2).
- Layers, text, compositing, poster, merch art: GIMP 3.x (VERIFIED non-destructive layer effects, section 5).
- Painting over a photo, tablet work: Krita (VERIFIED filter layers, Gradient Map, Halftone).
- Sorting thousands of gig photos and batch export: digiKam (VERIFIED Batch Queue Manager).
- Second RAW developer: RawTherapee (VERIFIED, Film Simulation uses Hald CLUT images, not .cube).
- Command line batch jobs: ImageMagick (VERIFIED docs, recipes tested locally on 6.9.12).
- Windows/macOS or paid: Lightroom, Photoshop, Affinity, Capture One, Photopea (all UNVERIFIED here, see section 15).
- Suggested split: darktable for the photo, GIMP for the poster, ImageMagick or darktable-cli for batches.

### Install on Bazzite (Flatpak first)
- App IDs exist on Flathub (VERIFIED, flathub repos): org.darktable.Darktable, org.gimp.GIMP, org.kde.krita, com.rawtherapee.RawTherapee, org.kde.digikam.
- Versions in those manifests on 23 Oct 2026 (VERIFIED): darktable 5.6.2, GIMP 3.2.6, Krita 6.0.4.1, RawTherapee 5.13, digiKam 9.1.0.
- Install through Bazaar (the Bazzite app store) first. Terminal form: `flatpak install flathub org.darktable.Darktable` (UNVERIFIED syntax, standard Flatpak). Order of preference is in bazzite-kde-linux.
- Run: `flatpak run org.darktable.Darktable` (VERIFIED, darktable docs).
- darktable, GIMP and Krita can read your whole home and external drives (`--filesystem=host`, VERIFIED manifests). RawTherapee only gets `home` (VERIFIED manifest), so a photo on another drive may not show. Fix: UNVERIFIED `flatpak override --user --filesystem=/path com.rawtherapee.RawTherapee`.
- darktable Flatpak settings live in `$HOME/.var/app/org.darktable.Darktable/config/darktable` (VERIFIED). Back this folder up. It also holds your styles.
- darktable talks to the colour manager `org.freedesktop.ColorManager` (VERIFIED manifest), so it can find a monitor profile.
- GIMP Flatpak accepts plug-ins as an extension `org.gimp.GIMP.Plugin` (VERIFIED). A G'MIC extension id is UNVERIFIED. Krita Flatpak builds G'MIC-Qt in (VERIFIED manifest).
- Windows/macOS: darktable, GIMP, Krita, RawTherapee and digiKam have installers on their sites (UNVERIFIED, not fetched).

## 2. RAW vs JPEG
- A RAW file is "data about the light captured", not yet an image. Each pixel holds one colour only and the colours are filled in by demosaic (VERIFIED, darktable colour pages).
- RAW looks flat on purpose. Grading brings back the film look (VERIFIED, darktable colour balance intro).
- RAW stores 12 or 14 bits per channel (4,096 to 16,384 shades). JPEG is 8-bit (256 shades) and already processed in camera, with sharpening and noise reduction baked in. RAW files are about 2 to 6 times bigger (VERIFIED, Wikipedia).
- In RAW the white balance is only a note. You can set any white point later. Edits change only the metadata, so the original stays (VERIFIED, Wikipedia). DNG is Adobe's open RAW format (VERIFIED, Wikipedia).
- JPEG is already processed, 8-bit, and lossy. darktable also reads PNG (8 and 16 bit) and TIFF (8, 16, 32 float) (VERIFIED).
- darktable accepts these RAW extensions among many: ARW, CR2, CR3, DNG, NEF, ORF, RAF, RW2 and more (VERIFIED list).
- Rule: shoot RAW when the camera allows it. RAW lets you fix exposure and white balance without damage (COMMUNITY).
- Phone shots: JPEG or HEIC is the norm. A DNG mode may exist in the camera app (UNVERIFIED). HEIC import in darktable is UNVERIFIED (not in the extension list I read).
- Always keep the original. Edit a copy. Export a master as 16-bit TIFF or PNG, then make small JPEGs from the master (COMMUNITY).
- More bits means less banding (VERIFIED, darktable export "bit depth"). Dark gradients on posters band easily, so keep the master at 16-bit.

## 3. The basic edit, one step at a time
Do the steps in this order. Order matters (COMMUNITY).
1. Crop and straighten first (section 12).
2. Exposure: set mid-tones by eye. In darktable use the exposure module and ignore highlights for now (VERIFIED). The slider can go to plus or minus 18 EV by right click and typing (VERIFIED).
3. Tone mapper: use exactly one of sigmoid, filmic rgb or AgX (VERIFIED). New darktable installs default to sigmoid (VERIFIED, sigmoid page). Set mid-tones with exposure first, because sigmoid pivots on middle grey (VERIFIED).
4. White balance: neutralise the cast first, grade later (VERIFIED, darktable tells you to use color calibration or white balance for primary correction). GIMP: Colors > Color Temperature, in Kelvin (VERIFIED). The doc example moves 5,000 K to 6,500 K.
5. Contrast: use a curve or the contrast slider, not both. darktable contrast has a grey fulcrum at 18.45 percent by default (VERIFIED). For global contrast darktable suggests tone equalizer (VERIFIED).
6. Colour: raise vibrance before saturation. Vibrance lifts low-chroma colours first (VERIFIED, color balance rgb).
7. Local fixes with masks (section 5).
8. Sharpen last, then export (section 11).

### Levels, curves, tone curve
- Levels moves the black point, white point and gamma (mid) of a channel (VERIFIED, GIMP Levels: "Values, Gamma, Black point, White point").
- Curves works on any tonal range. Levels only shadows, mids, highlights (VERIFIED, GIMP Curves).
- GIMP Curves channels: Value, Red, Green, Blue, Alpha. It also has Linear, Non-Linear and Perceptual axis buttons (VERIFIED).
- Curve recipe, S-curve: Colors > Curves. Click once low in the shadows and pull down a little. Click once high in the highlights and push up a little. Contrast rises in the middle (COMMUNITY).
- Curve recipe, faded blacks: drag the bottom-left point up a little. Blacks turn grey, a film look (COMMUNITY).
- Moving a point on the Red curve up adds red and moves down adds cyan (COMMUNITY, standard channel logic).

### HSL and colour mixer
- HSL changes hue, saturation and lightness per colour range. darktable has color zones and color equalizer. The equalizer is the scene-referred version that avoids the noise and harsh edges of color zones (VERIFIED).
- digiKam has HSL Correction, Channel Mixer, Curves Adjust, White Balance (VERIFIED, batch tool list). GIMP has Colors > Hue-Saturation (file exists in manual, UNVERIFIED details).
- Recipe, make magenta pop: pick the magenta range, raise saturation a little, raise lightness a little. Check the skin did not move (COMMUNITY).
- Hue shift in darktable: color balance rgb "hue shift" rotates all colours at constant luminance and chroma. Best used with a mask (VERIFIED).

## 4. Reading the histogram and scopes
- darktable scopes: vectorscope, waveform, split, RGB parade, histogram (VERIFIED). Toggle with Ctrl+Shift+H (VERIFIED).
- The histogram x axis runs from 0 to 100 percent lightness per channel. The y axis is pixel count. A button switches log or linear (VERIFIED).
- Scopes are computed from the small preview, so they are approximate for fine detail (VERIFIED).
- Waveform keeps the picture left to right on the x axis. The dotted top line is 100 percent, and values above it may clip (VERIFIED).
- Reading it (COMMUNITY reading of the edges, Wikipedia calls it an inference):
  - Left is dark, middle is mid-tones, right is light (VERIFIED, Wikipedia). Wikipedia notes a histogram is only an approximation for RAW.
  - Pile touching the left wall: crushed blacks, detail lost.
  - Pile touching the right wall: clipped highlights.
  - One channel hitting the wall alone: that colour clipped. LED stage reds do this often.
  - Dark rave art may sit mostly left on purpose. Keep a few percent of headroom so the blacks are not flat.
- Use the RGB parade to see a colour cast. If red sits higher than blue in the shadows, the shadows are warm.
- darktable has a "raw overexposed" indicator and a "gamut check" tool (names VERIFIED in the module list, details UNVERIFIED).
- Krita ships a Histogram docker (VERIFIED, source folder).

## 5. Non-destructive workflow
- Idea: keep every edit changeable. Never flatten until the last step.
- darktable: edits are a history stack that can be saved as a style and applied to other photos (VERIFIED). The original RAW is never written. Edits sit in the database and in an XMP sidecar file (VERIFIED, LUT page mentions XMP).
- A darktable style saves each module state. You can build your own defaults by setting a module, switching it off, saving the style (VERIFIED).
- GIMP 3 layer effects (NDE): a filter you can tweak later, stored in the XCF file (VERIFIED). A "Merge Filter" tick box makes it permanent. Only GEGL filters can be layer effects. Many live effects slow the app, so merge some (VERIFIED).
- Adjustment layer equivalent in GIMP: add a new layer, set it to a blend mode, use a layer effect and a layer mask (COMMUNITY pattern).
- Smart Object equivalent in GIMP: File > Open as Link Layer. The file stays linked and can be updated separately (VERIFIED, manual page).
- Krita: filters can be used as filter layers or filter masks (VERIFIED, Krita Gradient Map page says filter layer or filter brush).
- Masks: white shows the effect, black hides it (COMMUNITY, universal). darktable offers drawn masks (circle, ellipse, path, brush) and parametric masks (VERIFIED, retouch and vignette pages).
- Blend modes (VERIFIED, GIMP layer modes page):
  - Multiply darkens. White does nothing.
  - Screen inverts both, multiplies, inverts again. It brightens. Black does nothing.
  - Overlay multiplies where the lower layer is under 0.5 and screens above it.
  - Soft light is like overlay but gentler.
- Safe save rule: save the app's own format (XCF, KRA, darktable history) as the master, plus an exported TIFF.

## 6. Colour management
- sRGB: primaries R 0.64/0.33, G 0.30/0.60, B 0.15/0.06, white point D65 at 0.3127/0.3290. Same primaries as Rec. 709 (VERIFIED, Wikipedia fetched).
- sRGB transfer curve: for linear L at or under 0.0031308 use 12.92 x L. Above that use 1.055 x L^(1/2.4) minus 0.055 (VERIFIED, colour-science source). It is close to a plain gamma of 2.2 (VERIFIED, Wikipedia).
- Rec. 709 luma weights: 0.2126 R, 0.7152 G, 0.0722 B (VERIFIED, Wikipedia). This is why pure green looks bright and pure blue looks dark in black and white.
- Adobe RGB (1998): R 0.64/0.33, G 0.21/0.71, B 0.15/0.06, D65 white, gamma about 2.2 with no linear toe. It covers about 52.1 percent of the CIE 1931 space vs about 35 percent for sRGB, mostly in cyan-greens (VERIFIED, Wikipedia).
- Display P3 is Apple's wide gamut: DCI-P3 primaries, D65 white, sRGB curve. About 25 percent more surface area than sRGB (VERIFIED, Wikipedia).
- sRGB is the safe default for web, social, most phones and print shops (COMMUNITY). digiKam says to stay in sRGB if you never use wider gamut (VERIFIED). GIMP says sRGB is the default and recommended working space (VERIFIED).
- darktable output profiles shipped: sRGB, Adobe RGB, XYZ, linear RGB. The profile is embedded in the file. Stick to sRGB unless you have a reason (VERIFIED).
- darktable's working profile is linear Rec. 2020 by default, in 32-bit float (VERIFIED). The pipeline is input profile, then working profile, then output profile (VERIFIED).
- Adobe RGB and DCI-P3 are larger than sRGB (VERIFIED, digiKam gamut figure). A big working space can posterise, a small one can clip (VERIFIED, digiKam).
- Rule: wide gamut only if the whole chain supports it. Then export a copy as sRGB for web (COMMUNITY).
- Opening in GIMP: when a file has an embedded profile, GIMP offers to convert to the working space (VERIFIED). You can assign a profile by hand if it is missing. Menu: Image > Color Management (VERIFIED menu files).
- ICC profile: a file that maps a device or space to a common space (CIELAB or CIEXYZ) and back. The current spec is ICC.1 v4.4, May 2022 (VERIFIED, Wikipedia). GIMP and darktable read them (VERIFIED). Not every app reads them, so sRGB is safest.
- Rendering intents (VERIFIED, darktable and Wikipedia). For photos use relative or perceptual. Absolute can cause casts, saturation looks unnatural (Wikipedia).
  - Perceptual: best for photos. Keeps colour relationships.
  - Relative colorimetric: out-of-gamut colours get same lightness, other saturation. In-gamut colours stay.
  - Saturation: keeps saturation, shifts lightness a bit.
  - Absolute colorimetric: keeps the white point.
- Soft proofing: darktable Ctrl+S, right click the icon to pick the printer profile and intent. You must create the folder `color/out` in the config directory and put the printer .icc there (VERIFIED). GIMP has Soft-proof profile, rendering intent and black point entries under the Image menu (VERIFIED, manual files).
- Get a printer profile from your print shop (COMMUNITY). Neon cyan and magenta often shift or dull in CMYK print. Check a soft proof before ordering (COMMUNITY).
- Monitor: sRGB assumes a calibrated screen (VERIFIED, digiKam). A wrong white point makes you over-correct. LCD native is about 5500 K and sRGB assumes 6500 K (VERIFIED, digiKam).
- darktable: a good factory sRGB screen needs no custom profile. A poor custom profile is worse than the default (VERIFIED). `darktable-cmstest` shows which profile it found (Linux only, VERIFIED).
- To calibrate for real you need a colorimeter. Software on Linux (ArgyllCMS, DisplayCAL) and KDE Plasma's ICC support: UNVERIFIED.
- Practical: turn off night light, set a fixed brightness, edit in a dim room, and check the export on your phone (COMMUNITY).

## 7. Colour grading theory
- Primary grade changes the whole frame through the R, G, B density curves. Secondary grade isolates a range of hue, saturation or brightness and changes only that (VERIFIED, Wikipedia). darktable says the same split: primary fixes casts, secondary makes the look (VERIFIED). Do primary first and the look will transfer between photos.
- ASC CDL: three controls (nominal values: slope 1.0, offset 0, power 1.0, VERIFIED Wikipedia; version 1.2 added saturation). Slope multiplies (acts like gain or highlights). Offset adds (acts like lift or shadows). Power is an exponent (acts like gamma or mid-tones) (VERIFIED, darktable colour balance rgb and old colour balance pages). Krita has a filter named "Slope, Offset, Power" (VERIFIED, source).
- Lift, gamma, gain (COMMUNITY plain words): lift raises or tints the blacks, gamma moves the middle, gain scales the whites.
- darktable colour balance rgb: tabs master, 4 ways, masks. Uses a hue-linear grading space and soft-clips out-of-gamut colours at constant hue (VERIFIED).
- Split toning: one colour for shadows, one for highlights, with a balance point and a compress slider that protects the mid-tones. darktable says it works best on a monochrome input (VERIFIED).
- Teal and orange: darktable ships a "teal/orange" preset on the old colour balance module. It uses two instances with masks. One shifts neutrals to teal and excludes skin, the second restores skin warmth (VERIFIED). Wikipedia dates the look to films from 2010, such as Iron Man 2 (VERIFIED). Why it works: orange skin sits opposite teal on the hue wheel (COMMUNITY).
- Film emulation (VERIFIED, darktable): grain module simulates silver grain on the L channel with coarseness (scaled like ISO), strength and mid-tone bias. A newer spektrafilm module simulates film and paper physically, including grain and halation. A LUT is a colour recipe measured from film (spektrafilm page).
- Grade in this order (COMMUNITY): exposure, white balance, contrast, global colour, shadows tint, highlights tint, local masks, grain, vignette.
- Keep it believable: lower the effect to 60 percent, look away, look back (COMMUNITY).

## 8. LUTs and how to apply a .cube
- A 3D LUT turns each input RGB value into an output RGB value through a table. It is used for film looks and grading (VERIFIED, darktable). Hardware and software interpolate between table nodes (VERIFIED, Wikipedia). darktable offers tetrahedral (default), trilinear and pyramid. You only see a difference with small LUTs (VERIFIED).
- .cube files are text with LUT_3D_SIZE or LUT_1D_SIZE and optional DOMAIN_MIN lines (VERIFIED, colour-science reader source). Do not edit by hand.
- A LUT expects a certain input. Cube files are usually Rec. 709, others sRGB (VERIFIED, darktable). A LUT built for camera log will look wrong on a normal photo (VERIFIED).
- Always grade on a neutral, well exposed image first. darktable's module clips values outside 0 to 1 (VERIFIED).
- darktable (VERIFIED): accepts .cube, .3dl, haldclut .png and .gmz.
  1. Preferences > processing > set "LUT 3D root folder". Put your LUT files inside.
  2. Darkroom, module "lut 3D". Pick the file.
  3. Set "application color space" to match the LUT. Cube usually Rec. 709.
  4. Keep it after filmic or sigmoid, where it sits by default.
  5. Back up the LUT folder. The XMP stores only the path, not the LUT (VERIFIED).
- GIMP 3.2: I found no native .cube support in the manual or the GEGL source I read (VERIFIED absence, not proof). Use G'MIC "Apply External CLUT" with a Filename. Its code treats a .cube name with `input_cube` and otherwise reads a Hald CLUT image (VERIFIED, G'MIC source). Menu location UNVERIFIED, search the filter name.
- Krita: its LUT docker is an OpenColorIO display transform, not a bake into pixels (VERIFIED, source). For a baked look use the Slope, Offset, Power filter, Gradient Map, or G'MIC (built into the Flatpak, VERIFIED). .cube through G'MIC in Krita is UNVERIFIED.
- RawTherapee: Film Simulation reads Hald CLUT images from a folder you set in Preferences. I found no .cube code in its source (VERIFIED).
- ImageMagick: Hald CLUT only, `magick image.png hald.png -hald-clut out.png`. Make a neutral Hald with `HALD:8` (VERIFIED, docs and tested). Use the Hald trick to bake any look: grade the Hald image in GIMP, then apply it to a whole folder (VERIFIED, ImageMagick docs say exactly this).
- Photoshop: Color Lookup adjustment layer, "Load 3D LUT" (UNVERIFIED). Lightroom Classic and Affinity: UNVERIFIED.
- Free LUTs vary a lot. Treat each as a starting point and lower its strength (COMMUNITY).

## 9. Filters: what they really do
All maths below is VERIFIED from the cited doc unless marked. Local tests used ImageMagick 6.9.12.
- Curves: a mapping from input level to output level. S-curve raises contrast. Applied per channel it also shifts colour.
- Contrast with a pivot: out = pivot + k x (in minus pivot) in linear light (COMMUNITY maths). Sigmoid instead uses a modified log-logistic curve with contrast and skew sliders (VERIFIED, darktable). ImageMagick `-sigmoidal-contrast 5x50%` means contrast 5, mid-point 50 percent (VERIFIED).
- Grain: random texture. Film grain gets bigger as ISO rises. Digital noise is different (VERIFIED, Wikipedia). darktable adds noise to lightness, strongest in the mid-tones (VERIFIED). Recipe tested: grey 50 percent layer plus Gaussian noise, blended with Overlay.
  - `convert in.png \( +clone -fill gray50 -colorize 100 -attenuate 0.4 +noise Gaussian -colorspace Gray \) -compose overlay -composite grain.jpg`
- Vignette: darkens (and desaturates) edges in an ellipse with a soft falloff. darktable warns of banding and unnatural results. Use dither or posterize, or an exposure module with a big ellipse mask (VERIFIED). GIMP: Filters > Light and Shadow > Vignette (VERIFIED). ImageMagick: `-vignette 0x40+10%+10%` (VERIFIED, tested).
- Bloom: blur only the bright parts, then add them back (VERIFIED, darktable). GIMP Bloom has Threshold, Softness, Radius, Strength, Limit exposure (VERIFIED). Recipe tested: threshold at 75 percent, blur, screen onto the original.
  - `convert in.png \( +clone -threshold 75% -blur 0x20 \) -compose screen -composite bloom.jpg`
- Orton glow: blend a sharp image with a blurred, overexposed copy (VERIFIED, darktable soften). GIMP has Softglow in Artistic (file exists).
- Halation: a glow around bright points, from light reflecting off the film base back into the emulsion. Most film shows a slight red halo on the brightest highlights (VERIFIED, Wikipedia). Spektrafilm simulates it (VERIFIED). A DIY version: take highlights, blur, tint red, screen at low opacity (COMMUNITY recipe, UNVERIFIED as tested).
- Glitch / RGB split: shift one channel sideways (tested):
  - `convert in.png -channel R -separate r.png` and the same for G and B, then `convert r.png g.png \( b.png -roll +12+0 \) -combine -colorspace sRGB glitch.jpg`
  - GIMP: Filters > Distorts > Shift and Video Degradation exist (VERIFIED files). Scan-line glitch effects there: UNVERIFIED.
- Duotone: map black to colour A and white to colour B. ImageMagick `+level-colors` does it (VERIFIED, tested): `convert in.png -colorspace Gray -sigmoidal-contrast 5x50% +level-colors '#10002a','#00f0ff' duo.jpg`
- Gradient map: the lightness of each pixel picks a colour from a gradient (VERIFIED, GIMP and Krita). GIMP: Colors > Map > Gradient Map, uses the current gradient. Krita Filters > Map > Gradient Map has Blend, Nearest, Dither modes. ImageMagick: `convert gm.png grad.png -clut out.jpg` (tested).
- Halftone: dots of varying size or spacing that the eye blends into smooth tone (VERIFIED, Wikipedia). Print screens are measured in lines per inch (150 lpi is a Wikipedia example). CMYK uses set screen angles to avoid moire (angles UNVERIFIED). GIMP: Filters > Distorts > Newsprint. Krita: Filters > Artistic > Halftone (VERIFIED). ImageMagick: `-ordered-dither h8x8a` (VERIFIED docs name, tested).
- Posterize and dither: cut the number of levels, or spread the error (VERIFIED, darktable dither or posterize).
- Blur types and glows use Gaussian kernels. Wider blur radius means softer glow (COMMUNITY).

## 10. Retouching
- Frequency separation: split detail (pores, scratches) from colour and tone, edit each alone.
  - GIMP: Filters > Enhance > Wavelet decompose. It builds layers called scales, 5 by default, finest detail on top, plus a residual layer (VERIFIED). Each scale is in Grain Merge mode, so 50 percent grey does nothing and painting grey erases detail at that scale (VERIFIED).
  - darktable: retouch module with wavelet decompose layers (VERIFIED).
  - Classic two-layer way (blur layer plus a high-frequency layer in linear light): COMMUNITY, not read.
- Dodge and burn: darkroom terms. Dodging holds back light to keep an area lighter, burning adds light to make it darker (VERIFIED, Wikipedia). Digital tools copy this.
  - darktable tone equalizer does "dodge and burn while preserving local contrast" using a guided mask (VERIFIED).
  - GIMP has a Dodge/Burn tool (VERIFIED, manual file). Safer: a 50 percent grey layer in Overlay or Soft light, painted white or black at low opacity (COMMUNITY).
- Clone and heal: clone copies pixels. Heal copies and then matches colour and brightness to the surround (VERIFIED, darktable retouch, heal is based on GIMP's heal). Use heal for blemishes, clone for hard edges.
- darktable retouch modes: clone, heal, fill, blur, all with drawn shapes (VERIFIED). GIMP: Clone, Heal and Perspective Clone tools (VERIFIED files).
- Remove a cable or a mic stand: heal tool, small strokes, change the source often. Avoid repeating patterns (COMMUNITY).
- AI help: darktable has a "neural restore" module and an AI features page (VERIFIED existence). Treat AI fill and upscale as UNVERIFIED for quality on your files. Always check faces and text.

## 11. Sharpening and noise reduction
- Unsharp mask: sharpened = original + (original minus blurred) x amount (VERIFIED, Wikipedia). Big radius can give light halos. It raises contrast around edges. Parameters: radius (blur size), amount, threshold (skip small differences so noise is not boosted) (VERIFIED, darktable). ImageMagick `-unsharp radiusxsigma+gain+threshold`, radius 0 lets it pick (VERIFIED). Tested: `-unsharp 0x1+0.8+0.02`.
- darktable calls its own USM module "no longer recommended". Use contrast equalizer presets for deblur or local contrast for general crispness (VERIFIED). High pass with Soft light blend also sharpens (VERIFIED).
- GIMP: Filters > Enhance > Unsharp Mask, Noise Reduction, Despeckle, High Pass, Wavelet decompose (VERIFIED files).
- Noise reduction in darktable: denoise (profiled) has sensor profiles for over 300 cameras. Wavelets is the default. One instance handles luma and chroma (VERIFIED). It runs early in the pipe, before the colour profile (VERIFIED).
- Order (COMMUNITY): denoise first, grade, sharpen last, and sharpen after the final resize. RawTherapee has a Post-Resize Sharpening tool (VERIFIED label). darktable resizes at export; high quality resampling downsizes at the very end (VERIFIED).
- Gig photos at high ISO: accept some grain. Add your own fine grain after denoising so it looks even (COMMUNITY).
- Never sharpen a photo twice for two sizes. Export a separate sharpened file per size (COMMUNITY).

## 12. Cropping and aspect ratios
- darktable crop: shows the full image while you work, aspect list is predefined, one button swaps portrait and landscape, "square" is 1:1, "original image" keeps the ratio (VERIFIED). Do rotate and perspective first, then crop last (VERIFIED).
- Ratio maths: width / height. Album art is square, 1:1 (COMMUNITY). A-series paper is 1 : 1.414 (square root of 2, VERIFIED, Wikipedia ISO 216). A4 is 210 x 297 mm, A3 297 x 420, A2 420 x 594, A1 594 x 841. Check poster size with the printer.
- Cropping for several formats: keep the subject in the centre 60 percent of a wide master so a square and a tall crop both work (COMMUNITY).
- GIMP: Tool options of the Crop tool offer fixed aspect and size (UNVERIFIED details). Image > Canvas Size adds room (VERIFIED file). Zealous Crop trims same-colour borders (VERIFIED file name).
- Leave bleed for print. Ask the printer for the bleed size (UNVERIFIED number).

## 13. Resize and export (only numbers I can source)
- Pixels for print = inches x dpi. Example: 12 in x 300 dpi = 3600 px (maths).
- darktable export defaults: JPEG quality 95 "for archiving or printing". Use 90 for web (VERIFIED). dpi is stored in Exif and set to 300 when you size in pixels or by scale (VERIFIED).
- darktable export options: size in pixels, cm, inch or scale. Max size 0 means no limit. Allow upscaling is off by default. High quality resampling can be set yes (VERIFIED).
- GIMP web guide: JPEG for photos, PNG for few colours, icons and screenshots. Flatten if you do not need alpha. PNG default settings are fine. JPEG loses quality as compression rises (VERIFIED).
- JPEG normally uses 4:2:0 chroma subsampling, where each 2 x 2 block shares colour (VERIFIED, Wikipedia). It can smear thin red or magenta lines on dark art, so use 4:4:4 for small text and neon edges (COMMUNITY). `-strip` removes metadata. Tested with ImageMagick: `convert in.png -resize 400x -unsharp 0x1+0.8+0.02 -strip -quality 90 -sampling-factor 4:2:0 small.jpg`.
- Merch printers: ask for dpi, size, colour mode, file type, bleed and whether transparency is needed (COMMUNITY). Do not guess. Print-on-demand sizes are UNVERIFIED.
- Social and streaming sizes (Instagram, Spotify, Bandcamp, DistroKid, YouTube): UNVERIFIED. I could not fetch their help pages. Look each up before you export, and state the page you used.
- Website: export the right pixel size, not a giant file scaled in CSS. Use JPEG for photos. WebP and AVIF are in GIMP's file-format docs list (UNVERIFIED which versions). See squarespace-expert for the Squarespace upload rules.
- Name files clearly: `release-cover-3000-master.tif`, `release-cover-1400-web.jpg` (COMMUNITY).
- Always check the export at 100 percent and on a phone.

## 14. Batch processing
- darktable-cli (VERIFIED): `darktable-cli input_folder output_folder --width 2000 --height 2000 --style "my style" --hq true --out-ext jpg`. It also takes `--icc-type`, `--icc-file`, `--icc-intent`, `--upscale`. The output folder must already exist, or it is read as a filename.
- Flatpak form: `flatpak run --command=darktable-cli org.darktable.Darktable ...` (the `--command` pattern is VERIFIED for darktable-cltest, so it should hold for the cli, UNVERIFIED).
- darktable styles: apply the same history to many photos (VERIFIED). Good for a consistent gig set.
- digiKam Batch Queue Manager: Ctrl+B adds items. Tools run top to bottom and you can drag to reorder. Export to a new format at the end for best quality. Tools include curves, HSL, white balance, sharpen, noise reduction, local contrast and Convert (VERIFIED). No preview per image and no Adjust Levels there (VERIFIED).
- ImageMagick `mogrify` resizes a whole folder (tested): `mkdir out && mogrify -path out -resize 1600x -format jpg -quality 85 *.png`. In ImageMagick 7 the command is `magick` (VERIFIED, docs). Bazzite install by Homebrew: UNVERIFIED. Test on 3 copies first.
- GIMP and Photoshop batch scripting: UNVERIFIED.

## 15. Other apps (all UNVERIFIED unless stated)
- Lightroom and Photoshop: Adobe help was blocked. Basics are Lightroom for RAW and sync, Photoshop for layers, smart objects and actions.
- Affinity Photo: layers, adjustment layers, LUT adjustment. Pricing changed recently: check design-software-guide.
- Capture One: RAW, strong colour editor, tethering. Not read.
- Photopea: free in-browser editor that opens PSD. Not read.
- RawTherapee (VERIFIED labels in source): tools named Exposure, Color Toning (methods include L*a*b* blending and Color Balance Shadows/Midtones/Highlights), Film Simulation, Haze Removal, Graduated Filter, Selective Editing (Locallab, includes Film Grain), Resize and Framing, Post-Resize Sharpening.
- digiKam editor: Color, Enhance, Decorate, Effects, Transform tools (VERIFIED folder names).
- Krita filters of use (VERIFIED, source): Gradient Map, Halftone, Slope Offset Power, Color Transfer, Dodge/Burn, Unsharp, Levels, Posterize, Palettize.

## 16. Look-book: dark rave, hardstyle, trance (COMMUNITY opinion)
Palettes themselves: use color-palette-expert. This is the photo treatment.
- Rules for all looks: deep but not clipped blacks, one hero colour, one accent, grain over gradients, keep faces readable, check on a phone at night brightness.
- Look A, neon night club: near-black base, magenta and cyan light.
  1. Exposure so the crowd mid-tone is not black.
  2. Tone curve S, faded blacks slightly.
  3. Split toning: shadows blue-violet, highlights magenta.
  4. Bloom on lights at low strength. Fine grain.
- Look B, hardstyle red and black: industrial, high contrast.
  1. Convert to black and white with red channel weighted up, or a duotone from black to red.
  2. Hard S curve, crush blacks a little.
  3. Strong vignette. Add halftone or scratch texture.
- Look C, trance beam and haze: blue, violet, white light beams, soft glow.
  1. Lift the shadows toward navy.
  2. Orton or Softglow at 30 percent.
  3. Haze removal reversed or a gradient map from navy to cyan to white.
- Look D, UK hardcore / happy hardcore: loud, saturated, candy colours.
  1. Raise vibrance, not saturation.
  2. Gradient map from purple to hot pink to yellow.
  3. Halftone or comic overlay at low opacity.
- Look E, glitch: RGB channel split, scan lines, banding on purpose. Keep the face of the artist clean and the glitch on the edges.
- Pet or animal subjects: keep fur highlights and eyes bright, grade the background down (COMMUNITY).
- For posters, test a small crop printed at real size on any home printer before ordering (COMMUNITY).
- Dark gradients on merch can band or turn muddy. Add 1 to 2 percent grain and ask the printer for a test (COMMUNITY).
- Copyright: use only photos you took or have a licence for. Remove location Exif before posting (COMMUNITY).

## 17. Common mistakes to catch
- Editing on a bright screen with night mode on.
- Two tone mappers on at once in darktable (VERIFIED warning).
- Stacking sharpen on a downsized, already sharpened file.
- Saving a 16-bit master only as JPEG.
- Exporting in Adobe RGB for the web. Colours look dull in apps that ignore profiles (VERIFIED advice to stick to sRGB).
- Using a LUT made for log footage on a normal photo (VERIFIED warning).

## Not verified (say so, never guess)
- Adobe, Affinity, Capture One, Photopea features and menu paths.
- Social, streaming and print-on-demand pixel sizes and bleed values.
- KDE Plasma colour management, ArgyllCMS/DisplayCAL on Bazzite.
- G'MIC menu location in GIMP and Krita, and .cube through G'MIC in Krita.
- Flatpak override for RawTherapee drives, the G'MIC Flatpak extension id, Homebrew ImageMagick on Bazzite.
- HEIC and WebP/AVIF export support per app.
- Classic two-layer frequency separation recipe, DIY halation recipe, CMYK screen angles.
- Reddit r/photoediting and r/colorists: blocked.

## Sources (fetched)
- darktable user manual source (github.com/darktable-org/dtdocs): modules exposure, filmic rgb, sigmoid, color balance rgb, color balance, split-toning, lut 3D, color look up table, grain, vignetting, bloom, soften, sharpen, highpass, retouch, denoise (profiled), crop, dither or posterize, haze removal, spektrafilm, tone equalizer, color equalizer, output color profile, input color profile; scopes, export, styles, soft proof; colour-management pages (color spaces, rendering intent, display profile); darktable-cli, supported file formats, wavelets, preferences (processing, config directory), invocation per OS.
- GIMP manual source (github.com/GNOME/gimp-help): colour management, Levels, Curves, Color Temperature, Gradient Map, layer modes, layer effects (NDE), Wavelet decompose, Bloom, Vignette, Scale Image, Web guide, Open as Link Layer, file menu and Image menu file lists.
- GEGL source (github.com/GNOME/gegl) and Krita source (github.com/KDE/krita): filter lists, LUT docker, ASC CDL filter.
- digiKam manual source (github.com/KDE/digikam-doc): Batch Queue Manager, monitor profiles, working space.
- RawTherapee source (github.com/Beep6581/RawTherapee): language file tool names, Hald CLUT.
- G'MIC source (github.com/GreycLab/gmic): input_cube, fx_apply_haldclut.
- Flathub manifests (github.com/flathub/org.darktable.Darktable, org.gimp.GIMP, org.kde.krita, com.rawtherapee.RawTherapee, org.kde.digikam).
- colour-science (github.com/colour-science/colour): sRGB constants, .cube reader.
- ImageMagick docs source (github.com/ImageMagick/Website): -hald-clut, -level-colors, -sigmoidal-contrast, -vignette, -unsharp, -modulate. Recipes run locally on ImageMagick 6.9.12.
- Wikipedia: SRGB, 3D_lookup_table, ASC_CDL, Display_P3, Adobe_RGB_color_space, Unsharp_masking, Halftone, Halation, Color_grading, ISO_216, ICC_profile, Rendering_intent, Chroma_subsampling, Raw_image_format, Image_histogram, Dodging_and_burning, Film_grain (all https://en.wikipedia.org/wiki/<name>)
- https://docs.krita.org/en/reference_manual/filters/map.html
