label talk_butler:

    show butler smile at character_speak
    with dissolve

    $ context = room_intro("butler")

    if context:
        "[context]"

    jump talk_butler_menu


label talk_butler_menu:

    show butler smile at character_speak

    menu:

        "Ask about the will":

            if inventory.has("scroll"):

                butler neutral "You have it in your possession."
                butler happy "I’m looking forward to the reading tonight."

            else:

                butler neutral look away "If you’re looking for it,{w=.2} it should still be here."

        "Ask about the locked basement door" if seen_basement_door and is_basement_locked:

            butler "That door has been locked since the Master died."

            player "Do you have the key?"

            butler smile look away "No,{w=.1} I don’t."

        "Ask why he spends so much time with Madelyn" if knows_affair:

            butler happy "I’m just helping her with work."

            player "Is it just work?"

            butler neutral "Yes,{w=.3} and you shouldn’t pry into other people’s affairs."

            if knows_nurse_maid_sisters:

                player "I’m aware she’s your wife’s sister."

                butler "{cps=10}..."

                show butler neutral look away

                "He stares off into the distance before answering."

                butler neutral "Yes,{w=.2} they were raised under the same roof.{w=.3} Madelyn has always coveted what her sister had."

                player "With the will reading coming up,{w=.2} do you think she’ll try to make your relationship public?"

                butler neutral look away "She mentioned it,{w=.2} but I told her that as long as I have Nora,{w=.2} I won’t marry anyone else."

                player "I see."

                $ knows_maid_plans = True

        "Ask about the Master":

            butler neutral "He was the Master of this house."

            player "What was your relationship with him?"

            butler neutral look away "He treated me like a younger brother."

            player "And you?"

            butler neutral "I treated him as I would anyone else."

            player "Were you close?"

            butler neutral look away "Somewhat."

            butler "At this point,{w=.3} all I’m looking forward to is the reading of the will."

        "Do you remember me?" if loop_count == 2:

            player "Do you remember having a conversation like this before?"

            butler neutral "What do you mean?{w=.3} We only met a while ago...{w=.2} didn’t we?"

            player "Yes,{w=.1} forget I asked."

        "Nevermind":

            hide butler
            with dissolve

            return

    jump talk_butler_menu
