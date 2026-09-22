init python:

    class InventoryItem(object):

        def __init__(self, item_id, name, image, description):
            self.item_id = item_id
            self.name = name
            self.image = image
            self.description = description

        def __eq__(self, other):
            return isinstance(other, InventoryItem) and other.item_id == self.item_id

        def __hash__(self):
            return hash(self.item_id)


    class Inventory(object):

        def __init__(self):
            self.items = []
            self.given = []

        def add(self, item_id):
            item = INVENTORY_ITEMS.get(item_id)
            if item is not None and item not in self.items:
                self.items.append(item)

        def remove(self, item_id):
            self.items[:] = [item for item in self.items if item.item_id != item_id]

        def has(self, item_id):
            return any(item.item_id == item_id for item in self.items)

        def get(self, item_id):
            return INVENTORY_ITEMS.get(item_id)

        def give(self, item_id, character_id):
            if not self.has(item_id):
                return
            self.given.append((item_id, character_id))
            self.remove(item_id)


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


    def inventory_read_cb(drag):
        return ("read", drag.drag_name)


    def inventory_drop_cb(drags, drop):
        if drop is None:
            drag = drags[0]
            drag.snap(drag.start_x, drag.start_y, delay=0.25)
            return None
        return ("give", drags[0].drag_name, drop.drag_name)


    def inventory_noop_cb(drag):
        return None


    def inventory_panel_height():
        item_rows = max(len(inventory.items), 1)
        return INVENTORY_SLOT_Y + item_rows * INVENTORY_SLOT_YSTEP + 2 * INVENTORY_CHAR_YSTEP - INVENTORY_PANEL_Y + 6


define INVENTORY_ITEMS = {
    "scroll": InventoryItem(
        "scroll",
        _("Scroll"),
        "images/items/scroll.webp",
        _("An aged parchment, creased from being tucked away in the rafters. In curling ink, it reads:\n\n“To whoever finds this: the will you seek is not the one they will read aloud. Follow the truth to whoever holds the real document.”"),
    ),
}


define CHARACTER_ROSTER = [
    CharacterInfo("butler", _("Butler Ben"), "butler neutral"),
    CharacterInfo("maid", _("Maid Madelyn"), "maid neutral"),
    CharacterInfo("miss", _("Miss Mia"), "miss neutral"),
    CharacterInfo("nurse", _("Nurse Nora"), "nurse neutral"),
]


define GIVE_LINES = {
    ("scroll", "butler"): _("The will? I’ll take a look, though it smells of the attic."),
    ("scroll", "maid"): _("This is the Owner’s handwriting... I’ve seen it on his private notes."),
    ("scroll", "miss"): _("His seal... He never let anyone touch his papers, not even Mother."),
    ("scroll", "nurse"): _("Where did you find this? Careful, detective. Not in front of the others."),
}

define GIVE_LINE_FALLBACK = _("I’ll keep that safe for now.")


define INVENTORY_PANEL_X = 1632
define INVENTORY_PANEL_Y = 12
define INVENTORY_PANEL_WIDTH = 272
define INVENTORY_PANEL_PAD = 12

define INVENTORY_SLOT_W = 248
define INVENTORY_SLOT_H = 60
define INVENTORY_SLOT_X = INVENTORY_PANEL_X + INVENTORY_PANEL_PAD
define INVENTORY_SLOT_Y = INVENTORY_PANEL_Y + 82
define INVENTORY_SLOT_YSTEP = 68

define INVENTORY_CHAR_W = 124
define INVENTORY_CHAR_H = 148
define INVENTORY_CHAR_X1 = INVENTORY_PANEL_X + INVENTORY_PANEL_PAD
define INVENTORY_CHAR_X2 = INVENTORY_CHAR_X1 + INVENTORY_CHAR_W + 8
define INVENTORY_CHAR_Y0 = INVENTORY_SLOT_Y + 2 * INVENTORY_SLOT_YSTEP + 4
define INVENTORY_CHAR_YSTEP = INVENTORY_CHAR_H + 10


default inventory = Inventory()


