label loop_start:

    $ loop_count += 1

    $ clock = Clock(Clock.START_MINUTES)

    $ inventory.items = []
    $ inventory.given = []
    $ inventory.picked_up = []

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

    if loop_count == 2:

        scene black

        player "Something’s wrong."

        "You can feel your surroundings tilt."

        "Your heart pounds against your ribs,{w=.2} each beat louder than the last."

        player "What’s happening to me?"

        $ is_interactable = False
        $ set_scene_characters("interior_entrance")

        scene bg interior entrance evening
        show screen item_scroll
        show screen time_display
        show butler smile at character_target(xalign=.2)
        with dissolve

        stop music fadeout 3

        "Your vision returns and it snaps back into focus."

        "The manor surrounds you again."

        player "...What?{w=.5} What just happened?"

        "You check the time.{w=.5} Six o’clock."

        player "No.{w=.3} That’s impossible."

        "The same silence.{w=.3} The same cold air.{w=.3} The same sight of the butler standing right in front of you."

        player "I was just here.{w=.5} Did I...{w=.3} loop?"

        "Your pulse quickens."

        player "This means I have another chance."

    $ is_interactable = True

    jump explore_interior_entrance
