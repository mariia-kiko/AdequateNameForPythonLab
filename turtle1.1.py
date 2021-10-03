import turtle
from random import *

turtle.shape('turtle')
turtle.speed(150)
for el in range(200):
    turtle.right(randint(0,360))
    turtle.forward(randint(0,50))

turtle.done()