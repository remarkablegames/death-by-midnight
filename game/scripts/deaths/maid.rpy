label death_maid:

    $ hide_explore_screens()

    scene bg manor door evening
    show screen death_body("maid", expression="shocked head tilt bloody", label="death_maid_found", xalign=.5, enabled=False)
    with dissolve

    player "Someone is on the step."

    call screen death_body("maid", expression="shocked head tilt bloody", label="death_maid_found", xalign=.5, enabled=True)


label death_maid_found:

    show maid shocked head tilt bloody at character_body
    with dissolve

    "Madelyn is lying by the door and she’s no longer responsive."

    player "Looks like multiple stab wounds."

    if confirmed_knife_gone:

        player "The kitchen knife.{w=.3} She told me it was there,{w=.1} but now it’s gone."

    elif persistent.knows_knife_exists:

        player "She told me there was a knife in the kitchen this evening."

    "The clock strikes half past seven.{w=.3} Your vision starts to fade..."

    scene black
    with fade

    jump loop_start
