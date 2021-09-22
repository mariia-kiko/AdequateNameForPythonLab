import turtle

def func(x):
    for el in range(x):
        turtle.right(180*(1-1/x))
        turtle.forward(150)

turtle.shape('turtle')
turtle.speed(150)
func(5)
turtle.penup()
turtle.forward(200)
turtle.pendown()
func(11)

turtle.done()