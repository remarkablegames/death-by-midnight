init python:

    def character_schedule_band():
        if store.clock.is_night_dark:
            return "night_dark"
        if store.clock.is_night_light:
            return "night_light"
        return "evening"

    def set_scene_characters(room_id):

        store.current_room = room_id

        band = character_schedule_band()
        entry = CHARACTER_SCHEDULE.get(room_id, {}).get(band, [])

        tint = "#333" if store.clock.is_night_dark else "#ffffff00"

        store.scene_characters = [
            SceneCharacter(character_id, expression=expression, xalign=xalign, tint=tint)
            for character_id, expression, xalign in entry
        ]

    def room_intro(character_id):

        line = ROOM_INTRO.get(character_id, {}).get(store.current_room)

        if line is None:
            return None

        key = (character_id, store.current_room)

        if key in store.room_intros_seen:
            return None

        store.room_intros_seen.add(key)

        return line


define CHARACTER_SCHEDULE = {
    "interior_entrance": {
        "evening": [("butler", "smile", .2)],
    },
    "manor_door": {
        "night_light": [("butler", "neutral", .2)],
    },
    "living_room": {
        "evening": [("miss", "neutral", .3), ("maid", "neutral", .7)],
        "night_dark": [("butler", "neutral", .3)],
    },
    "kitchen": {
        "evening": [("nurse", "neutral", .2)],
        "night_light": [("nurse", "neutral", .2)],
        "night_dark": [("miss", "neutral", .2)],
    },
    "bedroom": {
        "night_dark": [("nurse", "neutral", .3), ("maid", "neutral", .7)],
    },
    "pond": {
        "night_light": [("miss", "neutral", .7)],
    },
    "hallway_right": {
        "night_light": [("maid", "neutral", .5)],
    },
}


define ROOM_INTRO = {
    "butler": {
        "interior_entrance": _("The butler stands just inside the hall, watching the door as if the night owes him something."),
        "manor_door": _("You find the butler at the manor door, peering out at the grounds."),
        "living_room": _("The butler is in the living room, straightening chairs that were already straight."),
    },
    "nurse": {
        "kitchen": _("Nora is at the kitchen counter, wiping it dry with a folded cloth."),
        "bedroom": _("You find Nora in the bedroom, still as a sentinel over the Master’s things."),
    },
    "miss": {
        "living_room": _("Mia sits at the edge of the living room, folding and refolding her hands."),
        "pond": _("Mia is by the pond, gazing in at her own reflection."),
        "kitchen": _("Mia stands at the pantry, caught — reaching for the milk."),
    },
    "maid": {
        "living_room": _("Madelyn moves through the living room, clearing away the evening’s cups."),
        "hallway_right": _("You meet Madelyn in the hall, arms full of pressed linen."),
        "bedroom": _("Madelyn is in the bedroom, sorting the Master’s effects into careful piles."),
    },
}
