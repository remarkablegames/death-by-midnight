style arrow_button is text_sans_serif:
    size 150
    color COLOR_ACTION + "cc"
    hover_color COLOR_ACTION
    outlines [(2, COLOR_OUTLINE + "cc", 0, 0)]


style arrow_button_dark is arrow_button:
    color COLOR_ACTION + "40"
    hover_color COLOR_ACTION
    outlines [(2, COLOR_OUTLINE + "40", 0, 0)]


screen arrow_button(arrow, label, xalign, yalign, minutes=0):

    textbutton arrow:
        text_style ("arrow_button_dark" if clock.is_night_dark else "arrow_button")
        xalign xalign 
        yalign yalign
        action [
            Function(clock.advance, minutes),
            Hide("arrow_button"),
            Hide("arrow_up_button"),
            Hide("arrow_right_button"),
            Hide("arrow_down_button"),
            Hide("arrow_left_button"),
            Hide("item_scroll"),
            Hide("item_key"),
            Hide("item_will"),
            Hide("interactable_door"),
            Jump(label),
        ]


screen arrow_up_button(label, xalign, yalign, minutes=0):

    use arrow_button("↑", label, xalign, yalign, minutes)


screen arrow_right_button(label, xalign, yalign, minutes=0):

    use arrow_button("→", label, xalign, yalign, minutes)


screen arrow_down_button(label, xalign, yalign, minutes=0):

    use arrow_button("↓", label, xalign, yalign, minutes)


screen arrow_left_button(label, xalign, yalign, minutes=0):

    use arrow_button("←", label, xalign, yalign, minutes)
