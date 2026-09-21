label intro:

    scene bg mansion gate evening
    show screen intro_butler_greet(enabled=False)
    with fade

    player "Looks like the butler is waiting for me."
    player "I should go speak to him."

    call screen intro_butler_greet(enabled=True)


screen intro_butler_greet(enabled):

    imagebutton:
        idle "images/butler/butler neutral.webp"
        at character_button(xalign=0.15)
        sensitive enabled
        action [Hide("intro_butler_greet"), Jump("intro_butler_greet")]


label intro_butler_greet:

    show butler neutral at character_speak
    with dissolve

    butler "How may I help you?"

    jump end
