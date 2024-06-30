import os
import sys
import config
import pygame

def mensaje_final(screen, mensaje, color, reloj, fuente):
    # Dividir el mensaje en líneas donde se detecte el signo de dólar
    lineas = mensaje.split('$')

    # Crear una nueva fuente para el texto "Presiona Enter para continuar"
    fuente_continuar = pygame.font.Font(os.path.join(config.FONTS_DIR, "minecraft.ttf"), 30)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                return

        screen.fill((0,0,0))

        # Calcular el tamaño total del mensaje incluyendo el texto "Presiona Enter para continuar"
        altura_total = sum(fuente.render(linea, True, color).get_height() for linea in lineas)
        altura_total += fuente_continuar.render("Presiona Enter para continuar", True, color).get_height() + 40

        # Calcular la posición inicial para centrar el mensaje verticalmente
        posicion_y_inicial = config.ALTO_VENTANA // 2 - altura_total // 2

        # Renderizar cada línea del mensaje
        y_offset = posicion_y_inicial
        for linea in lineas:
            texto = fuente.render(linea, True, color)
            screen.blit(texto, (config.ANCHO_VENTANA // 2 - texto.get_width() // 2, y_offset))
            y_offset += texto.get_height()

        # Renderizar el texto "Presiona Enter para continuar"
        texto_continuar = fuente_continuar.render("Presiona Enter para continuar", True, color)
        screen.blit(texto_continuar, (config.ANCHO_VENTANA // 2 - texto_continuar.get_width() // 2, y_offset + 40))

        pygame.display.flip()
        reloj.tick(config.FPS)

def images_fondo_load():
    animation_load = []
    for i in range(6):
        img_path = os.path.join(config.TOSHI_DIR, "loading", f"load{i}.png")
        img = pygame.image.load(img_path)
        animation_load.append(img)
    return animation_load

def escalar_imagen(image, scale):
    w = image.get_width()
    h = image.get_height()
    new_image = pygame.transform.scale(image, (int(w * scale), int(h * scale)))
    return new_image

def mostrar_indicador_mouse(buttons):
    mouse_pos = pygame.mouse.get_pos()
    if any(boton.collidepoint(mouse_pos) for boton in buttons):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

def fondo_loading(screen):
    pygame.mixer.music.stop()
    animation_load = images_fondo_load()
    for frame in animation_load:
        screen.blit(frame, (0, 0))
        pygame.display.flip()
        pygame.time.delay(500)
    # Limpiar la cola de eventos de Pygame
    pygame.event.clear()