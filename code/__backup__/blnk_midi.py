import RPi.GPIO as GPIO
from mingus.midi import fluidsynth
from mingus.containers import *

led_pin = 11
button_pin = 12

VELOCITY = 127
channel = 8
SF2 = "JR_analog.sf2"

def setup():
    print('Programm is starting')
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    if not fluidsynth.init(SF2, 'alsa'):
        print("Couldn't load soundfont", SF2)
        sys.exit(1)




def release_note(note):
   print('release', note)
   fluidsynth.stop_Note(note, channel)



def play_note(note):
    print('play', note, int(note))
    fluidsynth.play_Note(note, channel, VELOCITY)



def loop():

    is_down = True



    note = 0
    while True:
        if GPIO.input(button_pin) == GPIO.LOW:
            GPIO.output(led_pin, GPIO.HIGH)
            if is_down:
                continue

            note = note +1
            play_note(Note("C", 4))
            print('\t switch to on ', note)
            is_down = True
        else:
            GPIO.output(led_pin, GPIO.LOW)
            #print('\t led down')

            if not is_down:
                continue
            release_note(Note("C", 4))
            print('\t switched to off')
            is_down = False

def destroy():
    GPIO.output(led_pin, GPIO.LOW)
    GPIO.cleanup()


if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        print('stopping')
        destroy()
