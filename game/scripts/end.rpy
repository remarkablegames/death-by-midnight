label end:

    $ hide_explore_screens()

    scene black
    with fade

    "The clock strikes twelve."
    "The reading begins,{w=.1} and the clause waits for a name."

    if not inventory.has("will"):

        "You have no instrument."
        "The Master’s hand is not on anything you can lay before them,{w=.1} and the clause will not take a name on your word alone."

    else:

        "The True Will is in your hands."
        "It’s the one thing here that carries the Master’s intention."

    player "The clause requires a name spoken before the reading can be completed."

    menu:
        "Who should inherit the manor?"

        "Miss Mia":
            jump ending_miss

        "Butler Ben":
            jump ending_butler

        "Nurse Nora":
            jump ending_nurse

        "Maid Madelyn":
            jump ending_maid


label ending_miss:

    show miss shocked at character_speak
    with dissolve

    player "Mia shall inherit the manor."

    if persistent.knows_miss_parentage and inventory.has("will"):

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

    elif persistent.knows_miss_parentage and not inventory.has("will"):

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

        "The hall laughs."
        "Then silence fills the room."

        miss "Don’t."

        "That’s all the answer she gets."
        "The clause is not satisfied,{w=.1} and the reading closes on nothing."

        jump ending_bad


label ending_butler:

    show butler neutral at character_speak
    with dissolve

    player "Ben shall inherit the manor."

    if inventory.has("will") and persistent.knows_affair:

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

        butler "It’s about time."

        "You feel that something is amiss,{w=.1} but you can’t quite put your finger on what it is."
        "You leave having let it stand."

        jump ending_good


label ending_nurse:

    show nurse neutral at character_speak
    with dissolve

    player "Nora shall inherit the manor."

    if inventory.has("will") and persistent.knows_miss_parentage:

        "The True Will is in your hands and you have pieced together the evidence."

        player "The girl is the Master’s,{w=.1} and the nurse kept it as a secret."
        player "Nora is the mother and the estate is the daughter’s."

        "It is the cleanest reading of the three and it costs Nora everything she buried to keep."

        "The reading holds. The house goes to Mia,{w=.1} and Nora keeps the child she saved by lying."

        jump ending_true

    elif inventory.has("will"):

        nurse "It’s a mistake."
        nurse "The Master left this to his family."

        "The reading does not hold."
        "You named the nurse,{w=.1} and the clause finds no heir in it,{w=.1} and the night closes on your error."

        jump ending_bad

    else:

        nurse "It’s a mistake."
        nurse "Ask the will,{w=.1} not me."

        "You have not seen the will."
        "You have asked a woman who has spent her life holding a house together to hand it to herself,{w=.1} and she tells you plainly that it is a mistake."

        "The reading does not hold."
        "The clause is not satisfied."

        jump ending_bad


label ending_maid:

    show maid neutral at character_speak
    with dissolve

    player "Madelyn shall inherit the manor."

    if inventory.has("will") and persistent.knows_affair:

        "The True Will is in your hands and you name the affair with it."
        "You give the manor to the woman who was under it the whole time."
        "The maid.{w=.3} Ben’s lover.{w=.3} Mia’s aunt."

        maid "You’re not serious."

        player "I am."

        "You’re entirely serious and the will does not stop you."
        "The reading holds."
        "Madelyn takes a house that was never hers and the family watches the one person they never counted on walk out with everything."

        jump ending_good

    elif inventory.has("will"):

        "The True Will is in your hands,{w=.1} and it does not name a maid,{w=.1} and you name her anyway."

        maid "On what grounds?"

        player "There are no grounds."

        "The will is real and it does not say her name."
        "The reading does not hold."

        jump ending_bad

    else:

        maid "It’s a mistake."
        maid "Check the will."

        "You have not seen the will."
        "You have named a maid in a room full of people who have never once thought about whether she deserved anything."
        "Now they’re laughing."
        "The reading does not hold."
        "The clause is not satisfied."

        jump ending_bad


label ending_true:

    scene black
    with fade

    "The reading completes."
    "Mia is the Master’s heir,{w=.1} named and proven,{w=.1} and the night releases the man who read it."
    "You leave the manor at dawn."
    "Behind you the house is already arguing about what you did, and none of it is about the will."

    player "Good night."

    return


label ending_good:

    scene black
    with fade

    "The reading completes."
    "The family keeps what it kept,{w=.1} and the clause is satisfied with a name,{w=.1} and you’re released."
    "You leave the manor at dawn."
    "You leave having let it stand."

    player "Good night."

    return


label ending_bad:

    scene black
    with fade

    "The name does not take."
    "The reading closes unfinished,{w=.1} the clause is not satisfied,{w=.1} and the man who named nothing true is the only one still in the hall when the lights go out."
    "The night does not snap back."
    "Time does not rewind."
    "There’s only the reading that never finished and you."

    player "It was not a good outcome."

    return
