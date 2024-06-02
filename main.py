import pygame
from sys import exit
from tiles import Tiles
from menu import Menu
import input

pygame.init()
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((0,0), pygame.RESIZABLE)
        pygame.display.set_caption('cwbbb')
        self.clock = pygame.time.Clock()

        self.tile_size = self.screen.get_width() // 28
        self.scroll = [0, 0]
        self.selected_plant = ""
        self.selected_upgrade = -1
        self.plants = {}

        self.upgrades = { #type upgrade : (currency, times bought, formula/ upgrade cost)
            "multiplier" : ["wheat", 1, "int(upgrades['multiplier'][1]**2)"], #x²
            "speed" : ["carrot", 1, "int(upgrades['speed'][1]**2 / 2)"],#x² / 2
            "extra growth" : ['watermelon', 1, 'int(((1)/(-0.1 * upgrades["extra growth"][1]))+10)' ], #1/-0.1x + 10
            "auto harvest" : ["lemon", 1, "4* upgrades['extra growth'][1])" ], # 4x (not implented yet)
        }

        self.tiles = Tiles(self)
        self.menu = Menu(self.screen)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            keys = pygame.key.get_pressed()

            self.screen.fill("#000000")

            self.scroll = input.camera(keys, self.scroll)
            self.selected_plant = input.select_crop(keys, self.selected_plant, self.plants)

            if pygame.mouse.get_pos()[0] > self.screen.get_width() // 3.5: #plants editing
                mouse_pos, mouse_input = input.mouse_plantside(self.tile_size, self.scroll)
                self.plants = self.tiles.change_tiles(mouse_pos, mouse_input, self.selected_plant, self.plants, self.upgrades["multiplier"][1])
                self.selected_upgrade = -1 #resets selected upgrade
            else: #upgrade selection
                self.selected_upgrade, mouse_input = input.mouse_upgrades(self.plants)
                self.upgrades = self.menu.upgrade(self.selected_upgrade, mouse_input, self.plants, self.upgrades)
            
            self.tiles.update_plants(self.upgrades["speed"][1], self.upgrades["extra growth"][1])

            self.tiles.draw(self.scroll, self.tile_size)
            self.menu.draw(self.plants, self.selected_plant,  self.upgrades, self.selected_upgrade)

            pygame.display.update()
            self.clock.tick(60)
Game().run()