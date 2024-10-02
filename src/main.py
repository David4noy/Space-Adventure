import pygame
import sys
import random
from config import screen_width, screen_height
from player import Player
from asteroid import Asteroid
from bullet import Bullet
from gamestate import GameState

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Adventure")

# Load the background image
background_image = pygame.image.load("assets/images/background.jpg")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Set up the game clock
clock = pygame.time.Clock()

# Create game state, player, and lists for asteroids and bullets
game_state = GameState()
player = Player()
asteroids = []
bullets = []

# Time to spawn a new asteroid (every second)
asteroid_spawn_time = pygame.USEREVENT + 1
pygame.time.set_timer(asteroid_spawn_time, 100)  # Spawn asteroid every 1 second

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for start screen interactions
        if not game_state.running:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_state.start_button_rect.collidepoint(event.pos):
                    game_state.start_game()
        
        # Spawn new asteroid if the game is running
        if game_state.running and event.type == asteroid_spawn_time:
            asteroid = Asteroid(random.randint(0, screen_width - 40), random.randint(3, 10))
            asteroids.append(asteroid)

    # Handle player input and actions if the game is running
    if game_state.running:
        keys = pygame.key.get_pressed()
        player.handle_input()

        # Handle shooting
        if keys[pygame.K_SPACE]:
            bullet = Bullet(player.rect.centerx, player.rect.y)
            bullets.append(bullet)

        # Move asteroids and bullets
        for asteroid in asteroids:
            asteroid.move()
        for bullet in bullets:
            bullet.move()

        # Remove bullets and asteroids that are off-screen
        bullets = [bullet for bullet in bullets if bullet.rect.y > 0]
        asteroids = [asteroid for asteroid in asteroids if asteroid.rect.y < screen_height]

        # Check for collisions
        for bullet in bullets:
            for asteroid in asteroids:
                if bullet.rect.colliderect(asteroid.rect):
                    bullets.remove(bullet)
                    asteroids.remove(asteroid)
                    break

        for asteroid in asteroids:
            if player.rect.colliderect(asteroid.rect):
                print("Game Over!")
                pygame.quit()
                sys.exit()

    # Draw the background
    screen.blit(background_image, (0, 0))

    # Draw different screens depending on the game state
    if game_state.running:
        player.draw(screen)
        for asteroid in asteroids:
            asteroid.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
    else:
        game_state.draw_start_screen(screen)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)
