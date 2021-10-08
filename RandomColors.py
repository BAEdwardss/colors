##Initialize

import turtle
import random
t=turtle.Turtle()
t.speed(9999)
turtle.colormode(255)
r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
size=random.randint(10,150)
xran=random.randint(-500,500)
yran=random.randint(-500,500)

##Function

def randomDot():
    t.color(r, g, b)
    t.begin_fill()
    t.circle(size)
    t.end_fill()

##Main
    
for i in range(100):
    t.penup()
    t.goto(xran, yran)
    t.pendown()
    randomDot()
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    size=random.randint(10,150)
    xran=random.randint(-500,500)
    yran=random.randint(-500,500)

    
