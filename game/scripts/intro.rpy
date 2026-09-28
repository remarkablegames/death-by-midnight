label intro:

    scene bg manor gate evening
    show screen intro_butler_greet(enabled=False)
    with fade

    player "Looks like the butler’s waiting outside."
    player "I should talk to him."

    call screen intro_butler_greet(enabled=True)


screen intro_butler_greet(enabled):

    imagebutton:
        style "character_button"
        idle character_sprite("butler", "smile")
        at character_button(xalign=.15)
        sensitive enabled
        action [Hide("intro_butler_greet"), Jump("intro_butler_greet")]


label intro_butler_greet:

    show butler smile at character_speak
    with dissolve

    butler happy "Ah,{w=.1} you must be the detective."

    player "That’s correct."

    butler smile "Follow me inside."

    hide butler
    with dissolve

    call screen arrow_up_button(label="intro_butler_door", xalign=.53, yalign=.85)


label intro_butler_door:

    scene bg manor door evening
    show butler smile at character_speak
    with dissolve

    butler "The others are waiting.{w=.3} Please come in."
    player "Thanks."

    hide butler
    with dissolve

    call screen arrow_up_button(label="intro_household", xalign=.491, yalign=.6)


label intro_household:

    scene bg interior entrance evening

    $ is_interactable = False
    show screen item_scroll

    show butler smile at character_speak(xalign=.125)
    show nurse neutral at character_speak(xalign=.375)
    show miss neutral at character_speak(xalign=.625)
    show maid smile at character_speak(xalign=.875)
    with dissolve

    player "Is this everyone?"

    butler "Yes,{w=.1} it is."
    butler "Allow me to introduce everyone who lives here."

    butler @ happy "This is my wife Nora."

    nurse smile "Pleasure meeting you,{w=.1} detective."
    nurse smile look away "I have something to take care of in the kitchen,{w=.2} so please excuse me."

    hide nurse
    with dissolve

    butler "Next up is my daughter."

    miss neutral look away "You may address me as Mia.{w=.3} Be sure to remember it."

    hide miss
    with dissolve

    butler @ happy "{i}(chuckle){/i} She’s in her rebellious phase."

    player "I see."

    butler "And finally,{w=.1} this is our maid."

    maid happy "Call me Madelyn."
    maid "If you need anything,{w=.1} please let me know."

    hide maid
    with dissolve

    butler "That’s the household."
    butler happy "So when can the will be read?"

    player "I was instructed to read it after midnight."

    butler smile "All right, then.{w=.3} Please make yourself at home until the time comes."

    hide butler
    with dissolve

    jump loop_start
