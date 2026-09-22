label explore_hallway_left:

    if clock.is_night_dark:
        scene bg hallway left night dark
    elif clock.is_night_light:
        scene bg hallway left night light
    else:
        scene bg hallway left evening
    with dissolve

    show screen time_display

    show screen arrow_left_button(label="explore_kitchen", xalign=.05, yalign=.65, minutes=5)
    call screen arrow_right_button(label="explore_interior_entrance", xalign=.95, yalign=.65, minutes=5)
