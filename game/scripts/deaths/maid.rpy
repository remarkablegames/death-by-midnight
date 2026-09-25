label death_maid_approach:

    $ hide_explore_screens()

    scene bg manor door evening
    show screen death_body("maid", "shocked head tilt bloody", "death_maid", xalign=.5, enabled=False)
    with dissolve

    player "Someone is on the step."

    call screen death_body("maid", "shocked head tilt bloody", "death_maid", xalign=.5, enabled=True)


label death_maid:

    show maid shocked head tilt bloody at character_body
    with dissolve

    "Madelyn is lying by the door and she is no longer responsive."

    player "Looks like multiple stab wounds."

    if confirmed_knife_gone:

        player "The kitchen knife. She told me it was in there, and then I stood at the board and it was gone."

    elif persistent.knows_knife_exists:

        player "She told me there was a knife in that kitchen this evening.{w=.3} She was right."

    "The hall clock strikes half past seven. Nobody else comes."

    scene black
    with fade

    jump loop_start
