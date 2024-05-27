import pygame

class Menu:
    def __init__(self, screen):
        self.background = pygame.Rect(0,0,(screen.get_width() // 3.5),screen.get_height())
        self.colour = "#285d8f"
        self.screen = screen
        self.font = pygame.font.Font(("assets/pixel_font.ttf"), 25)
        self.upgrades = { #type upgrade : (currency, times bought, formula/ upgrade cost)
            "multiplier" : ("wheat", 1, "self.upgrades['multiplier'][1]**2"), #x²
            "speed" : ("carrot", 1, "self.upgrades['speed'][1]**2 / 2"),#x² / 2
        }

    def upgrade(self, selected_upgrade):
        pass #gebruik eval()

    def draw(self, plants, selected_plant):
        pygame.draw.rect(self.screen, self.colour, self.background)
        
        for num, plant in enumerate(plants):
            if plant == selected_plant:               
                score_display = self.font.render(f"{num + 1}. {plant} : {plants[plant]}", False, ("#643f1c"))
            else:
                score_display = self.font.render(f"{num + 1}. {plant} : {plants[plant]}", False, ("#8f5a28"))
            score_rect = score_display.get_rect(midtop=(200, 0+ num*30))
            self.screen.blit(score_display, score_rect)