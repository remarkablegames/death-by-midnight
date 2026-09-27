label explore_basement_door:

    $ set_scene_characters("basement_door")
    $ door_drop_active = is_basement_locked
    $ is_interactable = True

    if is_basement_locked:
        if clock.is_night_dark:
            scene bg basement door closed dark
            $ character_tint = "#1f3a5f"
        else:
            scene bg basement door closed light
            $ character_tint = "#ffffff00"
        show screen interactable_door onlayer master zorder 0
    else:
        if clock.is_night_dark:
            scene bg basement door open dark
            $ character_tint = "#1f3a5f"
        else:
            scene bg basement door open light
            $ character_tint = "#ffffff00"

    call death_hint

    show screen time_display
    show screen inventory_hud
    with dissolve

    if not is_basement_locked:
        show screen arrow_down_button(label="explore_basement_stairs", xalign=.475, yalign=.4, minutes=5)

    call screen arrow_left_button(label="explore_hallway_right", xalign=.05, yalign=.7, minutes=5)

    if _return is not None:
        $ _inventory_result = _return
        $ _inventory_return_label = "explore_basement_door"
        $ _return = None
        jump inventory_handle

    jump explore_basement_door


screen interactable_door():

    imagebutton:
        idle Transform("images/interactables/door.webp", alpha=0)
        hover Transform("images/interactables/door.webp", alpha=.1, matrixcolor=TintMatrix("#ffffff00" if clock.is_night_dark else "#000"))
        style "interactable_button"
        xpos 736
        ypos 146
        sensitive is_interactable
        action [
            Hide("interactable_door"),
            SetVariable("is_interactable", False),
            Jump("explore_basement_door_locked"),
        ]


label explore_basement_door_locked:

    $ seen_basement_door = True

    show screen time_display
    show screen inventory_hud

    player "The door is locked."

    if inventory.has_picked_up("basement_key"):
        player "Should I use the key?"

        menu:
            "Yes":
                jump basement_door_unlock
            "No":
                pass

    else:
        player "The key must be somewhere."

    jump explore_basement_door


label basement_door_unlock:

    hide screen inventory_hud
    hide screen interactable_door

    $ is_basement_locked = False
    $ door_drop_active = False
    $ inventory.remove("basement_key")

    "You slide the key into the lock and turn it."
    "The bolt yields with a dry click."

    $ renpy.notify("You unlocked the basement door")

    jump explore_basement_door
