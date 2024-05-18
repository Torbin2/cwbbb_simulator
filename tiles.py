import pygame
import random

class Tiles:
    def __init__(self, game):
        self.game = game
        self.timer = 0
        
        self.tiles = {}
        self.colour = {
            "wheat" : ("#e4d36f","#E4C76F",'#e4bb6f'),
            "lemon" : ("#edfb0c","#Fbf10c", "#fbd90c") ,         
            "watermelon" : ('#5fce33',"#50ce33","#2f791e"),
        }
        
        possible = []

        blocks = 128
        for x in range(blocks):
            for y in range(blocks // 2):
                possible.append((x-blocks // 2, y- blocks // 4))
        choices = random.choices(possible,k = blocks * 2)
        for a in choices:
            self.tiles[a] = {"type" : random.choice(tuple(self.colour.keys())), "age" : 0,"timer": 0}
        

    def change_tiles(self, mouse_pos,inputs, selected_crop, plants):
        if inputs[0] and mouse_pos not in self.tiles:
            try:
                plants[selected_crop] -= 1
                self.tiles[mouse_pos] = {"type" : selected_crop, "age" : 0, "timer": 0}
                if plants[selected_crop] == 0:
                    plants.pop(selected_crop)
            except KeyError:
                pass

        if inputs[2] and mouse_pos in self.tiles:
            #if self.tiles[mouse_pos]["age"] == len(self.colour[self.tiles[mouse_pos]["type"]]) - 1:
            #use age to determin amount given
            try:
                plants[self.tiles[mouse_pos]["type"]] += random.randint(2,5)
            except KeyError:
                plants[self.tiles[mouse_pos]["type"]] = random.randint(2,5)

            self.tiles.pop(mouse_pos)

        return plants

    def update_plants(self):
        for plant in self.tiles:
            if self.tiles[plant]["age"] != len(self.colour[self.tiles[plant]["type"]]) - 1:
                self.tiles[plant]["timer"] += 1
                if self.tiles[plant]["timer"] == 60:
                    if random.randint(0,3) == 0:
                        self.tiles[plant]["age"] +=1
                    
                    self.tiles[plant]["timer"] = 0
                    

    def draw(self, scroll, tile_size = 25):
        for tile in self.tiles:
            x = pygame.Rect(int(tile[0])* tile_size + scroll[0], int(tile[1])* tile_size + scroll[1], tile_size, tile_size)
            pygame.draw.rect(self.game.screen, self.colour[self.tiles[tile]["type"]][self.tiles[tile]['age']], x)