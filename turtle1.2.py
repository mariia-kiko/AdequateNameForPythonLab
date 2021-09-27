import turtle as t
import math
from random import *

c=20 

def f0():
    coords = [(c, 90), (2*c, 90), (c, 90), (2*c, 90), (2*c, 0)]
    for el in coords:
        if coords.index(el)==4:
            t.penup()
        else:
            t.pendown()
        step, angle = el
        t.forward(step)
        t.right(angle)
        t.pendown()
def f1():
    coords = [(0, 90), (c, 225), (math.sqrt(2)*c, 135), (2*c, 180), (2*c, 90), (c, 0)]
    for el in coords:
        if coords.index(el)==1:
            t.penup()
        elif coords.index(el)==5:
            t.penup()
        else:
            t.pendown()
        step, angle = el
        t.forward(step)
        t.right(angle)
        t.pendown()
def f2():
    coords = [(c, 90), (c, 45), (math.sqrt(2)*c,225), (c, 270), (2*c, 90), (c, 0)]
    for el in coords:
        if coords.index(el)>3:
            t.penup()
        else:
            t.pendown()
        step, angle = el
        t.forward(step)
        t.right(angle)
        t.pendown()
def f3():
    coords = [(c, 135), (math.sqrt(2)*c, 225), (c, 135), (math.sqrt(2)*c, 225), (c, 270), (2*c, 90), (c, 0)]
    for el in coords:
        if coords.index(el)>3:
            t.penup()
        else: 
            t.pendown()
        step, angle = el
        t.forward(step)
        t.right(angle)
        t.pendown()
def f4():
    coords = [(0, 90), (c, 270), (c, 90), (c, 180), (2*c, 90), (c, 0)]
    for el in coords:
        if coords.index(el)==5:
            t.penup()
        else:
            t.pendown()
        step, angle = el
        t.forward(step)
        t.right(angle)
        t.pendown()
def f5():
    coords = [(0, 90), (2*c, 270), (c, 270), (c, 270), (c, 90), (c, 90), (c, 0), (c+0.0001, 0)]
    for el in coords:
        if coords.index(el)<2:
            t.penup()
        elif coords.index(el)==7:
            t.penup()
        else:
            t.pendown()
        step, angle = el
        t.forward(step)
        t.right(angle)
        t.pendown()
def f6():
    coords = [(c, 135), (math.sqrt(2)*c, 315), (c, 270), (c, 270), (c,270), (c+0.0001, 135), (math.sqrt(2)*c,45), (c, 0)]
    for el in coords:
        if coords.index(el)==0:
            t.penup()
        elif coords.index(el)==7:
            t.penup()
        else:
            t.pendown()
        step, angle = el
        t.forward(step)
        t.right(angle)
        t.pendown()
def f7():
    coords = [(c, 135), (math.sqrt(2)*c, 315), (c, 210), (math.sqrt(5)*c, 60), (c, 0)]
    for el in coords:
        if coords.index(el)>2:
            t.penup()
        else:
            t.pendown()
        step, angle = el
        t.forward(step)
        t.right(angle)
        t.pendown()
def f8():
    coords = [(c, 90), (c, 90), (c, 90), (c,180), (c, 270), (c, 90), (c, 90), (c, 90), (c, 45), (math.sqrt(2)*c, 45), (c, 0)]
    for el in coords:
        if coords.index(el)>8:
            t.penup()
        else:
            t.pendown()
        step, angle = el
        t.forward(step)
        t.right(angle)
        t.pendown()
def f9():
    coords = [(c, 90), (c, 90), (c, 90), (c, 90), (0, 45), (math.sqrt(2)*c, 90), (math.sqrt(2)*c, 165), (math.sqrt(5)*c, 60), (c, 0)]
    for el in coords:
        if coords.index(el)==4:
            t.penup()
        elif coords.index(el)==5:
            t.penup()
        elif coords.index(el)>6:
            t.penup()
        else:
            t.pendown()
        step, angle = el
        t.forward(step)
        t.right(angle)
        t.pendown()
t.shape('turtle')
t.speed(150)
f1()
f4()
f1()
f7()
f0()
f0()

t.done()