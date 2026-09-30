label explore_living_room:

    $ set_scene_characters("living_room")

    if clock.is_night_dark:
        scene bg living room night dark
        $ character_tint = COLOR_TINT_BLUE
    elif clock.is_night_light:
        scene bg living room night light
        $ character_tint = COLOR_TRANSPARENT
    else:
        scene bg living room evening
        $ character_tint = COLOR_TRANSPARENT

    if not inventory.has_picked_up("coffee") and clock.minutes >= clock_time("19:30"):
        show screen item_coffee onlayer master zorder 0

    call death_hint

    $ death_here = death_waiting_in("living_room")
    if death_here:
        jump expression death_here["label"]

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
        $ item_tint = "#050a18"
    elif clock.is_night_light:
        $ item_tint = COLOR_TINT_GREY
    else:
        $ item_tint = COLOR_TRANSPARENT

    imagebutton:
        idle "images/items/coffee.webp"
        style "item_button"
        at item_button(zoom=.13, xalign=.155, yalign=.602, matrixcolor=TintMatrix(item_tint))
        sensitive is_interactable
        action [
            Hide("item_coffee"),
            SetVariable("resolved_butler", True),
            Function(inventory.add, "coffee"),
            Function(renpy.notify, "Picked up coffee"),
            Jump("explore_living_room"),
        ]
