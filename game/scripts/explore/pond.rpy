label explore_pond:

    play music running_water fadeout 1

    $ set_scene_characters("pond")

    if clock.is_night_light:
        scene bg pond night
        $ character_tint = COLOR_TINT_BLUE
    else:
        scene bg pond evening
        $ character_tint = COLOR_TRANSPARENT

    if not inventory.has_picked_up("diary") and clock.minutes >= clock_time("19:00"):
        show screen item_diary onlayer master zorder 0

    call death_hint

    $ death_here = death_waiting_in("pond")
    if death_here:
        jump expression death_here["label"]

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
        $ item_tint = "#2a4468"
    else:
        $ item_tint = "#ffcf9a"

    imagebutton:
        idle "images/items/diary.webp"
        style "item_button"
        at item_button(zoom=.035, xalign=.385, yalign=.535, matrixcolor=TintMatrix(item_tint))
        sensitive is_interactable
        action [
            Hide("item_diary"),
            Function(diary_pickup),
            Jump("explore_pond"),
        ]


init python:

    def diary_recent_entry_text():

        if gave_miss_milk:
            return _("“I’m grateful to the person who brought me milk today.”")
        elif inventory.has_picked_up("milk"):
            return _("“They took the milk. Not that it mattered. I didn’t want it anyway.”")
        else:
            return _("“I wish they paid more attention to me. Father is always with Madelyn. I wish he spent more time with me.”")

    def diary_entry_hints_affair():
        return not gave_miss_milk and not inventory.has_picked_up("milk")

    def diary_pickup():

        store.diary_recent_entry = diary_recent_entry_text()
        inventory.add("diary")
        renpy.notify(_("Picked up diary"))

    def diary_description():

        if diary_entry_hints_affair():
            store.knows_affair = True

        text = _("Someone’s journal, left behind by the pond.\n\nRecent entry:\n") + diary_recent_entry

        text += _(
            "\n\nAn older page:\n"
            "“Mother says there are mixtures that heal and mixtures that harm. Knowing which is which is the difference between a cure or a toxin.”"
        )

        if knows_red_hair:
            text += _(
                "\n\nA middle page, the ink smudged:\n"
                "“Mother says my red hair must come from some ancestor long ago. I wonder which one.”"
            )

        text += _(
            "\n\nLast page:\n"
            "“I smile at dinner and everyone believes it. I’m so tired of acting. Sometimes I come to the pond so no one can see me.”"
        )

        return text
