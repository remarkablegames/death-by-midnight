label explore_pond:

    $ set_scene_characters("pond")

    if clock.is_night_light:
        scene bg pond night
    else:
        scene bg pond evening

    if not inventory.has_picked_up("diary"):
        show screen item_diary onlayer master zorder 0

    show screen time_display
    show screen inventory_hud
    with dissolve

    call screen arrow_right_button(label="explore_manor_door", xalign=.95, yalign=.7, minutes=5)

    if _return is not None:
        $ _inventory_result = _return
        $ _inventory_return_label = "explore_pond"
        $ _return = None
        jump inventory_handle

    jump explore_pond


screen item_diary():

    if clock.is_night_light:
        $ tint = "#2a4468"
    else:
        $ tint = "#ffcf9a"

    imagebutton:
        idle "images/items/diary.webp"
        style "item_button"
        at item_button(zoom=.035, xalign=.385, yalign=.535, matrixcolor=TintMatrix(tint))
        sensitive is_item_interactable
        action [
            Hide("item_diary"),
            Function(diary_pickup),
            Jump("explore_pond"),
        ]


init python:

    def diary_recent_entry_text():

        if gave_miss_milk:
            return _("“I’m grateful to the person who brought me milk today.”")
        elif milk_taken:
            return _("“They took the milk. Not that it mattered. I didn’t want it anyway.”")
        else:
            return _("“I wish they paid more attention to me. Father is always with Madelyn. I feel like he’s hiding something.”")

    def diary_pickup():

        store.diary_recent_entry = diary_recent_entry_text()
        inventory.add("diary")
        renpy.notify(_("Picked up diary"))

    def diary_description():

        text = _("Someone’s journal, left behind by the pond.\n\nRecent entry:\n") + diary_recent_entry

        text += _(
            "\n\nAn older page:\n"
            "“Mother says there are mixtures that heal and mixtures that harm. Knowing which is which is the difference between a cure or a toxin.”"
        )

        if persistent.knows_red_hair:
            text += _(
                "\n\nA middle page, the ink smudged:\n"
                "“Mother says my red hair must come from some ancestor long ago. I wonder which one.”"
            )

        text += _(
            "\n\nLast page:\n"
            "“I smile at dinner and everyone believes it. I’m so tired of acting. Sometimes I come to the pond so no one can see me.”"
        )

        return text
