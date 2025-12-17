import pygame
from laberinto1 import Laberinto1
from laberinto2 import Laberinto2
from player import Player
from enemy import Enemy
from star import Star
from portal import Portal
from ajustes import WIDTH, HEIGHT, FPS, NEGRO


class Game():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.4)

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Escape Robot')
        self.clock = pygame.time.Clock()

        #nivel actual
        self.level = 1

        #cargar nivel inicial
        self.cargar_nivel()

        #fuente del HUD
        self.font = pygame.font.SysFont('Consolas', 18)

    def cargar_nivel(self):
        #detener música anterior
        pygame.mixer.music.stop()

        #musica del laberinto
        pygame.mixer.music.load("sprites/music-laberinto.mp3")
        pygame.mixer.music.play(-1)

        #nivel 1
        if self.level == 1:
            self.laberinto = Laberinto1()
            self.player = Player(self.laberinto)

            self.enemy = Enemy(400, 150, "vertical", 1)
            self.enemy2 = Enemy(50, 440, "vertical", 1)
            self.enemy3 = Enemy(650, 350, "horizontal", 1)

            self.stars = [
                Star(200, 550),
                Star(675, 100),
                Star(500, 325)
            ]

            self.portal = Portal(685, 485)

        #nivel 2
        elif self.level == 2:
            self.laberinto = Laberinto2()
            self.player = Player(self.laberinto)

            self.enemy = Enemy(125, 425, "vertical", 2)
            self.enemy2 = Enemy(475, 175, "vertical", 2)
            self.enemy3 = Enemy(475, 25, "vertical", 2)

            self.stars = [
                Star(225, 550),
                Star(700, 25),
                Star(500, 175)
            ]

            self.portal = Portal(675, 475)

    def reset_level(self):
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
                    pygame.mixer.music.stop()
                    return None

            keys = pygame.key.get_pressed()
            self.player.update(keys)

            self.enemy.update()
            self.enemy2.update()
            self.enemy3.update()

            if (self.player.rect.colliderect(self.enemy.rect) or
                self.player.rect.colliderect(self.enemy2.rect) or
                self.player.rect.colliderect(self.enemy3.rect)):
                self.reset_level()

            stars_collected = 0
            for star in self.stars:
                if not star.collected and self.player.rect.colliderect(star.rect):
                    star.collected = True
                if star.collected:
                    stars_collected += 1

            if self.player.rect.colliderect(self.portal.rect):
                if stars_collected == len(self.stars):
                    if self.level == 1:
                        self.level = 2
                        self.cargar_nivel()
                    else:
                        pygame.mixer.music.stop()
                        return 'completado'

            self.screen.fill(NEGRO)
            self.laberinto.draw(self.screen)

            for star in self.stars:
                star.draw(self.screen)

            self.portal.draw(self.screen)

            self.enemy.draw(self.screen)
            self.enemy2.draw(self.screen)
            self.enemy3.draw(self.screen)

            self.player.draw(self.screen)

            nivel_text = self.font.render(f'Nivel: {self.level}', True, (255, 255, 255))
            stars_text = self.font.render(
                f'Estrellas: {stars_collected}/{len(self.stars)}',
                True,
                (255, 255, 255)
            )

            self.screen.blit(nivel_text, (10, 5))
            self.screen.blit(stars_text, (120, 5))

            pygame.display.flip()