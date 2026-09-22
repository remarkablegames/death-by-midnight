label explore_basement_door:

    scene bg door open light
    with dissolve

    show screen arrow_down_button(label="explore_basement_stairs", xalign=.475, yalign=.45)
    call screen arrow_left_button(label="explore_hallway_right", xalign=.05, yalign=.6)
