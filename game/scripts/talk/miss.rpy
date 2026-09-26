label talk_miss:

    show miss neutral at character_speak
    with dissolve

    $ context = room_intro("miss")

    if context:
        "[context]"

    miss "Oh,{w=.1} a guest.{w=.3} How...{w=.2} unusual for the hour."

    if not milk_taken and not milk_beat_shown:

        $ milk_beat_shown = True

        miss "Have you seen the milk?{w=.3} I can’t seem to find it."

        $ persistent.knows_miss_milk = True

    elif persistent.knows_miss_milk:

        menu:
            "Ask about the milk habit":

                miss "Drinking it during the night helps me fall asleep."

            "Say nothing about the milk":

                pass

    hide miss
    with dissolve

    return
