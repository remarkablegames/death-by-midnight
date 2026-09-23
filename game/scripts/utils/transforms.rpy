transform character_speak:
    zoom .6
    xalign .5
    yalign 1.0


transform character_button(xalign=.5):
    zoom .5
    xalign xalign
    yalign 1.02
    on hover:
        linear .1 zoom .51
    on idle:
        linear .1 zoom .5


transform character_target(xalign):
    zoom .5
    xalign xalign
    yalign 1.0


transform character_target_hover(xalign):
    zoom .51
    xalign xalign
    yalign 1.0


transform item_button(zoom, xalign, yalign, matrixcolor=TintMatrix("#ffffff00"), rotate=0):
    zoom zoom
    xalign xalign
    yalign yalign
    matrixcolor matrixcolor
    rotate rotate
    on hover:
        linear .1 zoom zoom + .01
    on idle:
        linear .1 zoom zoom
