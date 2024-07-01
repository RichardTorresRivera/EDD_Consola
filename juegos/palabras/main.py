import pygame
import random
import sys
import os
import config
from common.utils import mensaje_final

# Inicialización de Pygame
pygame.init()

class CompleteWordsPuzzle:
    def __init__(self, screen, nivel):
        self.screen = screen
        self.nivel = nivel
        self.word_list = self.obtener_palabras()
        self.words_guessed = []
        self.lives = 3
        self.waiting_for_key = False
        self.reset_puzzle()
        self.font = pygame.font.Font(None, 72)
        self.small_font = pygame.font.Font(None, 36)
        self.input_box = pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() - 100, 200, 32)
        self.active = False
        self.user_text = ''
        self.message = ''
        self.final_message = False

    def obtener_palabras(self):
        palabras = {
            1: ["PILA", "COLA", "ARBOL"],
            2: ["PILA", "COLA", "ARBOL", "GRAFO"],
            3: ["PILA", "COLA", "ARBOL", "GRAFO", "LISTAENLAZADA"]
        }
        return palabras[self.nivel]

    def reset_puzzle(self):
        if len(self.words_guessed) < len(self.word_list):
            remaining_words = [word for word in self.word_list if word not in self.words_guessed]
            self.current_word = random.choice(remaining_words)
            self.guesses = ["_"] * len(self.current_word)
            self.reveal_letters()
            self.attempts = 6
        else:
            self.final_message = True
            self.message = [
                "¡Has adivinado todas las palabras!",
                "Las palabras agradecen y dan información",
                "del siguiente camino que es un buscaminas",
                "que se encuentra en un campo minado cerca.",
                "",
                "Presiona 1 para reiniciar el juego",
                "Presiona 2 para continuar al siguiente nivel"
            ]
            self.waiting_for_key = True

    def reveal_letters(self):
        letters_to_reveal = random.sample(range(len(self.current_word)), len(self.current_word) // 2)
        for index in letters_to_reveal:
            self.guesses[index] = self.current_word[index]

    def handle_events(self, event):
        if self.waiting_for_key:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and self.final_message:
                    self.message = ''
                    self.final_message = False
                    self.waiting_for_key = False
                    self.words_guessed = []
                    self.lives = 3
                    self.reset_puzzle()
                elif event.key == pygame.K_2 and self.final_message:
                    return True
                else:
                    self.message = ''
                    self.waiting_for_key = False
                    if self.final_message:
                        self.final_message = False
                        self.words_guessed = []
                        self.lives = 3
                    else:
                        self.reset_puzzle()
            return False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_box.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.check_guess(self.user_text.upper())
                    self.user_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.user_text = self.user_text[:-1]
                else:
                    self.user_text += event.unicode
        return False

    def check_guess(self, guess):
        if len(guess) == 1 and guess.isalpha():
            if guess in self.current_word:
                for i, l in enumerate(self.current_word):
                    if l == guess:
                        self.guesses[i] = guess
            else:
                self.attempts -= 1

        if "_" not in self.guesses:
            self.words_guessed.append(self.current_word)
            if len(self.words_guessed) == len(self.word_list):
                self.message = [
                    "¡Has adivinado todas las palabras!",
                    "Las palabras agradecen y dan información",
                    "del siguiente camino que es un buscaminas",
                    "que se encuentra en un campo minado cerca.",
                    "",
                    "Presiona 1 para reiniciar el juego",
                    "Presiona 2 para continuar al siguiente nivel"
                ]
                self.final_message = True
            else:
                self.message = ["¡Palabra adivinada! Presiona cualquier tecla para continuar."]
            self.waiting_for_key = True

        elif self.attempts <= 0:
            self.lives -= 1
            if self.lives <= 0:
                self.message = ["¡Has perdido todas tus vidas! Intente de nuevo. Presiona cualquier tecla para reiniciar."]
                self.lives = 3
                self.words_guessed = []
            else:
                self.message = [f"¡Intento fallido! Vidas restantes: {self.lives}. Presiona cualquier tecla para continuar."]
            self.waiting_for_key = True

    def draw(self):
        if isinstance(self.message, list):
            y_offset = 100
            for line in self.message:
                text = self.small_font.render(line, True, (255, 255, 255))
                self.screen.blit(text, (50, y_offset))
                y_offset += 40
        elif self.message:
            text = self.small_font.render(self.message, True, (255, 255, 255))
            self.screen.blit(text, (50, 100))
        else:
            # Mostrar palabra a adivinar centrada en la parte inferior
            text = self.font.render(" ".join(self.guesses), True, (255, 255, 255))
            text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() - 100))
            self.screen.blit(text, text_rect.topleft)

            # Mostrar intentos y vidas en la parte superior izquierda
            attempts_text = self.small_font.render(f"Intentos: {self.attempts}", True, (255, 255, 255))
            self.screen.blit(attempts_text, (50, 50))

            lives_text = self.small_font.render(f"Vidas: {self.lives}", True, (255, 255, 255))
            self.screen.blit(lives_text, (50, 100))

            # Mostrar caja de entrada centrada en la parte inferior
            txt_surface = self.small_font.render(self.user_text, True, (255, 255, 255))
            width = max(200, txt_surface.get_width() + 10)
            self.input_box.w = width
            self.input_box.centerx = self.screen.get_width() // 2
            self.input_box.y = self.screen.get_height() - 50
            self.screen.blit(txt_surface, (self.input_box.x + 5, self.input_box.y + 5))
            pygame.draw.rect(self.screen, (255, 255, 255), self.input_box, 2)

        pygame.display.flip()

def main_palabras(screen, reloj, estado, dificultad):
    pygame.mixer.music.load(os.path.join('recursos', 'Contar Palabras - Words.mp3'))
    pygame.mixer.music.play(-1)
    
    fondo_img = pygame.image.load(os.path.join('recursos', 'palabrasHD.png')).convert()
    fondo_img = pygame.transform.scale(fondo_img, (screen.get_width(), screen.get_height()))

    juego = CompleteWordsPuzzle(screen, dificultad[0] + 1)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if juego.handle_events(event):
                running = False

        screen.blit(fondo_img, (0, 0))
        juego.draw()
        pygame.display.flip()
        reloj.tick(60)
    
    estado[0] = config.SCREEN_MAPA

if __name__ == "__main__":
    main_palabras(pygame.display.set_mode((1280, 720)), pygame.time.Clock(), [0], [0])
