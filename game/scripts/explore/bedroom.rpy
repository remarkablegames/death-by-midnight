label explore_bedroom:

    $ scene_characters = []

    if clock.is_night_light:
        scene bg bedroom night
    else:
        scene bg bedroom evening

    show screen time_display
    show screen inventory_hud
    with dissolve

    call screen arrow_left_button(label="explore_interior_entrance", xalign=.05, yalign=1.0, minutes=5)

    if _return is not None:
        $ _inventory_result = _return
        $ _inventory_return_label = "explore_bedroom"
        $ _return = None
        jump inventory_handle

    jump explore_bedroom
