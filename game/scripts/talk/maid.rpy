label talk_maid:

    show maid smile at character_speak
    with dissolve

    $ context = room_intro("maid")

    if context:
        "[context]"

    jump talk_maid_menu


label talk_maid_menu:

    show maid smile at character_speak

    menu:

        "Ask about the missing kitchen knife" if not knows_knife_exists and not knows_knife_taken:

            maid @ smile look away "What do you mean?{w=.3} The knife should still be there."

            player "Not anymore."

            maid shocked look away "I—{w=.2}I don’t understand.{w=.3} I saw it there earlier."

            $ knows_knife_exists = True

        "Ask who took the knife" if knows_knife_exists and not knows_knife_taken:

            maid @ smile look away "I clean the kitchen.{w=.3} I didn’t take it."

            player "You know whose hands it was in."

            maid neutral "You know a great deal for a man who arrived this evening."

            player "Someone in this house saw who had it."

            maid shocked look away "You should be more careful...{w=.3} nobody in this house forgives being named."

            $ knows_knife_taken = True

        "Nevermind":

            hide maid
            with dissolve

            return

    jump talk_maid_menu
