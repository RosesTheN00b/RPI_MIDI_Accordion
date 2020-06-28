from mingus.containers import *


def initial_configuration():
    return Configuration(key_note_mapping={12: Note('C', 4)}, instrument="JR_analog.sf2")


class Configuration:
    def __init__(self, key_note_mapping, instrument, channel=8, velocity=127):
        self.instrument = instrument

        self.keys = key_note_mapping.keys()
        '''
        replace dict init
        '''
        self.is_down = {}
        for key in self.keys:
            self.is_down[key] = False

        self.key_note_mapping = key_note_mapping
        self.channel = channel
        self.velocity = velocity

        print('-------------------------------')
        print('-------------------------------')
        print('initializing configuration with the following values:')
        print(' -> instrument:', instrument)
        print(' -> channel:', channel)
        print(' -> velocity', velocity)
        print(' -> key_note_mapping', key_note_mapping)
        print(' - - - - - computed:')
        print(' -> is_down', self.is_down)
        print(' -> keys:', self.keys)
        print('-------------------------------')
        print('-------------------------------')
