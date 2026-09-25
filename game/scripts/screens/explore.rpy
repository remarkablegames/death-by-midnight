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


init python:

    def hide_explore_screens():
        for screen_name in store.EXPLORE_SCREENS:
            renpy.hide_screen(screen_name)
