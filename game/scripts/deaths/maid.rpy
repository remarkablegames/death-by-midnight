label death_maid_hint:

    play sound crash volume .7

    "{i}(Crash){/i}"

    player "What was that?"
    player "It sounded like it came from the manor door."

    return


label death_maid:

    play music night_outdoors fadeout 1

    $ hide_explore_screens()

    # use dark background for suspense
    scene bg manor door night dark
    show screen death_body("maid", expression="shocked head tilt bloody", label="death_maid_found", xalign=.8, tintcolor=COLOR_TINT_UNLIT, enabled=False)
    with dissolve

    player "What happened to the lights?"
    player "I can barely make out someone’s silhouette in the shadows."
    player "Hello?{w=.3} Is someone there?"

    call screen death_body("maid", expression="shocked head tilt bloody", label="death_maid_found", xalign=.8, tintcolor=COLOR_TINT_UNLIT, enabled=True)


label death_maid_found:

    play sound string_hit1

    show maid shocked head tilt bloody at character_speak
    with hpunch

    play music fractal_fragments1

    player "Madelyn! What happened to you?"

    maid @ shocked bloody "{i}(Gurgle){/i}"

    "She tries to speak,{w=.1} but only blood spills from her mouth."
    "You notice multiple stab wounds on her body."

    if confirmed_knife_gone:

        player "The kitchen knife.{w=.3} I knew it was gone,{w=.1} and I didn’t go look for it."

    elif knows_knife_exists:

        player "There was a knife in this house tonight."

    player "Stay where you are,{w=.1} I’ll get help!"

    play sound tick_tock

    "The clock strikes half past seven."

    play music fractal_fragments2

    "Your vision begins to blur..."

    scene black
    with Fade(1, 0, 1)

    jump loop_start
