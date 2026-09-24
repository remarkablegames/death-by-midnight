label explore_basement_inside:

    $ scene_characters = []

    scene bg basement inside

    show screen time_display
    show screen inventory_hud
    with dissolve

    show screen arrow_up_button(label="explore_basement_ladder", xalign=.515, yalign=.47, minutes=5)
    call screen arrow_down_button(label="explore_basement", xalign=.515, yalign=.95, minutes=5)

    if _return is not None:
        $ _inventory_result = _return
        $ _inventory_return_label = "explore_basement_inside"
        $ _return = None
        jump inventory_handle

    jump explore_basement_inside
