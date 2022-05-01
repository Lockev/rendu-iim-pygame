import pygame

class Player (pygame.sprite.Sprite): 
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.width = self.height = 32
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.facing = 'right'
        
        self.jump_height = 8
        self.fall_speed = 0
        self.fall_speed_per_frame = 0.16
        self.latteral_speed = 0
        self.max_latteral_speed = 3.2

        self.image = pygame.Surface([self.width, self.height])
        self.image = pygame.image.load('assets/doodle.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = (screen_width // 2) - (self.width // 2)
        self.rect.y = (screen_height // 2) - (self.height // 2)

    def jump(self):
        if self.fall_speed > 2.4: # Waits for the player to fall a little before allowing him to jump again
            self.fall_speed = -self.jump_height
    
    def move(self, x_movement):
        self.latteral_speed += x_movement
        if self.latteral_speed < -self.max_latteral_speed:
            self.latteral_speed = -self.max_latteral_speed
        elif self.latteral_speed > self.max_latteral_speed:
            self.latteral_speed = self.max_latteral_speed
    
    def gravity(self): 
        self.fall_speed += self.fall_speed_per_frame
        self.rect.y += self.fall_speed 

        if self.fall_speed < 0 and self.rect.y <= self.screen_height // 2:
            self.rect.y = self.screen_height // 2

        self.latteral_speed = self.latteral_speed * 0.995
        self.rect.x += self.latteral_speed
    
    def isSideSwapping(self):
        if self.latteral_speed > 0 and self.facing == 'left':
            self.image = pygame.transform.flip(self.image, True, False)
            self.facing = 'right'
        elif self.latteral_speed < 0 and self.facing == 'right':
            self.image = pygame.transform.flip(self.image, True, False)
            self.facing = 'left'

    def isClippingTroughSide(self):
        if self.rect.x > self.screen_width:
            self.rect.x = -40
        elif self.rect.x < -40:
            self.rect.x = self.screen_width

    def update(self):
        self.isSideSwapping()
        self.gravity()
        self.isClippingTroughSide()
        
        
    