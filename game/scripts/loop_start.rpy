label loop_start:

    $ clock = Clock()

    $ inventory.items = []
    $ inventory.given = []
    $ inventory.picked_up = []

    $ is_item_interactable = True
    $ scene_characters = []

    $ current_room = ""
    $ room_intros_seen = set()

    $ seen_basement_door = False
    $ is_basement_locked = True
    $ door_drop_active = False

    $ milk_taken = False
    $ milk_beat_shown = False
    $ confirmed_knife_gone = False
    $ gave_miss_milk = False
    $ diary_recent_entry = diary_recent_entry_text()

    $ disclosed_affair = False
    $ accused_nurse = False

    jump explore_interior_entrance
