import pygame
from pygame.locals import *
from classes.game.config.GameConfig import GameConfig
from classes.game.logic.GameHandler import GameHandler
from const.colors import *
from classes.Game import Game
from classes.events.Mouse import Mouse
from const.sprites import load_sprites
from const.params import *
from const.colors import *

# params
WIDTH = 680
HEIGHT = 468
FPS = 30
CLOCK = pygame.time.Clock()

# initialize game
pygame.init()
pygame.font.init()
pygame.display.set_caption("Arena of Kingdoms")
canvas = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
canvas.fill(COLOR_WINDOW)

load_sprites()

game = Game(canvas, PLAYER_AMOUNT)
game.initialize_game()
game.draw_self()
mouse = Mouse(game.elements)
gameHandler = GameHandler.get_instance()
gameHandler.create_board(WIDTH, HEIGHT)
gameHandler.set_config(GameConfig())
for player in range(PLAYER_AMOUNT):
    gameHandler.register_player(f"Player-{player}", PLAYER_COLORS[player])
started = gameHandler.start_game()
if(not started):
    print("something wrong:")
    print(gameHandler.board)
    print(gameHandler.game_config)

exit = False
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            mouse.on_mouse_motion()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse.on_mouse_buttondown()

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
        game.draw_self()

        if event.type == pygame.QUIT:
            exit = True

    pygame.display.update()
    CLOCK.tick(FPS)
