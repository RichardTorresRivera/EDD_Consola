import pygame
import random
import os

class CompleteWordsPuzzle:
    def __init__(self, screen):
        self.screen = screen
        self.word_list = ["PILA", "COLA", "ARBOL", "GRAFO", "LISTAENLAZADA"]
        self.words_guessed = []
        self.lives = 3
        self.waiting_for_key = False
        self.reset_puzzle()
        self.font = pygame.font.Font(None, 72)
        self.small_font = pygame.font.Font(None, 36)
        self.input_box = pygame.Rect(50, 400, 140, 32)
        self.active = False
        self.user_text = ''
        self.message = ''
        self.final_message = False

        # Cargar el fondo de pantalla
        self.background = pygame.image.load(os.path.join('recursos', 'palabrasHD.png')).convert()
        self.background = pygame.transform.scale(self.background, (800, 600))

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
        # Revelar algunas letras al inicio
        letters_to_reveal = random.sample(range(len(self.current_word)), len(self.current_word) // 2)
        for index in letters_to_reveal:
            self.guesses[index] = self.current_word[index]

    def handle_events(self, event):
        if self.waiting_for_key:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and self.final_message:
                    # Reiniciar el juego
                    self.message = ''
                    self.final_message = False
                    self.waiting_for_key = False
                    self.words_guessed = []
                    self.lives = 3
                    self.reset_puzzle()
                elif event.key == pygame.K_2 and self.final_message:
                    # Continuar al siguiente nivel
                    self.level_manager.next_level()
                else:
                    self.message = ''
                    self.waiting_for_key = False
                    if self.final_message:
                        self.final_message = False
                        self.words_guessed = []
                        self.lives = 3
                    else:
                        self.reset_puzzle()
            return

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

    def check_guess(self, guess):
        if len(guess) == 1 and guess.isalpha():
            if guess in self.current_word:
                for i, letter in enumerate(self.current_word):
                    if letter == guess:
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
        self.screen.blit(self.background, (0, 0))
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
            text = self.font.render(" ".join(self.guesses), True, (255, 255, 255))
            self.screen.blit(text, (50, 200))

            attempts_text = self.small_font.render(f"Attempts: {self.attempts}", True, (255, 255, 255))
            self.screen.blit(attempts_text, (50, 300))

            lives_text = self.small_font.render(f"Lives: {self.lives}", True, (255, 255, 255))
            self.screen.blit(lives_text, (50, 350))

            # Dibuja el cuadro de entrada y el texto introducido por el usuario
            txt_surface = self.small_font.render(self.user_text, True, (255, 255, 255))
            width = max(200, txt_surface.get_width() + 10)
            self.input_box.w = width
            self.screen.blit(txt_surface, (self.input_box.x + 5, self.input_box.y + 5))
            pygame.draw.rect(self.screen, (255, 255, 255), self.input_box, 2)

        pygame.display.flip()
