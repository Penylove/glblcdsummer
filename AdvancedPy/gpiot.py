import requests
from gpiozero import LED
from time import sleep

red = LED(27)
yellow = LED(18)
green = LED(17)

url = "https://maker.ifttt.com/trigger/riz/with/key/bImrrVn3Rj0hjm3mZxaJL3nD1tRDsq-6jX90oE4DoJN"
r = requests.get(url)

c = r.status_code
print(c)

red.on()
yellow.on()
green.on()
