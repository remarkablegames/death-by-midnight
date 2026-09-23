label give_scroll_butler:

    show butler neutral at character_speak
    with dissolve

    player "Here,{w=.1} take the scroll.{w=.3} I think you should see it."

    butler "The will?{w=.3} I’ll take a look,{w=.1} but it looks old and dusty."

    hide butler
    with dissolve

    return


label give_scroll_maid:

    show maid neutral at character_speak
    with dissolve

    player "Here,{w=.1} take the scroll.{w=.3} I think you should see it."

    maid "This is the Master’s handwriting...{w=.3} I’ve seen it on his private notes."

    hide maid
    with dissolve

    return


label give_scroll_miss:

    show miss neutral at character_speak
    with dissolve

    player "Here,{w=.1} take the scroll.{w=.3} I think you should see it."

    miss "His seal...{w=.3} He never let anyone touch his papers,{w=.1} not even Mother."

    hide miss
    with dissolve

    return


label give_scroll_nurse:

    show nurse neutral at character_speak
    with dissolve

    player "Here,{w=.1} take the scroll.{w=.3} I think you should see it."

    nurse "Where did you find this?{w=.3} Careful,{w=.1} detective.{w=.3} Not in front of the others."

    hide nurse
    with dissolve

    return


label give_basement_key_butler:

    show butler neutral at character_speak
    with dissolve

    player "Do you know what this key unlocks?"

    butler "It’s the Master’s key.{w=.3} Why would you hand me that."

    hide butler
    with dissolve

    return


label give_basement_key_maid:

    show maid neutral at character_speak
    with dissolve

    player "Do you know what this key unlocks?"

    maid "Careful with that one.{w=.3} The Master never let it out of his sight."

    hide maid
    with dissolve

    return


label give_basement_key_miss:

    show miss neutral at character_speak
    with dissolve

    player "Do you know what this key unlocks?"

    miss "It opens the underground chamber.{w=.3} I’m told not to go there..."

    hide miss
    with dissolve

    return


label give_basement_key_nurse:

    show nurse neutral at character_speak
    with dissolve

    player "Do you know what this key unlocks?"

    nurse "Where did you find this?{w=.3} Put it away before anyone sees you with it."

    hide nurse
    with dissolve

    return


label give_will_butler:

    show butler neutral at character_speak
    with dissolve

    player "Hey,{w=.1} does this look like the true will?"

    butler "This is no will I have read.{w=.3} And I have read every paper in this house."

    hide butler
    with dissolve

    return


label give_will_maid:

    show maid neutral at character_speak
    with dissolve

    player "Hey,{w=.1} does this look like the true will?"

    maid "So you found it after all.{w=.3} I suspected this existed,{w=.1} but I never found the courage to search for it."

    hide maid
    with dissolve

    return


label give_will_miss:

    show miss neutral at character_speak
    with dissolve

    player "Hey,{w=.1} does this look like the true will?"

    miss "His seal...{w=.3} He never trusted anyone with this but himself.{w=.3} And now he’s trusting me?"

    hide miss
    with dissolve

    return


label give_will_nurse:

    show nurse neutral at character_speak
    with dissolve

    player "Hey,{w=.1} does this look like the true will?"

    nurse "This changes everything.{w=.3} But at midnight,{w=.1} no one will want to hear it."

    hide nurse
    with dissolve

    return


label give_kitchen_knife_butler:

    show butler neutral at character_speak
    with dissolve

    player "I found a knife in the kitchen."

    butler "I’m the butler,{w=.1} not the cook.{w=.3} Return it back to where you found it."

    $ inventory.add("kitchen_knife")
    $ renpy.notify("Butler Ben handed the kitchen knife back to you")

    hide butler
    with dissolve

    return


label give_kitchen_knife_maid:

    show maid neutral at character_speak
    with dissolve

    player "I found a knife in the kitchen."

    maid "That belongs on the rack,{w=.1} not in a guest’s pocket.{w=.3} I’ll take it and see it put away before the cook misses it."

    hide maid
    with dissolve

    return


label give_kitchen_knife_miss:

    show miss neutral at character_speak
    with dissolve

    player "I found a knife in the kitchen."

    miss "You’re not planning to carve anything with that,{w=.1} are you?{w=.3} I’d put it back before the cook notices."

    $ inventory.add("kitchen_knife")
    $ renpy.notify("Miss Mia handed the kitchen knife back to you")

    hide miss
    with dissolve

    return


label give_kitchen_knife_nurse:

    show nurse neutral at character_speak
    with dissolve

    player "I found a knife in the kitchen."

    nurse "Sharp things are best left where they live.{w=.3} I won’t take it,{w=.1} and neither should you."

    $ inventory.add("kitchen_knife")
    $ renpy.notify("Nurse Nora handed the kitchen knife back to you")

    hide nurse
    with dissolve

    return
