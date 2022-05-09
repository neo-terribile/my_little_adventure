from rpg.sprites.view import *

import pygame
import random

class Enemies(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = enemy_layer
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * tile_size
        self.y = y * tile_size
        self.width = tile_size
        self.height = tile_size

        self.delta_x = 0
        self.delta_y = 0

        self.direction = random.choice(['west', 'east'])
        self.animation_loop = 1
        self.movement_loop = 0
        self.delta_max = random.randint(10, 50)

        self.image = self.game.enemy_sprite.get_sprite(0, 0, 50, 50)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()
        self.animate()

        self.rect.x += self.delta_x
        self.rect.y += self.delta_y

        self.delta_x = 0
        self.delta_y = 0

    def movement(self):
        if self.direction == 'west':
            self.delta_x -= enemy_speed
            self.movement_loop -= 1
            if self.movement_loop <= -self.delta_max:
                self.direction = 'east'

        if self.direction == 'east':
            self.delta_x += enemy_speed
            self.movement_loop += 1
            if self.movement_loop >= self.delta_max:
                self.direction = 'west'

    def animate(self):
        pass