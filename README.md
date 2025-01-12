# # QR Synth Plus

A browser-based synthesizer that fits in a QR code. Features keyboard interface, effects, and arpeggiator.

## Files

- `qrMusic.html` - Full source code
- `qrMusicMin.html` - Minimized version
- `qrMusicCreate.py` - QR code generator
- `qrMusic.png` - Generated QR code

## Features

- 🎹 Virtual keyboard (Z through /)
- 🌊 4 waveforms: sine, triangle, saw, square
- 📊 Volume control
- 🎼 8 octave range (0-8)
- 🔄 Delay with feedback
- 🎸 Distortion effect
- 🎵 Arpeggiator

## Quick Start

```bash
python qrMusicCreate.py
```

## Controls

- Keyboard: Z through / keys
- Wave: Select waveform type
- Vol: Adjust volume
- Oct: Change octave (+/-)
- Delay/Feedback: Echo effect
- Dist: Distortion amount
- Arp: Toggle arpeggiator

## Technical Details

- Uses Web Audio API
- QR Version: 40
- Error Correction: L
- Custom minimization

## Features:

- Oscillators
- Gain nodes
- Delay nodes
- WaveShaper
- Arpeggiator

## Requirements

- Python 3.x
- qrcode library
- PIL/Pillow

## Installation

```bash
pip install qrcode pillow
```

## Note

Always use qrMusicCreate.py to generate QR code. This is due to specific settings required for the QR code to compress and generate properly.
