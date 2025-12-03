import pygame
import sys

pygame.init()

# Pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Escape Robot - Menú")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (180, 180, 180)
GRIS_OSCURO = (100, 100, 100)
MORADO = (58, 0, 112)

# Fuentes
boton_fuente = pygame.font.Font("04B_30__.TTF", 50)

#LOGO
logo = pygame.image.load("logo.jpg").convert_alpha()
logo = pygame.transform.scale(logo, (200, 200))



# Función dibujar botón
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
        pygame.time.delay(200)  # Evita múltiples clics
        return True
    return False

# Bucle principal
while True:
    pantalla.fill(NEGRO)
    mouse_pos = pygame.mouse.get_pos()

    
    # Botón JUGAR
    if dibujar_boton("Jugar", ANCHO//2 - 150, 250, 300, 70, MORADO, GRIS, mouse_pos):
        print("Has pulsado JUGAR")

    # Botón OPCIONES
    if dibujar_boton("Opciones", ANCHO//2 - 150, 350, 300, 70, MORADO, GRIS, mouse_pos):
        print("Has pulsado OPCIONES")

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pantalla.blit(logo, (ANCHO//2 - logo.get_width()//2, 30))
    
    pygame.display.update()