label talk_miss:

    show miss neutral at character_speak
    with dissolve

    $ context = room_intro("miss")

    if context:
        "[context]"

    miss "Oh,{w=.1} a guest.{w=.3} How...{w=.2} unusual for the hour."

    if inventory.has("diary") and not persistent.resolved_miss:

        miss "You’ve read it."

        player "The last page."

        miss "I know what it says."

        menu:
            "“Everyone believes it.” Who is it for?":

                player "“I smile at dinner and everyone believes it.”{w=.3} Who is that for?"

                miss "I don’t know.{w=.3} That’s the trouble.{w=.2} I’ve been at it so long I’ve forgotten where it stops."

            "Tell her what you asked all night":

                player "I spent tonight asking who did this.{w=.3} I never once asked you a thing."

                miss "No.{w=.2} You didn’t."

                player "I’m asking now."

            "Say nothing":

                "You don’t answer.{w=.3} She does."

                miss "You never once asked me what I wanted."

        miss "I don’t want to die.{w=.3} Not tonight."

        $ persistent.resolved_miss = True
        $ renpy.notify(_("Mia will not go to the pond tonight"))

    elif not milk_taken and not milk_beat_shown:

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
