import pygame
from ajustes import TILE, ROJO

class Enemy:
    def __init__(self, x, y):
        #posición inicial
        self.start_x = x
        self.start_y = y
        
        #rectángulo del enemigo
        self.rect = pygame.Rect(x, y, int(TILE*0.9), int(TILE*0.9))
        self.color = ROJO

        #movimiento vertical
        self.speed = 2
        self.move_range = 3 * TILE #3 espacios hacia arriba y abajo
        self.direction = 1 #1 = abajo, -1 = arriba

    def update(self):
        #mover en Y (vertical)
        self.rect.y += self.direction * self.speed

        #cambiar dirección cuando llega al límite
        if self.rect.y > self.start_y + self.move_range:
            self.direction = -1
        if self.rect.y < self.start_y:
            self.direction = 1

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
