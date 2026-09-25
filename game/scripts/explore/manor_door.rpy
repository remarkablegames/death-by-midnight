label explore_manor_door:

    $ set_scene_characters("manor_door")

    if clock.is_night_dark:
        scene bg manor door night dark
    elif clock.is_night_light:
        scene bg manor door night light
    else:
        scene bg manor door evening

    show screen time_display
    show screen inventory_hud
    with dissolve

    show screen arrow_left_button(label="explore_pond", xalign=.05, yalign=.7, minutes=5)
    show screen arrow_right_button(label="explore_backyard", xalign=.95, yalign=.7, minutes=5)
    show screen arrow_up_button(label="explore_interior_entrance", xalign=.491, yalign=.6, minutes=5)
    call screen arrow_down_button(label="explore_manor_gate", xalign=.491, yalign=.95, minutes=5)

    if _return is not None:
        $ _inventory_result = _return
        $ _inventory_return_label = "explore_manor_door"
        $ _return = None
        jump inventory_handle

    jump explore_manor_door
