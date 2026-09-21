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
