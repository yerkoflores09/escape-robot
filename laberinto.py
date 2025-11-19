import pygame
from ajustes import TILE, BLANCO

#clase que representa el mapa (nivel 1)

class Laberinto():
    def __init__(self):
        #laberinto simple (de prueba)
        self.grid = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
            [1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,1,0,1],
            [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1],
            [1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]

    def draw(self, screen):
        for y, row in enumerate(self.grid):
            for x, tile in enumerate(row):
                if tile == 1:
                    pygame.draw.rect(screen, BLANCO, (x*TILE, y*TILE, TILE, TILE))