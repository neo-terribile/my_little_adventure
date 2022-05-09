import pygame
import os

from pygame.transform import scale
from pygame.locals import RLEACCEL

screen_width = 1600
screen_height = 800
tile_size = 64
scalar = 2

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
transparent_colour = green
count = 0

player_speed = 3
enemy_speed = 2

no_dir, north, east, south, west = 0, 1, 2, 3, 4
directions = [north, east, south, west]

player_layer = 4
enemy_layer = 3
block_layer = 2
ground_layer = 1
block_type = 1

tile_map = [
        'WWWWWWWWWWWWWWWWWWWWWWWW',
        'W.......AAA............W',
        'W......................W',
        'W...............W......W',
        'W...E...........W......W',
        'W.........P....EWWWWWWWW',
        'W...........W..........W',
        'W......................W',
        'W......................W',
        'W......................W',
        'W......................W',
        'WWWWWWWWWWWWWWWWWWWWWWWW']


def create_rectangle(dimensions, colour=None):
    rectangle = pygame.Surface(dimensions).convert()
    if colour is not None:
        rectangle.fill(colour)
    return rectangle


def create_transparent_rect(dimensions):
    transparent_rect = create_rectangle(dimensions, transparent_colour)
    transparent_rect.set_colorkey(transparent_colour, RLEACCEL)
    return transparent_rect


def load_image(image_path, colour_key=None):
    try:
        image = pygame.image.load(image_path)
    except pygame.error as message:
        print("Cannot load image: ", os.path.abspath(image_path))
        raise SystemExit(message)
    image = image.convert()
    if colour_key is not None:
        image.set_colorkey(colour_key, RLEACCEL)
    return image


def load_scaled_image(image_path, colour_key=None):
    image = load_image(image_path, colour_key)
    return scale(image, (image.get_width() * scalar, image.get_height() * scalar))
