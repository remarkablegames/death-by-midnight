label loop_start:

    $ loop_count += 1

    $ clock = Clock(Clock.START_MINUTES)

    $ inventory.items = []
    $ inventory.given = []
    $ inventory.picked_up = []

    $ is_interactable = True
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

    $ resolved_butler = False
    $ resolved_maid = False
    $ resolved_miss = False
    $ resolved_nurse = False

    $ pending_death = ""
    $ pending_hint = ""

    jump explore_interior_entrance
