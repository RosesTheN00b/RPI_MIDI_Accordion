
import RPi.GPIO as origGPIO

class Board:

    def setmode(self, mode):
        origGPIO.setmode(mode)

    def setup(self, pin, mode):
        origGPIO.setup(pin, mode)

    def setup(self, pin, mode, pull_down_mode):
        origGPIO.setup(pin, mode, pull_up_down=pull_down_mode)


class GPIO:
    BOARD = origGPIO.BOARD

    IN = origGPIO.IN
    OUT = origGPIO.OUT

    HIGH = origGPIO.HIGH
    LOW = origGPIO.LOW

    PUD_UP = origGPIO.PUD_UP

    def input(self, pin):
        return origGPIO.input(pin)

    def output(selfs, pin, output):
        return origGPIO.output(pin, output)

    def cleanup(self):
        GPIO.cleanup()
