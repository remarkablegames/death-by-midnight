label explore_basement:

    $ set_scene_characters("basement")

    scene bg basement light

    show screen time_display
    show screen inventory_hud
    with dissolve

    if not inventory.has_picked_up("will"):
        show screen item_will

    show screen arrow_up_button(label="explore_basement_inside", xalign=.515, yalign=.6, minutes=5)
    call screen arrow_down_button(label="explore_basement_stairs", xalign=.515, yalign=.95, minutes=5)

    if _return is not None:
        $ _inventory_result = _return
        $ _inventory_return_label = "explore_basement"
        $ _return = None
        jump inventory_handle

    jump explore_basement


screen item_will():

    imagebutton:
        idle "images/items/will.webp"
        style "item_button"
        at item_button(zoom=.05, xalign=.52, yalign=.399, matrixcolor=TintMatrix("#444"), rotate=-13)
        action [
            Hide("item_will"),
            Function(inventory.add, "will"),
            Function(renpy.notify, "Found the Master’s true will"),
            Jump("explore_basement"),
        ]
