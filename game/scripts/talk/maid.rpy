label talk_maid:

    show maid neutral at character_speak
    with dissolve

    $ context = room_intro("maid")

    if context:
        "[context]"

    jump talk_maid_menu


label talk_maid_menu:

    $ can_ask_knife = not persistent.knows_knife_exists and not persistent.knows_affair
    $ can_ask_thief = persistent.knows_knife_exists and not persistent.knows_affair

    menu:

        "Ask about the missing kitchen knife" if can_ask_knife:

            maid "There was a knife in the kitchen this evening."

            player "There isn’t one now."

            maid "Then your eyes are better than mine."

            $ persistent.knows_knife_exists = True

        "Ask who took the knife" if can_ask_thief:

            maid "I clean the kitchen.{w=.3} I didn’t take it."

            player "You know whose hands it was in."

            maid "You know a great deal for a man who arrived this evening."

            player "Someone in this house saw him with it."

            maid "You should be more careful...{w=.3} nobody in this house forgives being named."

            $ persistent.knows_affair = True

        "Nevermind":

            hide maid
            with dissolve

            return

    jump talk_maid_menu
