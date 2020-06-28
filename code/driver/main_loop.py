
from mingus.midi import fluidsynth
from mingus.containers import *

from configuration import initial_configuration

VELOCITY = 127
channel = 8

def setup_board(board, gpio, conf):
    print('Programm is starting')
    board.setmode(gpio.BOARD)
    '''
    todo: remove button pin var with configuration
    '''
    for button_pin in conf.keys:
        board.setup(button_pin, gpio.IN, gpio.PUD_UP)

def setup_midi(synth, configuration):
    if not synth.init(configuration.instrument, 'alsa'):
        print("Couldn't load soundfont", configuration.instrument)
        sys.exit(1)
    print('Sound font loaded and initialized with alsa')


def release_note(note, synth):
   print('release', note)
   synth.stop_note(note)



def play_note(note, conf, synth):
    print('play', note, int(note))
    synth.play_note(note, conf.velocity)


def update_key(current_key, is_down, key_note_mapping, conf, gpio, synth):
    if gpio.input(current_key) == GPIO.LOW:
        if is_down[current_key]:
            '''
            Key already pressed 
            '''
            return

        play_note(key_note_mapping[current_key], conf, synth)
        print('\t switch to on ', note)
        is_down[current_key] = True
    else:
        if not is_down[current_key]:
            '''
            key already released
            '''
            return
        release_note(key_note_mapping[current_key], synth)
        print('\t switched to off')
        is_down[current_key] = False


def loop(gpio, conf, synth):
    while True:
        for current_note in conf.keys:
            update_key(current_note, conf.is_down, conf.key_note_mapping, conf, gpio, synth)


def destroy(gpio):
    gpio.cleanup()


if __name__ == '__main__':
    from rpi.rpi import Board
    from rpi.rpi import GPIO
    from midi.synth import Synth

    configuration = initial_configuration()

    board = Board()
    gpio = GPIO()
    synth = Synth(channel)

    setup_board(board, gpio, configuration)
    setup_midi(synth, configuration)
    try:
        loop(gpio, configuration, synth)
    except KeyboardInterrupt:
        print('stopping')
        destroy(gpio)
