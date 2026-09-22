label explore_pond:

    if is_night_light():
        scene bg pond night
    else:
        scene bg pond evening
    with dissolve

    show screen time_display

    call screen arrow_right_button(label="explore_manor_door", xalign=.95, yalign=.65, minutes=5)
