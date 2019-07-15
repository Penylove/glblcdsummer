from gpiozero import LED
from time import sleep

led = LED(18)


name = input("Enter your name: ")

def dot():
    led.on()
    sleep(1)
    
def dot_gap():
    led.on()
    sleep(1)
    gap()
    
    
def dash_gap():
    led.on()
    sleep(2)
    gap()
    
def dash():
    led.on()
    sleep(2)
    gap()
    
def gap():
    led.off()
    sleep(1)
    
def space():
    led.off()
    sleep(4)
def wait():
    led.off()
    sleep(2)
for i in name:
    if i is 'A':
        dot_gap()
        dash()
        wait()
    if i is 'B':
       dash_gap()
       dot_gap()
       dot_gap()
       dot()
       wait()
       
    if i is 'C':
       dash_gap()
       dot_gap()
       dash_gap()
       dot()
       wait()
    if i is 'D':
        dash_gap()
        dot_gap()
        dot()
        wait()        
    if i is 'E':
        dot()
        wait()
        
    if i is 'F':
        dot_gap()
        dot_gap()
        dash_gap()
        dot()
        wait()
    
    if i is 'G':
        dash_gap()
        dash_gap()
        dot()
        wait()
    
    if i is 'H':
        dot_gap()
        dot_gap()
        dot_gap()
        dot()
        wait()
        
    if i is 'I':
        dot_gap()
        dot()
        wait()
        
    if i is 'J':
        dot_gap()
        dash_gap()
        dash_gap()
        dash()
        wait()
    
    if i is 'K':
        dash_gap()
        dot_gap()
        dash()
        wait()
        
    if i is 'L':
        dot_gap()
        dash_gap()
        dot_gap()
        dot()
        wait()
    
    if i is 'M':
        dash_gap()
        dash()
        wait()
        
    if i is 'N':
        dash_gap()
        dot()
        wait()
        
    if i is 'O':
        dash_gap()
        dash_gap()
        dash()
        wait()
        
    if i is 'P':
        dot_gap()
        dash_gap()
        dash_gap()
        dot()
        wait()
    if i is 'Q':
        dash_gap()
        dash_gap()
        dot_gap()
        dash()
        wait()
        
    if i is 'R':
        dot_gap()
        dash_gap()
        dot()
        wait()
    if i is 'S':
        dot_gap()
        dot_gap()
        dot_gap()
        dot()
        wait()
    if i is 'T':
        dash()
        wait()
        
    if i is 'U':
        dot_gap()
        dot_gap()
        dash()
        wait()
        
    if i is 'V':
        dot_gap()
        dot_gap()
        dot_gap()
        dash()
        wait()
        
    if i is 'W':
        dot_gap()
        dash_gap()
        dash()
        wait()
        
        
    if i is 'X':
        dash_gap()
        dot_gap()
        dot_gap()
        dash()
        
    if i is 'Y':
        dash_gap()
        dot_gap()
        dash_gap()
        dash()
        wait()
        
    if i is 'Z':
        dash_gap()
        dash_gap()
        dot()
        wait()
        
        
    if i is " ":
        space()
   