label end_incomplete:

    $ victim = dead_character()

    if not victim:
        jump end

    play music fractal_fragments1 fadeout 1

    $ hide_explore_screens()

    scene black
    with fade

    play sound tick_tock

    "The clock strikes twelve."

    scene bg interior entrance night dark

    if victim != "butler":
        show butler smile at character_speak(xalign=.125)

    if victim != "nurse":
        show nurse neutral at character_speak(xalign=.375)

    if victim != "miss":
        show miss neutral at character_speak(xalign=.625)

    if victim != "maid":
        show maid smile at character_speak(xalign=.875)

    with dissolve

    player "Where’s [character_info(victim).name.split()[-1]]?"

    if victim != "nurse":
        nurse sad "I’ve searched this entire house..."
        nurse "...but I could not find ['him' if victim == 'butler' else 'her']..."
    else:
        butler neutral "I have not laid eyes on her tonight."

    "The will’s history must be spoken aloud before the reading can be completed."
    "There’s a death in this house that was never named."
    "The reading cannot be completed."

    play music fractal_fragments2

    scene black
    with fade

    "The night starts over."

    jump loop_start


label end:

    stop music fadeout 1

    $ hide_explore_screens()

    scene black
    with fade

    play sound tick_tock

    "The clock strikes twelve."
    "The time has come to read the will...{w=0.5} and reveal whose name completes the missing clause."

    play music stone_walls_bridge1 volume .7

    scene bg interior entrance night dark
    show butler smile at character_speak(xalign=.125)
    show nurse neutral at character_speak(xalign=.375)
    show miss neutral at character_speak(xalign=.625)
    show maid smile at character_speak(xalign=.875)
    with dissolve

    if not inventory.has("will"):
        player "I don’t have the will on me."
        player "Should I just wing it?"

        menu:
            "Yes":
                pass
    else:
        player "I have the True Will in my hands."
        player "For once,{w=.1} I get to choose what happens."

    "The clause requires a name spoken before the reading can be completed."

    menu:
        "Who should inherit the manor?"

        "Butler Ben":
            jump ending_butler

        "Nurse Nora":
            jump ending_nurse

        "Miss Mia":
            jump ending_miss

        "Maid Madelyn":
            jump ending_maid


label ending_miss:

    scene bg interior entrance night dark
    show miss shocked at character_speak
    with dissolve

    player "Mia shall inherit the manor."

    if knows_miss_parentage and inventory.has("will"):

        "The photograph in the camera,{w=.1} the red hair,{w=.1} the truth Nora carried alone,{w=.1} and the Master’s own will to back it."
        "Every thread comes taut at once."

        miss "Me?{w=.3} I never—"

        "She stops."
        "The reading holds,{w=.1} because you named her with proof,{w=.1} and the proof is as clear as the night itself."

        player "The estate passes to the Master’s true heir."
        player "The clause has nothing left to collect."

        "Mia’s parentage is named aloud, and no one in the hall can dispute it."

        miss "I’m not pretending anymore.{w=.3} I’m just...{w=.3} me."

        "You leave having told her the truth and let her keep it."

        jump ending_true

    elif knows_miss_parentage and not inventory.has("will"):

        miss "Me?{w=.3} On what grounds?"

        player "None."

        "The clause waits."
        "It does not find you convincing."
        "Someone laughs,{w=.1} low and cruel,{w=.1} and the moment passes."

        jump ending_bad

    elif inventory.has("will"):

        miss "Me?{w=.3} I’m not the one the Master—"

        "The reading does not hold."
        "You named the girl the will does not name,{w=.1} and the clause will not bend the instrument to fit the wish."

        jump ending_bad

    else:

        "The hall laughs.{w=.5} Then silence fills the room."

        miss neutral "Don’t."

        "That’s all the answer she gets."
        "The clause is unsatisfied,{w=.1} and the reading closes on nothing."

        jump ending_bad


