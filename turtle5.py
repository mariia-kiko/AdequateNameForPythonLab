import turtle

turtle.shape('turtle')
turtle.speed(15)
for el in range(11):
    turtle.penup()
    turtle.backward(7)
    turtle.left(90)
    turtle.forward(7)
    turtle.right(90)
    turtle.pendown()
    for ol in range(4):
        turtle.forward(14*el)
        turtle.right(90)
        
turtle.done()

