label explore_living_room:

    $ set_scene_characters("living_room")

    if clock.is_night_dark:
        scene bg living room night dark
    elif clock.is_night_light:
        scene bg living room night light
    else:
        scene bg living room evening

    if not inventory.has_picked_up("coffee"):
        show screen item_coffee onlayer master zorder 0

    show screen time_display
    show screen inventory_hud
    with dissolve

    call screen arrow_right_button(label="explore_interior_entrance", xalign=.95, yalign=1.0, minutes=5)

    if _return is not None:
        $ _inventory_result = _return
        $ _inventory_return_label = "explore_living_room"
        $ _return = None
        jump inventory_handle

    jump explore_living_room


screen item_coffee():

    if clock.is_night_dark:
        $ tint = "#050a18"
    elif clock.is_night_light:
        $ tint = "#333"
    else:
        $ tint = "#ffe59a"

    imagebutton:
        idle "images/items/coffee.webp"
        style "item_button"
        at item_button(zoom=.13, xalign=.155, yalign=.602, matrixcolor=TintMatrix(tint))
        sensitive is_item_interactable
        action [
            Hide("item_coffee"),
            Function(inventory.add, "coffee"),
            Function(renpy.notify, "Picked up coffee"),
            Jump("explore_living_room"),
        ]
