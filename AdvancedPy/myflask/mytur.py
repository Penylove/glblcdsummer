import turtle
import math
t = turtle.Turtle()
def star(turtle,size):
    if(size <=10):
        return
    else:
        for i in range(1,size):
            turtle.forward(size)
            star(turtle,int(size/2))
            turtle.left(216)
# star(t,150)
for i  in range(1,10000):
    t.forward(i)
    t.left(216)