import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the player
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - player_size
player_speed = 5

# Set up the enemy
enemy_size = 50
enemy_x = random.randint(0, width - enemy_size)
enemy_y = 0
enemy_speed = 3

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += player_speed

    # Update enemy position
    enemy_y += enemy_speed
    if enemy_y > height:
        enemy_x = random.randint(0, width - enemy_size)
        enemy_y = 0

    # Check for collision
    if (enemy_x >= player_x and enemy_x < player_x + player_size) or (
        player_x >= enemy_x and player_x < enemy_x + enemy_size
    ):
        if (enemy_y >= player_y and enemy_y < player_y + player_size) or (
            player_y >= enemy_y and player_y < enemy_y + enemy_size
        ):
            running = False

    # Draw everything
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(window, WHITE, (enemy_x, enemy_y, enemy_size, enemy_size))
    pygame.display.update()

# Quit the game
pygame.quit()
