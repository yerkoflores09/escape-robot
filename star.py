import pygame
from ajustes import TILE

class Star:
    def __init__(self, x, y):

        self.image_original = pygame.image.load("sprites/star.png").convert_alpha()

        #ajusta el tamaño 
        self.image = pygame.transform.scale(self.image_original, (TILE, TILE))

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        #estado de recoleccion
        self.collected = False

    def draw(self, screen):
        
        if not self.collected:
            screen.blit(self.image, self.rect)