screen arrow_button(arrow, label, xalign, yalign, minutes=0):

    textbutton arrow:
        text_style "arrow_button"
        xalign xalign 
        yalign yalign
        action [
            Function(clock.advance, minutes),
            Hide("arrow_button"),
            Hide("arrow_up_button"),
            Hide("arrow_right_button"),
            Hide("arrow_down_button"),
            Hide("arrow_left_button"),
            Jump(label),
        ]


screen arrow_up_button(label, xalign, yalign, minutes=0):

    use arrow_button("↑", label, xalign, yalign, minutes)


screen arrow_right_button(label, xalign, yalign, minutes=0):

    use arrow_button("→", label, xalign, yalign, minutes=0)


screen arrow_down_button(label, xalign, yalign, minutes=0):

    use arrow_button("↓", label, xalign, yalign, minutes)


screen arrow_left_button(label, xalign, yalign, minutes=0):

    use arrow_button("←", label, xalign, yalign, minutes)
