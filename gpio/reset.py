from gpiozero import LED, Button
from signal import pause

from subprocess import call
led = LED(18)
button = Button(2)

def print_thing():
    print ("button pressed")

button.when_pressed = print_thing