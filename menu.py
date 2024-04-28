import pygame

class Menu:
    def __init__(self, screen):
        self.background = pygame.Rect(0,0,(screen.get_width() // 3.5),screen.get_height())
        self.colour = "#7b7f13"
        self.screen = screen
        self.font = pygame.font.Font(("assets/pixel_font.ttf"), 25)

    def draw(self,plants):
        pygame.draw.rect(self.screen, self.colour, self.background)
        
        
        score_display = self.font.render(f"{self.colour}", False, ("#8f5a28"))
        score_rect = score_display.get_rect(midtop=(200, 0))
        self.screen.blit(score_display, score_rect)