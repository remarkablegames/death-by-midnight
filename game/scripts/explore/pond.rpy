label explore_pond:

    $ scene_characters = []

    if clock.is_night_light:
        scene bg pond night
    else:
        scene bg pond evening

    show screen time_display
    show screen inventory_hud
    with dissolve

    call screen arrow_right_button(label="explore_manor_door", xalign=.95, yalign=.7, minutes=5)

    if _return is not None:
        $ _inventory_result = _return
        $ _inventory_return_label = "explore_pond"
        $ _return = None
        jump inventory_handle

    jump explore_pond
