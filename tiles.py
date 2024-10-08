import pygame
import random

class Tiles:
    def __init__(self, game):
        self.game = game
        self.harvester_timer = 0
        
        self.tiles = {}
        self.colour = {
            "wheat" : ("#c4b28f","#ddc8a1", '#f5deb3'), 
            "lemon" : ("#edfb0c","#d5e20b", "#bec90a", "#a6b008", "#8e9707") ,         
            "watermelon" : ('#5fce33',"#50ce33",'#448635',"#2f791e", "#2a6d1b"),
            "carrot" : ("#f9ba5f", "#f9b048", "#f8a631", "#F79c1a"),
            "tuinkers" : ("#643e17", "#774a1c", "#8b5620","#9f6225","#b36f29" ,"#c77b2e", )
        }
        
        possible = []

        blocks = 128
        for x in range(blocks):
            for y in range(blocks // 2):
                possible.append((x-blocks // 2, y- blocks // 4))
        choices = random.choices(possible,k = blocks * 2)
        for a in choices:
            self.tiles[a] = {"type" : random.choice(tuple(self.colour.keys())), "age" : 2,"timer": 0} #age 2 is 3th colour
        

    def change_tiles(self, mouse_pos,inputs, selected_crop, plants, mult,  auto_harvesters, harvest_timer):
        if inputs[0] and mouse_pos not in self.tiles:
            try:
                plants[selected_crop] -= 1
                self.tiles[mouse_pos] = {"type" : selected_crop, "age" : 0, "timer": 0}
                if plants[selected_crop] <= 0:
                    plants.pop(selected_crop)
            except KeyError:
                pass

        if inputs[2] and mouse_pos in self.tiles:
            #randint * (age²) / (posbl_age / 2)
            plant_amount = int(random.randint(1,3) * ((self.tiles[mouse_pos]["age"]**2) / (len(self.colour[self.tiles[mouse_pos]["type"]]) / 2 ))) * mult
            if plant_amount != 0:
                try:
                    plants[self.tiles[mouse_pos]["type"]] += plant_amount
                except KeyError:
                    plants[self.tiles[mouse_pos]["type"]] = plant_amount

            self.tiles.pop(mouse_pos)

        self.harvester_timer += 1
        if self.harvester_timer >= (3600 // harvest_timer) + 60:
            grown_plants = [i for i in self.tiles if self.tiles[i]["age"] == len(self.colour[self.tiles[i]["type"]]) - 1]
            
            if auto_harvesters > len(grown_plants): harvested = grown_plants
            else: harvested = random.sample(grown_plants, k = auto_harvesters)
            
            for i in harvested:
                plant_amount = int(random.randint(1,3) * ((self.tiles[i]["age"]**2) / (len(self.colour[self.tiles[i]["type"]]) / 2 ))) * mult
                if plant_amount != 0:
                    try:
                        plants[self.tiles[i]["type"]] += plant_amount
                    except KeyError:
                        plants[self.tiles[i]["type"]] = plant_amount

                self.tiles.pop(i)
            self.harvester_timer = 0

        return plants

    def update_plants(self, speed_level, extra_grow_chance,):
        

        for plant in self.tiles:
            if self.tiles[plant]["age"] != len(self.colour[self.tiles[plant]["type"]]) - 1:
                self.tiles[plant]["timer"] += 1
                
                if self.tiles[plant]["timer"] >= 360 / speed_level: #1 min
                    
                    if random.randint(0, 10) >= 10 - extra_grow_chance:
                        if random.randint(0, 100) >= 100 - extra_grow_chance:                    
                            if random.randint(0, 10_000) >= 10_000 - extra_grow_chance:

                                self.tiles[plant]["age"] = len(self.colour[self.tiles[plant]["type"]]) - 1
                            else:self.tiles[plant]["age"] +=3                       
                        else: self.tiles[plant]["age"] +=2
                    else: self.tiles[plant]["age"] +1
                    
                    self.tiles[plant]["timer"] = 0
                   
                    if self.tiles[plant]["age"] > len(self.colour[self.tiles[plant]["type"]]) - 1:  #out of index fix
                        self.tiles[plant]["age"] = len(self.colour[self.tiles[plant]["type"]]) - 1
        

    def draw(self, scroll, tile_size = 25):
        for tile in self.tiles:
            x = pygame.Rect(int(tile[0])* tile_size + scroll[0], int(tile[1])* tile_size + scroll[1], tile_size, tile_size)
            pygame.draw.rect(self.game.screen, self.colour[self.tiles[tile]["type"]][self.tiles[tile]['age']], x)