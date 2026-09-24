label give_scroll_to_butler:

    show butler neutral at character_speak
    with dissolve

    player "Here,{w=.1} take the scroll.{w=.3} I think you should see it."

    butler "The will?{w=.3} I’ll take a look,{w=.1} but it looks old and dusty."

    hide butler
    with dissolve

    return


label give_scroll_to_maid:

    show maid neutral at character_speak
    with dissolve

    player "Here,{w=.1} take the scroll.{w=.3} I think you should see it."

    maid "This is the Master’s handwriting...{w=.3} I’ve seen it on his private notes."

    hide maid
    with dissolve

    return


label give_scroll_to_miss:

    show miss neutral at character_speak
    with dissolve

    player "Here,{w=.1} take the scroll.{w=.3} I think you should see it."

    miss "His seal...{w=.3} He never let anyone touch his papers,{w=.1} not even Mother."

    hide miss
    with dissolve

    return


label give_scroll_to_nurse:

    show nurse neutral at character_speak
    with dissolve

    player "Here,{w=.1} take the scroll.{w=.3} I think you should see it."

    nurse "Where did you find this?{w=.3} Careful,{w=.1} detective.{w=.3} Not in front of the others."

    hide nurse
    with dissolve

    return


label give_basement_key_to_butler:

    show butler neutral at character_speak
    with dissolve

    player "Do you know what this key unlocks?"

    butler "It’s the Master’s key.{w=.3} Why would you hand me that."

    hide butler
    with dissolve

    return


label give_basement_key_to_maid:

    show maid neutral at character_speak
    with dissolve

    player "Do you know what this key unlocks?"

    maid "Careful with that one.{w=.3} The Master never let it out of his sight."

    hide maid
    with dissolve

    return


label give_basement_key_to_miss:

    show miss neutral at character_speak
    with dissolve

    player "Do you know what this key unlocks?"

    miss "It opens the underground chamber.{w=.3} I’m told not to go there..."

    hide miss
    with dissolve

    return


label give_basement_key_to_nurse:

    show nurse neutral at character_speak
    with dissolve

    player "Do you know what this key unlocks?"

    nurse "Where did you find this?{w=.3} Put it away before anyone sees you with it."

    hide nurse
    with dissolve

    return


label give_will_to_butler:

    show butler neutral at character_speak
    with dissolve

    player "Hey,{w=.1} does this look like the true will?"

    butler "This is no will I have read.{w=.3} And I have read every paper in this house."

    hide butler
    with dissolve

    return


label give_will_to_maid:

    show maid neutral at character_speak
    with dissolve

    player "Hey,{w=.1} does this look like the true will?"

    maid "So you found it after all.{w=.3} I suspected this existed,{w=.1} but I never found the courage to search for it."

    hide maid
    with dissolve

    return


label give_will_to_miss:

    show miss neutral at character_speak
    with dissolve

    player "Hey,{w=.1} does this look like the true will?"

    miss "His seal...{w=.3} He never trusted anyone with this but himself.{w=.3} And now he’s trusting me?"

    hide miss
    with dissolve

    return


label give_will_to_nurse:

    show nurse neutral at character_speak
    with dissolve

    player "Hey,{w=.1} does this look like the true will?"

    nurse "This changes everything.{w=.3} But at midnight,{w=.1} no one will want to hear it."

    hide nurse
    with dissolve

    return


label give_milk_to_butler:

    show butler neutral at character_speak
    with dissolve

    player "Is the milk expired?"

    butler "Looks like it.{w=.3} But keep it in the fridge,{w=.1} someone might still be drinking it."

    $ inventory.add("milk")
    $ renpy.notify("Butler Ben handed the milk back to you")

    hide butler
    with dissolve

    return


label give_milk_to_maid:

    show maid neutral at character_speak
    with dissolve

    player "Is the milk expired?"

    maid "Past its date,{w=.1} like everything in this house lately."

    $ inventory.add("milk")
    $ renpy.notify("Maid Madelyn handed the milk back to you")

    hide maid
    with dissolve

    return


label give_milk_to_miss:

    show miss neutral at character_speak
    with dissolve

    player "I brought you some milk."

    miss "You thought of me?{w=.3} Thank you for your kindnesses."

    hide miss
    with dissolve

    return


