import pygame
from config import screen_width, screen_height, ship_speed

class Player:
    def __init__(self):
        self.image = pygame.image.load("assets/images/space_ship.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = (screen_width - self.rect.width) // 2
        self.rect.y = screen_height - self.rect.height - 40

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= ship_speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += ship_speed
        if keys[pygame.K_UP]:
            self.rect.y -= ship_speed
        if keys[pygame.K_DOWN]:
            self.rect.y += ship_speed

        # Ensure the ship stays within the screen bounds
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > screen_width - self.rect.width:
            self.rect.x = screen_width - self.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > screen_height - self.rect.height:
            self.rect.y = screen_height - self.rect.height

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
