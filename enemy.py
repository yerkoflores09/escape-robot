import pygame
from ajustes import TILE

class Enemy():
    def __init__(self, x, y, movement="vertical", speed=2):
        # posicion inicial
        self.start_x = x
        self.start_y = y

        # tipo de movimiento: "vertical" o "horizontal"
        self.movement = movement

        # velocidad
        self.speed = speed

        # rango de movimiento
        self.move_range = 4 * TILE
        self.direction = 1

        # cargar sprite
        self.image = pygame.image.load('sprites/fantasma.png').convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (int(TILE * 0.9), int(TILE * 0.9))
        )

        # rectangulo del enemigo
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        # movimiento vertical
        if self.movement == "vertical":
            self.rect.y += self.direction * self.speed

            if self.rect.y > self.start_y + self.move_range:
                self.direction = -1
            if self.rect.y < self.start_y:
                self.direction = 1

        # movimiento horizontal
        elif self.movement == "horizontal":
            self.rect.x += self.direction * self.speed

            if self.rect.x > self.start_x + self.move_range:
                self.direction = -1
            if self.rect.x < self.start_x:
                self.direction = 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)