---
name: hyperframes-data-video
description: Create verified HyperFrames business videos from structured data, including financial reports, quarterly/annual scorecards, user growth reports, ROI proof, leaderboards, milestone videos, and data-in-motion explainers. Use when Codex needs to turn numeric data into a horizontal or vertical animated video with charts, counters, brand-aware visual identity, BGM/tick audio, source verification, rendered MP4 output, and optional storyboard long images.
---

# HyperFrames Data Video

## Workflow

Use the HyperFrames, HyperFrames CLI, and GSAP skills before authoring or rendering compositions.

1. Clarify the story: classify the request as growth, comparison, long-term trend, structure shift, leaderboard, milestone, or pressure/downturn. Do not default to a celebratory growth video when the data is mixed.
2. Verify data: for financial, market, regulatory, or current figures, confirm sources before building. Normalize units and keep values in a data/config file rather than scattering hard-coded numbers.
3. Define visual identity: create or update `DESIGN.md` before writing composition HTML. Base the palette on the brand, industry, official reports, or user references, not on generic finance tropes.
4. Pick data forms: vary visual mechanisms across scenes. Avoid repeating "large number + upward arrow" for every page.
5. Build in HyperFrames: design final layouts first, animate entrances second, add transitions, then render and inspect.
6. Add audio: default to no narration unless requested. Use restrained business BGM and soft data cues.
7. Verify deliverables: run lint/validate/inspect, render preview, extract representative frames, check numeric finals, then render final MP4. Offer or create a storyboard long image when useful.

## Reference Routing

- Read `references/data-patterns.md` when choosing scene types, charts, and motion for a dataset.
- Read `references/visual-identity.md` when creating or adapting brand style, colors, typography, and "what not to do".
- Read `references/financial-verification.md` for financial reports, listed companies, public-company announcements, investor videos, or investment disclaimers.
- Read `references/audio-guidelines.md` when generating or revising BGM, tick sounds, lock sounds, or audio-reactive cues.

## Non-Negotiables

- Treat numbers as evidence, not decoration. Every key number needs a visual body: bar, band, route, trajectory, scale, ring, ranking strip, or structural panel.
- Do not use red/green market-terminal language unless the user explicitly wants that convention. Show declines through negative signs, contraction, line direction, desaturation, pressure labels, and shrinking geometry.
- Preserve brand assets faithfully. Do not turn logos into decorative textures or distort official proportions.
- Use balanced analysis for financial videos unless the user explicitly requests a promotional one.
- Include data source notes when the video uses externally sourced data. For investment-related content, include "not investment advice" or the user's preferred equivalent.
- Prefer 1920x1080 horizontal business presentation format unless the user asks for portrait or square.

## Useful Script

Use `scripts/storyboard_from_video.py` to extract stable frames from a rendered MP4 and stack them top-to-bottom:

```bash
python scripts/storyboard_from_video.py final.mp4 storyboard.png --times 2.1,7.6,14.7,20.7,27.2,33.5
```

Choose timestamps where each scene has finished entering and before the outgoing transition starts.
