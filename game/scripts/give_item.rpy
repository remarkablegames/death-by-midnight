label give_scroll_to_butler:

    show butler smile at character_speak
    with dissolve

    player "Here,{w=.1} take the scroll.{w=.3} I think you should see it."

    butler smile look away "The will?{w=.3} It looks good to me."

    $ inventory.add("scroll")
    $ renpy.notify("Ben handed the scroll back to you")

    hide butler
    with dissolve

    return


label give_scroll_to_maid:

    show maid smile at character_speak
    with dissolve

    player "Here,{w=.1} take the scroll.{w=.3} I think you should see it."

    maid shocked "This is the Master’s handwriting...{w=.3} I’ve seen it on his private notes."

    $ inventory.add("scroll")
    $ renpy.notify("Madelyn handed the scroll back to you")

    hide maid
    with dissolve

    return


label give_scroll_to_miss:

    show miss smile at character_speak
    with dissolve

    player "Here,{w=.1} take the scroll.{w=.3} I think you should see it."

    miss shocked "His seal...{w=.3} He never let anyone touch his papers,{w=.1} not even Mother."

    $ inventory.add("scroll")
    $ renpy.notify("Mia handed the scroll back to you")

    hide miss
    with dissolve

    return


label give_scroll_to_nurse:

    show nurse smile at character_speak
    with dissolve

    player "Here,{w=.1} take the scroll.{w=.3} I think you should see it."

    nurse @ smile look away "Let me see..."

    nurse neutral "{cps=10}..."

    if not accused_nurse and clock.minutes >= clock_time("20:30"):

        "She reads it without hurrying.{w=.3} The only part that stops her is the date at the top."

        nurse "This is older than the will you were hired to read.{w=.3} He kept the other one locked away."

        nurse "I’ve had a key to that door for years.{w=.3} I just never used it."

        $ inventory.add("basement_key")
        $ renpy.notify("Nora gave you a key")

    else:

        "She skims it quickly."

        nurse "It looks fine to me."

        $ inventory.add("scroll")
        $ renpy.notify("Nora handed the scroll back to you")

    hide nurse
    with dissolve

    return


label give_basement_key_to_butler:

    show butler smile at character_speak
    with dissolve

    player "Do you know what this key unlocks?"

    butler neutral "It’s the Master’s key.{w=.3} I’ll hold on to it."

    hide butler
    with dissolve

    return


label give_basement_key_to_maid:

    show maid smile at character_speak
    with dissolve

    player "Do you know what this key unlocks?"

    maid smile look away "Careful with that one.{w=.3} The Master never let it out of his sight."
    maid happy "I’ll keep it safe."

    hide maid
    with dissolve

    return


label give_basement_key_to_miss:

    show miss smile at character_speak
    with dissolve

    player "Do you know what this key unlocks?"

    miss sad look away "It opens the underground chamber.{w=.3} I’m told not to go there..."

    $ inventory.add("basement_key")
    $ renpy.notify("Mia handed the key back to you")

    hide miss
    with dissolve

    return


label give_basement_key_to_nurse:

    show nurse smile at character_speak
    with dissolve

    player "Do you know what this key unlocks?"

    nurse "Where did you find this?{w=.3} Put it away before anyone sees you with it."

    $ inventory.add("basement_key")
    $ renpy.notify("Nora handed the key back to you")

    hide nurse
    with dissolve

    return


label give_will_to_butler:

    show butler smile at character_speak
    with dissolve

    player "Hey,{w=.1} does this look like the True Will?"

    butler neutral "This will is unfamiliar to me,{w=.3} and I have read every paper in this house."
    butler neutral look away "Leave it with me until the reading."

    hide butler
    with dissolve

    return


label give_will_to_maid:

    show maid smile at character_speak
    with dissolve

    player "Hey,{w=.1} does this look like the True Will?"

    maid shocked "So you found it after all."
    maid "I knew it existed,{w=.2} but I never dared search for it."
    maid shocked look away "Give it here before someone walks in."

    hide maid
    with dissolve

    return


label give_will_to_miss:

    show miss smile at character_speak
    with dissolve

    player "Hey,{w=.1} does this look like the True Will?"

    miss shocked "His seal...{w=.3} He never trusted anyone with this but himself."
    miss shocked look away "I’d like to hold on to it."

    hide miss
    with dissolve

    return


label give_will_to_nurse:

    show nurse smile at character_speak
    with dissolve

    player "Hey,{w=.1} does this look like the True Will?"

    nurse sad "This changes everything."
    nurse "But by midnight,{w=.1} no one will want to hear it."
    nurse sad look away "You can leave it with me."

    hide nurse
    with dissolve

    return


label give_milk_to_butler:

    show butler smile at character_speak
    with dissolve

    player "Is the milk expired?"

    butler "Looks like it.{w=.3} But keep it in the fridge,{w=.1} someone might still drink it."

    $ inventory.add("milk")
    $ renpy.notify("Ben handed the milk back to you")

    hide butler
    with dissolve

    return


label give_milk_to_maid:

    show maid smile at character_speak
    with dissolve

    player "Is the milk expired?"

    maid happy "Past its date,{w=.1} like everything in this house lately."
    maid happy head tilt "I’ll dispose of it for you."

    hide maid
    with dissolve

    return


label give_milk_to_miss:

    show miss smile at character_speak
    with dissolve

    player "I brought you some milk."

    miss smile look away "You thought of me?{w=.3} Thank you for your kindnesses."

    $ gave_miss_milk = True

    hide miss
    with dissolve

    return


label give_milk_to_nurse:

    show nurse smile at character_speak
    with dissolve

    player "Is the milk expired?"

    nurse smile look away "The milk is fine."

    $ inventory.add("milk")
    $ renpy.notify("Nora handed the milk back to you")

    hide nurse
    with dissolve

    return


