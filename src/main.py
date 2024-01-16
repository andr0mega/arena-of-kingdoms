import pygame
from pygame.locals import *
from const.colors import *
from classes.Board import Board
from classes.Player import Player
from classes.Shop import Shop
from classes.Screen import Screen
from classes.events.Mouse import Mouse

# params
WIDTH = 680
HEIGHT = 468
FPS = 60
CLOCK = pygame.time.Clock()

# initialize game
pygame.init()
pygame.font.init()
pygame.display.set_caption("Arena of Kingdoms")
canvas = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
canvas.fill(COLOR_WINDOW)
player1 = Player("Maurice", COLOR_PLAYER1)
player2 = Player("Colin", COLOR_PLAYER2)
board = Board(canvas)
shop = Shop(canvas)
screen = Screen(canvas)
mouse = Mouse(screen, board, shop, player2)
board.draw_board()
shop.draw_shop_icon()
screen.draw_end_turn_icon()


exit = False
while not exit:
    for event in pygame.event.get():
        mouse.on_mouse_event()

        if event.type == pygame.VIDEORESIZE:
            display_height = event.h
            display_width = event.w
            if display_height < HEIGHT:
                display_height = HEIGHT
            if display_width < WIDTH:
                display_width = WIDTH
            canvas = pygame.display.set_mode(
                (display_width, display_height), pygame.RESIZABLE)
            canvas.fill(COLOR_WINDOW)
            board.draw_board()
            shop.draw_shop_icon()
            screen.draw_end_turn_icon()
            if (shop.isopen):
                shop.draw_shop()

        if event.type == pygame.QUIT:
            exit = True

    pygame.display.update()
    CLOCK.tick(FPS)
