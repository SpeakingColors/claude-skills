---
name: dsp-references-and-licences
description: Use when designing audio DSP and choosing papers, code to study and licences: oscillators, supersaw, filters, ADAA, true-peak, reverb, pitch shifting, stereo widening, and what you may copy.
---

# DSP references and licences

Companion to `plugin-dsp-quality`, `synth-engine-design`, `fx-plugin-design`. Labels: VERIFIED (read on the page), COMMUNITY (single source or forum), UNVERIFIED. Research date: November 2026. Read the paper, do not rely on this summary for coefficients.

## Oscillators and supersaw
- PolyBLEP (Valimaki and Huovilainen 2007) is closed form, cheap, fine for saw and square. PolyBLAMP fixes slope corners such as triangle, hard clip and rectifier (Esqueda, Bilbao, Valimaki, DAFx 2016). VERIFIED. minBLEP (Brandt 2001) suits hard sync but is table based and overshoots. COMMUNITY.
- Supersaw: Szabo 2010 (KTH thesis) reverse engineers the JP-8000: a non linear, asymmetric detune curve and a separate mix law for the six side saws against the centre saw. Exact coefficients were not retrieved; read the PDF. COMMUNITY. Keep the centre saw in tune, use a curve not a linear detune, free running random phases. COMMUNITY. Level compensation (about 1/sqrt(N) or a measured RMS) and a high pass on the side saws for hardstyle are practice, UNVERIFIED.
- Wavetable mip mapping (one band limited table per octave) is common practice, UNVERIFIED.

## Filters
- Zavalishin, The Art of VA Filter Design (free PDF): TPT and zero delay feedback, ladder, diode ladder, nonlinear ZDF. VERIFIED. Cheap "lagged nonlinearity" is not truly zero delay; fine at 2x oversampling, check stability at high resonance. COMMUNITY (forum). Modulate `g` and clamp it below Nyquist. UNVERIFIED.

## Saturation, ADAA, clipping, limiting
- ADAA first order: Parker, Zavalishin, Le Bivic, DAFx 2016. Second and third order: Bilbao, Esqueda, Parker, Valimaki 2017. Second order adds a sample of latency and some high frequency roll off, and needs a fallback near equal samples. VERIFIED (CCRMA notebook). Code: audiovention/ADAA (BSD 3). COMMUNITY.
- ADAA plus 2x to 4x oversampling is the usual combination for heavy distortion (practice, UNVERIFIED). DC blocker (5 to 20 Hz one pole) after asymmetric shapers. UNVERIFIED.
- True peak (BS.1770): 4x oversample, low pass, absolute value. VERIFIED (Essentia tutorial). FabFilter states 4x with at least 0.1 ms lookahead keeps inter sample peaks within about 0.1 dB. COMMUNITY (vendor). A clipper (up to 16x oversampled) followed by a true peak limiter is a published design (Slate Bus Clipper). COMMUNITY (vendor).
- Compressors, Linkwitz Riley crossovers (4th order, allpass compensation for non adjacent bands), linear phase EQ latency and pre ringing: general knowledge, UNVERIFIED here.

## Reverb, pitch, stretch
- Dattorro 1997 (JAES 45 no 9) plate topology. VERIFIED (Valhalla DSP write up). Signalsmith "Let's Write a Reverb": FDN with Householder or Hadamard mixing and per line decay filters; an FDN is not automatically colourless. VERIFIED. Modulate delay lines slightly to avoid metallic ringing. COMMUNITY. Low cut in the feedback path for bass heavy music. UNVERIFIED.
- Phase vocoder: Laroche and Dolson 1999 phase locking; transients need a phase reset (Roebel). VERIFIED (paper). Formant preservation and WSOLA were not covered by research. Granular two head pitch shift is the cheap shimmer option. UNVERIFIED.

## Stereo widening
- Mid/side side gain is inherently mono compatible. A Haas delay comb filters on a mono sum. Allpass decorrelation is not fully mono safe. A delayed mono signal fed only into the side channel is mono safe but colours left and right. COMMUNITY (Sound On Sound, Csound journal, Softube manual). Always check the mono sum and keep bass out of the widener.

## Licences, what you may copy
- Signalsmith Stretch: MIT, header only C++. VERIFIED (check the current LICENSE). Rubber Band and FFTW: GPL, or a paid commercial licence for proprietary use (Rubber Band). VERIFIED. Surge XT: GPL 3. COMMUNITY. Vital and Dexed licences were not checked.
- Rule: study GPL code, reimplement from the papers, never paste GPL code into a closed plugin. For your own free AGPL plugins GPL code is compatible but keep notices.

## Typical quality mistakes to audit for
Aliasing from naive saw or sync or FM; distortion without oversampling or ADAA; block rate cutoff modulation (zipper); no DC blocker after asymmetric saturation; supersaw level jumps and wide sub; limiter that only checks sample peaks or distortion after the limiter; clicks on parameter or oversampling switches; metallic reverb tails and low end build up; denormals in feedback; widener that collapses in mono; pitch shift that smears transients; wet and dry level or latency mismatch.
