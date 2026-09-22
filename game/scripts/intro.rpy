label intro:

    scene bg manor gate evening
    show screen intro_butler_greet(enabled=False)
    with fade

    player "Looks like the butler’s waiting for me."
    player "I should go speak with him."

    call screen intro_butler_greet(enabled=True)


screen intro_butler_greet(enabled):

    imagebutton:
        style "character_button"
        idle "images/butler/butler neutral.webp"
        at character_button(xalign=.15)
        sensitive enabled
        action [Hide("intro_butler_greet"), Jump("intro_butler_greet")]


label intro_butler_greet:

    show butler neutral at character_speak
    with dissolve

    butler "You must be the detective."

    player "That’s correct."

    butler "Follow me inside."

    hide butler
    with dissolve

    call screen arrow_up_button(label="intro_butler_door", xalign=.53, yalign=.85)


label intro_butler_door:

    scene bg manor door evening
    show butler neutral at character_speak
    with dissolve

    butler "Please come in."
    player "Thanks."

    hide butler
    with dissolve

    call screen arrow_up_button(label="explore_interior_entrance", xalign=.491, yalign=.65)
