def num_entero(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            valor = int(entrada)
            return valor
        except ValueError:
            print("Error: Debes ingresar un número entero válido.\n")

def menu_opcion(n):
    while True:
        try:
            opcion = int(input(f"Elige una opción (0-{n}): "))
            if 0 <= opcion <= n:
                return opcion
            else:
                print(f"Error: Debes elegir un número entre 0 y {n}.\n")
        except ValueError:
            print("Error: Debes ingresar un número entero.")

def arbol_opcion():
    while True:
        print()
        rpta = input("Elige una opcion (a/b - s para salir): ")
        if rpta == "a" or rpta == "b" or rpta == "s":
            return rpta
        else:
            print("Error: Opcion no valida, intente de nuevo")
