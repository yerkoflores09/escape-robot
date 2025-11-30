import pygame
from ajustes import TILE, AZUL

#clase que representa el robot/personaje principal

class Player():
    def __init__(self, laberinto):
        self.laberinto = laberinto
        self.x = 1 * TILE
        self.y = 1 * TILE

        self.width = TILE
        self.height = TILE
        self.color = AZUL

        self.speed = 6

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def puede_moverse(self, nx, ny):
        futuro_rect = pygame.Rect(nx, ny, self.width, self.height)

        #colisiones contra las paredes del laberinto
        for fila in range(len(self.laberinto.grid)):
            for col in range(len(self.laberinto.grid[fila])):
                if self.laberinto.grid[fila][col] == 1:  # es muro
                    muro_rect = pygame.Rect(col*TILE, fila*TILE, TILE, TILE)
                    if futuro_rect.colliderect(muro_rect):
                        return False
        return True
    

    def update(self, keys):
        nx, ny = self.x, self.y

        if keys[pygame.K_UP]:
            ny -= self.speed

        if keys[pygame.K_DOWN]:
            ny += self.speed

        if keys[pygame.K_LEFT]:
            nx -= self.speed

        if keys[pygame.K_RIGHT]:
            nx += self.speed

        #validar las colisiones
        if self.puede_moverse(nx, self.y):
            self.x = nx
        if self.puede_moverse(self.x, ny):
            self.y = ny

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
