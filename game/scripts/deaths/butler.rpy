label death_butler_hint:

    show maid sad at character_speak
    with dissolve

    maid "Have you seen Ben?{w=.3} Can you tell him to find me?"
    maid shocked look away "Last I heard,{w=.2} he was going to watch the news."

    player "Will do."

    hide maid
    with dissolve

    return


label death_butler:

    $ hide_explore_screens()

    scene bg living room night dark

    show screen death_body("butler", expression="shocked bloody", label="death_butler_found", xalign=.5, enabled=False)
    with dissolve

    player "Someone is slumped on the sofa."

    call screen death_body("butler", expression="shocked bloody", label="death_butler_found", xalign=.5, enabled=True)


label death_butler_found:

    show butler shocked bloody at character_body
    with dissolve

    "Ben lies quietly on the side,{w=.2} his face ashen."

    player "What happened?"
    player "He was fine just a moment ago."

    if ("coffee", "butler") in inventory.given:

        "You smell coffee on him."

    "The clock strikes half past nine."
    "Time starts to unravel..."

    scene black
    with fade

    jump loop_start
