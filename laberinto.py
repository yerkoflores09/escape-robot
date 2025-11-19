import pygame
from ajustes import tile, blanco

#clase que representa el mapa (nivel 1)

class Laberinto():
    def __init__(self):
        #laberinto simple (de prueba)
        self.laberinto1 = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
            [1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,1,0,1],
            [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1],
            [1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]

    def draw(self, screen):
        for y, row in enumerate(self.laberinto1):
            for x, tile in enumerate(row):
                if tile == 1:
                    pygame.draw.rect(screen, blanco, (x*tile, y*tile, tile, tile))