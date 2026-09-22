label explore_kitchen:

    if clock.is_night_light:
        scene bg kitchen night
    else:
        scene bg kitchen evening
    with dissolve

    show screen time_display

    call screen arrow_right_button(label="explore_hallway_left", xalign=.95, yalign=.65, minutes=5)
