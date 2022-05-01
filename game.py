import pygame, math, random
from entities.killZone import KillZone
from entities.player import Player
from entities.ground import Ground
from fonts import Fonts

class Game:
    def __init__(self, screen_width, screen_height):
        self.game_started = False
        self.app_closed = False

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.clock = pygame.time.Clock()
        self.fonts = Fonts()
        self.score = 0
        
        self.grounds_sprites = pygame.sprite.Group()
        self.grounds_sprites.add(Ground((self.screen_width - 100) // 2, screen_height - 100, [64, 8]))
        self.generate_grounds(10)

        self.killzones_sprites = pygame.sprite.Group()
        self.killzone = KillZone(self.screen_width, self.screen_height)
        self.killzones_sprites.add(self.killzone)

        self.player_sprites = pygame.sprite.Group()
        self.player = Player(self.screen_width, self.screen_height)
        self.player_sprites.add(self.player)

    def logic(self):
        self.player.update()
        self.moveGrounds()

        if len(self.grounds_sprites) < 100:
            self.generate_grounds(1)

        if pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_q]:
            self.player.move(-0.5)
        if pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]:
            self.player.move(0.5)
        if pygame.sprite.spritecollide(self.player, self.grounds_sprites, False):
            self.player.jump()

        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                self.score += 1
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                print('nsm')
                self.app_closed = False

    def drawGame(self, screen):
        self.player_sprites.draw(screen)
        self.grounds_sprites.draw(screen)
        self.killzones_sprites.draw(screen)

            
        score_counter = self.fonts.titles.render(str(self.score), False, (0, 0, 0))
        screen.blit(score_counter, ((self.screen_width - score_counter.get_width()) // 2, 10))

        self.clock.tick(60)
        fps_counter = self.fonts.texts.render(str(math.trunc(self.clock.get_fps())), False, (0, 0, 0))
        screen.blit(fps_counter, (self.screen_width - fps_counter.get_width(), 0))
    
    def generate_grounds(self, amount):
        for i in range(amount): 
            self.grounds_sprites.add(Ground(random.randint(0, self.screen_width - 64), (self.screen_height - ((len(self.grounds_sprites)*100) + random.randint(0, 30))), [64, 8]))

    def moveGrounds(self):
        if self.player.rect.y <= (self.screen_height // 2) and self.player.fall_speed < 0:
            self.grounds_sprites.update(self.player.fall_speed)
            
