label death_nurse:

    $ hide_explore_screens()

    scene bg kitchen evening

    show maid shocked at character_speak(xalign=.68)
    show screen death_body("nurse", expression="creepier bloody", label="death_nurse_found", xalign=.35, enabled=False)
    with dissolve

    maid "Before you say anything.{w=.3} I was with her the whole time."

    player "..."

    call screen death_body("nurse", expression="creepier bloody", label="death_nurse_found", xalign=.35, enabled=True)


label death_nurse_found:

    show nurse creepier bloody at character_body(xalign=.35)
    show maid neutral at character_speak(xalign=.68)
    with dissolve

    "Nora lies motionless, her eyes rolled back, showing only the whites."

    player "What happened here?"

    maid "I—{w=.1}I just found her like this...{w=.3} She’s not breathing."

    player "Did you see the culprit?"

    maid "No..."

    "The clock strikes half past eight.{w=.3} Time begins to unwind..."

    scene black
    with fade

    jump loop_start
