import pygame
from pygame.locals import *
from const.colors import *
from classes.Board import Board
from classes.Player import Player
from classes.events.Mouse import Mouse

#params
WIDTH = 1440
HEIGHT = 1124
FPS = 60
CLOCK = pygame.time.Clock()

#initialize game
pygame.init()
pygame.display.set_caption("Arena of Kingdoms")
canvas = pygame.display.set_mode((WIDTH, HEIGHT))
canvas.fill(COLOR_WINDOW)
player1 = Player("Maurice", COLOR_PLAYER1)
board = Board(canvas)
mouse = Mouse(board, player1)
board.draw_board()


exit = False
while not exit:
    for event in pygame.event.get(): 
        mouse.on_mouse_event()
        

        if event.type == pygame.QUIT: 
            exit = True

    pygame.display.update() 
    CLOCK.tick(FPS)