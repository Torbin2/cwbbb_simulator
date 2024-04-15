import pygame


class Tiles:
    def __init__(self, game):
        self.game = game
        self.tile_size = 100
        self.tiles = {}
        self.create_tiles()
        self.colours = {
            "corn": "#ad7e29",
            "cabbage":"#15581e",
        }
    
    def create_tiles(self):
        for x in range(10):
            self.tiles[str(x) + ",0"] = {"plant": "corn", "pos":(x,0)}

    def draw(self):
        for tile in self.tiles:
            pygame.draw.rect(self.game.screen, self.colours[tile["plant"]], pygame.Rect(int(tile["pos"][0])*self.tile_size, int(tile["pos"][1])*self.tile_size, self.tile_size,self.tile_size))