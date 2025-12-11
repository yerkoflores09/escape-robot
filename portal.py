import pygame
from ajustes import TILE

class Portal():
    def __init__(self, x, y):

        self.image = pygame.image.load('sprites/portal.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(TILE*4), int(TILE*4)))

        #rectangulo del portal
        self.rect = self.image.get_rect(topleft=(x, y))


    def draw(self, screen):
        screen.blit(self.image, self.rect)