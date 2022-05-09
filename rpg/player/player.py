from rpg.sprites.view import *
import pygame
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = player_layer
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * tile_size
        self.y = y * tile_size
        self.width = tile_size
        self.height = tile_size

        self.delta_x = 0
        self.delta_y = 0

        self.direction = "south"

        self.animation_loop = 1
        self.collision = False

        self.image = self.game.char_sprite.get_sprite(0, 0, 64, 64)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.health_max = 100
        self.health = self.health_max

        self.damage_collision = 2

    def event(self):
        pass

    def update(self):
        self.movement()
        self.animate()
        self.collide_enemy()
        self.health_and_mana()

        self.rect.x += self.delta_x
        self.collide_block('x')
        self.rect.y += self.delta_y
        self.collide_block('y')

        self.camera()

        self.delta_x = 0
        self.delta_y = 0
        self.collision = False

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.delta_x -= player_speed
            self.direction = "west"
        if keys[pygame.K_RIGHT]:
            self.delta_x += player_speed
            self.direction = "east"
        if keys[pygame.K_UP]:
            self.delta_y -= player_speed
            self.direction = "north"
        if keys[pygame.K_DOWN]:
            self.delta_y += player_speed
            self.direction = "south"

    def camera(self):
        if not self.collision:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                for sprite in self.game.all_sprites:
                    sprite.rect.x += player_speed
                for sprite in self.game.fixed_pos:
                    sprite.rect.x -= player_speed
            if keys[pygame.K_RIGHT]:
                for sprite in self.game.all_sprites:
                    sprite.rect.x -= player_speed
                for sprite in self.game.fixed_pos:
                    sprite.rect.x += player_speed
            if keys[pygame.K_UP]:
                for sprite in self.game.all_sprites:
                    sprite.rect.y += player_speed
                for sprite in self.game.fixed_pos:
                    sprite.rect.y -= player_speed
            if keys[pygame.K_DOWN]:
                for sprite in self.game.all_sprites:
                    sprite.rect.y -= player_speed
                for sprite in self.game.fixed_pos:
                    sprite.rect.y += player_speed

    def animate(self):
        south_animations = [self.game.char_sprite.get_sprite(0, 0, self.width, self.height),
                            self.game.char_sprite.get_sprite(64, 0, self.width, self.height),
                            self.game.char_sprite.get_sprite(128, 0, self.width, self.height),
                            self.game.char_sprite.get_sprite(192, 0, self.width, self.height),
                            self.game.char_sprite.get_sprite(256, 0, self.width, self.height),
                            self.game.char_sprite.get_sprite(320, 0, self.width, self.height),
                            self.game.char_sprite.get_sprite(384, 0, self.width, self.height)]

        north_animations = [self.game.char_sprite.get_sprite(0, 64, self.width, self.height),
                            self.game.char_sprite.get_sprite(64, 64, self.width, self.height),
                            self.game.char_sprite.get_sprite(128, 64, self.width, self.height),
                            self.game.char_sprite.get_sprite(192, 64, self.width, self.height),
                            self.game.char_sprite.get_sprite(256, 64, self.width, self.height),
                            self.game.char_sprite.get_sprite(320, 64, self.width, self.height),
                            self.game.char_sprite.get_sprite(384, 64, self.width, self.height)]

        east_animations = [self.game.char_sprite.get_sprite(64, 128, self.width, self.height),
                           self.game.char_sprite.get_sprite(0, 128, self.width, self.height),
                           self.game.char_sprite.get_sprite(128, 128, self.width, self.height),
                           self.game.char_sprite.get_sprite(192, 128, self.width, self.height),
                           self.game.char_sprite.get_sprite(256, 128, self.width, self.height),
                           self.game.char_sprite.get_sprite(320, 128, self.width, self.height),
                           self.game.char_sprite.get_sprite(384, 128, self.width, self.height)]

        west_animations = [self.game.char_sprite.get_sprite(0, 192, self.width, self.height),
                           self.game.char_sprite.get_sprite(64, 192, self.width, self.height),
                           self.game.char_sprite.get_sprite(128, 192, self.width, self.height),
                           self.game.char_sprite.get_sprite(192, 192, self.width, self.height),
                           self.game.char_sprite.get_sprite(256, 192, self.width, self.height),
                           self.game.char_sprite.get_sprite(320, 192, self.width, self.height),
                           self.game.char_sprite.get_sprite(384, 192, self.width, self.height)]

        if self.direction == 'south':
            if self.delta_y == 0:
                self.image = self.game.char_sprite.get_sprite(0, 0, self.width, self.height)
            else:
                self.image = south_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.2
                if self.animation_loop >= 7:
                    self.animation_loop = 1

        if self.direction == 'north':
            if self.delta_y == 0:
                self.image = self.game.char_sprite.get_sprite(0, 64, self.width, self.height)
            else:
                self.image = north_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.2
                if self.animation_loop >= 7:
                    self.animation_loop = 1

        if self.direction == 'east':
            if self.delta_x == 0:
                self.image = self.game.char_sprite.get_sprite(0, 128, self.width, self.height)
            else:
                self.image = east_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.2
                if self.animation_loop >= 7:
                    self.animation_loop = 1

        if self.direction == 'west':
            if self.delta_x == 0:
                self.image = self.game.char_sprite.get_sprite(0, 192, self.width, self.height)
            else:
                self.image = west_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.2
                if self.animation_loop >= 7:
                    self.animation_loop = 1

    def collide_enemy(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if hits:
            self.health -= self.damage_collision

    def collide_block(self, direction):
        if direction == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.delta_x > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    self.collision = True
                if self.delta_x < 0:
                    self.rect.x = hits[0].rect.right
                    self.collision = True
        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.delta_y > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    self.collision = True
                if self.delta_y < 0:
                    self.rect.y = hits[0].rect.bottom
                    self.collision = True

    def health_and_mana(self):
        if self.health == 0:
            self.game.playing = False
        if self.health >= self.health_max:
            self.health = self.health_max