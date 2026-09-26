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

        "Nevermind":

            hide butler
            with dissolve

            return

    jump talk_butler_menu
