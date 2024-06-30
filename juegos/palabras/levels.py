from puzzles.complete_words import CompleteWordsPuzzle

class LevelManager:
    def __init__(self, screen):
        self.screen = screen
        self.levels = [CompleteWordsPuzzle(screen)]
        self.current_level = 0

    def handle_events(self, event):
        self.levels[self.current_level].handle_events(event)

    def draw(self):
        self.levels[self.current_level].draw()
