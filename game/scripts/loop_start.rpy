default seen_basement_door = False
default is_basement_locked = True
default door_drop_active = False
default milk_taken = False
default milk_beat_shown = False
default gave_mia_milk = False
default diary_recent_entry = ""
default scene_characters = []


label loop_start:

    $ inventory.items = []
    $ inventory.given = []
    $ inventory.picked_up = []

    $ scene_characters = []

    $ seen_basement_door = False
    $ is_basement_locked = True
    $ door_drop_active = False

    $ milk_taken = False
    $ milk_beat_shown = False
    $ gave_mia_milk = False
    $ diary_recent_entry = diary_recent_entry_text()

    jump explore_interior_entrance
