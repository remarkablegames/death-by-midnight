label death_nurse_hint:

    show maid shocked at character_speak
    with dissolve

    maid "Detective.{w=.3} You need to come to the kitchen."

    player "What happened?"

    maid shocked look away "I don’t know...{w=.5} Please,{w=.1} just come and look."

    player "Ok."

    hide maid
    with dissolve

    return


label death_nurse:

    $ hide_explore_screens()

    scene bg kitchen night
    show maid shocked at character_target(xalign=.7), tint(COLOR_TINT_UNLIT)
    call screen death_body("nurse", expression="creepier", label="death_nurse_found", xalign=.3, tintcolor=COLOR_TINT_UNLIT, enabled=True)
    with dissolve


label death_nurse_found:

    play sound string_hit3

    hide maid shocked
    show nurse creepier bloody at character_speak(xalign=.3)
    show maid shocked at character_speak(xalign=.7)
    with hpunch

    play music fractal_fragments1

    "Nora’s eyes have rolled back,{w=.3} showing only the whites."

    player "What happened here?"

    maid "I—{w=.2}I just found her like this...{w=.3} She’s cold...{w=.3} and I can’t feel a pulse..."

    player "Did you see who did this?"

    maid @ shocked look away "No..."

    play sound tick_tock

    "The clock strikes half past eight."

    play music fractal_fragments2

    "Time begins to unwind..."

    scene black
    with Fade(1, 0, 1)

    jump loop_start
