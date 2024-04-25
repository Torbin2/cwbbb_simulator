import pygame
import random

class Tiles:
    def __init__(self, game):
        self.game = game
        
        self.tiles = {}
        self.colour = {
            "wheat" : "#E4C76F",
            "lemon" : "#Fbf10c" ,         
            "watermelon" : "#2f791e"
        }
        
        possible = []
        for x in range(32):
            for y in range(16):
                possible.append((x, y))
        choices = random.choices(possible,k = 50)
        for a in choices:
            self.tiles[a] = random.choice(tuple(self.colour.keys()))
        

    def change_tiles(self, mouse_pos,inputs, selected_crop):
        if inputs[0] and mouse_pos not in self.tiles:
            self.tiles[mouse_pos] = selected_crop
        if inputs[2] and mouse_pos in self.tiles:
            self.tiles.pop(mouse_pos)

    def draw(self, scroll, tile_size = 25):
        for tile in self.tiles:
            x = pygame.Rect(int(tile[0])* tile_size + scroll[0], int(tile[1])* tile_size + scroll[1], tile_size, tile_size)
            pygame.draw.rect(self.game.screen, self.colour[self.tiles[tile]], x)