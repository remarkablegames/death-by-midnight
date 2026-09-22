default clock_minutes = 18 * 60 # 6pm

define MIDNIGHT_MINUTES = 24 * 60 # 12pm
define TIME_NIGHT_LIGHT_START = 20 * 60 # 8pm
define TIME_NIGHT_DARK_START = 22 * 60 # 10pm


init python:

    def is_night_light():
        return clock_minutes >= TIME_NIGHT_LIGHT_START

    def is_night_dark():
        return clock_minutes >= TIME_NIGHT_DARK_START

    def advance_clock(minutes=0):
        global clock_minutes
        if minutes <= 0:
            return
        clock_minutes = max(0, clock_minutes + minutes)
        if clock_minutes >= MIDNIGHT_MINUTES:
            renpy.jump("end")

    def clock_string():
        total = clock_minutes % (24 * 60)
        suffix = "PM" if total // 60 >= 12 else "AM"
        hour12 = (total // 60) % 12 or 12
        return "{}:{:02d} {}".format(hour12, total % 60, suffix)


screen time_display():

    text clock_string():
        xpos 24
        ypos 14
        style "clock_text"


style clock_text:
    font "DejaVuSans.ttf"
    size 36
    color COLOR_ACTION
    outlines [(2, COLOR_OUTLINE, 0, 0)]
