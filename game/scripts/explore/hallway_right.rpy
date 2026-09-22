label explore_hallway_right:

    if is_night_dark():
        scene bg hallway right night dark
    elif is_night_light():
        scene bg hallway right night light
    else:
        scene bg hallway right evening
    with dissolve

    show screen time_display

    show screen arrow_right_button(label="explore_basement_door", xalign=.95, yalign=.65, minutes=5)
    call screen arrow_left_button(label="explore_interior_entrance", xalign=.05, yalign=.65, minutes=5)
