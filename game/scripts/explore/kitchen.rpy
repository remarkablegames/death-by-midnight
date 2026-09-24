label explore_kitchen:

    $ scene_characters = []

    if clock.is_night_light:
        scene bg kitchen night
    else:
        scene bg kitchen evening

    if not inventory.has_picked_up("kitchen_knife"):
        show screen item_kitchen_knife

    if not milk_taken:
        show screen item_milk

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


screen item_kitchen_knife():

    if clock.is_night_light:
        $ tint = "#1f3a5f"
    else:
        $ tint = "#ffcf9a"

    imagebutton:
        idle "images/items/kitchen_knife.webp"
        style "item_button"
        at item_button(zoom=.2, xalign=.53, yalign=.436, matrixcolor=TintMatrix(tint))
        action [
            Hide("item_kitchen_knife"),
            Function(inventory.add, "kitchen_knife"),
            Function(renpy.notify, "Picked up kitchen knife"),
            Jump("explore_kitchen"),
        ]


screen item_milk():

    if clock.is_night_light:
        $ tint = "#1f3a5f"
    else:
        $ tint = "#ffd9ae"

    imagebutton:
        idle "images/items/milk.webp"
        style "item_button"
        at item_button(zoom=.1, xalign=.7, yalign=.329, matrixcolor=TintMatrix(tint)), flip(xzoom=-1)
        action [
            Hide("item_milk"),
            SetVariable("milk_taken", True),
            Function(inventory.add, "milk"),
            Function(renpy.notify, "Picked up milk"),
            Jump("explore_kitchen"),
        ]
