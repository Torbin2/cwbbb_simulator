import pygame
from sys import exit
from tiles import Tiles
import input

pygame.init()
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((0,0), pygame.RESIZABLE)
        pygame.display.set_caption('cwbbb')
        self.clock = pygame.time.Clock()
        
        self.tile_size = 50
        self.scroll = [0, 0]
        self.selected = "wheat"

        self.tiles = Tiles(self)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            keys = pygame.key.get_pressed()

            self.screen.fill("#000000")

            self.scroll = input.camera(keys, self.scroll)
            self.selected = input.select_crop(keys, self.selected)

            mouse_pos, mouse_input = input.mouse(self.tile_size, self.scroll)
            self.tiles.change_tiles(mouse_pos, mouse_input, self.selected)
            self.tiles.update_plants()

            self.tiles.draw(self.scroll, self.tile_size)

            pygame.display.update()
            self.clock.tick(60)
Game().run()