import pygame
from ajustes import TILE, AZUL

#clase que representa el robot/personaje principal

class Player():
    def __init__(self, laberinto):
        self.laberinto = laberinto
        self.x = 1
        self.y = 1
        self.color = AZUL

    def puede_moverse(self, nx, ny):
        return self.laberinto.grid[ny][nx] == 0
    
    def moverse(self, dx, dy):
        nx = self.x + dx
        ny = self.y + dy

        if self.puede_moverse(nx, ny):
            self.x = nx
            self.y = ny

    def update(self, keys):
        if keys[pygame.K_UP]:
            self.moverse(0, -1)

        if keys[pygame.K_DOWN]:
            self.moverse(0, 1)

        if keys[pygame.K_LEFT]:
            self.moverse(-1, 0)

        if keys[pygame.K_RIGHT]:
            self.moverse(1, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x*TILE, self.y*TILE, TILE, TILE))
