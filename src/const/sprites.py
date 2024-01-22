import os
import pygame

SPRITES = {}


def load_sprites():
    sprite_folder = os.path.join('src', 'graphics', 'sprites')
    for file in os.listdir(sprite_folder):
        if file.endswith('.png'):
            file_name = os.path.splitext(file)[0]

            SPRITES[file_name] = pygame.image.load(
                os.path.join(sprite_folder, file)).convert_alpha()
