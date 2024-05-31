import pygame

class Menu:
    def __init__(self, screen):
        self.menu_len = screen.get_width() // 3.5
        self.background = pygame.Rect(0,0,(self.menu_len ),screen.get_height())
        self.colour = "#285d8f"
        self.screen = screen
        self.font = pygame.font.Font(("assets/generic.ttf"), 25)
        self.upgrades = { #type upgrade : (currency, times bought, formula/ upgrade cost)
            "multiplier" : ("wheat", 1, "self.upgrades['multiplier'][1]**2"), #x²
            "speed" : ("carrot", 1, "self.upgrades['speed'][1]**2 / 2"),#x² / 2
        }

    def upgrade(self, selected_upgrade, mouse_input):
        pass #gebruik eval()

    def draw(self, plants, selected_plant, selected_upgrade = -1):
        pygame.draw.rect(self.screen, self.colour, self.background)
        
        for num, plant in enumerate(plants):
            if plant == selected_plant:               
                score_display = self.font.render(f"{num + 1}. {plant} : {plants[plant]}", False, ("#643f1c"))
            else:
                score_display = self.font.render(f"{num + 1}. {plant} : {plants[plant]}", False, ("#8f5a28"))
            score_rect = score_display.get_rect(topleft=(10, 10 + num*30))
            self.screen.blit(score_display, score_rect)
        
        #line
        pygame.draw.rect(self.screen, "#0E3050" ,pygame.Rect(0, len(plants)*30 + 10 , self.menu_len, 15))

        for num, upgrade in enumerate(self.upgrades):
            backg_rect = pygame.Rect(0, len(plants)*30 +25 +num*64, self.menu_len, 59)
            if num == selected_upgrade: pygame.draw.rect(self.screen, "#41641c", backg_rect)  
            else: pygame.draw.rect(self.screen, "#5d8f28", backg_rect)
            
            score_display = self.font.render(f"{upgrade}, type:{self.upgrades[upgrade][0]}", True, ("#8f285d"))
            score_rect = score_display.get_rect(topleft=(0, backg_rect.top + 3))
            self.screen.blit(score_display, score_rect)

            score_display = self.font.render(f"{eval(self.upgrades[upgrade][2])}", True, ("#8f285d"))
            score_rect = score_display.get_rect(bottomright=(backg_rect.right, backg_rect.bottom - 3))
            self.screen.blit(score_display, score_rect)
