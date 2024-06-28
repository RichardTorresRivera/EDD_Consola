# Archivo principal del juego
from juegos.hanoi.main import main_hanoi
from juegos.decisiones.main import main_decisiones
from Menu.inicio import Menu

def main():
    menu = Menu()
    nivel_seleccionado = menu.mostrar_menu() # Comentar si quieres probar el main de tu archivo

if __name__ == "__main__":
    main()