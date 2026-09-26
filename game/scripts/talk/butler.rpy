label talk_butler:

    show butler smile at character_speak
    with dissolve

    $ context = room_intro("butler")

    if context:
        "[context]"

    butler "The master’s will has gone quiet these past weeks. The family argues over it constantly."
    butler "If you intend to see it set right, you’ll want to mind who holds it now."

    menu:

        "Ask who holds the will now":

            if inventory.has("scroll"):

                butler "You have taken it up.{w=.3} I hope you know what reading it makes you."

            else:

                butler "The entrance hall.{w=.3} Exactly where he left it,{w=.1} and where I have left it."

            butler "I have not signed for it.{w=.1} I will not.{w=.3} Whoever reads that paper gets a house with a family still arguing in it."

            player "That is not an answer."

            butler "It is the answer you will use.{w=.3} The reading is at midnight."

        "Leave it":

            pass

    hide butler
    with dissolve

    return
