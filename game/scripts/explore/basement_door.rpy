default seen_basement_door = False
default is_basement_locked = True


label explore_basement_door:

    $ scene_characters = []

    if clock.is_night_dark:
        if is_basement_locked:
            scene bg door closed dark
        else:
            scene bg door open dark
    else:
        if is_basement_locked:
            scene bg door closed light
        else:
            scene bg door open light

    show screen time_display
    show screen inventory_hud
    with dissolve

    if inventory.has("basement_key"):
        show screen arrow_down_button(label="explore_basement_stairs", xalign=.475, yalign=.4, minutes=5)
    else:
        show screen arrow_down_button(label="locked_gate", xalign=.475, yalign=.4)

    call screen arrow_left_button(label="explore_hallway_right", xalign=.05, yalign=.7, minutes=5)

    if _return is not None:
        $ _inventory_result = _return
        $ _inventory_return_label = "explore_basement_door"
        $ _return = None
        jump inventory_handle

    jump explore_basement_door


label locked_gate:

    $ seen_basement_door = True

    show screen time_display
    show screen inventory_hud

    player "The door is locked."

    if not inventory.has_picked_up("basement_key"):
        player "The key must be somewhere."

    jump explore_basement_door
