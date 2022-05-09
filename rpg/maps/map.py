from rpg.enemies.enemies import Enemies
from rpg.player.player import Player
from rpg.sprites.sprites import Ground, Block, Bar
from rpg.sprites.view import *

tile_map = [
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


class CreateTileMap():
    def __init__(self):
        self.groups = self.all_sprites
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
                    Player(self, j, i)

        Bar(self, 16, 16, white)
        Bar(self, 16, 16, red)
        Bar(self, 16, 48, white)
        Bar(self, 16, 48, blue)
