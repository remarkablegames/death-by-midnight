default clock_minutes = 18 * 60

define MIDNIGHT_MINUTES = 24 * 60


init python:

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
    color "#f2c14e"
    outlines [(2, "#160b08cc", 0, 0)]
