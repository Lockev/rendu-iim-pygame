import pygame

class Fonts:
    def __init__(self):
        self.titles  = pygame.font.SysFont('Arial', 36, True)
        self.subtitles = pygame.font.SysFont('Arial', 24)
        self.texts = pygame.font.SysFont('Arial', 18)
        self.subtexts = pygame.font.SysFont('Arial', 12)