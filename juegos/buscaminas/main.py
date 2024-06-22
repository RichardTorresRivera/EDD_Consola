import pygame
import sys
from recursos.constantes import *
from recursos.matriz import Matriz

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Buscaminas")

fondo_img = pygame.image.load('assets/images/fondos/buscaminasHD.png')
fondo_img = pygame.transform.scale(fondo_img, (ANCHO, ALTO))

# Fuente para el texto
fuente = pygame.font.Font(ruta_fuente, 30)
fuente_minas = pygame.font.Font(ruta_fuente, 24)

def mostrar_mensaje_final(pantalla, mensaje, color):
    reloj = pygame.time.Clock()
    boton_ancho, boton_alto = 200, 50
    margen_x, margen_y = 50, 10

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if (ANCHO // 2 - boton_ancho // 2 <= pos[0] <= ANCHO // 2 + boton_ancho // 2 and
                    ALTO // 2 <= pos[1] <= ALTO // 2 + boton_alto):
                    return 'jugar_de_nuevo'
                elif (ANCHO // 2 - boton_ancho // 2 <= pos[0] <= ANCHO // 2 + boton_ancho // 2 and
                      ALTO // 2 + boton_alto + margen_y <= pos[1] <= ALTO // 2 + 2 * boton_alto + margen_y):
                    return 'cerrar'

        pantalla.blit(fondo_img, (0, 0))

        texto_mensaje = fuente.render(mensaje, True, color)
        pantalla.blit(texto_mensaje, (ANCHO // 2 - texto_mensaje.get_width() // 2, ALTO // 2 - 100))

        pygame.draw.rect(pantalla, MARRON_CLARO, (ANCHO // 2 - boton_ancho // 2, ALTO // 2, boton_ancho, boton_alto))
        pygame.draw.rect(pantalla, NEGRO, (ANCHO // 2 - boton_ancho // 2, ALTO // 2, boton_ancho, boton_alto), 3)
        texto_jugar = fuente.render("Jugar de nuevo", True, NEGRO)
        pantalla.blit(texto_jugar, (ANCHO // 2 - texto_jugar.get_width() // 2, ALTO // 2 + 10))

        pygame.draw.rect(pantalla, MARRON_CLARO, (ANCHO // 2 - boton_ancho // 2, ALTO // 2 + boton_alto + margen_y, boton_ancho, boton_alto))
        pygame.draw.rect(pantalla, NEGRO, (ANCHO // 2 - boton_ancho // 2, ALTO // 2 + boton_alto + margen_y, boton_ancho, boton_alto), 3)
        texto_cerrar = fuente.render("Cerrar", True, NEGRO)
        pantalla.blit(texto_cerrar, (ANCHO // 2 - texto_cerrar.get_width() // 2, ALTO // 2 + boton_alto + margen_y + 10))

        pygame.display.flip()
        reloj.tick(30)

def main():
    while True:
        reloj = pygame.time.Clock()

        # Configuración de la matriz (ajustar según la dificultad)
        filas, columnas, minas = 12, 12, 25
        matriz = Matriz(filas, columnas, minas)
        tamaño_celda = TAMAÑO_CELDA

        # Calcular margen_x y margen_y para centrar el tablero en la pantalla
        tablero_ancho = columnas * tamaño_celda
        tablero_alto = filas * tamaño_celda
        margen_x = (ANCHO - tablero_ancho) // 2
        margen_y = (ALTO - tablero_alto) // 2

        game_over = False
        ganar = False

        while not game_over:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    columna = (pos[0] - margen_x) // tamaño_celda
                    fila = (pos[1] - margen_y) // tamaño_celda

                    # Verificar que el clic esté dentro de los límites del tablero
                    if 0 <= fila < filas and 0 <= columna < columnas:
                        if evento.button == 1:  # Botón izquierdo del ratón
                            if not matriz.revelado[fila][columna]:
                                if not matriz.revelar(fila, columna):
                                    game_over = True
                        elif evento.button == 3:  # Botón derecho del ratón
                            matriz.colocar_bandera(fila, columna)

            pantalla.blit(fondo_img, (0, 0))  # Dibujar la imagen de fondo
            matriz.mostrar(pantalla, tamaño_celda, margen_x, margen_y)  # Pasar margen_x y margen_y a la función mostrar

            # Dibujar el cuadro en la parte superior derecha
            cuadro_ancho, cuadro_alto = 200, 100
            cuadro_x, cuadro_y = ANCHO - cuadro_ancho - 10, 10
            pygame.draw.rect(pantalla, MARRON_CLARO, (cuadro_x, cuadro_y, cuadro_ancho, cuadro_alto))
            pygame.draw.rect(pantalla, NEGRO, (cuadro_x, cuadro_y, cuadro_ancho, cuadro_alto), 3)

            # Dibujar el texto "Buscaminas"
            texto_buscaminas = fuente.render("Buscaminas", True, GOLD)
            pantalla.blit(texto_buscaminas, (cuadro_x + 10, cuadro_y + 10))

            # Dibujar el texto de minas restantes
            minas_restantes = matriz.contar_minas_restantes()
            texto_minas = fuente_minas.render(f"Minas: {minas_restantes}", True, NEGRO)
            pantalla.blit(texto_minas, (cuadro_x + 10, cuadro_y + 60))

            pygame.display.flip()
            reloj.tick(30)

            # Verificar si se ha ganado
            if matriz.ganaste():
                game_over = True
                ganar = True

        mensaje = "Ganaste" if ganar else "Perdiste"
        color = (0, 255, 0) if ganar else (255, 0, 0)
        accion = mostrar_mensaje_final(pantalla, mensaje, color)

        if accion == 'cerrar':
            pygame.quit()
            sys.exit()
        elif accion == 'jugar_de_nuevo':
            continue

if __name__ == "__main__":
    main()