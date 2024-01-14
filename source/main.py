import pygame
from pygame.locals import *

#initialize pygame
pygame.init()

#params
WIDTH = 800
HEIGHT = 800

canvas = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Arena of Kingdoms")


exit = False
while not exit:
    for event in pygame.event.get(): 
        
        
        
        if event.type == pygame.QUIT: 
            exit = True
    pygame.display.update() 
