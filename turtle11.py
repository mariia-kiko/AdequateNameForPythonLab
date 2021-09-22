import turtle

def func(x): 
    for el in range(360):
        turtle.forward(x)
        turtle.right(1)

turtle.shape('turtle')
turtle.speed(0)
d=0
turtle.right(90)
for ol in range(6):
    d=d+0.5
    func(d)
    turtle.right(180)
    func(d)
    
turtle.done()