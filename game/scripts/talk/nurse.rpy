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
    $ can_ask_parentage = persistent.knows_red_hair and not persistent.knows_miss_parentage

    if can_ask_key or can_ask_bedroom or can_accuse or can_disclose or can_ask_parentage:

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

            "Show her the photograph in the camera" if can_ask_parentage:

                $ persistent.knows_miss_parentage = True

                player "There are photographs in the Master’s camera.{w=.3} A young man with red hair, standing beside your wife."

                nurse "..."

                player "Mia has his hair.{w=.3} Red like that doesn’t come from anywhere else in this house."

                "Nora looks at the door, then at the floor, then at you."

                nurse "He came to me when Elias was already ill.{w=.3} He did not ask.{w=.3} He never once asked."

                nurse "I buried it, because a nurse does that.{w=.3} I buried it so Mia would have a father standing in the doorway."

                nurse "Ben is her uncle.{w=.3} He has never been her father, and if you tell him you know, he will take the house apart before he takes his own share of it."

                "She folds her hands very tightly, as if holding something shut."

                nurse "The Master is her father.{w=.3} Write that down somewhere no one can lose it, and let me carry the rest."

            "Say nothing":

                pass

    hide nurse
    with dissolve

    return
