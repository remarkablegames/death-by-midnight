label talk_nurse:

    show nurse neutral at character_speak
    with dissolve

    $ context = room_intro("nurse")

    if context:
        "[context]"

    nurse "If you’re here about his care,{w=.1} speak plainly."

    $ can_ask_key = seen_basement_door and not inventory.has("basement_key")
    $ can_ask_bedroom = persistent.knows_affair
    $ can_accuse = persistent.knows_affair and inventory.has("coffee") and not accused_nurse
    $ can_disclose = persistent.knows_affair and not disclosed_affair

    if can_ask_key or can_ask_bedroom or can_accuse or can_disclose:

        menu:

            "Ask about the milk":

                nurse "The fridge keeps it cold.{w=.3} I would not take it from her."

            "Ask about the key" if can_ask_key:

                nurse "So you’ve seen the locked door.{w=.3} The Master kept the only key on his person to the very end."

                nurse "I keep a spare.{w=.3} Take it...{w=.3} and be careful what you find down there."

                $ inventory.add("basement_key")
                $ renpy.notify("Nora gave you the basement key")

            "Ask where Ben spends the night" if can_ask_bedroom:

                nurse "Not in the bedroom.{w=.3} I stopped waiting in the bedroom."

                player "And Madelyn?"

                nurse "My sister keeps her own counsel,{w=.3} as she keeps her own position."

            "Accuse her of poisoning him" if can_accuse:

                $ accused_nurse = True

                player "You knew about the two of them.{w=.3} You were standing in the kitchen when he took the coffee."

                nurse "I stand in the kitchen because that’s where I stand."

                player "Ben drinks whatever you hand him."

                nurse "He does.{w=.3} So does everyone in this house,{w=.1} detective,{w=.1} including you."

                nurse "Be careful what you accuse people of.{w=.3} Doors lock from the outside here."

            "Tell her about Ben and Madelyn" if can_disclose:

                $ disclosed_affair = True

                player "It’s Ben and Madelyn.{w=.3} I know what has been going on between them."

                nurse "I did not ask you to say that in this house."

                player "I know.{w=.3} I’m just saying."

                nurse "Then you’ve said it."

                "She doesn’t raise her voice.{w=.3} Silence settles between you."

            "Say nothing":

                pass

    hide nurse
    with dissolve

    return
