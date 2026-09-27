define DEATH_HOURS = [
    {"minutes": 19 * 60 + 30, "room": "manor_door", "hint": "death_maid_hint", "resolved": "resolved_maid", "label": "death_maid"},
    {"minutes": 20 * 60 + 30, "room": "kitchen", "hint": "death_nurse_hint", "resolved": "resolved_nurse", "label": "death_nurse", "depends": "accused_nurse"},
    {"minutes": 21 * 60 + 30, "room": "living_room", "hint": "death_butler_hint", "resolved": "resolved_butler", "label": "death_butler", "depends": "disclosed_affair"},
    {"minutes": 22 * 60 + 30, "room": "pond", "hint": "death_miss_hint", "resolved": "resolved_miss", "label": "death_miss"},
]

define KNIFE_TAKEN_MINUTES = 19 * 60

define HINT_DEFERRED_ROOMS = (
    "basement",
    "basement_stairs",
    "basement_ladder",
    "basement_inside",
    "basement_door",
)


init python:

    def death_is_pending(death):
        if getattr(store, death["resolved"]):
            return False
        depends = death.get("depends")
        if depends and not getattr(store, depends):
            return False
        return True

    def death_waiting_in(room_id):
        if not store.pending_death:
            return None
        for death in DEATH_HOURS:
            if death["label"] == store.pending_death and death["room"] == room_id:
                return death
        return None


label death_hint:

    if not pending_hint:
        return

    if current_room in HINT_DEFERRED_ROOMS:
        return

    $ hint = pending_hint

    $ pending_hint = ""
    $ hide_explore_screens()

    call expression hint

    return


screen death_body(character, expression, label, xalign=.5, enabled=True):

    imagebutton:
        style "character_button"
        idle character_sprite(character, expression)
        at character_body(xalign=xalign)
        sensitive enabled
        action [Hide("death_body"), Jump(label)]
