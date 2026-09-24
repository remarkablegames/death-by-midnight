label explore_pond:

    $ scene_characters = []

    if clock.is_night_light:
        scene bg pond night
    else:
        scene bg pond evening

    if not inventory.has_picked_up("diary"):
        show screen item_diary

    show screen time_display
    show screen inventory_hud
    with dissolve

    call screen arrow_right_button(label="explore_manor_door", xalign=.95, yalign=.7, minutes=5)

    if _return is not None:
        $ _inventory_result = _return
        $ _inventory_return_label = "explore_pond"
        $ _return = None
        jump inventory_handle

    jump explore_pond


screen item_diary():

    if clock.is_night_light:
        $ tint = "#2a4468"
    else:
        $ tint = "#ffcf9a"

    imagebutton:
        idle "images/items/diary.webp"
        style "item_button"
        at item_button(zoom=.035, xalign=.385, yalign=.535, matrixcolor=TintMatrix(tint))
        action [
            Hide("item_diary"),
            Function(inventory.add, "diary"),
            Function(renpy.notify, "Picked up diary"),
            Jump("explore_pond"),
        ]
