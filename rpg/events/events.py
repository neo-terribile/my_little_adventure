"""Gibt Events wie laufen, Kisten öffnen, Angriff, Kollision wieder"""


class Event():
    def get_metadata(self):
        pass

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