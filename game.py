import pygame
from laberinto import Laberinto
from player import Player
from ajustes import ancho, alto, fps, negro

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((ancho, alto))
        pygame.display.set_caption('Escape Robot')
        self.clock = pygame.time.Clock()

        self.laberinto = Laberinto()
        self.player = Player(self.laberinto)

        def run(self):
            running = True
            while running:
                self .clock.tick(fps)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                