label explore_living_room:

    $ scene_characters = []

    if clock.is_night_dark:
        scene bg living room night dark
    elif clock.is_night_light:
        scene bg living room night light
    else:
        scene bg living room evening

    show screen time_display
    show screen inventory_hud
    with dissolve

    call screen arrow_right_button(label="explore_interior_entrance", xalign=.95, yalign=1.0, minutes=5)

    if _return is not None:
        $ _inventory_result = _return
        $ _inventory_return_label = "explore_living_room"
        $ _return = None
        jump inventory_handle

    jump explore_living_room
