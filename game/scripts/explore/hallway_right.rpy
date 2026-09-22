label explore_hallway_right:

    scene bg hallway right evening
    with dissolve

    show screen time_display

    show screen arrow_right_button(label="explore_basement_door", xalign=.95, yalign=.65, minutes=5)
    call screen arrow_left_button(label="explore_interior_entrance", xalign=.05, yalign=.65, minutes=5)
