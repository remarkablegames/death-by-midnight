label explore_basement_stairs:

    scene bg basement stairs
    with dissolve

    show screen time_display

    show screen arrow_right_button(label="explore_basement", xalign=.8, yalign=.6, minutes=5)
    call screen arrow_down_button(label="explore_basement_door", xalign=.5, yalign=.98, minutes=5)
