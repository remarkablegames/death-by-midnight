init python:

    class SceneCharacter(object):

        def __init__(self, character_id, expression="smile", xalign=.5, tint="#ffffff00"):
            self.character_id = character_id
            self.expression = expression
            self.xalign = xalign
            self.tint = tint


    def character_schedule_band():
        if clock.is_night_dark:
            return "night_dark"
        if clock.is_night_light:
            return "night_light"
        return "evening"

    def set_scene_characters(room_id):

        store.current_room = room_id

        band = character_schedule_band()
        entry = CHARACTER_SCHEDULE.get(room_id, {}).get(band, [])

        tint = "#333" if clock.is_night_dark else "#ffffff00"

        store.scene_characters = [
            SceneCharacter(character_id, expression=expression, xalign=xalign, tint=tint)
            for character_id, expression, xalign in entry
        ]

    def room_intro(character_id):

        line = ROOM_INTRO.get(character_id, {}).get(current_room)

        if line is None:
            return None

        key = (character_id, current_room)

        if key in room_intros_seen:
            return None

        room_intros_seen.add(key)

        return line


define CHARACTER_SCHEDULE = {
    "interior_entrance": {
        "evening": [("butler", "smile", .2)],
    },
    "manor_door": {
        "night_light": [("butler", "smile", .2)],
    },
    "living_room": {
        "evening": [("miss", "smile", .3), ("maid", "smile", .7)],
        "night_dark": [("butler", "smile", .3)],
    },
    "kitchen": {
        "evening": [("nurse", "smile", .2)],
        "night_light": [("nurse", "smile", .2)],
        "night_dark": [("miss", "smile", .2)],
    },
    "bedroom": {
        "night_dark": [("nurse", "smile", .3), ("maid", "smile", .7)],
    },
    "pond": {
        "night_light": [("miss", "smile", .7)],
    },
    "hallway_right": {
        "night_light": [("maid", "smile", .5)],
    },
}


define ROOM_INTRO = {
    "butler": {
        "interior_entrance": _("The butler stands just inside the hall,{w=.1} watching the door as if waiting for something."),
        "manor_door": _("You find the butler at the manor door,{w=.1} peering out at the grounds."),
        "living_room": _("The butler is in the living room,{w=.1} tidying up around the pool table."),
    },

    "nurse": {
        "kitchen": _("You find someone at the kitchen counter,{w=.1} brewing a pot of coffee."),
        "bedroom": _("The nurse is in the bedroom,{w=.1} wiping away the dust."),
    },

    "miss": {
        "living_room": _("A young girl sits at the edge of the living room,{w=.1} waiting for time to pass."),
        "pond": _("The young miss stands by the pond,{w=.1} gazing at her own reflection."),
        "kitchen": _("You find the miss in the pantry,{w=.1} reaching for the milk."),
    },

    "maid": {
        "living_room": _("The maid moves through the room,{w=.1} collecting everyone’s cups."),
        "hallway_right": _("You encounter the maid in the hallway."),
        "bedroom": _("You find the maid in the bedroom,{w=.1} sorting the Master’s belongings into neat piles."),
    },
}
