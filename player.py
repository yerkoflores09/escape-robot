import pygame
from ajustes import TILE, AZUL

#clase que representa el robot/personaje principal

class Player():
    def __init__(self, laberinto):
        self.laberinto = laberinto
        self.x = 64
        self.y = 64
        self.color = AZUL
        self.speed = 4
        self.rect = pygame.Rect(self.x, self.y, TILE*0.9, TILE*0.9)

    def mover(self, dx,dy):
        #movimiento en X
        self.rect.x += dx
        for muro in self.laberinto.wall_rects:
            if self.rect.colliderect(muro):
                if dx > 0:   #moviendo derecha
                    self.rect.right = muro.left
                if dx < 0:   #moviendo izquierda
                    self.rect.left = muro.right

        #movimiento en Y
        self.rect.y += dy
        for muro in self.laberinto.wall_rects:
            if self.rect.colliderect(muro):
                if dy > 0:   # abajo
                    self.rect.bottom = muro.top
                if dy < 0:   # arriba
                    self.rect.top = muro.bottom
    

    def update(self, keys):
        dx, dy = 0, 0

        if keys[pygame.K_UP]:
            dy = -self.speed

        if keys[pygame.K_DOWN]:
            dy = self.speed

        if keys[pygame.K_LEFT]:
            dx = -self.speed

        if keys[pygame.K_RIGHT]:
            dx = self.speed

        self.mover(dx, dy)


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
