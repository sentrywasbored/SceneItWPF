# Scene It? DVD Structure

[![Game Type](https://img.shields.io/badge/Type-DVD%20Game-blue)](https://github.com)
[![Format](https://img.shields.io/badge/Format-DVD--VIDEO-orange)](https://github.com)

## Overview

This document outlines the standard structure of Scene It? DVD games. While there may be minor variations between different editions and versions, the content generally adheres to the following organizational pattern.

## DVD Structure

| Directory | Content | Description |
|-----------|---------|-------------|
| `VIDEO_TS` | In-Game Menu | Core DVD system files and game menu functionality |
| `VTS_01` | Splash & Main Menu | Opening logos, title screens, and main navigation |
| `VTS_02` | Support Content | Tiebreakers, timers, and miscellaneous menu screens |
| `VTS_03-04` | AllPlay Content | Content accessible to all players during standard gameplay |
| `VTS_05` | Final Cut Content | Special content reserved for final rounds |
| `VTS_06-07` | My Play Content | Mixed content including movie clips and special challenges<br>(e.g., Finish the Line, Marauder's Map, etc.) |

## Special Notes

- Specialty additions and expansion content are typically appended as additional VTS directories at the end of the standard structure
- Different editions of the game may have slight variations in this structure
- These DVD volumes are designed for interaction with the Scene It? board game components

## Technical Information

DVD navigation and content access is managed through the game's menu system. The structure allows for random content selection while maintaining organized categories for different gameplay modes.

```
Scene It? DVD
├── VIDEO_TS/
├── VTS_01_*.VOB    # Splash & Main Menu
├── VTS_02_*.VOB    # Tiebreaks & Timers
├── VTS_03_*.VOB    # AllPlay Content (Part 1)
├── VTS_04_*.VOB    # AllPlay Content (Part 2)
├── VTS_05_*.VOB    # Final Cut Content
├── VTS_06_*.VOB    # My Play Content (Part 1)
├── VTS_07_*.VOB    # My Play Content (Part 2)
└── VTS_08+_*.VOB   # Specialty/Expansion Content (when present)
```

## References

- Scene It? is a registered trademark
- DVD structure analysis based on standard Scene It? game editions
- Content organization may differ in specialty editions
