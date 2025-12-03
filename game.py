import pygame
from laberinto import Laberinto
from player import Player
from enemy import Enemy
from star import Star
from ajustes import WIDTH, HEIGHT, FPS, NEGRO


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Escape Robot')
        self.clock = pygame.time.Clock()

        self.laberinto = Laberinto()
        self.player = Player(self.laberinto)

        #enemigos
        self.enemy = Enemy(75, 475) #enemigo en movimiento
        self.enemy2 = Enemy(475, 200) #quieto
        self.enemy3 = Enemy(450, 75) #quieto

        #estrellas
        self.stars = [
            Star(225, 550),
            Star(700, 25),
            Star(500, 175)
        ]

        #fuente del contador
        self.font = pygame.font.SysFont('Arial', 24)


    def reset_level(self):
        #reiniciar jugador y estrellas
        self.player.rect.x = 64
        self.player.rect.y = 64

        for star in self.stars:
            star.collected = False


    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            self.player.update(keys)

            #movimiento del enemigo 1
            self.enemy.update()

            #colisiones con enemigo
            if (self.player.rect.colliderect(self.enemy.rect) or
                self.player.rect.colliderect(self.enemy2.rect) or
                self.player.rect.colliderect(self.enemy3.rect)):
                self.reset_level()

            #colision con estrella
            stars_collected = 0
            for star in self.stars:
                if not star.collected and self.player.rect.colliderect(star.rect):
                    star.collected = True

                if star.collected:
                    stars_collected += 1

            #dibujar todo
            self.screen.fill(NEGRO)
            self.laberinto.draw(self.screen)

            #dibujar estrellas
            for star in self.stars:
                star.draw(self.screen)

            #dibujar enemigos
            self.enemy.draw(self.screen)
            self.enemy2.draw(self.screen)
            self.enemy3.draw(self.screen)

            #dibujar jugador
            self.player.draw(self.screen)

            #dibujar contador
            text = self.font.render(f'{stars_collected}/3', True, (255, 255, 255))
            self.screen.blit(text, (5, 5))

            pygame.display.flip()

        pygame.quit()
