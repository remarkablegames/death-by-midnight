init -100 python:

    def clock_time(time: str) -> int:
        hours, _, minutes = time.partition(":")
        return int(hours) * 60 + int(minutes)


init python:

    class Clock:

        MIDNIGHT_MINUTES = clock_time("24:00")
        TIME_NIGHT_LIGHT_START = clock_time("20:00")
        TIME_NIGHT_DARK_START = clock_time("22:00")
        START_MINUTES = clock_time("18:00")

        def __init__(self, minutes):
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
                if self.minutes < death["minutes"]:
                    continue
                if not death_is_pending(death):
                    continue
                if not store.pending_death:
                    store.pending_death = death["label"]
                    store.pending_hint = death["hint"]
                break

            if self.minutes >= self.MIDNIGHT_MINUTES:
                if store.pending_death:
                    renpy.jump("end_incomplete")
                renpy.jump("end")

        @property
        def display(self):
            total = self.minutes % (24 * 60)
            suffix = "PM" if total // 60 >= 12 else "AM"
            hour12 = (total // 60) % 12 or 12
            return "{}:{:02d} {}".format(hour12, total % 60, suffix)


default clock = Clock(Clock.START_MINUTES)


screen time_display():

    text clock.display:
        xpos 24
        ypos 14
        style "clock_text"


style clock_text is text_sans_serif:
    size 36
    color COLOR_ACTION
    outlines [(2, COLOR_OUTLINE, 0, 0)]
