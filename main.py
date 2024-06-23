# Archivo principal del juego
from juegos.hanoi.main import main_hanoi
from juegos.decisiones.main import main_decisiones

def main():
    print("Soy la funcion principal")
    main_decisiones() # Comentar si quieres probar el main de tu archivo

if __name__ == "__main__":
    main()