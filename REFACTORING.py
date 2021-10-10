import pygame
from pygame.draw import *
import math as m
pygame.init()

#SCREEN PARAMETERS
WIDTH = 1000
HEIGHT = 600
#LIST OF COLORS
LIGHT_OLIVE = (206, 235, 206)
BLUE = (44, 117, 255)
YELLOW = (237, 255, 33)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (168,47,20)
LIGHT_RED = (235, 76, 66)

FPS = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
def background (color1 = LIGHT_OLIVE, color_2 = BLUE, color3 = YELLOW):
    rect(screen, LIGHT_OLIVE, (0, 0 ,WIDTH, HEIGHT/3))
    rect(screen, BLUE, (0, HEIGHT/3, WIDTH, HEIGHT/3))
    rect(screen, YELLOW, (0, 2*HEIGHT/3, WIDTH, HEIGHT/3))

background()

def cloud (x0, y0, r, surf_color = LIGHT_OLIVE, cloud_color = WHITE):
    '''
        x0, y0 - coordinates of upper left corner of the surface
        cloud_color - color of cloud in RGB
        surf_color - surface color in RGB
        r - radius of each circle
    '''
    surf = pygame.Surface((6*r, 4*r))
    surf.fill(surf_color)
    for i in range (3):
        circle(surf, cloud_color, ((i+2)*r, 1.5*r), r)
        circle(surf, BLACK, ((i+2)*r, 1.5*r), r, 1)
    for j in range (4):
        circle(surf, cloud_color, (2*r - 2*r/3 + j*r, 2.5*r), r)
        circle(surf, BLACK, (2*r - 2*r/3 + j*r, 2.5*r), r, 1)
    screen.blit(surf, (x0, y0))
    
cloud(0, 0, 30, LIGHT_OLIVE, WHITE)

def sun (x0, y0, r, color = YELLOW):
    '''
        x0, y0 - coordinates of center of the Sun
        r - radius of the Sun
    '''
    circle(screen, color, (x0, y0), r)
    
sun(830, 100, 50, YELLOW)

def umbrella(x0, y0, hat_width, hat_height, stick_width, stick_height, n):
    '''
       x0, y0 - coordinates of top of umbrella hat
       n - number of lines on umbrella hat
    '''
    surf = pygame.Surface((hat_width, hat_height + stick_height), pygame.SRCALPHA)
    #surf.fill(BLACK)
    surf.set_alpha(100)
    rect(surf, (168, 47, 20, 128), (x0 - stick_width/2, y0 + hat_height, stick_width, stick_height))
    polygon(surf, (235, 76, 66, 128), [(x0 - (hat_width/2), y0 + hat_height), (x0, y0),
                               (x0 + (hat_width/2), y0 + hat_height)])
    for i in range (n + 1):
        line(surf, BLACK, (x0 - hat_width/2 + i*hat_width/(n+1), y0 + hat_height), (x0, y0))
    screen.blit(surf, (x0 - 0.5*hat_width, y0))
    
umbrella(525, 350, 140, 30, 20, 180, 6)

def boat (x0, y0, bottom_width, boat_height, stick_width, stick_height):
    '''
        x0, y0 - coordinates of bow
    '''
    surf = pygame.Surface((1.5*bottom_width + boat_height, boat_height + stick_width))
    rect(surf, (168, 47, 20, 128), (x0 - 1.5*bottom_width, y0, bottom_width, boat_height))
    polygon(surf, (168, 47, 20, 128), [(x0 - bottom_width/2, y0), (x0, y0),
                               (x0 - bottom_width/2, y0 + boat_height)])
    arc(surf, (168, 47, 20, 128), [x0 - 1.5*bottom_width - boat_height, y0 - boat_height, 2*boat_height, 2*boat_height],m.pi,m.pi*1.5, boat_height)
    arc(surf, (168, 47, 20, 128), [x0 - 1.5*bottom_width - boat_height + 1, y0 - boat_height, 2*boat_height, 2*boat_height],m.pi,m.pi*1.5, boat_height)
    arc(surf, (168, 47, 20, 128), [x0 - 1.5*bottom_width - boat_height + 2, y0 - boat_height, 2*boat_height, 2*boat_height],m.pi,m.pi*1.5, boat_height)
    rect(surf, BLACK, (x0 - bottom_width, y0 - stick_height, stick_width, stick_height))
    polygon(surf, (255, 255, 255, 128), [(x0 - bottom_width + stick_width, y0 - stick_height), (x0 - 0.5*bottom_width + stick_width, y0 - stick_height + 0.4*stick_height),
                               (x0 - 0.8*bottom_width + stick_width, y0 - stick_height + 0.4*stick_height)])
    polygon(surf, (255, 255, 255, 128), [(x0 - bottom_width + stick_width, y0 - 0.2*stick_height), (x0 - 0.5*bottom_width + stick_width, y0 - stick_height + 0.4*stick_height),
                               (x0 - 0.8*bottom_width + stick_width, y0 - stick_height + 0.4*stick_height)])
    line(surf, BLACK, (x0 - bottom_width + stick_width, y0 - stick_height), (x0 - 0.5*bottom_width + stick_width, y0 - stick_height + 0.4*stick_height))      
    line(surf, BLACK, (x0 - bottom_width + stick_width, y0 - 0.2*stick_height), (x0 - 0.5*bottom_width + stick_width, y0 - stick_height + 0.4*stick_height))
    line(surf, BLACK, (x0 - 0.5*bottom_width + stick_width, y0 - stick_height + 0.4*stick_height),
                               (x0 - 0.8*bottom_width + stick_width, y0 - stick_height + 0.4*stick_height))
    line(surf, BLACK, (x0 - 0.8*bottom_width + stick_width, y0 - 0.6*stick_height), (x0 - bottom_width + stick_width, y0 - 0.2*stick_height))
    line(surf, BLACK, (x0 - 0.8*bottom_width + stick_width, y0 - 0.6*stick_height), (x0 - bottom_width + stick_width, y0 - stick_height))
    circle(surf, WHITE, (x0 - 0.6*bottom_width, y0 + 0.5*boat_height), 0.35*boat_height)   
    circle(surf, BLACK, (x0 - 0.6*bottom_width, y0 + 0.5*boat_height), 0.35*boat_height, 2)

boat(725, 270, 250, 50, 10, 200)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
