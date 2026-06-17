# Data Patterns

Use this file to map data relationships to visual forms. Vary mechanisms across pages so a data video feels authored, not templated.

## Pattern Selection

| Data relationship | Use | Avoid |
| --- | --- | --- |
| One hero metric | Counter, large number lock, radial glow, single proportional bar | Unanchored floating number |
| Long-term trend | Stair-step bars, timeline, cumulative curve, year-by-year build | Tiny gridline charts |
| Two-period comparison | Dual columns, bridge line, before/after band, mirror bars | Three unrelated stat cards |
| Mixed growth and pressure | Split frame, conversion bridge, contraction band, balanced conclusion | Pure "good news" framing |
| Share or structure shift | Proportion migration, stacked band, twin progress tracks, route expansion | Pie charts unless explicitly requested |
| Regional/global expansion | Horizon, route arcs, diffusion nodes, map-like stage | Stock map clutter |
| Quarter pressure | Horizontal contraction flow, shrinking mirror bar, pulse path | Identical upward arrows |
| Ranking/list | Animated ranking bars, score strips, podium only for top-3 | Static table screenshot |
| Milestone/ROI proof | Timeline nodes, cumulative lock, before/after result panel | Confetti by default |

## Scene Mix

For a 30-45 second business video, prefer 5-6 pages:

1. Title and framing.
2. Long-term scale or context.
3. Current-period scorecard or comparison.
4. Structural driver or segment story.
5. Recent quarter or risk pressure.
6. Balanced conclusion with source note.

For shorter 8-15 second videos, use 3 pages:

1. Hook title.
2. Two or three kinetic metrics.
3. Summary lock and source.

## Motion Rules

- Build, breathe, resolve. Let each scene have at least one visible change after the first second.
- Animate chart geometry through `scaleX`, `scaleY`, SVG stroke draw, transforms, opacity, and controlled glow.
- Use counters only for final values that matter. Too many simultaneous counters becomes unreadable.
- Keep charts visually proportional, but optimize for video comprehension over analytical precision.
- Put units close to numbers. Standardize units across the whole video.
