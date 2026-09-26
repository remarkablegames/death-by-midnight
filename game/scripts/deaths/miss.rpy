label death_miss:

    $ hide_explore_screens()

    scene bg pond night

    show screen death_body("miss", expression="sad bloody", label="death_miss_found", xalign=.5, enabled=False)
    with dissolve

    "She is face down at the water,{w=.1} and she has been still a long time."

    player "Mia...{w=.3} No.{w=.2} Not you too."

    call screen death_body("miss", expression="sad bloody", label="death_miss_found", xalign=.5, enabled=True)


label death_miss_found:

    show miss sad bloody at character_body(xalign=.5)
    with dissolve

    "Her clothes are folded on the bank.{w=0.3} Her shoes are set side by side,{w=.1} toes pointing out,{w=.1} the way a child lines them up."

    player "Did she fall in?{w=.3} Or did someone arrange this."

    "The clock strikes half past ten.{w=.3} Your vision fades..."

    scene black
    with fade

    jump loop_start
