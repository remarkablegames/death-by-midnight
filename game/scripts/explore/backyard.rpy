label explore_backyard:

    $ scene_characters = []

    if clock.is_night_dark:
        scene bg backyard night dark
    elif clock.is_night_light:
        scene bg backyard night light
    else:
        scene bg backyard evening

    show screen time_display
    show screen inventory_hud
    with dissolve

    show screen arrow_down_button(label="explore_basement_ladder", xalign=.36, yalign=.55, minutes=5)
    call screen arrow_left_button(label="explore_manor_door", xalign=.05, yalign=.7, minutes=5)

    if _return is not None:
        $ _inventory_result = _return
        $ _inventory_return_label = "explore_backyard"
        $ _return = None
        jump inventory_handle

    jump explore_backyard
