"""Gib den Status des Spiels wieder, z.B. Titelscreen, Menu, Game"""

import pygame
import sys

from pygame.locals import *
from rpg.maps.map import CreateTileMap
from rpg.events.eventbus import EventBus
from rpg.player.player import Player
import rpg.sprites.sprites

from rpg.sprites.sprites import velocity
from rpg.sprites.sprites import *
from rpg.sprites.view import *
from rpg.enemies.enemies import Enemies
from rpg.player.player import Player
from rpg.maps.map import tile_map

dimensions = (screen_width, screen_height)
fps = 60 // velocity

thirty_two = 32 // velocity
sixty_four = 64 // velocity

pygame.display.set_caption("My little Adventure")
screen = pygame.display.set_mode(dimensions)
blackRect = rpg.sprites.view.create_rectangle(dimensions)
fontsize = 64 // scalar

#font = pygame.font.Font('fonts/Pixel.ttf', 32)

eventBus = None


def setup():
    pass
    global eventBus
    eventBus = EventBus()

def show_title():
    pass

def show_menu():
    return Menu()

def start_game():
    return Game(True)



class Game():
    def __init__(self, running):
        self.running = running
        self.char_sprite = Spritesheet('img/chars.png')
        self.terrain_sprite = Spritesheet('img/tilesets/wall_top_middle.png')
        self.ground_sprite = Spritesheet('img/tilesets/dirt.png')
        self.enemy_sprite = Spritesheet('img/blob.png')
        self.attack_sprite = Spritesheet('img/chars.png')
        self.bar_sprite = Spritesheet('img/chars.png')


    def new(self):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.bars = pygame.sprite.LayeredUpdates()
        self.fixed_pos = pygame.sprite.LayeredUpdates()
        self.create_tile_map()

    def create_tile_map(self):

        self.tile_map = [
            'WWWWWWWWWWWWWWWWWWWWWWWW',
            'W.......AAA............W',
            'W......................W',
            'W...............W......W',
            'W...E...........W......W',
            'W.........P....EWWWWWWWW',
            'W...........W..........W',
            'W......................W',
            'W.....A................W',
            'W......................W',
            'W......................W',
            'WWWWWWWWWWWWWWWWWWWWWWWW']

        for i, row in enumerate(self.tile_map):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == 'E':
                    Enemies(self, j, i)
                if column == 'W':
                    Block(self, j, i)
                if column == 'A':
                    Block(self, j, i)
                if column == 'P':
                    Player(self, j, i)

        Bar(self, 16, 16, white)
        Bar(self, 16, 16, red)
        Bar(self, 16, 48, white)
        Bar(self, 16, 48, blue)

    def events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        screen.fill(black)
        self.all_sprites.draw(screen)
        clock = pygame.time.Clock()
        clock.tick(fps)
        pygame.display.update()

    def main(self):

        while self.playing:
            self.events()
            self.update()
            self.draw()

            clock = pygame.time.Clock()
            clock.tick(fps)

    def menu(self):
        return Menu

    def game_over(self):
        return GameOver


class Menu:

    def __init__(self):
        image_path = pygame.image.load('img/background.png')
        self.menu_background = pygame.transform.scale(image_path, dimensions)
        title = font.render('Main Menu', True, black)
        title_rect = title.get_rect(x=10, y=10)
        menu = False

        play_button = Button(50, 100, 250, 50, white, black, 'Start Game', 20)
        load_button = Button(50, 200, 250, 50, white, black, 'Load Game', 20)
        options_button = Button(50, 300, 250, 50, white, black, 'Options', 20)
        credits_button = Button(50, 400, 250, 50, white, black, 'Credits', 20)
        exit_button = Button(50, 500, 250, 50, white, black, 'Exit Game', 20)

        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                return Game()

            if load_button.is_pressed(mouse_pos, mouse_pressed):
                menu = False

            if options_button.is_pressed(mouse_pos, mouse_pressed):
                menu = False

            if credits_button.is_pressed(mouse_pos, mouse_pressed):
                menu = False

            if exit_button.is_pressed(mouse_pos, mouse_pressed):
                pygame.quit()
                sys.exit()

            screen.blit(self.menu_background, (0, 0))
            screen.blit(title, title_rect)
            screen.blit(play_button.image, play_button.rect)
            screen.blit(load_button.image, load_button.rect)
            screen.blit(options_button.image, options_button.rect)
            screen.blit(credits_button.image, credits_button.rect)
            screen.blit(exit_button.image, exit_button.rect)
            pygame.display.update()


class GameOver:
    def __init__(self):
        text = font.render('Game Over', False, red)
        text_rect = text.get_rect(center=(screen_width / 2, screen_height / 2))

        menu_button = Button(125, 500, 250, 50, white, red, 'Menu', 20)
        load_button = Button(425, 500, 250, 50, white, red, 'Load Game', 20)
        exit_button = Button(725, 500, 250, 50, white, red, 'Exit', 20)

        for sprite in self.all_sprites:
            sprite.kill()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if menu_button.is_pressed(mouse_pos, mouse_pressed):
                Menu()

            if load_button.is_pressed(mouse_pos, mouse_pressed):
                pass

            if exit_button.is_pressed(mouse_pos, mouse_pressed):
                pygame.quit()
                sys.exit()

            screen.blit(text, text_rect)
            screen.blit(menu_button.image, menu_button.rect)
            screen.blit(load_button.image, load_button.rect)
            screen.blit(exit_button.image, exit_button.rect)
            pygame.display.update()


class Button:
    def __init__(self, x, y, width, height, fg, bg, content, fontsize):
        self.font = pygame.font.Font('fonts/Pixel.ttf', fontsize)
        self.content = content

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.fg = fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width / 2, self.height / 2))
        self.image.blit(self.text, self.text_rect)

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False
