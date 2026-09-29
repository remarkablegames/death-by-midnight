init python:

    class CharacterInfo(object):

        def __init__(self, character_id, name):
            self.character_id = character_id
            self.name = name


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
        renpy.sound.play("ui/switch13.ogg")
        renpy.restart_interaction()


    def character_hover_clear(character_id):
        store.character_hover_id = None
        renpy.restart_interaction()


default character_hover_id = None


define CHARACTER_ROSTER = [
    CharacterInfo("butler", _("Butler Ben")),
    CharacterInfo("maid", _("Maid Madelyn")),
    CharacterInfo("miss", _("Miss Mia")),
    CharacterInfo("nurse", _("Nurse Nora")),
]
