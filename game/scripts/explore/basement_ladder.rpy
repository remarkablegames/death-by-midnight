label explore_basement_ladder:

    scene bg basement ladder
    with dissolve

    show screen time_display

    show screen arrow_up_button(label="explore_backyard", xalign=.516, yalign=.4, minutes=5)
    call screen arrow_down_button(label="explore_basement_inside", xalign=.516, yalign=.95, minutes=5)
