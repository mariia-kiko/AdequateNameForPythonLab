import pygame
from pygame.draw import *
import math as m
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 600))
rect(screen, (206, 235, 206), (0 ,0 ,1000 ,200))
rect(screen, (44, 117, 255), (0, 200, 1000, 200))
rect(screen, (237, 255, 33), (0, 400, 1000, 200))

circle(screen, (255, 255, 255), (150, 80), 30)
circle(screen, (0, 0, 0), (150, 80), 30, 1)
circle(screen, (255, 255, 255), (185, 80), 30)
circle(screen, (0, 0, 0), (185, 80), 30, 1)
circle(screen, (255, 255, 255), (210, 80), 30)
circle(screen, (0, 0, 0), (210, 80), 30, 1)
circle(screen, (255, 255, 255), (130, 100), 30)
circle(screen, (0, 0, 0), (130, 100), 30, 1)
circle(screen, (255, 255, 255), (160, 100), 30)
circle(screen, (0, 0, 0), (160, 100), 30, 1)
circle(screen, (255, 255, 255), (190, 100), 30)
circle(screen, (0, 0, 0), (190, 100), 30, 1)
circle(screen, (255, 255, 255), (230, 100), 30)
circle(screen, (0, 0, 0), (230, 100), 30, 1)
circle(screen, (237, 255, 33), (830, 100), 50)

rect(screen, (168,47,20), (520,354,10,150))
polygon(screen, (235, 76, 66, 0.1), [(440,380), (525,350),
                               (610,380),])
line(screen, (0, 0, 0), (465, 380), (525, 350))
line(screen, (0, 0, 0), (490, 380), (525, 350))
line(screen, (0, 0, 0), (515, 380), (525, 350))
line(screen, (0, 0, 0), (535, 380), (525, 350))
line(screen, (0, 0, 0), (560, 380), (525, 350))
line(screen, (0, 0, 0), (585, 380), (525, 350))

rect(screen, (168,47,20), (350,270,250,50))
polygon(screen, (168,47,20), [(600,270), (725,270),
                               (600,320)])
arc(screen,(168,47,20),[308,220,100,100],m.pi,m.pi*1.5,50)
arc(screen,(168,47,20),[309,220,100,100],m.pi,m.pi*1.5,50)
arc(screen,(168,47,20),[310,220,100,100],m.pi,m.pi*1.5,50)
rect(screen, (0,0,0), (450, 120, 7, 150))
polygon(screen, (255,255,255), [(457,120), (490,195),
                               (560,195)])
polygon(screen, (255,255,255), [(457,270), (490,195),
                               (560,195)])
line(screen, (0, 0, 0), (457, 120), (490, 195))      
line(screen, (0, 0, 0), (457, 120), (560, 195))
line(screen, (0, 0, 0), (457, 270), (490, 195))
line(screen, (0, 0, 0), (457, 270), (560, 195))
line(screen, (0, 0, 0), (490, 195), (560, 195)) 
circle(screen, (255,255,255), (565,295), 18)   
circle(screen, (0,0,0), (565,295), 18, 2)                    
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()