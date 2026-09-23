label talk_nurse:

    show nurse neutral at character_speak
    with dissolve

    nurse "If you’re here about his care,{w=.1} speak plainly."

    if seen_basement_door and not inventory.has("basement_key"):

        menu:
            "Ask about the basement key":

                nurse "So you’ve seen the gate.{w=.3} The Master kept the only key on his person to the very end."

                nurse "I keep a spare.{w=.3} Take it...{w=.3} and be careful what you find down there."

                $ inventory.add("basement_key")
                $ renpy.notify("Nora gave you the basement key")

            "Say nothing about the key":

                pass

    hide nurse
    with dissolve

    return
