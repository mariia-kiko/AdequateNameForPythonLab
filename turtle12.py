import turtle

def func(x): 
    for el in range(180):
        turtle.forward(x)
        turtle.right(1)

turtle.shape('turtle')
turtle.speed(0)
turtle.left(90)
for ol in range(3):
    func(1.5)
    func(0.3)
    
turtle.done()