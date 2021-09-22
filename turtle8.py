import turtle
import math as m

def func(x):
    return m.sqrt(1+x**2)*10

turtle.shape('turtle')
turtle.speed(150)
for el in range(50):
    turtle.right(90)
    turtle.forward(func(el))

turtle.done()