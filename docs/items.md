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

## The missing knife

The kitchen knife is not in the kitchen. It is the weapon in Madelyn's death, and its absence is the first evidence that points at Ben.

- It is taken from the kitchen early, by Ben, and left at the scene.
- The empty block in the kitchen is a clue the player can look at in every loop.
- It surfaces at the manor door in a later loop, once the detective knows to look for it, and its condition is what convicts Ben.

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
- **Manor door**: the missing kitchen knife, once the detective knows to look
- **Pond**: Mia's journal
- **Kitchen**: milk, and the empty block where the knife was
- **Living room**: coffee
- **Basement**: True Will, pocket watch
- **Entrance hall**: scroll
