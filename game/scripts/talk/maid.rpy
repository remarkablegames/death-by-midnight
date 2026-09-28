label talk_maid:

    show maid smile at character_speak
    with dissolve

    $ context = room_intro("maid")

    if context:
        "[context]"

    jump talk_maid_menu


label talk_maid_menu:

    menu:

        "Ask about the missing kitchen knife" if not knows_knife_exists and not knows_affair:

            maid "There was a knife in the kitchen this evening."

            player "There isn’t one now."

            maid "Then your eyes are better than mine."

            $ knows_knife_exists = True

        "Ask who took the knife" if knows_knife_exists and not knows_affair:

            maid "I clean the kitchen.{w=.3} I didn’t take it."

            player "You know whose hands it was in."

            maid "You know a great deal for a man who arrived this evening."

            player "Someone in this house saw him with it."

            maid "You should be more careful...{w=.3} nobody in this house forgives being named."

            $ knows_affair = True

        "Nevermind":

            hide maid
            with dissolve

            return

    jump talk_maid_menu
