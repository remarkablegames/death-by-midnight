label explore_manor_gate:

    if is_night_dark():
        scene bg manor gate night dark
    elif is_night_light():
        scene bg manor gate night light
    else:
        scene bg manor gate evening
    with dissolve

    show screen time_display

    call screen arrow_up_button(label="explore_manor_door", xalign=.525, yalign=.8, minutes=5)
