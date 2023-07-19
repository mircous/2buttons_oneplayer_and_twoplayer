import pygame
import random
import time

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
GRAVITY = 0.5
JUMP_FORCE = -1
width = 800
height = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Define colors (RGB format)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)


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



class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = ((head_x + dx) % GRID_WIDTH, (head_y + dy) % GRID_HEIGHT)
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        tail_x, tail_y = self.body[-1]
        dx, dy = self.direction
        new_tail = ((tail_x - dx) % GRID_WIDTH, (tail_y - dy) % GRID_HEIGHT)
        self.body.append(new_tail)


def generate_food(snake):
    while True:
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if food not in snake.body:
            return food




pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My platformer Game")

background_img = pygame.image.load("start_screen.png")

start_btn_img = pygame.image.load("start_button.png")
button_width = 200
button_height = 100
start_btn_img = pygame.transform.scale(start_btn_img, (button_width, button_height))
start_btn_rect = start_btn_img.get_rect(center=(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
start_btn_rect2 = start_btn_img.get_rect(center=(SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT // 2))

hero = Hero(100, 485, 100, 100)
platforms = [
    Platform(0, 580, 230, 10),
    Platform(345, 520, 348, 10),
    Platform(420, 400, 138, 10),
    Platform(130, 365, 170, 10),
    Platform(690, 580, 115, 10),
    Platform(345, 240, 115, 10),
    Platform(0, 138, 230, 10),
    Platform(508, 165, 112, 10),
    Platform(731, 138, 200, 10),
]

all_sprites = pygame.sprite.Group()
all_sprites.add(hero)
all_sprites.add(*platforms)

second_game = False
running = True
game_started = False

clock = pygame.time.Clock()
snake = Snake()
snake2 = Snake()
food = generate_food(snake)
food = generate_food(snake2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif hero.rect.y > 490:
            screen.blit(end_screen_img, end_screen_rect)
            pygame.display.flip()
            time.sleep(5)
            running = False
        elif hero.rect.y <= 40 and hero.rect.x >= 800:
            screen.blit(win_screen_img, win_screen_rect)
            pygame.display.flip()
            time.sleep(5)
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_btn_rect.collidepoint(mouse_pos):
                game_started = True
            elif start_btn_rect2.collidepoint(mouse_pos):
                second_game = True

    if game_started:
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
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, (player_x, player_y, player_size, player_size))
        pygame.draw.rect(screen, WHITE, (enemy_x, enemy_y, enemy_size, enemy_size))
        pygame.display.update()

    elif second_game:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            snake.direction = (0, -1)
        elif keys[pygame.K_DOWN]:
            snake.direction = (0, 1)
        elif keys[pygame.K_LEFT]:
            snake.direction = (-1, 0)
        elif keys[pygame.K_RIGHT]:
            snake.direction = (1, 0)

        

        if keys[pygame.K_w]:
            snake2.direction = (0, -1)
        elif keys[pygame.K_s]:
            snake2.direction = (0, 1)
        elif keys[pygame.K_a]:
            snake2.direction = (-1, 0)
        elif keys[pygame.K_d]:
            snake2.direction = (1, 0)
        snake.move()
        snake2.move()

        if snake.body[0] == food:
            snake.grow()
            food = generate_food(snake)


        if snake2.body[0] == food:
            snake2.grow()
            food = generate_food(snake2)

        screen.fill(BLACK)

        # Draw the snake
        for segment in snake.body:
            pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        for segment in snake2.body:
            pygame.draw.rect(screen, ORANGE, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        # Draw the food
        pygame.draw.rect(screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        pygame.display.flip()
        clock.tick(10)  # Adjust the snake's speed here


    else:
        screen.blit(background_img, (0, 0))
        screen.blit(start_btn_img, start_btn_rect)
        screen.blit(start_btn_img, start_btn_rect2)
        pygame.display.flip()

pygame.quit()
