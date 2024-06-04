import random

# Lista de palabras relacionadas con estructuras de datos
palabras = ["PILA", "COLA", "ARBOL", "GRAFO", "LISTAENLAZADA"]

def mostrar_menu():
    """
    Muestra el menú del juego.
    """
    print("\n-----------------------------------------")
    print("|      JUEGO DE COMPLETAR PALABRAS      |")
    print("-----------------------------------------")
    print("| Toshi, el protagonista, llega a un    |")
    print("| pueblo misterioso donde las palabras  |")
    print("| estan atrapadas. Para liberarlas debe |")
    print("| adivinar una serie de claves que le   |")
    print("| faltan caracteres con ayuda de las    |")
    print("| palabras atrapadas.                   |")
    print("-----------------------------------------\n")

def elegir_palabra(palabras_disponibles):
    """
    Selecciona una palabra aleatoria de la lista de palabras disponibles.
    """
    return random.choice(palabras_disponibles)

def revelar_letras(palabra, porcentaje=0.5):
    """
    Revela un porcentaje de letras al inicio del juego.
    """
    guiones = ["_"] * len(palabra)
    letras_a_revelar = random.sample(range(len(palabra)), int(len(palabra) * porcentaje))
    for index in letras_a_revelar:
        guiones[index] = palabra[index]
    return guiones

def jugar_palabra(palabras):
    """
    Inicia el juego de adivinar la palabra.
    """
    intentos = 6
    vidas = 3
    palabras_adivinadas = []
    letras_adivinadas = set()
    palabras_disponibles = palabras[:]
    palabra_actual = elegir_palabra(palabras_disponibles)
    guiones = revelar_letras(palabra_actual)
    
    while True:
        print("\nPalabra a adivinar: " + " ".join(guiones))
        print(f"Intentos restantes: {intentos}")
        print(f"Vidas restantes: {vidas}")
        letra = input("Introduce una letra: ").upper()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, introduce una sola letra.")
            continue

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra.")
            continue

        letras_adivinadas.add(letra)

        if letra in palabra_actual:
            for i, l in enumerate(palabra_actual):
                if l == letra:
                    guiones[i] = letra
            if "_" not in guiones:
                palabras_adivinadas.append(palabra_actual)
                print(f"\n¡Felicidades! Has adivinado la palabra: {palabra_actual}")
                palabras_disponibles.remove(palabra_actual)
                if len(palabras_adivinadas) == len(palabras):
                    print("\n¡Has adivinado todas las palabras!")
                    print("Gracias por rescatarnos, el siguiente punto es un campo minado cerca. ¡Suerte!")
                    break
                else:
                    palabra_actual = elegir_palabra(palabras_disponibles)
                    guiones = revelar_letras(palabra_actual)
                    letras_adivinadas = set()
                    print("Presiona cualquier tecla para continuar a la siguiente palabra.")
                    input()
        else:
            intentos -= 1
            if intentos == 0:
                vidas -= 1
                if vidas == 0:
                    print("\n¡Has perdido todas tus vidas! Intenta de nuevo.")
                    break
                else:
                    print(f"\n¡Has fallado! Te quedan {vidas} vidas.\nPresiona cualquier tecla para continuar.")
                    intentos = 6
                    guiones = revelar_letras(palabra_actual)
                    letras_adivinadas = set()
                    input()

def main_palabras():
    """
    Función principal del juego.
    """
    mostrar_menu()
    while True:
        jugar_palabra(palabras)
        opcion = input("\n¿Quieres jugar de nuevo? (s/n): ").lower()
        if opcion != 's':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
