label explore_basement_inside:

    scene bg basement inside
    with dissolve

    show screen time_display

    show screen arrow_up_button(label="explore_basement_ladder", xalign=.515, yalign=.47, minutes=5)
    call screen arrow_down_button(label="explore_basement", xalign=.515, yalign=.95, minutes=5)
