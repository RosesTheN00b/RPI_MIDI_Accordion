import unittest
from unittest.mock import Mock

from main_loop import setup_board
from main_loop import setup_midi
from main_loop import play_note
from main_loop import release_note
from main_loop import destroy
from configuration import Configuration
from test.rpi.rpi import GPIO
from test.rpi.rpi import Board
from test.midi.synth import Synth


class TestMainLoop(unittest.TestCase):
    def test_setup_board(self):
        button_key = 0

        board = Board()
        gpio = GPIO()
        conf = Configuration(key_note_mapping={button_key: Mock()}, instrument='JR_analog.sf2')

        setup_board(board, gpio, conf)

        board.setmode.assert_called_with(gpio.BOARD)
        board.setup.assert_called_with(button_key, gpio.IN, pull_up_down=gpio.PUD_UP)

    def test_setup_midi(self):
        synth = Synth()
        instrument = 'JR_analog.sf2'
        conf = Configuration(key_note_mapping={}, instrument='JR_analog.sf2')

        setup_midi(synth, conf)

        synth.init.assert_called_with(instrument, 'alsa')

    def test_destroy(self):
        gpio = GPIO()

        destroy(gpio)

        gpio.cleanup.assert_called_with()

    def test_play_note(self):
        synth = Synth()
        note = Mock()
        note.__int__ = lambda x: 10
        conf = Configuration(key_note_mapping={}, instrument='JR_analog.sf2')

        play_note(note, conf, synth)

        synth.play_note.assert_called_with(note, conf.velocity)

    def test_release_note(self):
        synth = Synth()
        note = Mock()

        release_note(note, synth)

        synth.stop_note.assert_called_with(note)



if __name__ == '__main__':
    unittest.main()
