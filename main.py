import pygame
from sys import exit
from tiles import Tiles
from gameplay import Gameplay

pygame.init()
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800,400))
        pygame.display.set_caption('cwbbb')
        self.clock = pygame.time.Clock()

        self.tiles = Tiles(self)
        self.player = Gameplay()
    def run(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit
                    exit()
            self.player.planting(events)
            self.screen.fill("#000000")

            self.tiles.draw()

            pygame.display.update()
            self.clock.tick(60)
Game().run()