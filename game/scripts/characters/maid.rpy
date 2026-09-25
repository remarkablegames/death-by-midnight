label talk_maid:

    show maid neutral at character_speak
    with dissolve

    $ context = room_intro("maid")

    if context:
        "[context]"

    maid "You have my ear, though I’d keep your voice down around here."

    hide maid
    with dissolve

    return
