label explore_basement_door:

    scene bg door open light

    show screen time_display
    show screen inventory_hud
    with dissolve

    show screen arrow_down_button(label="explore_basement_stairs", xalign=.475, yalign=.4, minutes=5)
    call screen arrow_left_button(label="explore_hallway_right", xalign=.05, yalign=.7, minutes=5)

    if _return is not None:
        $ _inventory_result = _return
        $ _inventory_return_label = "explore_basement_door"
        $ _return = None
        jump inventory_handle

    jump explore_basement_door
