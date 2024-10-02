import pygame

class Asteroid:
    def __init__(self, x_pos, speed):
        self.image = pygame.image.load("assets/images/asteroid.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = -40  # Start above the screen
        self.speed = speed

    def move(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
