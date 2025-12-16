import pygame
from ajustes import WIDTH, HEIGHT
from menu import Menu
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    menu = Menu(screen)

    while True:
        opcion = menu.mostrar_menu()

        if opcion == "jugar":
            juego = Game()
            resultado = juego.run()

            if resultado == "completado":
                menu.mostrar_juego_completado()

        elif opcion == "opciones":
            print("Opciones")
            pygame.time.delay(300) #corregir

if __name__ == "__main__":
    main()