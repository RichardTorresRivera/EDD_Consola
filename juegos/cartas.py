import random

# Definición de las Listas Enlazadas
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        if not self.cabeza:
            self.cabeza = Nodo(valor)
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = Nodo(valor)

    def mostrar(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        return elementos

    def ordenar(self):
        if not self.cabeza or not self.cabeza.siguiente:
            return

        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            while siguiente:
                if actual.valor > siguiente.valor:
                    actual.valor, siguiente.valor = siguiente.valor, actual.valor
                siguiente = siguiente.siguiente
            actual = actual.siguiente

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
    print("\n----------------------------------------------")
    print("|         JUEGO DE EMPAREJAMIENTO DE CARTAS         |")
    print("| Toshi se encuentra con un viejo brujo |")
    print("| que no lo permitirá pasar hasta que haga unas adivinanzas con cartas. |")
    print("| El brujo le dirá una frase y las cartas tendrán imágenes relacionadas a ello. |")
    print("| Toshi deberá ordenarlas de tal forma que dé con la adivinanza |")
    print("|para poder completar el desafío. |")
    print("----------------------------------------------")

    for nivel in range(3):
        jugar_nivel(nivel)

    print("\n¡Felicidades! Has completado todos los niveles del juego de emparejamiento de cartas.")
    print("Puedes avanzar al siguiente desafío.")

def main():
    juego_emparejamiento_cartas()
    opcion = input("\n¿Quieres jugar de nuevo? (s/n): ").lower()
    if opcion == 's':
        main()
    else:
        print("Gracias por jugar. ¡Hasta la próxima!")

if __name__ == "__main__":
    main()
