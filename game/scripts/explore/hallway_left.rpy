label explore_hallway_left:

    $ scene_characters = []

    if clock.is_night_dark:
        scene bg hallway left night dark
    elif clock.is_night_light:
        scene bg hallway left night light
    else:
        scene bg hallway left evening

    show screen time_display
    show screen inventory_hud
    with dissolve

    show screen arrow_left_button(label="explore_kitchen", xalign=.05, yalign=.7, minutes=5)
    call screen arrow_right_button(label="explore_interior_entrance", xalign=.95, yalign=.7, minutes=5)

    if _return is not None:
        $ _inventory_result = _return
        $ _inventory_return_label = "explore_hallway_left"
        $ _return = None
        jump inventory_handle

    jump explore_hallway_left
