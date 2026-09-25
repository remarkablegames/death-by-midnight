label explore_manor_gate:

    $ set_scene_characters("manor_gate")

    if clock.is_night_dark:
        scene bg manor gate night dark
    elif clock.is_night_light:
        scene bg manor gate night light
    else:
        scene bg manor gate evening

    show screen time_display
    show screen inventory_hud
    with dissolve

    call screen arrow_up_button(label="explore_manor_door", xalign=.525, yalign=.8, minutes=5)

    if _return is not None:
        $ _inventory_result = _return
        $ _inventory_return_label = "explore_manor_gate"
        $ _return = None
        jump inventory_handle

    jump explore_manor_gate
