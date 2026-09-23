init python:

    class SceneCharacter(object):

        def __init__(self, character_id, expression="neutral", xalign=.5, tint="#ffffff00"):
            self.character_id = character_id
            self.expression = expression
            self.xalign = xalign
            self.tint = tint


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


    def character_sprite(character_id, expression="neutral"):
        return "images/%s/%s %s.webp" % (character_id, character_id, expression)


    def character_hover_set(character_id):
        store.character_hover_id = character_id
        renpy.sound.play("ui/mouserelease1.ogg")
        renpy.restart_interaction()


    def character_hover_clear(character_id):
        store.character_hover_id = None
        renpy.restart_interaction()


default character_hover_id = None


define CHARACTER_ROSTER = [
    CharacterInfo("butler", _("Butler Ben"), "butler neutral"),
    CharacterInfo("maid", _("Maid Madelyn"), "maid neutral"),
    CharacterInfo("miss", _("Miss Mia"), "miss neutral"),
    CharacterInfo("nurse", _("Nurse Nora"), "nurse neutral"),
]


screen inventory_character_menu(character):

    modal True
    zorder 300

    frame:
        align (.5, .5)
        background Solid(COLOR_ACTION)

        frame:
            background Solid("#160b08")
            padding (30, 30, 30, 30)

            vbox:
                spacing 12

                text character.name:
                    style "inventory_read_title"
                    align (.5, .5)

                textbutton _("Talk"):
                    text_style "text_sans_serif"
                    action Return("talk")

                if inventory.items:
                    textbutton _("Give"):
                        text_style "text_sans_serif"
                        action Return("give")

                textbutton _("Leave"):
                    text_style "text_sans_serif"
                    action Return(None)


screen inventory_choose_item(character):

    modal True
    zorder 300

    frame:
        align (.5, .5)
        background Solid(COLOR_ACTION)

        frame:
            background Solid("#160b08")
            padding (30, 30, 30, 30)

            vbox:
                spacing 12

                text _("Give to [character.name]"):
                    style "inventory_read_title"
                    xalign .5

                for item in inventory.items:
                    textbutton item.name action Return(item.item_id)

                textbutton _("Nevermind") action Return(None)


label inventory_talk_scene(character_id):

    $ character = character_info(character_id)

    if character is None:
        return

    hide screen inventory_hud

    call expression "talk_" + character_id

    return
