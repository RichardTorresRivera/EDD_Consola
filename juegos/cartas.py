import random
from edd.lista_enlazada import ListaEnlazada

# Funciones del Juego
def crear_cartas(nivel):
    cartas = list(range(1, 6 + nivel * 2))  # Incrementar el número de cartas por nivel
    random.shuffle(cartas)
    lista_enlazada = ListaEnlazada()
    for carta in cartas:
        lista_enlazada.agregar(carta)
    return lista_enlazada

def jugar_nivel(nivel):
    print(f"\n--- Nivel {nivel + 1} ---")
    print("El brujo te da las siguientes cartas desordenadas:")
    cartas = crear_cartas(nivel)
    print("Cartas desordenadas:", cartas.mostrar())

    input("Presiona Enter para ordenar las cartas...")

    cartas.ordenar()
    print("Cartas ordenadas:", cartas.mostrar())

    frase = " ".join(str(valor) for valor in cartas.mostrar())
    print(f"La clave para desbloquear la puerta es: {frase}")

def juego_emparejamiento_cartas():
    print("\n-----------------------------------------")
    print("|   JUEGO DE EMPAREJAMIENTO DE CARTAS   |")
    print("-----------------------------------------")
    print("| Toshi se encuentra con un viejo brujo |")
    print("| que no lo permitirá pasar hasta que   |")
    print("| haga unas adivinanzas con cartas.     |")
    print("| El brujo le dirá una frase y las      |")
    print("| cartas tendrán imágenes relacionadas  |")
    print("| a ello.                               |")
    print("| Toshi deberá ordenarlas de tal forma  |")
    print("| que dé con la adivinanza paea poder   |")
    print("| completar el desafío.                 |")
    print("-----------------------------------------\n")

    for nivel in range(3):
        jugar_nivel(nivel)

    print("\n¡Felicidades! Completaste todos los niveles\ndel juego de emparejamiento de cartas.")
    print("Puedes avanzar al siguiente desafío.")

def main_cartas():
    juego_emparejamiento_cartas()
    opcion = input("\n¿Quieres jugar de nuevo? (s/n): ").lower()
    if opcion == 's':
        main_cartas()
    else:
        print("Gracias por jugar. ¡Hasta la próxima!")
