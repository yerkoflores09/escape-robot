import pygame
import sys
from ajustes import WIDTH, HEIGHT, BLANCO, NEGRO, GRIS, MORADO, FPS


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Escape Robot - Menú")

        # fuentes
        self.boton_fuente = pygame.font.Font("sprites/04B_30__.TTF", 50)
        self.titulo_fuente = pygame.font.Font("sprites/04B_30__.TTF", 40)
        self.texto_fuente = pygame.font.Font("sprites/04B_30__.TTF", 20)

        # logo
        self.logo = pygame.image.load("sprites/logo.jpg").convert_alpha()
        self.logo = pygame.transform.scale(self.logo, (200, 200))

    
    def dibujar_boton(self, texto, x, y, ancho, alto, color_normal, color_hover, mouse_pos):
        if x <= mouse_pos[0] <= x + ancho and y <= mouse_pos[1] <= y + alto:
            color = color_hover
        else:
            color = color_normal

        pygame.draw.rect(self.screen, color, (x, y, ancho, alto))
        texto_surface = self.boton_fuente.render(texto, True, BLANCO)
        self.screen.blit(
            texto_surface,
            (x + ancho // 2 - texto_surface.get_width() // 2,
             y + alto // 2 - texto_surface.get_height() // 2)
        )

        click = pygame.mouse.get_pressed()
        if click[0] == 1 and x <= mouse_pos[0] <= x + ancho and y <= mouse_pos[1] <= y + alto:
            pygame.time.delay(200)
            return True
        return False

    
    def mostrar_menu(self):
        while True:
            self.clock.tick(FPS)
            self.screen.fill(NEGRO)
            mouse_pos = pygame.mouse.get_pos()

            # botón JUGAR
            if self.dibujar_boton(
                "Jugar",
                WIDTH // 2 - 150, 250, 300, 70,
                MORADO, GRIS, mouse_pos
            ):
                return "jugar"

            # botón OPCIONES
            if self.dibujar_boton(
                "Opciones",
                WIDTH // 2 - 150, 350, 300, 70,
                MORADO, GRIS, mouse_pos
            ):
                return "opciones"

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.blit(
                self.logo,
                (WIDTH // 2 - self.logo.get_width() // 2, 30)
            )

            pygame.display.update()

    
    def mostrar_juego_completado(self):
        while True:
            self.clock.tick(FPS)
            self.screen.fill(NEGRO)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            titulo = self.titulo_fuente.render("¡JUEGO COMPLETADO!", True, BLANCO)
            mensaje = self.texto_fuente.render("Gracias por jugar", True, BLANCO)
            salir = self.texto_fuente.render("Presiona ESC para salir", True, BLANCO)

            self.screen.blit(titulo, titulo.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60)))
            self.screen.blit(mensaje, mensaje.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
            self.screen.blit(salir, salir.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60)))

            pygame.display.update()