label ending_butler:

    scene bg interior entrance night dark
    show butler smile at character_speak
    with dissolve

    player "Ben shall inherit the manor."

    if inventory.has("will") and knows_affair:

        "The reading holds."
        "Ben takes the manor and all family secrets are buried under it."

        jump ending_good

    elif inventory.has("will"):

        "The True Will is in your hands,{w=.1} but you do not name the affair with it."
        "You hand a dead man’s estate to his brother,{w=.1} and the will lets it stand because the will does not care why."

        "The reading holds."
        "Ben takes the manor and all family secrets are buried under it."

        jump ending_good

    else:

        butler creepy "It’s about time."

        "You feel that something’s amiss,{w=.1} but you can’t quite put your finger on what it is."
        "You leave having let it stand."

        jump ending_good


label ending_nurse:

    scene bg interior entrance night dark
    show nurse neutral at character_speak
    with dissolve

    player "Nora shall inherit the manor."

    if inventory.has("will") and knows_miss_parentage:

        "The True Will is in your hands and you have pieced together the evidence."

        player "The girl is the Master’s,{w=.1} and the nurse kept it as a secret."
        player "Nora is the mother and the estate is the daughter’s."

        "It is the cleanest reading of the three and it costs Nora everything she buried to keep."

        "The reading holds. The house goes to Mia,{w=.1} and Nora keeps the child she saved by lying."

        jump ending_true

    elif inventory.has("will"):

        nurse sad "It’s a mistake."
        nurse @ sad look away "The Master left this to his family."

        "The reading does not hold."
        "You named the nurse,{w=.1} and the clause finds no heir in it,{w=.1} and the night closes on your error."

        jump ending_bad

    else:

        nurse sad "It’s a mistake."
        nurse sad look away "Ask the will,{w=.2} not me."

        "You have not seen the will."
        "You have asked a woman who has spent her life holding a house together to hand it to herself."
        "And she has told you plainly...{w=.3} it’s a mistake."
        "The reading does not hold and the clause is unsatisfied."

        jump ending_bad


label ending_maid:

    scene bg interior entrance night dark
    show maid neutral at character_speak
    with dissolve

    player "Madelyn shall inherit the manor."

    if inventory.has("will") and knows_affair:

        "The True Will is in your hands and you name the affair with it."
        "You give the manor to the woman who was under it the whole time."
        "The maid.{w=.3} Ben’s lover.{w=.3} Mia’s aunt."

        maid shocked "You’re not serious."

        player "I am."

        "You’re entirely serious and the will does not stop you."
        "The reading holds."
        "Madelyn takes a house that was never hers and the family watches the one person they never counted on walk out with everything."

        jump ending_good

    elif inventory.has("will"):

        "The True Will is in your hands,{w=.1} and it does not name a maid,{w=.1} and you name her anyway."

        maid shocked "On what grounds?"

        player "There are no grounds."

        "The will is real and it does not say her name."
        "The reading does not hold."

        jump ending_bad

    else:

        maid shocked "It’s a mistake."
        maid @ shocked look away "Check the will."

        "You have not seen the will."
        "You have named a maid in a room full of people who have never once thought about whether she deserved anything."
        "Now they’re laughing."
        "The reading does not hold and the clause is unsatisfied."

        jump ending_bad


label ending_true:

    stop music fadeout 2
    play music misery1
    queue music misery2
    queue music misery3

    scene black
    with fade

    "The reading is complete."
    "Mia is the Master’s heir,{w=.2} named and proven."
    "The night releases the man who read it."
    "You leave the manor at dawn."
    "Behind you,{w=.2} the house is already arguing about what you did,{w=.2} and none of it is about the will."

    player "{cps=10}Good morning..."

    jump end_game


label ending_good:

    queue music stone_walls_bridge2 volume .7

    scene black
    with fade

    "The reading is complete."
    "The family keeps its inheritance."
    "The clause is satisfied with a name,{w=.3} and you’re released."
    "You leave the manor at dawn."

    player "{cps=10}Good day..."

    jump end_game


label ending_bad:

    queue music stone_walls_bridge2 volume .7

    scene black
    with fade

    "The name is not accepted and the reading ends incomplete."
    "Tired and frustrated,{w=.2} they all leave.{w=.5} You’re the only one left standing."
    "The night does not snap back.{w=.3} Time does not rewind.{w=.3} You stare at your own shadow."

    player "{cps=10}Good night..."

    jump end_game


label end_game:

    stop music fadeout 4

    scene black
    with Fade(1, 0, 1)

    return
