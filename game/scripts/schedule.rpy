init python:

    class SceneCharacter(object):

        def __init__(self, character_id, expression="smile", xalign=.5):
            self.character_id = character_id
            self.expression = expression
            self.xalign = xalign


    def set_scene_characters(room_id):

        store.current_room = room_id

        now = clock.minutes

        dead = dead_character()

        store.scene_characters = [
            SceneCharacter(character_id, expression, xalign)
            for character_id, expression, xalign, start, end, room in CHARACTER_SCHEDULE
            if room == room_id and start <= now < end and character_id != dead
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


define CHARACTER_SCHEDULE = [
    ("butler", "smile", .2, clock_time("18:00"), clock_time("19:00"), "interior_entrance"),
    ("butler", "smile", .7, clock_time("19:30"), clock_time("20:30"), "manor_door"),
    ("butler", "smile", .3, clock_time("20:30"), clock_time("24:00"), "living_room"),

    ("nurse", "smile", .2, clock_time("18:00"), clock_time("22:00"), "kitchen"),
    ("nurse", "smile", .3, clock_time("22:00"), clock_time("24:00"), "bedroom"),

    ("miss", "smile", .3, clock_time("18:00"), clock_time("19:00"), "living_room"),
    ("miss", "smile", .7, clock_time("19:00"), clock_time("20:30"), "kitchen"),
    ("miss", "smile", .7, clock_time("20:30"), clock_time("24:00"), "pond"),

    ("maid", "smile", .7, clock_time("18:00"), clock_time("18:30"), "hallway_left"),
    ("maid", "smile", .7, clock_time("18:30"), clock_time("19:00"), "kitchen"),
    ("maid", "smile", .5, clock_time("19:30"), clock_time("20:30"), "backyard"),
    ("maid", "smile", .7, clock_time("20:30"), clock_time("21:30"), "kitchen"),
    ("maid", "smile", .5, clock_time("21:30"), clock_time("22:00"), "hallway_right"),
    ("maid", "smile", .7, clock_time("22:00"), clock_time("24:00"), "bedroom"),
]


define ROOM_INTRO = {
    "butler": {
        "interior_entrance": _("The butler stands beside the staircase,{w=.2} watching the door as if he’s waiting for something."),
        "manor_door": _("You find the butler at the manor door,{w=.2} peering out at the grounds."),
        "living_room": _("The butler is in the living room,{w=.2} tidying up the furniture."),
    },

    "nurse": {
        "kitchen": _("You find someone at the kitchen counter,{w=.2} brewing a pot of coffee."),
        "bedroom": _("The nurse is in the bedroom,{w=.2} wiping away the dust."),
    },

    "miss": {
        "living_room": _("A young girl sits at the edge of the living room,{w=.2} waiting for time to pass."),
        "pond": _("The young miss stands by the pond,{w=.2} gazing at her own reflection."),
        "kitchen": _("You find the miss in the pantry,{w=.2} reaching for the milk."),
    },

    "maid": {
        "hallway_left": _("The maid is in the west hallway,{w=.2} carrying a stack of cups."),
        "backyard": _("You find the maid outside,{w=.2} sweeping the courtyard."),
        "kitchen": _("The maid is at the kitchen sink,{w=.2} washing a coffee cup."),
        "hallway_right": _("You pass the maid in the hall,{w=.2} on her way upstairs."),
        "bedroom": _("You find the maid in the bedroom,{w=.2} sorting the Master’s belongings into neat piles."),
    },
}
