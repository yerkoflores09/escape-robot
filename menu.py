import pygame
import sys

pygame.init()

#pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Escape Robot - Menú")

#colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (180, 180, 180)
GRIS_OSCURO = (100, 100, 100)
MORADO = (58, 0, 112)

#fuentes
boton_fuente = pygame.font.Font("sprites/04B_30__.TTF", 50)

#logo
logo = pygame.image.load("sprites/logo.jpg").convert_alpha()
logo = pygame.transform.scale(logo, (200, 200))



#función dibujar botón
def dibujar_boton(texto, x, y, ancho, alto, color_normal, color_hover, mouse_pos):
    if x <= mouse_pos[0] <= x + ancho and y <= mouse_pos[1] <= y + alto:
        color = color_hover
    else:
        color = color_normal

    pygame.draw.rect(pantalla, color, (x, y, ancho, alto))
    texto_superficie = boton_fuente.render(texto, True, BLANCO)
    pantalla.blit(texto_superficie, (x + ancho//2 - texto_superficie.get_width()//2,
                                     y + alto//2 - texto_superficie.get_height()//2))

    
    click = pygame.mouse.get_pressed()
    if click[0] == 1 and x <= mouse_pos[0] <= x + ancho and y <= mouse_pos[1] <= y + alto:
        pygame.time.delay(200)  #evita multiples clics
        return True
    return False

#bucle principal
def mostrar_menu():
    while True:
        pantalla.fill(NEGRO)
        mouse_pos = pygame.mouse.get_pos()

    
        #botón JUGAR
        if dibujar_boton("Jugar", ANCHO//2 - 150, 250, 300, 70, MORADO, GRIS, mouse_pos):
            return "jugar"

        #botón OPCIONES
        if dibujar_boton("Opciones", ANCHO//2 - 150, 350, 300, 70, MORADO, GRIS, mouse_pos):
            print("Opciones")

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        pantalla.blit(logo, (ANCHO//2 - logo.get_width()//2, 30))
    
        pygame.display.update()