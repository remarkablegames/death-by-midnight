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
    show screen death_body("butler", expression="creepy bloody", label="death_butler_found", xalign=.8, tintcolor=COLOR_TINT_UNLIT, enabled=False)
    with dissolve

    "It looks like someone is resting on the sofa."

    player "Hey,{w=.1} Madelyn was looking for you."

    call screen death_body("butler", expression="creepy bloody", label="death_butler_found", xalign=.8, tintcolor=COLOR_TINT_UNLIT, enabled=True)


label death_butler_found:

    play sound piano_horror

    show butler creepy bloody at character_speak
    with vpunch

    play music fractal_fragments1

    "Ben is slumped on the side,{w=.2} his face ashen."
    "He’s no longer breathing."

    player "What happened?"
    player "He was fine just a moment ago."

    if ("coffee", "butler") in inventory.given:
        "You smell coffee on him."

    play sound tick_tock

    "The clock strikes half past eight."

    play music fractal_fragments2

    "Time starts to unravel..."

    scene black
    with Fade(1, 0, 1)

    jump loop_start
