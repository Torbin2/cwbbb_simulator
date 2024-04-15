import pygame
from sys import exit
from tiles import Tiles

pygame.init()
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800,400))
        pygame.display.set_caption('cwbbb')
        self.clock = pygame.time.Clock()

        self.tiles = Tiles(self)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                    exit()
            self.screen.fill("#584015")

            self.tiles.draw()

            pygame.display.update()
            self.clock.tick(60)
Game().run()