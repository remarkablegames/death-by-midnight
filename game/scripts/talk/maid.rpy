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

        "Ask who would want to kill you" if knows_death_maid and not asked_maid_about_death:

            player "Who in this house would want you dead?"

            maid shocked "That’s a strange question to ask a maid."

            player "Does anyone come to mind?"

            maid @ shocked look away "{cps=10}..."

            maid sad "No one."

            player "You hesitated."

            maid @ sad look away "I think about being replaced.{w=.3} It’s not the same as being killed."

            player "Who would replace you?"

            maid @ sad look away "{cps=10}..."

            maid sad "I have no one to name.{w=.3} And I wouldn’t want to."

            player "You should be careful."

            maid "I will."

            $ asked_maid_about_death = True

        "Ask about the kitchen" if current_room == "kitchen":

            maid @ smile look away "It’s the one room nobody’s left alone this evening."

            if not resolved_maid and clock.minutes >= KNIFE_TAKEN_TIME and not knows_knife_exists:

                player "Has anything gone missing?"

                maid "I haven’t stopped to look properly."
                maid smile look away "{cps=10}..."
                maid neutral "Wait."

                player "What?"

                maid "There was a knife on the board earlier.{w=.3} I laid it out myself."

                player "And now?"

                maid shocked "I don’t know."

                $ knows_knife_exists = True

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

        "Tell her to leave Nora alone" if not resolved_nurse and knows_maid_plans:

            player "Whatever you’re thinking,{w=.3} it’s not worth it."

            maid happy head tilt "I don’t know what you’re talking about."

            player "I’m aware of what you’re planning to do."

            maid shocked "{cps=10}..."
            maid neutral "I’m only doing what I must."

            player "For him?"

            maid shocked look away "No..."

            player "For yourself."

            maid sad look away "{cps=10}..."

            maid "Leave me alone now,{w=.3} detective."

            $ resolved_nurse = True
            $ renpy.notify("Madelyn changed her plans")

        "Nevermind":

            hide maid
            with dissolve

            return

    jump talk_maid_menu
