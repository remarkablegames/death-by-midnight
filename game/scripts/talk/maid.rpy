label talk_maid:

    show maid smile at character_speak
    with dissolve

    $ context = room_intro("maid")

    if context:
        "[context]"

    jump talk_maid_menu


label talk_maid_menu:

    show maid smile at character_speak

    menu:

        "Ask about the missing kitchen knife" if not knows_knife_exists and not knows_knife_taken:

            maid @ smile look away "What do you mean?{w=.3} The knife should still be there."

            player "Not anymore."

            maid shocked look away "I—{w=.2}I don’t understand.{w=.3} I saw it there earlier."

            $ knows_knife_exists = True

        "Ask who took the knife" if knows_knife_exists and not knows_knife_taken:

            maid @ smile look away "I clean the kitchen.{w=.3} I didn’t take it."

            player "You know whose hands it was in."

            maid neutral "You know a great deal for a man who arrived this evening."

            player "Someone in this house saw who had it."

            maid shocked look away "You should be more careful...{w=.3} nobody in this house forgives being named."

            $ knows_knife_taken = True

        "Ask her about Nora" if not knows_nurse_maid_sisters:

            maid @ smile look away "She’s my sister."

            player "I didn’t know that."

            maid @ neutral "There’s a great deal about this house you don’t know."

            player "Are you close?"

            maid sad "Not really...{w=.3} She took everything I wanted,{w=.3} and she did it by marrying him."

            player "And you’ve made your peace with it?"

            maid happy "I’m the maid of this house.{w=.3} There’s not much peace to make."

            $ knows_nurse_maid_sisters = True

        "Ask her about Ben":

            player "What’s your relationship with Ben?"

            maid @ happy head tilt "We work together.{w=.3} Nothing more and nothing less."

            if knows_affair:

                player "Then why have people seen you together so often?"

                maid shocked "Who told you that?"

                player "I have my sources."

                maid @ shocked look away "It isn’t what you think.{w=.3} We only meet for walks...{w=.3} usually around seven-thirty."

                player "Only walks?"

                maid happy "Don’t make it sound like there’s more to it than that."

        "Nevermind":

            hide maid
            with dissolve

            return

    jump talk_maid_menu
