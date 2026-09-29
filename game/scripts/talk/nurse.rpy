label talk_nurse:

    show nurse smile at character_speak
    with dissolve

    $ context = room_intro("nurse")

    if context:
        "[context]"

    jump talk_nurse_menu


label talk_nurse_menu:

    show nurse smile at character_speak

    menu:

        "Ask for something to drink" if current_room == "kitchen":

            nurse @ smile look away "I’m making coffee,{w=.1} but there’s also milk beside the fridge."

        "Ask about the locked door" if knows_basement_locked and is_basement_locked:

            nurse @ smile look away "So,{w=.1} you’ve seen the locked door."
            nurse "The Master keeps something important behind it."

            player "What is it?"

            nurse @ neutral "I wouldn’t know."

        "Ask where Ben spends the night" if knows_affair:

            nurse sad look away "Not in the bedroom.{w=.3} I stopped waiting."

            player "I see..."

        "Accuse her of poisoning him" if knows_affair and inventory.has("coffee") and not accused_nurse:

            $ accused_nurse = True

            player "You knew about the two of them.{w=.3} You were standing in the kitchen when he took the coffee."

            nurse neutral "I just happened to be in the kitchen at the time."

            player "Ben drinks whatever you hand him."

            nurse @ twitch look away "He does.{w=.3} So does everyone in this house,{w=.1} detective,{w=.2} including you."

            nurse "Be careful what you accuse people of.{w=.3} Doors lock from the outside here."

        "Tell her about Ben and Madelyn" if knows_affair and not disclosed_affair:

            $ disclosed_affair = True

            player "It’s Ben and Madelyn.{w=.3} I know what’s going on between them."

            nurse sad look away "I didn’t ask you to bring this up."

            show nurse sad

            player "I know.{w=.3} I just wanted to let you know."

            nurse neutral "Then be careful of what you say next."

            "She doesn’t raise her voice.{w=.5} Silence settles between you."

        "Show her the photograph in the camera" if knows_red_hair and not knows_miss_parentage:

            $ knows_miss_parentage = True

            player "There are photographs in the Master’s camera.{w=.3} One shows a young man with red hair, standing right beside you."

            nurse sad look away "{cps=10}..."

            player "Mia has his hair.{w=.3} There’s no other red hair in this house."

            "Nora looks at the door,{w=.2} then at the floor,{w=.2} then at you."

            nurse sad "He came on to me when I was young."

            nurse "I buried it to protect my family and keep this household together."

            nurse @ sad look away "My husband...{w=.5} is her uncle."

            "She folds her hands very tightly,{w=.2} as if holding something shut."

            nurse "The Master is her father.{w=.5} No one else can know."

        "Nevermind":

            hide nurse
            with dissolve

            return

    jump talk_nurse_menu
