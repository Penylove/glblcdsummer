from gpiozero import LED
from time import sleep

red = LED(27)
yellow = LED(18)
green = LED(17)

while True:
    red.on()
    print("red : on")
    sleep(5)
    red.off()
    print("red : off")
    yellow.on()
    print("yellow : on")
    sleep(2)
    yellow.off()
    print("yellow : off")
    green.on()
    print("green : on")
    sleep(6)
    green.off()
    print("green : off")
    yellow.on()
    print("yellow : on")
    sleep(2)
    yellow.off()
    print("yellow : off")

