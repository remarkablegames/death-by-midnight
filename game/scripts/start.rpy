default player_name = "Danny"


label start:

    player "I’m on my way to the manor."
    player "The deceased owner asked me to execute his will."

    $ player_name = renpy.input("What’s my name again?", default="Danny").strip()

    if not player_name:
        $ player_name = "Danny"

    player "My name’s [player_name],{w=.1} and I’m a detective."

    scene bg mansion gate evening
    show screen start_butler_greet(enabled=False)
    with fade

    player "Looks like the butler is waiting for me."
    player "I should go speak to him."

    call screen start_butler_greet(enabled=True)


screen start_butler_greet(enabled):

    imagebutton:
        idle "images/butler/butler neutral.webp"
        at character_button(xalign=0.15)
        sensitive enabled
        action [Hide("start_butler_greet"), Jump("start_butler_greet")]


label start_butler_greet:

    show butler neutral at character_speak
    with dissolve

    butler "How may I help you?"

    jump end
