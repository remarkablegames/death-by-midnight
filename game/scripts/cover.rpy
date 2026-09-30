label cover:

    $ quick_menu = False

    scene bg manor gate night dark

    show screen cover_title

    show nurse smile:
        xalign .2
        yalign 1.0
        zoom .5

    show butler smile:
        xalign .4
        yalign 1.0
        zoom .5

    show miss neutral:
        xalign .6
        yalign 1.0
        zoom .5

    show maid smile:
        xalign .8
        yalign 1.0
        zoom .5

    pause


screen cover_title():

    text "[config.name!t]":
        xalign .5
        yalign .1
        font "LibreBaskerville.ttf"
        size 132
        color COLOR_ACTION
        outlines [(6, COLOR_OUTLINE, 0, 0)]
