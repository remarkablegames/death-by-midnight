label explore_manor_door:

    scene bg manor door evening
    with dissolve

    show screen time_display

    show screen arrow_left_button(label="explore_pond", xalign=.05, yalign=.65, minutes=5)
    show screen arrow_right_button(label="explore_backyard", xalign=.95, yalign=.65, minutes=5)
    show screen arrow_up_button(label="explore_interior_entrance", xalign=.491, yalign=.65, minutes=5)
    call screen arrow_down_button(label="explore_manor_gate", xalign=.491, yalign=.95, minutes=5)
