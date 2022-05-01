import pygame

class Ground (pygame.sprite.Sprite): 
    def __init__(self, rec_x, rec_y, surface):
        super().__init__()

        self.image = pygame.Surface(surface)
        self.image.fill([50, 205, 50, 0])
        self.rect = self.image.get_rect()
        self.rect.x = rec_x
        self.rect.y = rec_y

    def update(self, speed):
        self.rect.y -= speed
        if self.rect.y > 710:
            pygame.event.post(pygame.event.Event(pygame.USEREVENT))
            self.kill()