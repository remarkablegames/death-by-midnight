label talk_maid:

    show maid neutral at character_speak
    with dissolve

    $ context = room_intro("maid")

    if context:
        "[context]"

    maid "You have my ear, though I’d keep your voice down around here."

    if not persistent.knows_knife_taken and not persistent.knows_affair:

        menu:

            "Ask about the empty knife block":

                maid "There was a knife in that kitchen this evening."

                player "There isn’t one now."

                maid "Then your eyes are better than mine."

                $ persistent.knows_knife_taken = True

            "Leave it":

                pass

    elif persistent.knows_knife_taken and not persistent.knows_affair:

        menu:

            "Ask who took the knife":

                maid "I clean the kitchen.{w=.3} I didn’t take it."

                player "You know whose hands it was in."

                maid "You know a great deal for a man who arrived this evening."

                player "Someone in this house saw him with it."

                maid "You should be more careful...{w=.3} nobody in this house forgives being named."

                $ persistent.knows_affair = True

            "Leave it":

                pass

    hide maid
    with dissolve

    return
