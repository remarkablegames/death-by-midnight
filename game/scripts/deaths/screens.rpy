define DEATH_HOURS = [
    {"minutes": 19 * 60 + 30, "resolved": "resolved_maid", "label": "death_maid"},
    {"minutes": 20 * 60 + 30, "resolved": "resolved_nurse", "label": "death_nurse", "depends": "accused_nurse"},
    {"minutes": 21 * 60 + 30, "resolved": "resolved_butler", "label": "death_butler", "depends": "disclosed_affair"},
]

define KNIFE_TAKEN_MINUTES = 19 * 60


init python:

    def secure_kitchen_knife():
        persistent.resolved_maid = True

    def death_is_pending(death):
        if getattr(persistent, death["resolved"]):
            return False
        depends = death.get("depends")
        if depends and not getattr(store, depends):
            return False
        return True


screen death_body(character, expression, label, xalign=.5, enabled=True):

    imagebutton:
        style "character_button"
        idle character_sprite(character, expression)
        at character_body(xalign=xalign)
        sensitive enabled
        action [Hide("death_body"), Jump(label)]
