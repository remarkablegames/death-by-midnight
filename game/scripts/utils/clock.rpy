init python:

    class Clock:

        MIDNIGHT_MINUTES = 24 * 60 # 12am
        TIME_NIGHT_LIGHT_START = 20 * 60 # 8pm
        TIME_NIGHT_DARK_START = 22 * 60 # 10pm

        def __init__(self, minutes=18 * 60): # 6pm
            self.minutes = minutes

        @property
        def is_night_light(self):
            return self.minutes >= self.TIME_NIGHT_LIGHT_START

        @property
        def is_night_dark(self):
            return self.minutes >= self.TIME_NIGHT_DARK_START

        def advance(self, minutes=0):
            if minutes <= 0:
                return
            self.minutes = max(0, self.minutes + minutes)
            for death in DEATH_HOURS:
                if self.minutes >= death["minutes"] and death_is_pending(death):
                    renpy.jump(death["label"])
            if self.minutes >= self.MIDNIGHT_MINUTES:
                renpy.jump("loop_restart")

        @property
        def display(self):
            total = self.minutes % (24 * 60)
            suffix = "PM" if total // 60 >= 12 else "AM"
            hour12 = (total // 60) % 12 or 12
            return "{}:{:02d} {}".format(hour12, total % 60, suffix)


default clock = Clock()


screen time_display():

    text clock.display:
        xpos 24
        ypos 14
        style "clock_text"


style clock_text is text_sans_serif:
    size 36
    color COLOR_ACTION
    outlines [(2, COLOR_OUTLINE, 0, 0)]
