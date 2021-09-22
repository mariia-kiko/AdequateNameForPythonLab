import turtle
import math as m

def func(x,y): 
    return 2*x*m.sin(m.pi/y)

r=25
turtle.shape('turtle')
turtle.speed(150)
for el in range(10):
    n=el+3
    r=r+25
    turtle.penup()
    turtle.forward(25)
    turtle.pendown()
    turtle.right(90*(1-2/n))
    for ol in range(n):
        turtle.right(360/n)
        turtle.forward(func(r,n))
    turtle.left(90*(1-2/n))
    
turtle.done()