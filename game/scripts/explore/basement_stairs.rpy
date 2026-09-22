label explore_basement_stairs:

    scene bg basement stairs

    show screen time_display
    show screen inventory_hud
    with dissolve

    show screen arrow_right_button(label="explore_basement", xalign=.8, yalign=.6, minutes=5)
    call screen arrow_down_button(label="explore_basement_door", xalign=.5, yalign=.98, minutes=5)

    if _return is not None:
        $ _inventory_result = _return
        $ _inventory_return_label = "explore_basement_stairs"
        $ _return = None
        jump inventory_handle

    jump explore_basement_stairs
