# Audio Guidelines

Default to music and subtle sound design, not narration.

## BGM

- Use restrained business electronic music, approximately 88-112 BPM.
- Prefer warm pads, soft bass pulses, and slow attack envelopes.
- Avoid piercing leads, bright chimes, aggressive drums, and high-frequency tick stacks.
- Use a smooth fade-in and fade-out.
- If generating procedural audio, avoid abrupt chord switches; crossfade chord changes.

## Data Cues

- Use light tick sounds only when numbers change. Keep ticks low, soft, and sparse.
- Prefer lower-frequency wooden or muted digital cues around 160-400 Hz.
- Avoid repeated 800 Hz+ tick peaks, especially 1-4 kHz, which read as harsh on phone speakers.
- Use short lock sounds for final values, but keep them softer than the BGM peak.
- Do not sync every visual change to a sound. Select important data arrivals.

## Audio QA

Run a volume check after generating or replacing audio:

```bash
ffmpeg -i soundtrack.wav -af volumedetect -f null -
ffmpeg -i soundtrack.wav -af highpass=f=800,volumedetect -f null -
ffmpeg -i soundtrack.wav -af highpass=f=2000,volumedetect -f null -
```

Targets for a calm business video:

- Overall max below about -12 dB, preferably -14 dB or softer if the user reports harshness.
- 800 Hz+ peak much lower than the full mix.
- 2 kHz+ content close to floor unless intentionally using bright percussion.
