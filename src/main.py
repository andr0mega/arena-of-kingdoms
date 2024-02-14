import pygame
from pygame.locals import *
from classes.game.config.GameConfig import GameConfig
from classes.game.logic.GameHandler import GameHandler
from const.colors import *
from classes.Game import Game
from classes.events.EventHandler import EventHandler
from const.sprites import load_sprites
from const.params import *
from const.colors import *

# params
WIDTH = 680
HEIGHT = 468
FPS = 30
CLOCK = pygame.time.Clock()

# Separated game logic part---------------------------------------------------------
gameSettings = json.loads(GAME_SETTINGS)
gameHandler = GameHandler.get_instance()
gameHandler.create_board(gameSettings["board_width"], gameSettings["board_height"])
gameHandler.set_config(GameConfig())
for player in range(gameSettings["player_amount"]):
    gameHandler.register_player(f"Player-{player}", PLAYER_COLORS[player])
if not gameHandler.start_game():
    print("something wrong:")
    print(gameHandler.board)
    print(gameHandler.game_config)
# Separated game logic part---------------------------------------------------------

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
event_handler = EventHandler.get_instance()
event_handler.reset_handler()
event_handler.set_elements(game.elements)

exit = False
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            event_handler.on_mouse_motion()

        if event.type == pygame.MOUSEBUTTONDOWN:
            event_handler.on_mouse_buttondown()

        if event.type == pygame.VIDEORESIZE:
            display_height = event.h
            display_width = event.w
            if display_height < HEIGHT:
                display_height = HEIGHT
            if display_width < WIDTH:
                display_width = WIDTH

            # Linux resize else not working
            if pygame.version.vernum >= (2, 0):
                canvas = pygame.display.get_surface()
            else:
                canvas = pygame.display.set_mode(
                    (display_width, display_height), pygame.RESIZABLE
                )

        canvas.fill(COLOR_WINDOW)
        game.draw_self()

        if event.type == pygame.QUIT:
            exit = True

    pygame.display.update()
    CLOCK.tick(FPS)
