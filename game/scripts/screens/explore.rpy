define EXPLORE_SCREENS = (
    "time_display",
    "inventory_hud",
    "arrow_button",
    "arrow_down_button",
    "arrow_left_button",
    "arrow_right_button",
    "arrow_up_button",
    "interactable_door",
    "item_key",
    "item_scroll",
    "item_will",
    "item_kitchen_knife",
    "item_camera",
    "item_coffee",
    "item_milk",
    "item_diary",
)

define TALK_VISIBLE_SCREENS = (
    "time_display",
)

define CHARACTER_MENU_VISIBLE_SCREENS = (
    "time_display",
    "inventory_hud",
)


init python:

    def hide_explore_screens(keep=()):
        for screen_name in EXPLORE_SCREENS:
            if screen_name not in keep:
                renpy.hide_screen(screen_name)
