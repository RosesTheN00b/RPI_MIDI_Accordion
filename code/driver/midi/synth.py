from mingus.midi import fluidsynth

class Synth:

    def __init__(self, channel):
        self.channel = channel

    def init(self, sound_font, sound_driver):
        return fluidsynth.init(sound_font, sound_driver)

    def stop_note(self, note):
        fluidsynth.stop_Note(note)

    def play_note(self, note, velocity):
        fluidsynth.play_Note(note, self.channel, velocity)

