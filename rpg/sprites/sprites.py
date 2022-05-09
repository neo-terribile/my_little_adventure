import math
from rpg.sprites.view import *


velocity = 1
movement = velocity * scalar


class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(green)  # sprite_background off
        return sprite


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, spriteFrames, position=(0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.spriteFrames = spriteFrames
        self.position = [i * scalar for i in position]


class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = block_layer
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * tile_size
        self.y = y * tile_size
        self.width = tile_size
        self.height = tile_size

        self.image = self.game.terrain_sprite.get_sprite(0, 0, 21, 21)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ground_layer
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * tile_size
        self.y = y * tile_size
        self.width = tile_size
        self.height = tile_size

        self.image = self.game.ground_sprite.get_sprite(0, 0, 21, 21)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Attack(pygame.sprite.Sprite):

    def __init__(self, game, x, y):

        self.game = game
        self._layer = player_layer
        self.groups = self.game.all_sprites, self.game.attacks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y
        self.width = tile_size / 2
        self.height = tile_size / 2

        self.animation_loop = 0

        self.image = self.game.char_sprite.get_sprite(448, 0, 480, 32)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.animate()
        self.collide()

    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, True)
        if hits:
            self.kill()

    def animate(self):
        direction = self.game.player.direction

        north_animations = [self.game.attack_sprite.get_sprite(448, 0, self.width, self.height),
                            self.game.attack_sprite.get_sprite(448, 32, self.width, self.height)]

        east_animations = [self.game.attack_sprite.get_sprite(512, 0, self.width, self.height),
                           self.game.attack_sprite.get_sprite(544, 0, self.width, self.height)]

        south_animations = [self.game.attack_sprite.get_sprite(448, 0, self.width, self.height),
                            self.game.attack_sprite.get_sprite(448, 32, self.width, self.height)]

        west_animations = [self.game.attack_sprite.get_sprite(512, 32, self.width, self.height),
                           self.game.attack_sprite.get_sprite(544, 32, self.width, self.height)]

        if direction == 'north':
            self.image = north_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 2:
                self.kill()
        if direction == 'east':
            self.image = east_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 2:
                self.kill()
        if direction == 'south':
            self.image = south_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 2:
                self.kill()
        if direction == 'west':
            self.image = west_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 2:
                self.kill()


class Bar(pygame.sprite.Sprite):
    def __init__(self, game, x, y, colour):
        self.game = game
        self._layer = player_layer
        self.groups = self.game.all_sprites, self.game.fixed_pos, self.game.bars
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y
        self.width = tile_size * 3
        self.height = tile_size / 4
        self.colour = colour

        if colour == white:
            self.image = self.game.char_sprite.get_sprite(448, 64, self.width, self.height)
            self.image = pygame.transform.scale(self.image, (self.width, self.height))

            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

        if colour == red:
            self.image = self.game.char_sprite.get_sprite(448, 80, self.width, self.height)
            self.image = pygame.transform.scale(self.image, (self.width, self.height))

            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

        if colour == blue:
            self.image = self.game.char_sprite.get_sprite(448, 96, self.width, self.height)
            self.image = pygame.transform.scale(self.image, (self.width, self.height))

            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y



