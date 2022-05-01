import pygame
from game import Game
from fonts import Fonts

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
fonts = Fonts()
is_game_running = True

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
    
while is_game_running:
    screen.fill([255, 255, 255])

    if game.app_closed:
        print('yo')
        pygame.display.flip() 

    if game.game_started:
        game.logic()

        if pygame.sprite.spritecollide(game.player, game.killzones_sprites, False):
            game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)          
        
        game.drawGame(screen)

    else:
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                game.game_started = True

        start_game_button = fonts.subtitles.render('Start game', False, (0, 0, 0))
        screen.blit(start_game_button, ((SCREEN_WIDTH - start_game_button.get_width()) // 2, (SCREEN_HEIGHT - start_game_button.get_height()) // 2))

    pygame.display.flip()

pygame.quit()
