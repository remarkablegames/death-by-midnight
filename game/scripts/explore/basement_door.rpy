label explore_basement_door:

    $ scene_characters = []
    $ door_drop_active = is_basement_locked

    if is_basement_locked:
        if clock.is_night_dark:
            scene bg basement door closed dark
        else:
            scene bg basement door closed light
        show screen interactable_door
    else:
        if clock.is_night_dark:
            scene bg basement door open dark
        else:
            scene bg basement door open light

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
        action [Hide("interactable_door"), Jump("explore_basement_door_locked")]


label explore_basement_door_locked:

    $ seen_basement_door = True

    show screen time_display
    show screen inventory_hud

    player "The door is locked."

    if inventory.has_picked_up("basement_key"):
        player "Should I use the key?"
    else:
        player "The key must be somewhere."

    jump explore_basement_door
