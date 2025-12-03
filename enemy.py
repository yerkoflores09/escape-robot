import pygame
from ajustes import TILE

class Enemy:
    def __init__(self, x, y):
        # posición inicial
        self.start_x = x
        self.start_y = y
        
        # rectángulo del enemigo
        self.rect = pygame.Rect(x, y, int(TILE*0.9), int(TILE*0.9))
        self.color = (255, 0, 0)  # rojo

        # Movimiento vertical
        self.speed = 2
        self.move_range = 3 * TILE   # 3 espacios hacia arriba y abajo
        self.direction = 1           # 1 = abajo, -1 = arriba

    def update(self):
        # Mover en Y (vertical)
        self.rect.y += self.direction * self.speed

        # Cambiar dirección cuando llega al límite
        if self.rect.y > self.start_y + self.move_range:
            self.direction = -1
        if self.rect.y < self.start_y:
            self.direction = 1

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
