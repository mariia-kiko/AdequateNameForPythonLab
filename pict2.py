import pygame
from pygame.draw import *

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
rect(screen, (168,47,20), (120,354,10,150))
polygon(screen, (235, 76, 66, 0.1), [(40,380), (125,350),
                               (210,380),])
line(screen, (0, 0, 0), (65, 380), (125, 350))
line(screen, (0, 0, 0), (90, 380), (125, 350))
line(screen, (0, 0, 0), (115, 380), (125, 350))
line(screen, (0, 0, 0), (135, 380), (125, 350))
line(screen, (0, 0, 0), (160, 380), (125, 350))
line(screen, (0, 0, 0), (185, 380), (125, 350))

rect(screen, (168,47,20), (550,270,250,50))
polygon(screen, (168,47,20), [(800,270), (925,270),
                               (800,320),])
arc(screen, (168,47,20), (450,270,100,50), 3.14, 1.5*3.14, 100)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()