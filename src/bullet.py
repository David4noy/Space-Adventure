import pygame

class Bullet:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/images/bullet.png")
        self.image = pygame.transform.scale(self.image, (10, 20))  # Resize bullet
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width // 2  # Center the bullet horizontally
        self.rect.y = y  # Start just above the player's ship
        self.speed = 10  # Bullet speed

    def move(self):
        self.rect.y -= self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
