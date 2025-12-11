from menu import mostrar_menu
from game import Game

def main():
    while True:
        opcion = mostrar_menu()

        if opcion == "jugar":
            juego = Game()
            juego.run()

        elif opcion == "opciones":
            print("Aquí abrirías el menú de opciones.")

if __name__ == "__main__":
    main()
