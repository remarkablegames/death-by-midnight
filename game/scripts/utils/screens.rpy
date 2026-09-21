screen arrow_button(arrow, label, xalign, yalign):

    textbutton arrow:
        text_style "arrow_button"
        xalign xalign 
        yalign yalign
        action Jump(label)


screen arrow_up_button(label, xalign, yalign):

    use arrow_button("↑", label, xalign, yalign)


screen arrow_right_button(label, xalign, yalign):

    use arrow_button("→", label, xalign, yalign)


screen arrow_down_button(label, xalign, yalign):

    use arrow_button("↓", label, xalign, yalign)


screen arrow_left_button(label, xalign, yalign):

    use arrow_button("←", label, xalign, yalign)
