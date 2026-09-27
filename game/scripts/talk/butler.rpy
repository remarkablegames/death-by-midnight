label talk_butler:

    show butler smile at character_speak
    with dissolve

    $ context = room_intro("butler")

    if context:
        "[context]"

    jump talk_butler_menu


label talk_butler_menu:

    menu:

        "Ask about the will":

            if inventory.has("scroll"):

                butler @ neutral "You have it in your possession."
                butler "I’m looking forward to the reading tonight."

            else:

                butler @ neutral look away "If you’re looking for it,{w=.2} it should still be here."

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
