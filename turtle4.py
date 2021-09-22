import turtle

def func(x): 
    for el in range(360):
        turtle.forward(x)
        turtle.right(1)

turtle.shape('turtle')
turtle.speed(0)

func(2)
    
turtle.done()