import pygame
from puzzles.complete_words import CompleteWordsPuzzle


class LevelManager:
    def __init__(self, screen):
        self.screen = screen
        self.current_level = 0
        self.levels = [
            CompleteWordsPuzzle(screen, self),
           
        ]

    def handle_events(self, event):
        if self.current_level < len(self.levels):
            self.levels[self.current_level].handle_events(event)

    def draw(self):
        if self.current_level < len(self.levels):
            self.levels[self.current_level].draw()

    def next_level(self):
        self.current_level += 1
