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

    jump explore_interior_entrance
