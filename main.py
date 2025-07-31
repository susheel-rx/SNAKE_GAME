import pygame
import random
import sys

# Game settings
WIDTH, HEIGHT = 640, 480
CELL_SIZE = 20
FPS = 15

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (0, -CELL_SIZE)

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        self.body.append(self.body[-1])

    def set_direction(self, dir):
        self.direction = dir

    def collides_with_self(self):
        return self.body[0] in self.body[1:]

    def collides_with_wall(self):
        x, y = self.body[0]
        return not (0 <= x < WIDTH and 0 <= y < HEIGHT)

class Meatball:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(0, HEIGHT, CELL_SIZE)
        return (x, y)

    def respawn(self, snake_body):
        while True:
            pos = self.random_position()
            if pos not in snake_body:
                self.position = pos
                break

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    snake = Snake()
    meatball = Meatball()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, CELL_SIZE):
                    snake.set_direction((0, -CELL_SIZE))
                elif event.key == pygame.K_DOWN and snake.direction != (0, -CELL_SIZE):
                    snake.set_direction((0, CELL_SIZE))
                elif event.key == pygame.K_LEFT and snake.direction != (CELL_SIZE, 0):
                    snake.set_direction((-CELL_SIZE, 0))
                elif event.key == pygame.K_RIGHT and snake.direction != (-CELL_SIZE, 0):
                    snake.set_direction((CELL_SIZE, 0))

        snake.move()

        # Check collision with meatball
        if snake.body[0] == meatball.position:
            snake.grow()
            meatball.respawn(snake.body)

        # Check collision with self or wall
        if snake.collides_with_self() or snake.collides_with_wall():
            print("Game Over!")
            pygame.quit()
            sys.exit()

        screen.fill(BLACK)
        for segment in snake.body:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, RED, (*meatball.position, CELL_SIZE, CELL_SIZE))
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
