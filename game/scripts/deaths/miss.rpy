label death_miss_hint:

    show nurse sad at character_speak
    with dissolve

    nurse "It’s getting late,{w=.1} and Mia is nowhere to be found."
    nurse "I’ve been searching for her inside the manor."
    nurse sad look away "Could you help me look for her outside?"

    player "Of course."

    hide nurse
    with dissolve

    return


label death_miss:

    play music running_water fadeout 1

    $ hide_explore_screens()

    scene bg pond night
    show screen death_body("miss", expression="creepy bloody", label="death_miss_found", xalign=.5, tintcolor="#111", enabled=False)
    with dissolve

    player "There you are.{w=.5} Your mother’s been worried sick."

    call screen death_body("miss", expression="creepy bloody", label="death_miss_found", xalign=.5, tintcolor="#111", enabled=True)


label death_miss_found:

    play sound string_hit2

    show miss creepy bloody at character_speak

    play music fractal_fragments1

    "She’s motionless,{w=.2} and she has been for a while."

    player "Mia...{w=.3} No...{w=.3} Not you too..."

    "There’s no sign of a struggle.{w=.3} Whoever did this left no trace."

    player "I need more clues.{w=.5} I’m running out of time."

    play sound tick_tock

    "The clock strikes half past ten."

    play music fractal_fragments2

    "Time starts to reverse..."

    scene black
    with fade

    jump loop_start
