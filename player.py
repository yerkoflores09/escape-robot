import pygame
from ajustes import TILE

#clase que representa el robot/personaje principal

class Player():
    def __init__(self, laberinto):
        self.laberinto = laberinto
        self.x = 64
        self.y = 64
        self.speed = 4

        hitbox_size = int(TILE*0.9)
        offset = (TILE - hitbox_size) // 2
        self.rect = pygame.Rect(self.x + offset, self.y + offset, hitbox_size, hitbox_size)

        #direccion inicial
        self.direccion = 'right'

        #sprite
        self.sprite_base = pygame.image.load('sprites/robot1-yellow.png').convert_alpha()
        #escalar al tamaño del TILE
        self.sprite_base = pygame.transform.scale(self.sprite_base, (TILE, TILE))

        self.sprite = self.sprite_base
        

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
            self.direccion = "left" #gira a la izquierda
            self.sprite = pygame.transform.flip(self.sprite_base, True, False)

        if keys[pygame.K_RIGHT]:
            dx = self.speed
            self.direccion = "right" #gira a la derecha
            self.sprite = self.sprite_base

        self.mover(dx, dy)


    def draw(self, screen):

        draw_x = self.rect.centerx - TILE // 2
        draw_y = self.rect.centery - TILE // 2
        screen.blit(self.sprite, (draw_x, draw_y))
