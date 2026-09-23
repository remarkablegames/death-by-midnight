transform character_speak:
    zoom 0.6
    xalign 0.5
    yalign 1.0


transform character_button(xalign=0.5):
    zoom 0.5
    xalign xalign
    yalign 1.0
    on hover:
        linear 0.1 zoom 0.51
    on idle:
        linear 0.1 zoom 0.5


transform character_target(xalign):
    zoom 0.5
    xalign xalign
    yalign 1.0


transform character_target_hover(xalign):
    zoom 0.51
    xalign xalign
    yalign 1.0


transform item_button(zoom, xalign, yalign, matrixcolor):
    zoom zoom
    xalign xalign
    yalign yalign
    matrixcolor matrixcolor
    on hover:
        linear 0.1 zoom zoom + .01
    on idle:
        linear 0.1 zoom zoom
