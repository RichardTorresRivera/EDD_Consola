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

def transicion(screen, speed):
    fade = pygame.Surface(screen.get_size())
    fade.fill((255, 255, 255))
    for alpha in range(0, 255, speed):
        fade.set_alpha(alpha)
        screen.fill((0, 0, 0))
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        pygame.time.delay(15)

def historia_loading(screen, images, audio_path, reloj):
    # Cargar el audio
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    # Duraciones en milisegundos
    image_durations = [10000, 10000, 13000]  # 10s, 10s, 13s

    # Loop para mostrar las imágenes y capturar eventos
    i = 0
    for img in images:
        
        # Mostrar imagen
        screen.blit(img, (0, 0))
        pygame.display.flip()

        # Tiempo que la imagen debe mostrarse
        image_start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - image_start_time < image_durations[i]:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    pygame.mixer.music.stop()
                    return
            
            reloj.tick(config.FPS)
        
        # Transición entre imágenes
        if i < len(images) - 1:
            transicion(screen, 4)
        i += 1
    
    pygame.mixer.music.stop()