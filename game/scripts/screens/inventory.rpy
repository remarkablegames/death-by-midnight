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
            self.picked_up = []

        def add(self, item_id):
            if item_id not in self.picked_up:
                self.picked_up.append(item_id)
            item = INVENTORY_ITEMS.get(item_id)
            if item is not None and item not in self.items:
                self.items.append(item)

        def remove(self, item_id):
            self.items[:] = [item for item in self.items if item.item_id != item_id]

        def has(self, item_id):
            return any(item.item_id == item_id for item in self.items)

        def has_picked_up(self, item_id):
            return item_id in self.picked_up

        def given_to(self, character_id):
            return any(character == character_id for _, character in self.given)

        def get(self, item_id):
            return INVENTORY_ITEMS.get(item_id)

        def give(self, item_id, character_id):
            if not self.has(item_id):
                return
            self.given.append((item_id, character_id))
            self.remove(item_id)


    def inventory_read_cb(drag):
        return ("read", drag.drag_name)


    def inventory_drop_cb(drags, drop):
        if drop is None:
            drag = drags[0]
            drag.snap(drag.start_x, drag.start_y, delay=0.25)
            return None
        if drop.drag_name == "basement_door" and drags[0].drag_name != "basement_key":
            drag = drags[0]
            drag.snap(drag.start_x, drag.start_y, delay=0.25)
            renpy.notify("That won’t open the door")
            return None
        return ("give", drags[0].drag_name, drop.drag_name)


    def inventory_character_click_cb(drag):
        renpy.sound.play("ui/click_003.ogg")
        return ("character", drag.drag_name)


    def inventory_panel_height():
        item_rows = max(len(inventory.items), 1)
        return INVENTORY_SLOT_Y + item_rows * INVENTORY_SLOT_YSTEP - INVENTORY_PANEL_Y + 6


define INVENTORY_ITEMS = {
    "scroll": InventoryItem(
        "scroll",
        _("Scroll"),
        "images/items/scroll.webp",
        _("An aged parchment, creased from being tucked away in the rafters. In curling ink, it reads:\n\n“To whoever finds this: the will you seek is not the one they will read aloud. Follow the truth to whoever holds the real document.”"),
    ),

    "basement_key": InventoryItem(
        "basement_key",
        _("Key"),
        "images/items/key.webp",
        _("A silver key."),
    ),

    "kitchen_knife": InventoryItem(
        "kitchen_knife",
        _("Kitchen Knife"),
        "images/items/kitchen_knife.webp",
        _("An old kitchen knife that’s starting to rust."),
    ),

    "coffee": InventoryItem(
        "coffee",
        _("Coffee"),
        "images/items/coffee.webp",
        _("A half-finished cup of brew from the living room. It has a sweet and chemical taste."),
    ),

    "milk": InventoryItem(
        "milk",
        _("Milk"),
        "images/items/milk.webp",
        _("A carton of milk from the kitchen. It smells faintly sour."),
    ),

    "diary": InventoryItem(
        "diary",
        _("Diary"),
        "images/items/diary.webp",
        _("Someone’s journal, left behind by the pond."),
    ),

    "camera": InventoryItem(
        "camera",
        _("Camera"),
        "images/items/camera.webp",
        _("Contains pictures of the young Master. Looks like before he went bald, he had a full head of red hair."),
    ),

    "will": InventoryItem(
        "will",
        _("The True Will"),
        "images/items/will.webp",
        _("The Master’s real will, hidden where no one could read it until the truth came out. It names his true heir, and binds the night to repeat until the family’s history is confessed before the reading."),
    ),
}


define INVENTORY_PANEL_X = 1632
define INVENTORY_PANEL_Y = 12
define INVENTORY_PANEL_WIDTH = 272
define INVENTORY_PANEL_PAD = 12

