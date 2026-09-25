# Items

Every item should have a **verb**: it either changes what the detective knows (which carries into the next loop as unlocked talk options) or changes what a character does when it is given to them. Items reset each loop and must be refound; knowledge carries over as persistent talk options.

Handing an item to a character runs a label named `give_<item>_to_<character>` (e.g. `give_scroll_to_nurse`). Every item/character pair needs a label since it owns the dialogue scene. `inventory_give_scene` in `scripts/screens/inventory.rpy` consumes the item and notifies before the label runs; if the character declines, the label calls `inventory.add(item_id)` and its own notify to return the item. Labels may set flags or unlock talk options. Labels live in `game/scripts/give_item.rpy`.

A give scene can close a cause on the death ladder or it can load one. Handing someone the thing that provokes them is disclosure, and disclosure kills. The giveable list below and the prevention list are therefore not the same list, and most items belong to both. See `docs/story.md`.

## Knowledge items

Read them to unlock talk options.

<!-- prettier-ignore-start -->

| Item | Where | Verb |
| --- | --- | --- |
| Scroll | Entrance hall | Hints the will being read aloud is not the real one; names the hunt for the _True Will_ |
| Family register | Bedroom | Reveals Ben's full name: Bernard Morrow, the Master's brother |
| Master's camera | Bedroom | Contains photos of the young Master with head full of red hair that links him to Mia's hair color |
| Mia's journal | Pond | Multi-entry; entries surface as knowledge unlocks (favoritism, poison/bloodline, red-hair wonder once the camera is read, despair). Unlocks the empathetic dialogue that prevents her self-inflicted death |

<!-- prettier-ignore-end -->

## Giveable backstory objects

Each carries a piece of the Master's history and a reaction when handed over.

<!-- prettier-ignore-start -->

| Item | Where | Give to |
| --- | --- | --- |
| Locket (engraved "E.M.", lock of red hair) | Study | Mia: the object-gesture of her empathy path; also connects her hair to the Master |
| Letter to "Brother Bernard" | Study | Anyone: reveals the Master's name and the brotherhood |
| Never-sent letter to "my girl" | Study | Mia or Nora: his affection, signed as her father |
| Milk | Kitchen | Red herring: companion to the poisoned coffee, but provably harmless. Left in place, Miss Mia drinks it and unlocks a persistent talk option; picked up, that beat is blocked |

<!-- prettier-ignore-end -->

## The kitchen knife

The kitchen knife is the one death weapon the player can reach, and it is the whole of the 7:30 prevention. It sits on the cutting board from 6 p.m. until 7 p.m., and at 7 p.m. it is gone, because Ben took it.

- It is pickable in the kitchen before 7 p.m. **Pocketing it closes the 7:30 hour permanently.**
- **Handing it to Madelyn closes the 7:30 hour permanently.** She takes it off your hands and puts it away. Every other character hands it straight back.
- Either path sets `persistent.closed_maid`, so the knife does not return to the kitchen on any later night.
- Nothing announces that the knife has gone. It is simply not on the board after 7 p.m., and a player who was in the kitchen before then already knows it was there.
- The board without the knife only registers as evidence if the player has asked Madelyn about the knife, so the game pays for knowledge rather than for walking around. A player who never asked sees a board with no knife on it and learns nothing from it.
- The 7:30 discovery names the knife only when the player has earned it: her testimony plus the board, her testimony alone, or neither.

## Prevention items

Each closes one cause on the death ladder in `docs/story.md`. A cause closed in one night stays closed in every later night.

<!-- prettier-ignore-start -->

| Item | Where | Verb |
| --- | --- | --- |
| Cup with residue | Study | Proves Ben died by poison, not by a knife, and by a hand other than Madelyn's |
| Coffee (Nora's) | Living room | The poison vehicle. Swapping or destroying it empties the 9:30 hour |

<!-- prettier-ignore-end -->

Prevention is not knowledge. Knowing the affair does not close the 9:30 hour. Only never having said it aloud, or removing the coffee, does.

## Endgame items

<!-- prettier-ignore-start -->

| Item | Where | Verb |
| --- | --- | --- |
| Basement key | Handed over by Nora once her talk track is earned; a spare is hidden in the bedroom | Unlocks the basement gate |
| True Will | Basement | Presented at the midnight reading → True ending |
| Master's pocket watch | The drawer beside the _True Will_ | Claiming it → Hidden ending |

<!-- prettier-ignore-end -->

## Placement map

- **Study**: locket, Bernard letter, never-sent letter, camera, wine cup
- **Bedroom**: family register, spare basement key, Master's camera
- **Manor door**: the body, from 7:30, on a later night
- **Pond**: Mia's journal
- **Kitchen**: milk, and the knife until 7 p.m., then the board with no knife on it
- **Living room**: coffee
- **Basement**: True Will, pocket watch
- **Entrance hall**: scroll
