label explore_room:

    if is_night_dark():
        scene bg room night dark
    elif is_night_light():
        scene bg room night light
    else:
        scene bg room evening
    with dissolve

    show screen time_display

    call screen arrow_right_button(label="explore_interior_entrance", xalign=.95, yalign=1.0, minutes=5)
