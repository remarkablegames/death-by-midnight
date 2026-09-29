label talk_miss:

    show miss smile at character_speak
    with dissolve

    $ context = room_intro("miss")

    if context:
        "[context]"

    if current_room == "kitchen" and inventory.has_picked_up("milk") and not milk_beat_shown:

        $ milk_beat_shown = True

        miss "Have you seen the milk?{w=.3} I can’t seem to find it."

        $ knows_miss_milk = True

    jump talk_miss_menu


label talk_miss_menu:

    show miss smile at character_speak

    menu:

        "Ask her about the diary" if inventory.has("diary") and not resolved_miss:

            miss neutral "You’ve read my diary."

            player "Yes,{w=.1} the very last page."

            miss neutral look away "That was supposed to be private."

            player "I want to talk to you about it."

            menu:

                "Do you ever feel happy?":

                    miss sad look away "Sometimes."

                    player "Sometimes?"

                    miss "I think so..."

                "Tell her about your investigation":

                    player "I kept asking who would want to hurt you,{w=.2} and I realized I’ve been asking the wrong question."

                    miss sad look away "{cps=10}..."

                "Say nothing":

                    player "{cps=10}..."

                    miss sad look away "{cps=10}..."

            player "Is there anything I can do?"

            miss sad "Give me a reason to see tomorrow."

            player "If you can have a little faith in me,{w=.2} then I’ll do my best."

            $ resolved_miss = True
            $ renpy.notify(_("Mia will look forward to tomorrow"))

        "Ask about her father" if gave_miss_milk and not knows_affair:

            player "Where does your father usually go?"

            miss neutral "The manor door,{w=.3} then Madelyn’s."

            player "{cps=10}..."

            miss sad look away "He spends more time with Madelyn than with me."

            player "Mia—"

            miss sad "I kept count."

            player "You should have told someone."

            miss "Who was I supposed to tell?{w=.3} That my father prefers the maid to his own daughter?"

            $ knows_affair = True

        "Ask about the milk habit" if knows_miss_milk:

            miss smile look away "Drinking it before bed helps me fall asleep."

            player "I see."

        "Ask her about the Master":

            player "Did you know him?{w=.3} The man whose final wishes everyone is waiting to hear."

            miss neutral "He was the one I was supposed to be afraid of."

            player "Were you afraid of him?"

            miss sad look away "He used to let me sit in his study.{w=.3} No one else was allowed in."

            player "And now?"

            miss sad "Now they keep it locked."

            player "You must miss him."

            miss sad look away "I’m not sure."

        "Nevermind":

            hide miss
            with dissolve

            return

    jump talk_miss_menu
