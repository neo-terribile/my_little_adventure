from rpg.sprites.sprites import *
from rpg.sprites.view import *
from rpg.player.player import Player
from rpg.enemies.enemies import Enemies
from rpg.states.gamestates import Button
from rpg.states.gamestates import fps


import pygame
import sys


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font('fonts/Pixel.ttf', 32)

        self.char_sprite = Spritesheet('img/chars.png')
        self.terrain_sprite = Spritesheet('img/tilesets/wall_top_middle.png')
        self.ground_sprite = Spritesheet('img/tilesets/dirt.png')
        self.enemy_sprite = Spritesheet('img/blob.png')
        self.attack_sprite = Spritesheet('img/chars.png')
        self.bar_sprite = Spritesheet('img/chars.png')

        self.menu_background = pygame.image.load('img/background.png')
        self.menu_background = pygame.transform.scale(self.menu_background, (screen_width, screen_height))

    def create_tile_map(self):
        for i, row in enumerate(tile_map):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == 'E':
                    Enemies(self, j, i)
                if column == 'W':
                    Block(self, j, i)
                if column == 'A':
                    Block(self, j, i)
                if column == 'P':
                    self.player = Player(self, j, i)

        Bar(self, 16, 16, white)
        Bar(self, 16, 16, red)
        Bar(self, 16, 48, white)
        Bar(self, 16, 48, blue)


    def new(self):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.bars = pygame.sprite.LayeredUpdates()
        self.fixed_pos = pygame.sprite.LayeredUpdates()

        self.create_tile_map()

    def events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.player.direction == 'north':
                        Attack(self, self.player.rect.x, self.player.rect.y - tile_size)
                    if self.player.direction == 'east':
                        Attack(self, self.player.rect.x + tile_size, self.player.rect.y)
                    if self.player.direction == 'south':
                        Attack(self, self.player.rect.x, self.player.rect.y + tile_size)
                    if self.player.direction == 'west':
                        Attack(self, self.player.rect.x - tile_size, self.player.rect.y)

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(black)
        self.all_sprites.draw(self.screen)
        self.clock.tick(fps)
        pygame.display.update()

    def main(self):

        while self.playing:
            self.events()
            self.update()
            self.draw()

    def game_over(self):
        text = self.font.render('Game Over', False, red)
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
                self.menu()

            if load_button.is_pressed(mouse_pos, mouse_pressed):
                pass

            if exit_button.is_pressed(mouse_pos, mouse_pressed):
                pygame.quit()
                sys.exit()

            self.screen.blit(text, text_rect)
            self.screen.blit(menu_button.image, menu_button.rect)
            self.screen.blit(load_button.image, load_button.rect)
            self.screen.blit(exit_button.image, exit_button.rect)
            self.clock.tick(fps)
            pygame.display.update()

    def menu(self):
        menu = True

        title = self.font.render('Main Menu', True, black)
        title_rect = title.get_rect(x=10, y=10)

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
                menu = False

            if load_button.is_pressed(mouse_pos, mouse_pressed):
                menu = False

            if options_button.is_pressed(mouse_pos, mouse_pressed):
                menu = False

            if credits_button.is_pressed(mouse_pos, mouse_pressed):
                menu = False

            if exit_button.is_pressed(mouse_pos, mouse_pressed):
                pygame.quit()
                sys.exit()

            self.screen.blit(self.menu_background, (0, 0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.screen.blit(load_button.image, load_button.rect)
            self.screen.blit(options_button.image, options_button.rect)
            self.screen.blit(credits_button.image, credits_button.rect)
            self.screen.blit(exit_button.image, exit_button.rect)
            self.clock.tick(fps)
            pygame.display.update()


g = Game()
g.menu()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()
