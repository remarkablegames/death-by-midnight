label explore_basement_inside:

    $ scene_characters = []

    scene bg basement inside

    show screen time_display
    show screen inventory_hud
    with dissolve

    if not inventory.has_picked_up("will"):
        show screen item_will

    show screen arrow_up_button(label="explore_basement_ladder", xalign=.515, yalign=.47, minutes=5)
    call screen arrow_down_button(label="explore_basement", xalign=.515, yalign=.95, minutes=5)

    if _return is not None:
        $ _inventory_result = _return
        $ _inventory_return_label = "explore_basement_inside"
        $ _return = None
        jump inventory_handle

    jump explore_basement_inside


screen item_will():

    imagebutton:
        idle "images/items/scroll.webp"
        style "item_button"
        at item_button(zoom=.12, xalign=.3, yalign=.85, matrixcolor=TintMatrix("#ffffff00"))
        action [
            Hide("item_will"),
            Function(inventory.add, "will"),
            Function(renpy.notify, "Found the Master’s true will"),
            Jump("explore_basement_inside"),
        ]