label give_milk_to_nurse:

    show nurse neutral at character_speak
    with dissolve

    player "Is the milk expired?"

    nurse "The milk is fine."

    $ inventory.add("milk")
    $ renpy.notify("Nurse Nora handed the milk back to you")

    hide nurse
    with dissolve

    return


label give_coffee_to_butler:

    show butler neutral at character_speak
    with dissolve

    player "I found a cup of coffee lying around."

    butler "It has an unnatural smell.{w=.3} I don’t believe it’s a blend from our kitchen."

    $ inventory.add("coffee")
    $ renpy.notify("Butler Ben handed the coffee back to you")

    hide butler
    with dissolve

    return


label give_coffee_to_maid:

    show maid neutral at character_speak
    with dissolve

    player "I found a cup of coffee lying around."

    maid "Sweet beneath the bitter.{w=.3} Whoever made that cup measured it carefully."

    $ inventory.add("coffee")
    $ renpy.notify("Maid Madelyn handed the coffee back to you")

    hide maid
    with dissolve

    return


label give_coffee_to_miss:

    show miss neutral at character_speak
    with dissolve

    player "I found a cup of coffee lying around."

    miss "Don’t give me that.{w=.3} I only drink milk."

    $ inventory.add("coffee")
    $ renpy.notify("Miss Mia handed the coffee back to you")

    hide miss
    with dissolve

    return


label give_coffee_to_nurse:

    show nurse neutral at character_speak
    with dissolve

    player "I found a cup of coffee lying around."

    nurse "Careless of someone to leave that lying about.{w=.3} Let me throw it out for you."

    hide nurse
    with dissolve

    return


label give_camera_to_butler:

    show butler neutral at character_speak
    with dissolve

    player "The Master’s camera.{w=.3} There’s pictures of him when he was young."

    butler "He was handsome once,{w=.1} before the manor took its dues."

    hide butler
    with dissolve

    return


label give_camera_to_maid:

    show maid neutral at character_speak
    with dissolve

    player "The Master’s camera.{w=.3} There’s pictures of him when he was young."

    maid "Heaven rest him,{w=.1} he lost that hair long before he lost himself."

    hide maid
    with dissolve

    return


label give_camera_to_miss:

    show miss neutral at character_speak
    with dissolve

    player "The Master’s camera.{w=.3} There’s pictures of him when he was young."

    miss "Although I didn’t interact with him often,{w=.1} he always treated me in a special way."

    hide miss
    with dissolve

    return


label give_camera_to_nurse:

    show nurse neutral at character_speak
    with dissolve

    player "The Master’s camera.{w=.3} There’s pictures of him when he was young."

    nurse "What a nostalic sight."

    hide nurse
    with dissolve

    return


label give_kitchen_knife_to_butler:

    show butler neutral at character_speak
    with dissolve

    player "I found a knife in the kitchen."

    butler "I’m the butler,{w=.1} not the cook.{w=.3} Put it back where you found it."

    $ inventory.add("kitchen_knife")
    $ renpy.notify("Butler Ben handed the kitchen knife back to you")

    hide butler
    with dissolve

    return


label give_kitchen_knife_to_maid:

    show maid neutral at character_speak
    with dissolve

    player "I found a knife in the kitchen."

    maid "That belongs on the rack,{w=.1} not in a guest’s pocket.{w=.3} I’ll take it and see it put away before the cook misses it."

    hide maid
    with dissolve

    return


label give_kitchen_knife_to_miss:

    show miss neutral at character_speak
    with dissolve

    player "I found a knife in the kitchen."

    miss "You’re not planning to carve anything with that,{w=.1} are you?{w=.3} I’d put it back before the cook notices."

    $ inventory.add("kitchen_knife")
    $ renpy.notify("Miss Mia handed the kitchen knife back to you")

    hide miss
    with dissolve

    return


label give_kitchen_knife_to_nurse:

    show nurse neutral at character_speak
    with dissolve

    player "I found a knife in the kitchen."

    nurse "Sharp things are best left where they live.{w=.3} I won’t take it,{w=.1} and neither should you."

    $ inventory.add("kitchen_knife")
    $ renpy.notify("Nurse Nora handed the kitchen knife back to you")

    hide nurse
    with dissolve

    return
