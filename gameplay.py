import pygame

class Gameplay:
    def __init__(self,  ):
        self.mouse_pos = ()

    def planting(self,events,):
        for event in events:
            if event == pygame.MOUSEBUTTONDOWN:
                mouse_pos = (pygame.mouse.get_pos)
                print(mouse_pos)