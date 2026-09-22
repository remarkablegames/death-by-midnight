label explore_interior_entrance:

    scene bg interior entrance evening
    with dissolve

    show screen arrow_button("↑", label="explore_bedroom", xalign=.728, yalign=.13)
    show screen arrow_up_button(label="explore_room", xalign=.345, yalign=.13)
    show screen arrow_left_button(label="explore_hallway_left", xalign=.05, yalign=.65)
    show screen arrow_right_button(label="explore_hallway_right", xalign=.95, yalign=.65)
    call screen arrow_down_button(label="explore_manor_door", xalign=.55, yalign=.95)
