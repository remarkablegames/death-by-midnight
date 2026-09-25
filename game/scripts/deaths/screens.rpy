define DEATH_HOURS = [
    {"minutes": 19 * 60 + 30, "closed": "closed_maid", "label": "death_maid_approach"},
]

define KNIFE_TAKEN_MINUTES = 19 * 60


init python:

    def secure_kitchen_knife():
        store.persistent.closed_maid = True


screen death_body(character_id, expression, discovery_label, xalign=.5, enabled=True):

    imagebutton:
        style "character_button"
        idle character_sprite(character_id, expression)
        at character_body(xalign=xalign)
        sensitive enabled
        action [Hide("death_body"), Jump(discovery_label)]