label give_coffee_to_butler:

    show butler smile at character_speak
    with dissolve

    player "I found a cup of coffee lying around."

    butler happy "Oh,{w=.1} that’s mine.{w=.3} Thanks for finding it."

    hide butler
    with dissolve

    return


label give_coffee_to_maid:

    show maid smile at character_speak
    with dissolve

    player "I found a cup of coffee lying around."

    maid smile look away "Sweet beneath the bitter.{w=.3} Whoever made that cup measured it carefully."

    $ inventory.add("coffee")
    $ renpy.notify("Madelyn handed the coffee back to you")

    hide maid
    with dissolve

    return


label give_coffee_to_miss:

    show miss smile at character_speak
    with dissolve

    player "I found a cup of coffee lying around."

    miss neutral "Don’t give me that.{w=.3} I only drink milk."

    $ inventory.add("coffee")
    $ renpy.notify("Mia handed the coffee back to you")

    hide miss
    with dissolve

    return


label give_coffee_to_nurse:

    show nurse smile at character_speak
    with dissolve

    player "I found a cup of coffee lying around."

    nurse neutral "Careless of someone to leave that lying about.{w=.3} Let me throw it out for you."

    $ resolved_butler = True
    $ renpy.notify("Nora took the coffee away")

    hide nurse
    with dissolve

    return


label give_diary_to_butler:

    show butler smile at character_speak
    with dissolve

    player "I found a diary by the pond."

    butler @ smile look away "That’s the young lady’s journal."
    butler "Make sure to hand it to her when you see her."

    $ inventory.add("diary")
    $ renpy.notify("Ben handed the diary back to you")

    hide butler
    with dissolve

    return


label give_diary_to_maid:

    show maid smile at character_speak
    with dissolve

    player "I found a diary by the pond."

    maid smile look away "That’s Mia’s journal.{w=.3} She’s currently looking for it."

    $ inventory.add("diary")
    $ renpy.notify("Madelyn handed the diary back to you")

    hide maid
    with dissolve

    return


label give_diary_to_miss:

    show miss smile at character_speak
    with dissolve

    player "I found this by the water."

    miss neutral "Did you read it?"

    menu:
        "Yes":
            miss "I can tell."

            player "{cps=10}I..."

            miss "Don’t look at me like that.{w=.3} This stays between us."

            player "Understood."

        "No":
            miss "I’ll take your word for it."

    $ resolved_miss = True

    hide miss
    with dissolve

    return


label give_diary_to_nurse:

    show nurse smile at character_speak
    with dissolve

    player "I found a diary by the pond."

    nurse sad "The girl’s diary."
    nurse @ sad look away "She’s been writing out at the pond during the evening."
    nurse "Please give it back to her when you can."

    $ inventory.add("diary")
    $ renpy.notify("Nora handed the diary back to you")

    hide nurse
    with dissolve

    return


label give_camera_to_butler:

    show butler smile at character_speak
    with dissolve

    player "The Master’s camera.{w=.3} There are pictures of him when he was young."

    butler neutral "He was handsome once,{w=.1} before the manor took its dues."

    $ inventory.add("camera")
    $ renpy.notify("Ben handed the camera back to you")

    hide butler
    with dissolve

    return


label give_camera_to_maid:

    show maid smile at character_speak
    with dissolve

    player "The Master’s camera.{w=.3} There are pictures of him when he was young."

    maid sad "Heaven rest him,{w=.1} he lost that hair long before he lost himself."

    $ inventory.add("camera")
    $ renpy.notify("Madelyn handed the camera back to you")

    hide maid
    with dissolve

    return


label give_camera_to_miss:

    show miss smile at character_speak
    with dissolve

    player "The Master’s camera.{w=.3} There are pictures of him when he was young."

    miss sad "Although I didn’t interact with him often,{w=.1} he always treated me in a special way."

    $ inventory.add("camera")
    $ renpy.notify("Mia handed the camera back to you")

    hide miss
    with dissolve

    return


label give_camera_to_nurse:

    show nurse smile at character_speak
    with dissolve

    player "The Master’s camera.{w=.3} There are pictures of him when he was young."

    nurse sad "What a nostalgic sight."

    $ inventory.add("camera")
    $ renpy.notify("Nora handed the camera back to you")

    hide nurse
    with dissolve

    return


label give_kitchen_knife_to_butler:

    show butler smile at character_speak
    with dissolve

    player "I found a knife in the kitchen."

    butler neutral "You have no business carrying that around the house."
    butler @ neutral look away "I’ll keep it safe."

    player "Thanks."

    hide butler
    with dissolve

    return


label give_kitchen_knife_to_maid:

    show maid smile at character_speak
    with dissolve

    player "I found a knife in the kitchen."

    maid neutral "That belongs on the board,{w=.1} not in a guest’s pocket.{w=.3} I’ll put it away."

    $ resolved_maid = True

    hide maid
    with dissolve

    return


label give_kitchen_knife_to_miss:

    show miss smile at character_speak
    with dissolve

    player "I found a knife in the kitchen."

    miss neutral "You’re not planning to carve anything with that,{w=.1} are you?{w=.3} I’d put it back before anyone notices."

    $ inventory.add("kitchen_knife")
    $ renpy.notify("Mia handed the kitchen knife back to you")

    hide miss
    with dissolve

    return


label give_kitchen_knife_to_nurse:

    show nurse smile at character_speak
    with dissolve

    player "I found a knife in the kitchen."

    nurse neutral "Sharp things are best left where they live.{w=.3} I won’t take it,{w=.1} and neither should you."

    $ inventory.add("kitchen_knife")
    $ renpy.notify("Nora handed the kitchen knife back to you")

    hide nurse
    with dissolve

    return
