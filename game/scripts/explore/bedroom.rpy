label explore_bedroom:

    if is_night_light():
        scene bg bedroom night
    else:
        scene bg bedroom evening
    with dissolve

    show screen time_display

    call screen arrow_left_button(label="explore_interior_entrance", xalign=.05, yalign=1.0, minutes=5)
