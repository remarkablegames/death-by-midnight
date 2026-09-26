default player_name = ""


label start:

    "You’re on your way to the manor."
    "The late Master tasked you with executing his will."

    $ player_name = renpy.input("What’s your name?", default="Danny").strip()

    if not player_name:
        $ player_name = "Danny"

    player "My name’s [player_name],{w=.1} and I’m a detective."

    jump intro
