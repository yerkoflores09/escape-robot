import pygame
from ajustes import TILE, ROJO

class Enemy:
    def __init__(self, x, y):
        #posicion inicial
        self.start_x = x
        self.start_y = y

        #cargar sprite
        self.image = pygame.image.load('sprites/fantasma.png').convert_alpha()
        
        #redimensionar el tamaño
        self.image = pygame.transform.scale(self.image, (int(TILE*0.9), int(TILE*0.9)))

        #rectangulo basado en la imagen
        self.rect = self.image.get_rect(topleft=(x, y))

        #movimiento vertical
        self.speed = 2
        self.move_range = 3 * TILE #3 espacios hacia arriba y abajo
        self.direction = 1 #1 = abajo, -1 = arriba

    def update(self):
        #mover en Y (vertical)
        self.rect.y += self.direction * self.speed

        #cambiar direccion cuando llega al limite
        if self.rect.y > self.start_y + self.move_range:
            self.direction = -1
        if self.rect.y < self.start_y:
            self.direction = 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)
