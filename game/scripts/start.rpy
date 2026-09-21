default player_name = "Danny"


label start:

    player "I’m on my way to the manor."
    player "The deceased owner asked me to execute his will."

    $ player_name = renpy.input("What’s my name again?", default="Danny").strip()

    if not player_name:
        $ player_name = "Danny"

    player "My name’s [player_name],{w=.1} and I’m a detective."

    jump intro
