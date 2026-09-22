label explore_interior_entrance:

    if clock.is_night_dark:
        scene bg interior entrance night dark
        show screen item_scroll(tint="#1f3a5f")
    elif clock.is_night_light:
        scene bg interior entrance night light
        show screen item_scroll
    else:
        scene bg interior entrance evening
        show screen item_scroll(tint="#555")
    show screen time_display
    with dissolve

    show screen arrow_button("↑", label="explore_bedroom", xalign=.728, yalign=.13, minutes=5)
    show screen arrow_up_button(label="explore_room", xalign=.345, yalign=.13, minutes=5)
    show screen arrow_left_button(label="explore_hallway_left", xalign=.05, yalign=.7, minutes=5)
    show screen arrow_right_button(label="explore_hallway_right", xalign=.95, yalign=.7, minutes=5)
    call screen arrow_down_button(label="explore_manor_door", xalign=.55, yalign=.95, minutes=5)
