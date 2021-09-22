import turtle

def func(): 
    for el in range(360):
        turtle.forward(1.5)
        turtle.right(1)

turtle.shape('turtle')
turtle.speed(0)
for ol in range(6):
    func()
    turtle.right(180)
    func()
    turtle.right(30)
    
turtle.done()