screen inventory_hud():

    zorder 110

    if inventory.items:

        fixed:

            add Solid("#160b08b8") xpos INVENTORY_PANEL_X ypos INVENTORY_PANEL_Y xysize (INVENTORY_PANEL_WIDTH, inventory_panel_height())
            add Solid(COLOR_ACTION) xpos INVENTORY_PANEL_X ypos INVENTORY_PANEL_Y xysize (INVENTORY_PANEL_WIDTH, 4)

            text _("Inventory"):
                style "inventory_header"
                pos (INVENTORY_PANEL_X + INVENTORY_PANEL_PAD, INVENTORY_PANEL_Y + 16)

            text _("Click to read. Drag onto a portrait to hand it over."):
                style "inventory_hint"
                pos (INVENTORY_PANEL_X + INVENTORY_PANEL_PAD, INVENTORY_PANEL_Y + 50)
                xmaximum INVENTORY_PANEL_WIDTH - INVENTORY_PANEL_PAD

            draggroup:

                for index, item in enumerate(inventory.items):
                    drag:
                        drag_name item.item_id
                        draggable True
                        droppable False
                        clicked inventory_read_cb
                        dragged inventory_drop_cb

                        pos (INVENTORY_SLOT_X, INVENTORY_SLOT_Y + index * INVENTORY_SLOT_YSTEP)

                        frame:
                            style "inventory_slot"
                            xysize (INVENTORY_SLOT_W, INVENTORY_SLOT_H)
                            add item.image:
                                fit "contain"
                                xysize (INVENTORY_SLOT_W - 16, INVENTORY_SLOT_H - 16)
                                align (0.5, 0.5)

                for index, character in enumerate(CHARACTER_ROSTER):
                    drag:
                        drag_name character.character_id
                        draggable False
                        droppable True
                        clicked inventory_noop_cb

                        pos ((INVENTORY_CHAR_X1 if index % 2 == 0 else INVENTORY_CHAR_X2), (INVENTORY_CHAR_Y0 + (index // 2) * INVENTORY_CHAR_YSTEP))

                        frame:
                            style "inventory_character_slot"
                            xysize (INVENTORY_CHAR_W, INVENTORY_CHAR_H)

                            vbox:
                                spacing 4

                                add character.image:
                                    fit "contain"
                                    xysize (INVENTORY_CHAR_W - 10, INVENTORY_CHAR_H - 30)
                                    align (0.5, 0.5)

                                text character.name:
                                    style "inventory_character_name"
                                    align (0.5, 1.0)


screen inventory_read(item):

    modal True
    zorder 300

    frame:
        align (0.5, 0.5)
        padding (4, 4, 4, 4)
        background Solid(COLOR_ACTION)

        frame:
            padding (34, 30, 34, 30)
            xmaximum 780
            background Solid("#160b08")

            vbox:
                xalign 0.5
                spacing 22

                text item.name:
                    style "inventory_read_title"
                    xalign 0.5

                add item.image:
                    fit "contain"
                    xysize (600, 160)
                    align (0.5, 0.5)

                text item.description:
                    style "inventory_read_body"
                    xalign 0.5
                    xmaximum 620

                hbox:
                    xalign 0.5
                    spacing 40

                    textbutton _("Give to a Character") action Return("give")
                    textbutton _("Close") action Return("close")


screen inventory_give_choose(item):

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

                text _("Give the [item.name] to:"):
                    style "inventory_read_title"
                    align (0.5, 0.5)

                for character in CHARACTER_ROSTER:
                    textbutton character.name action Return(character.character_id)

                textbutton _("Nevermind") action Return(None)


label inventory_handle:

    python:
        inventory_result_action = _inventory_result[0]
        inventory_result_item = _inventory_result[1]
        _return = None

    if inventory_result_action == "read":

        call screen inventory_read(inventory.get(inventory_result_item))

        if _return == "give":
            call screen inventory_give_choose(inventory.get(inventory_result_item))
            if _return is not None:
                call inventory_give_scene(inventory_result_item, _return)

    elif inventory_result_action == "give":

        call inventory_give_scene(inventory_result_item, _inventory_result[2])

    jump expression _inventory_return_label


label inventory_give_scene(item_id, character_id):

    $ item = inventory.get(item_id)
    $ character = character_info(character_id)

    if character is None:

        python:
            with open("game/inventory_diag.log", "a") as diag_file:
                diag_file.write("give_scene received character_id=%r item_id=%r\n" % (character_id, item_id))

        $ renpy.notify("Could not hand over that character.")
        return

    $ response_line = GIVE_LINES.get((item_id, character.character_id), GIVE_LINE_FALLBACK)

    $ renpy.show(character.image, tag=character.character_id, at_list=[character_speak])
    with dissolve

    player "Here, take the [item.name]. I think you should see it."

    python:
        character_object(character.character_id)(response_line)
        inventory.give(item_id, character.character_id)
        renpy.notify(f"You gave the {item.name} to {character.name}.")

    $ renpy.hide(character.character_id)
    with dissolve

    return


style inventory_header:
    font "DejaVuSans.ttf"
    size 28
    bold True
    color COLOR_ACTION
    outlines [(1, COLOR_OUTLINE, 0, 0)]


style inventory_hint:
    font "DejaVuSans.ttf"
    size 14
    color "#ddd5c9"
    outlines [(1, COLOR_OUTLINE, 0, 0)]


style inventory_slot is inventory_hint:
    background Solid("#24160fcc")
    padding (6, 6, 6, 6)


style inventory_character_slot is inventory_slot:
    padding (4, 4, 4, 4)


style inventory_character_name:
    font "DejaVuSans.ttf"
    size 13
    color COLOR_ACTION
    outlines [(1, COLOR_OUTLINE, 0, 0)]


style inventory_read_title:
    font "DejaVuSans.ttf"
    size 40
    color COLOR_ACTION
    outlines [(2, COLOR_OUTLINE, 0, 0)]


style inventory_read_body:
    font "DejaVuSans.ttf"
    size 22
    color "#f2ede2"
    outlines [(1, COLOR_OUTLINE, 0, 0)]
    line_spacing 4
