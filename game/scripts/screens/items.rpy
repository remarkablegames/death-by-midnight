screen item_scroll(tint="#ffffff00"):

    imagebutton:
        idle "images/items/scroll.webp"
        style "item_button"
        at item_button(zoom=.14, xalign=.02, yalign=.54, matrixcolor=TintMatrix(tint))
        action [
            Hide("item_scroll"),
            Function(inventory.add, "scroll"),
            Function(renpy.notify, "Picked up a scroll."),
            Jump("explore_interior_entrance"),
        ]
