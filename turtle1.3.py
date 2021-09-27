import math as m
import turtle as t
t.shape('circle')
dt = 0.1
time = 1000
g = -9.81
t.penup()
t.speed(150)
particlesYvelocity = 90
particlesXvelocity = 10
particlesXcoordinate = -200
particlesYcoordinate = 0
t.goto(particlesXcoordinate, particlesYcoordinate)
t.pendown()
for ul in range(time):
    if particlesYcoordinate<0.05:
        particlesYvelocity = 0.9*m.fabs(particlesYvelocity)
        print('ownego')
    else:
        particlesYvelocity = particlesYvelocity+0
    particlesYvelocity = particlesYvelocity + g*dt
    particlesXcoordinate = particlesXcoordinate + particlesXvelocity*dt
    particlesYcoordinate = particlesYcoordinate + particlesYvelocity*dt
    t.goto(particlesXcoordinate, particlesYcoordinate)
