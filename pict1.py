import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
rect(screen, (255, 255, 255), (0, 0, 400, 400))
circle(screen, (255, 215, 0), (200, 175), 100)
circle(screen, (0, 0, 0), (200, 175), 100, 2)
line(screen, (0, 0, 0), (110, 70), (190, 135), 17)
line(screen, (0, 0, 0), (310, 100), (210, 130), 17)
circle(screen, (255, 0, 0), (165, 145), 20)
circle(screen, (255, 0, 0), (235, 145), 15)
circle(screen, (0, 0, 0), (165, 145), 7)
circle(screen, (0, 0, 0), (235, 145), 5)
rect(screen, (0, 0, 0),(150,230, 100, 15) )
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()