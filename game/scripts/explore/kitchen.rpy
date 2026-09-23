label explore_kitchen:

    $ scene_characters = []

    if clock.is_night_light:
        scene bg kitchen night
    else:
        scene bg kitchen evening

    show screen time_display
    show screen inventory_hud
    with dissolve

    call screen arrow_right_button(label="explore_hallway_left", xalign=.95, yalign=.7, minutes=5)

    if _return is not None:
        $ _inventory_result = _return
        $ _inventory_return_label = "explore_kitchen"
        $ _return = None
        jump inventory_handle

    jump explore_kitchen
