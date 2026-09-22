screen arrow_button(arrow, label, xalign, yalign):

    textbutton arrow:
        text_style "arrow_button"
        xalign xalign 
        yalign yalign
        action [
            Hide("arrow_button"),
            Hide("arrow_up_button"),
            Hide("arrow_right_button"),
            Hide("arrow_down_button"),
            Hide("arrow_left_button"),
            Jump(label),
        ]


screen arrow_up_button(label, xalign, yalign):

    use arrow_button("↑", label, xalign, yalign)


screen arrow_right_button(label, xalign, yalign):

    use arrow_button("→", label, xalign, yalign)


screen arrow_down_button(label, xalign, yalign):

    use arrow_button("↓", label, xalign, yalign)


screen arrow_left_button(label, xalign, yalign):

    use arrow_button("←", label, xalign, yalign)