define INVENTORY_SLOT_W = 248
define INVENTORY_SLOT_H = 60
define INVENTORY_SLOT_X = INVENTORY_PANEL_X + INVENTORY_PANEL_PAD
define INVENTORY_SLOT_Y = INVENTORY_PANEL_Y + 104
define INVENTORY_SLOT_YSTEP = 68


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

            text _("Click to read. Drag onto a character to hand it over."):
                style "inventory_hint"
                pos (INVENTORY_PANEL_X + INVENTORY_PANEL_PAD, INVENTORY_PANEL_Y + 50)
                xmaximum INVENTORY_PANEL_WIDTH - INVENTORY_PANEL_PAD

            for index, item in enumerate(inventory.items):

                frame:
                    style "inventory_slot"
                    pos (INVENTORY_SLOT_X, INVENTORY_SLOT_Y + index * INVENTORY_SLOT_YSTEP)
                    xysize (INVENTORY_SLOT_W, INVENTORY_SLOT_H)

    draggroup:

        for scene_character in scene_characters:
            drag:
                drag_name scene_character.character_id
                draggable False
                droppable True
                clicked inventory_character_click_cb
                hovered (lambda c_id=scene_character.character_id: character_hover_set(c_id))
                unhovered (lambda c_id=scene_character.character_id: character_hover_clear(c_id))
                xalign scene_character.xalign
                yalign 1.0

                add character_sprite(scene_character.character_id, scene_character.expression):
                    matrixcolor TintMatrix(scene_character.tint)
                    at (character_target_hover(scene_character.xalign) if character_hover_id == scene_character.character_id else character_target(scene_character.xalign))

        if door_drop_active:

            drag:
                drag_name "basement_door"
                draggable False
                droppable True
                focus_mask None
                xpos 736
                ypos 146
                xysize (312, 739)
                add Solid("#ffffff00")

        for index, item in enumerate(inventory.items):
            drag:
                drag_name item.item_id
                draggable True
                droppable False
                clicked inventory_read_cb
                dragged inventory_drop_cb

                pos (INVENTORY_SLOT_X, INVENTORY_SLOT_Y + index * INVENTORY_SLOT_YSTEP)

                add item.image:
                    fit "contain"
                    xysize (INVENTORY_SLOT_W, INVENTORY_SLOT_H)
                    align (0.5, 0.5)


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

                text (diary_description() if item.item_id == "diary" else item.description):
                    style "inventory_read_body"
                    xalign 0.5
                    xmaximum 620

                hbox:
                    xalign 0.5
                    spacing 40

                    textbutton _("Close") action Return("close")


label inventory_handle:

    python:
        inventory_result_action = _inventory_result[0]
        inventory_result_item = _inventory_result[1]
        _return = None

    if inventory_result_action == "read":

        $ _read_item = inventory.get(inventory_result_item)

        if _read_item is None:

            $ renpy.notify("That item is gone.")
            jump expression _inventory_return_label

        call screen inventory_read(_read_item)

        if _read_item.item_id == "camera":
            $ persistent.knows_red_hair = True

    elif inventory_result_action == "give":

        if _inventory_result[2] == "basement_door":
            jump basement_door_unlock
        else:
            call inventory_give_scene(inventory_result_item, _inventory_result[2])

    elif inventory_result_action == "character":

        $ character_result_info = character_info(inventory_result_item)

        if character_result_info is not None:
            call screen inventory_character_menu(character_result_info)

            if _return == "talk":
                call inventory_talk_scene(inventory_result_item)
            elif _return == "give":
                call screen inventory_choose_item(character_result_info)
                if _return is not None:
                    call inventory_give_scene(_return, inventory_result_item)

    jump expression _inventory_return_label


label inventory_give_scene(item_id, character_id):

    $ item = inventory.get(item_id)
    $ character = character_info(character_id)

    if item is None or character is None:
        return

    $ is_item_interactable = False

    hide screen inventory_hud

    $ inventory.give(item_id, character.character_id)
    $ renpy.notify(f"You gave {item.name} to {character.name}")

    call expression f"give_{item_id}_to_{character.character_id}"

    $ is_item_interactable = True

    return


style inventory_header is text_sans_serif:
    size 28
    bold True
    color COLOR_ACTION
    outlines [(1, COLOR_OUTLINE, 0, 0)]


style inventory_hint is text_sans_serif:
    size 14
    color "#ddd5c9"
    outlines [(1, COLOR_OUTLINE, 0, 0)]


style inventory_slot is inventory_hint:
    background Solid("#24160fcc")
    padding (6, 6, 6, 6)


style inventory_read_title is text_sans_serif:
    size 40
    color COLOR_ACTION
    outlines [(2, COLOR_OUTLINE, 0, 0)]


style inventory_read_body is text_sans_serif:
    size 22
    color "#f2ede2"
    outlines [(1, COLOR_OUTLINE, 0, 0)]
    line_spacing 4
