import pygame
import random
import time

# Constants for the game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Define colors (RGB format)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)


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




def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Amazing Snake Game")
    clock = pygame.time.Clock()

    snake = Snake()
    snake2 = Snake()
    food = generate_food(snake)
    food = generate_food(snake2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

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

if __name__ == "__main__":
    main()
