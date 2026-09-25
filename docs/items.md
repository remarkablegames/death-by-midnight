# Items

Every item should have a **verb**: it either changes what the detective knows (which carries into the next loop as unlocked talk options) or changes what a character does when it is given to them. Items reset each loop and must be refound; knowledge carries over as persistent talk options.

Handing an item to a character runs a label named `give_<item>_to_<character>` (e.g. `give_scroll_to_nurse`). Every item/character pair needs a label since it owns the dialogue scene. `inventory_give_scene` in `scripts/screens/inventory.rpy` consumes the item and notifies before the label runs; if the character declines, the label calls `inventory.add(item_id)` and its own notify to return the item. Labels may set flags or unlock talk options. Labels live in `game/scripts/give_item.rpy`.

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

## Prevention items

Used or withheld to stop the night's death.

<!-- prettier-ignore-start -->

| Item | Where | Verb |
| --- | --- | --- |
| Cup with residue | Study | Proves Ben died by poison, not accident |
| Coffee (Nora's) | Living room | The poison vehicle: swapping or destroying it prevents Ben's death |
| Kitchen knife | Kitchen | Stays clean; not premeditated. Its condition exposes the frame on Ben |

<!-- prettier-ignore-end -->

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
- **Pond**: Mia's journal
- **Kitchen**: knife, milk
- **Living room**: coffee
- **Basement**: True Will, pocket watch
- **Entrance hall**: scroll
