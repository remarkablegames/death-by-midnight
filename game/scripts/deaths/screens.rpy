define DEATH_HOURS = [
    {"minutes": clock_time("19:30"), "character": "maid", "room": "manor_door", "hint": "death_maid_hint", "resolved": "resolved_maid", "label": "death_maid"},
    {"minutes": clock_time("20:30"), "character": "nurse", "room": "kitchen", "hint": "death_nurse_hint", "resolved": "resolved_nurse", "label": "death_nurse", "depends": "accused_nurse"},
    {"minutes": clock_time("21:30"), "character": "butler", "room": "living_room", "hint": "death_butler_hint", "resolved": "resolved_butler", "label": "death_butler", "depends": "disclosed_affair"},
    {"minutes": clock_time("22:30"), "character": "miss", "room": "pond", "hint": "death_miss_hint", "resolved": "resolved_miss", "label": "death_miss"},
]

define KNIFE_TAKEN_MINUTES = clock_time("19:00")

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
        if not pending_death:
            return None
        for death in DEATH_HOURS:
            if death["label"] == pending_death and death["room"] == room_id:
                return death
        return None

    def dead_character():
        if not pending_death:
            return None
        for death in DEATH_HOURS:
            if death["label"] == pending_death:
                return death["character"]
        return None


label death_hint:

    if not pending_hint:
        return

    if current_room in HINT_DEFERRED_ROOMS:
        return

    if death_waiting_in(current_room) is not None:
        return

    $ hint = pending_hint

    $ pending_hint = ""
    $ hide_explore_screens()

    call expression hint

    return


screen death_body(character, expression, label, xalign=.5, tintcolor=COLOR_TRANSPARENT, enabled=True):

    imagebutton:
        style "character_button"
        idle character_sprite(character, expression)
        at character_button(xalign=xalign), tint(tintcolor)
        sensitive enabled
        action [Hide("death_body"), Jump(label)]
