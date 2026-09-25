label explore_basement_ladder:

    $ set_scene_characters("basement_ladder")

    scene bg basement ladder

    show screen time_display
    show screen inventory_hud
    with dissolve

    show screen arrow_up_button(label="explore_backyard", xalign=.516, yalign=.4, minutes=5)
    call screen arrow_down_button(label="explore_basement_inside", xalign=.516, yalign=.95, minutes=5)

    if _return is not None:
        $ _inventory_result = _return
        $ _inventory_return_label = "explore_basement_ladder"
        $ _return = None
        jump inventory_handle

    jump explore_basement_ladder
