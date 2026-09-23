# Items

Every item should have a **verb**: it either changes what the detective knows (which carries into the next loop as unlocked talk options) or changes what a character does when it is given to them. Items reset each loop and must be refound; knowledge carries over as persistent talk options.

Handing an item to a character consumes and notifies the item and runs a label named `give_<item>_<character>` (e.g. `give_scroll_nurse`). Every item/character pair needs a label since it owns the dialogue scene and may set flags or unlock talk options.

## Knowledge items

Read them to unlock talk options.

<!-- prettier-ignore-start -->

| Item | Where | Verb |
| --- | --- | --- |
| Scroll | Entrance hall | Hints the will being read aloud is not the real one; names the hunt for the _True Will_ |
| Family register | Bedroom | Reveals Ben's full name: Bernard Morrow, the Master's brother |
| Mia's journal | Room | Her despair; unlocks the empathetic dialogue that prevents her self-inflicted death |
| Mother's letter | Basement | "To my two daughters, Nora and Madelyn": the sister reveal |

<!-- prettier-ignore-end -->

## Giveable backstory objects

Each carries a piece of the Master's history and a reaction when handed over.

<!-- prettier-ignore-start -->

| Item | Where | Give to |
| --- | --- | --- |
| Locket (engraved "E.M.", lock of red hair) | Study | Mia: the object-gesture of her empathy path; also connects her hair to the Master |
| Letter to "Brother Bernard" | Study | Anyone: reveals the Master's name and the brotherhood |
| Never-sent letter to "my girl" | Study | Mia or Nora: his affection, signed as her father |
| Master's camera | Study | Red herring: someone implies it "caught something"; the roll is empty |

<!-- prettier-ignore-end -->

## Prevention items

Used or withheld to stop the night's death.

<!-- prettier-ignore-start -->

| Item | Where | Verb |
| --- | --- | --- |
| Cup with residue | Study | Proves Ben died by poison, not accident |
| Medicine bottle (Nora's) | Kitchen | The poison vehicle: swapping or destroying it prevents Ben's death |
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
- **Bedroom**: family register, spare basement key
- **Room**: Mia's journal
- **Kitchen**: knife, medicine bottle
- **Basement**: mother's letter, True Will, pocket watch
- **Entrance hall**: scroll
