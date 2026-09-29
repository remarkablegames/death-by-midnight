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

            butler smile look away "No, I don’t."

        "Ask why he calls Nora his wife" if knows_affair:

            butler neutral look away "Because she is."

            player "Madelyn doesn’t think so."

            butler neutral "Then Madelyn should say it to me,{w=.3} and not to a detective she met this evening."

            player "She’s your wife’s sister."

            butler "..."

            show butler neutral look away

            "He looks at the door before he answers."

            butler neutral "Yes,{w=.2} they were raised under the same roof.{w=.3} Madelyn has always coveted what her sister had."

            $ knows_nurse_maid_sisters = True

        "Do you remember me?" if loop_count > 1:

            player "Do you remember having a conversation like this before?"

            butler neutral "What do you mean?{w=.3} We only met a while ago...{w=.2} didn’t we?"

            player "Yes,{w=.1} forget I asked."

            show butler smile

        "Nevermind":

            hide butler
            with dissolve

            return

    jump talk_butler_menu
