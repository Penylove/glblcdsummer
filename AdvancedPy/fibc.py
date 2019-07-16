def fibonacci(n):
    if n==0:
        return 0
    if n == 1:
         return 1
    elif n >= 2:
        return fibonacci(n-1)+fibonacci(n-2)
    
import turtle
import math

pr = turtle.Turtle()

def star(n):
    while n>=0:
        #works without the loop
        pr.forward(n*2)
        pr.left(216)
        star(n-5)

def drawsomething(j):
    pr.forward(100)
    while True:
        pr.forwarddd(j)
        pr.left(216)
        #pr.forward(j-(j*0.1))
        drawsomething(j-(j*0.1))
        pr.forward(100)
        drawsomething(j)
drawsomething(100)
    
pr.done


        