label explore_kitchen:

    $ set_scene_characters("kitchen")

    if clock.is_night_light:
        scene bg kitchen night
        $ character_tint = COLOR_TINT_BLUE
    else:
        scene bg kitchen evening
        $ character_tint = COLOR_TRANSPARENT

    if not resolved_maid and clock.minutes < KNIFE_TAKEN_MINUTES:
        show screen item_kitchen_knife onlayer master zorder 0

    if clock.is_night_light and not inventory.has_picked_up("milk"):
        show screen item_milk onlayer master zorder 0

    call death_hint

    $ death_here = death_waiting_in("kitchen")
    if death_here:
        jump expression death_here["label"]

    show screen time_display
    show screen inventory_hud
    with dissolve

    if knows_knife_exists and not resolved_maid and clock.minutes >= KNIFE_TAKEN_MINUTES and not confirmed_knife_gone:
        $ confirmed_knife_gone = True
        "The board is still out with bread on it, and the knife is gone. She was right."

    call screen arrow_right_button(label="explore_hallway_left", xalign=.95, yalign=.7, minutes=5)

    if _return is not None:
        $ _inventory_result = _return
        $ _inventory_return_label = "explore_kitchen"
        $ _return = None
        jump inventory_handle

    jump explore_kitchen


screen item_kitchen_knife():

    if clock.is_night_light:
        $ item_tint = COLOR_TINT_BLUE
    else:
        $ item_tint = "#ffcf9a"

    imagebutton:
        idle "images/items/kitchen_knife.webp"
        style "item_button"
        at item_button(zoom=.2, xalign=.53, yalign=.436, matrixcolor=TintMatrix(item_tint))
        sensitive is_interactable
        action [
            Hide("item_kitchen_knife"),
            Function(inventory.add, "kitchen_knife"),
            SetVariable("resolved_maid", True),
            Function(renpy.notify, "Picked up kitchen knife"),
            Jump("explore_kitchen"),
        ]


screen item_milk():

    if clock.is_night_light:
        $ item_tint = COLOR_TINT_BLUE
    else:
        $ item_tint = "#ffd9ae"

    imagebutton:
        idle "images/items/milk.webp"
        style "item_button"
        at item_button(zoom=.1, xalign=.7, yalign=.329, matrixcolor=TintMatrix(item_tint)), flip(xzoom=-1)
        sensitive is_interactable
        action [
            Hide("item_milk"),
            Function(inventory.add, "milk"),
            Function(renpy.notify, "Picked up milk"),
            Jump("explore_kitchen"),
        ]
