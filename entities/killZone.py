import pygame

class KillZone (pygame.sprite.Sprite): 
    def __init__(self, screen_width, screen_height):
        super().__init__()

        self.image = pygame.Surface([screen_width, 1])
        self.image.fill([50, 50, 50])
        self.rect = self.image.get_rect()
        self.rect.y = screen_height - 1