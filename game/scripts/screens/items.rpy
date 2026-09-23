screen item_scroll(tint="#ffffff00"):

    imagebutton:
        idle "images/items/scroll.webp"
        style "item_button"
        at item_button(zoom=.14, xalign=.02, yalign=.54, matrixcolor=TintMatrix(tint))
        action [
            Hide("item_scroll"),
            Function(inventory.add, "scroll"),
            Function(renpy.notify, "Picked up scroll"),
            Jump("explore_interior_entrance"),
        ]


screen item_will():

    imagebutton:
        idle "images/items/scroll.webp"
        style "item_button"
        at item_button(zoom=.12, xalign=.3, yalign=.85, matrixcolor=TintMatrix("#ffffff00"))
        action [
            Hide("item_will"),
            Function(inventory.add, "will"),
            Function(renpy.notify, "Found the Master’s true will"),
            Jump("explore_basement_inside"),
        ]
