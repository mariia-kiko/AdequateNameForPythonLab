import turtle

turtle.shape('turtle')
turtle.speed(15)
for el in range(12):
    turtle.forward(100)
    turtle.stamp()
    turtle.backward(100)
    turtle.right(30)

turtle.done()