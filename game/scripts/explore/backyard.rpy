label explore_backyard:

    if is_night_dark():
        scene bg backyard night dark
    elif is_night_light():
        scene bg backyard night light
    else:
        scene bg backyard evening
    with dissolve

    show screen time_display

    show screen arrow_down_button(label="explore_basement_ladder", xalign=.36, yalign=.55, minutes=5)
    call screen arrow_left_button(label="explore_manor_door", xalign=.05, yalign=.65, minutes=5)
