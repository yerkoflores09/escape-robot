import pygame
from laberinto import Laberinto
from player import Player
from enemy import Enemy
from ajustes import WIDTH, HEIGHT, FPS, NEGRO

#clase madre (controla las demás)

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Escape Robot')
        self.clock = pygame.time.Clock()

        self.laberinto = Laberinto()
        self.player = Player(self.laberinto)

        # ENEMIGOS
        self.enemy = Enemy(75, 475) #enemigo que se mueve
        self.enemy2 = Enemy(475, 200) #quieto
        self.enemy3 = Enemy(450, 75) #quieto

    def reset_level(self):
        # reiniciar jugador
        self.player.rect.x = 64
        self.player.rect.y = 64

    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            self.player.update(keys)

            #movimiento del enemigo
            self.enemy.update()

            #colision con enemigos
            if self.player.rect.colliderect(self.enemy.rect):
                self.reset_level()

            if self.player.rect.colliderect(self.enemy2.rect):
                self.reset_level()

            if self.player.rect.colliderect(self.enemy3.rect):
                self.reset_level()

            #dibujar
            self.screen.fill(NEGRO)
            self.laberinto.draw(self.screen)
            self.player.draw(self.screen)
            self.enemy.draw(self.screen)
            self.enemy2.draw(self.screen)
            self.enemy3.draw(self.screen)

            pygame.display.flip()

        pygame.quit()
