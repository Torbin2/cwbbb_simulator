import pygame
from sys import exit
from tiles import Tiles
from gameplay import Player

pygame.init()
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800,400))
        pygame.display.set_caption('cwbbb')
        self.clock = pygame.time.Clock()
        
        self.scroll = [0, 0]

        self.tiles = Tiles(self)
        self.player = Player()

    def camera(self, keys, camera):
        
        if keys[pygame.K_w]:
            camera[1] +=10
        if keys[pygame.K_a]:
            camera[0] +=10
        if keys[pygame.K_s]:
            camera[1] -=10
        if keys[pygame.K_d]:
            camera[0] -=10

        return camera

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                    exit()
            keys = pygame.key.get_pressed()

            self.screen.fill("#000000")

            self.scroll = self.camera(keys, self.scroll)
            self.player.planting()

            self.tiles.draw(self.scroll)

            pygame.display.update()
            self.clock.tick(60)
Game().run()