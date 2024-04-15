import pygame
import random

class Tiles:
    def __init__(self, game):
        self.game = game
        self.tile_size = 25
        self.tiles = {
            (2, 3): "#ffffff"
        }
        possible = []
        for x in range(32):
            for y in range(16):
                possible.append((x, y))
        choices = random.choices(possible,k = 50)
        for a in choices:
            self.tiles[a] = '#' + hex(random.randrange(1<<(8*3)))[2:].zfill(6)

    def draw(self):
        for tile in self.tiles:
            x = pygame.Rect(int(tile[0])* self.tile_size, int(tile[1])* self.tile_size, self.tile_size, self.tile_size)
            pygame.draw.rect(self.game.screen, self.tiles[tile], x)