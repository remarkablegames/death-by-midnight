init python:
    BLEEP_CHANNEL = "bleep"
    renpy.music.register_channel(BLEEP_CHANNEL, mixer="voice", loop=True)


    def make_voice(filename):
        def callback(event, **kwargs):
            if event == "show_done":
                renpy.music.play(f"voice/{filename}.ogg", channel=BLEEP_CHANNEL, relative_volume=2)

            elif event in ("slow_done", "end"):
                renpy.music.stop(channel=BLEEP_CHANNEL, fadeout=.2)

        return callback


    def dismiss_callback() -> bool:
        renpy.sound.play("ui/click.ogg")
        return True


    config.say_allow_dismiss = dismiss_callback


define butler = Character("Butler Ben", callback=make_voice("bleep008"), image="butler")
define maid = Character("Maid Madelyn", callback=make_voice("bleep021"), image="maid")
define miss = Character("Miss Mia", callback=make_voice("bleep024"), image="miss")
define narrator = Character(None, callback=make_voice("bleep001"))
define nurse = Character("Nurse Nora", callback=make_voice("bleep023"), image="nurse")
define player = Character("Detective [player_name]", callback=make_voice("bleep030"))
