# Character Schedule

Where each resident can be found during the evening/night, and the one-line observation the detective gets when first meeting them there each loop.

## Time windows

The clock runs from **6 p.m. to midnight** and only advances forward. Placement is by explicit window rather than by band, because a character's whereabouts have to line up with a death hour, and a two-hour band cannot express "gone from the hall at half past seven."

Windows are written as 24-hour strings (`"20:30"`) and converted at load by `clock_time()` in `scripts/utils/clock.rpy`. Midnight is `"24:00"`, not `"0:00"`, so the values sort and compare the same way `clock.minutes` does.

<!-- prettier-ignore-start -->

| Band | Clock range | Flavor |
| --- | --- | --- |
| Evening | 18:00 - 20:00 | House with sun setting down |
| Night-light | 20:00 - 22:00 | House with lights on |
| Night-dark | 22:00 - 24:00 | House with lights off |

<!-- prettier-ignore-end -->

The bands still drive backgrounds and item tinting, but placement is per-window.

## The schedule

A character is **present** in a room when that room is entered during one of their windows. Presence is what makes them findable for Talk/Give. Movements between rooms are unobserved (room-based navigation), so a window records only where someone is, not how they got there.

<!-- prettier-ignore-start -->

| Character | 18:00-19:00 | 19:00-19:30 | 19:30-20:30 | 20:30-21:30 | 21:30-22:30 | 22:30-24:00 |
| --- | --- | --- | --- | --- | --- | --- |
| **Butler Ben** | interior entrance | — | manor door | manor door | living room | living room |
| **Nurse Nora** | kitchen | kitchen | kitchen | kitchen | kitchen | bedroom |
| **Miss Mia** | living room | kitchen | kitchen | kitchen | pond | pond |
| **Maid Madelyn** | living room | living room | hallway right | kitchen | kitchen | bedroom |

<!-- prettier-ignore-end -->

## Why the windows sit where they do

Each window is pinned to a death hour, because the hour has to be survivable and the aftermath has to be readable.

- **Madelyn is in the living room until 7:30.** Handing her the knife is one of two ways to close the 7:30 hour, and the living room is the only place she can be handed it. She is in the kitchen from 8:30, which is where she kills Nora, so the 8:30 night has all three women in one room.
- **Ben is at the manor door from 7:30, and you never see him there.** The hall is his post until 7:00 and he is unplaceable for the half hour after. A player who sees him at 7:25 and finds the hall empty at 7:35 has bracketed the murder, and one who hears the 7:30 hint beside him has been handed an alibi.
- **Mia is in the kitchen until 9:30, then the pond.** The kitchen is where the milk is and where the pantry observation happens; the pond is where she dies at 10:30. Her diary is only recoverable from the pond before midnight, so the window leaves room to read it and then find her.
- **Nora holds the kitchen until 10 p.m.** She is there when the 8:30 hour fires, and she moves to the bedroom afterwards, which is where the current placement already had her.
- **Madelyn and Nora share the bedroom from 10 p.m.** The house is winding down, and it keeps the two of them findable together for the late game.
