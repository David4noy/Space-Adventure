import pygame
from config import screen_width, screen_height

class GameState:
    def __init__(self):
        self.running = False
        self.font = pygame.font.Font(None, 74)
        self.start_button_font = pygame.font.Font(None, 50)

        # "Level 1" text
        self.level_text = self.font.render("Level 1", True, (255, 255, 255))
        self.level_text_rect = self.level_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))

        # Start button
        self.start_button_text = self.start_button_font.render("Start", True, (255, 255, 255))
        self.start_button_rect = self.start_button_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))

    def draw_start_screen(self, screen):
        # Draw the paused screen with "Level 1" and "Start" button
        screen.blit(self.level_text, self.level_text_rect)
        pygame.draw.rect(screen, (0, 0, 0), self.start_button_rect.inflate(20, 20))
        screen.blit(self.start_button_text, self.start_button_rect)

    def start_game(self):
        self.running = True
