init python:

    class CharacterInfo(object):

        def __init__(self, character_id, name, image):
            self.character_id = character_id
            self.name = name
            self.image = image


    def character_info(character_id):
        if character_id is None:
            return None
        target = str(character_id).strip().lower()
        if not target:
            return None
        for character in CHARACTER_ROSTER:
            if character.character_id.strip().lower() == target:
                return character
        for character in CHARACTER_ROSTER:
            if character.name.strip().lower() == target:
                return character
        return None


    def character_object(character_id):
        return globals()[character_id]


    def character_sprite(character_id):
        return "images/%s/%s neutral.webp" % (character_id, character_id)


define CHARACTER_ROSTER = [
    CharacterInfo("butler", _("Butler Ben"), "butler neutral"),
    CharacterInfo("maid", _("Maid Madelyn"), "maid neutral"),
    CharacterInfo("miss", _("Miss Mia"), "miss neutral"),
    CharacterInfo("nurse", _("Nurse Nora"), "nurse neutral"),
]


define CHARACTER_GREETINGS = {
    "butler": _("Good evening. My master prefers a quiet manor, as you can see."),
    "maid": _("You have my ear, though I’d keep your voice down around here."),
    "miss": _("Oh, a guest. How... unusual for the hour."),
    "nurse": _("If you’re here about his care, speak plainly."),
}

define CHARACTER_GREETING_FALLBACK = _("…Yes?")


screen inventory_character_menu(character):

    modal True
    zorder 300

    frame:
        align (0.5, 0.5)
        background Solid(COLOR_ACTION)

        frame:
            background Solid("#160b08")
            padding (30, 30, 30, 30)

            vbox:
                spacing 12

                text character.name:
                    style "inventory_read_title"
                    align (0.5, 0.5)

                textbutton _("Talk"):
                    text_style "text_sans_serif"
                    action Return("talk")

                if inventory.items:
                    textbutton _("Give an item"):
                        text_style "text_sans_serif"
                        action Return("give")

                textbutton _("Leave"):
                    text_style "text_sans_serif"
                    action Return(None)


screen inventory_choose_item(character):

    modal True
    zorder 300

    frame:
        align (0.5, 0.5)
        background Solid(COLOR_ACTION)

        frame:
            background Solid("#160b08")
            padding (30, 30, 30, 30)

            vbox:
                spacing 12

                text _("Give an item to [character.name]:"):
                    style "inventory_read_title"
                    xalign 0.5

                for item in inventory.items:
                    textbutton item.name action Return(item.item_id)

                textbutton _("Nevermind") action Return(None)


label inventory_talk_scene(character_id):

    $ character = character_info(character_id)

    if character is None:
        return

    hide screen inventory_hud

    $ renpy.show(character.image, tag=character.character_id, at_list=[character_speak])
    with dissolve

    if renpy.has_label("talk_" + character_id):
        call expression "talk_" + character_id
    else:
        python:
            character_object(character.character_id)(CHARACTER_GREETINGS.get(character.character_id, CHARACTER_GREETING_FALLBACK))

    $ renpy.hide(character.character_id)
    with dissolve

    return
