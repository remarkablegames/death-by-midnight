label death_butler:

    $ hide_explore_screens()

    scene bg living room night light

    show screen death_body("butler", expression="shocked bloody", label="death_butler_found", xalign=.5, enabled=False)
    with dissolve

    player "Someone is on the floor."

    call screen death_body("butler", expression="shocked bloody", label="death_butler_found", xalign=.5, enabled=True)


label death_butler_found:

    show butler shocked bloody at character_body
    with dissolve

    "Ben lies on the floor,{w=.1} his face ashen."

    player "What happened?{w=.3} He was fine an hour ago."

    if ("coffee", "butler") in inventory.given:

        "You can smell coffee on him."

    "The clock strikes half past nine.{w=.3} Time starts to reverse..."

    scene black
    with fade

    jump loop_start
