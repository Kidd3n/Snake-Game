import pygame
import sys
import random

pygame.init()

WIDTH = 400
HEIGHT = 400
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
SNAKE_SPEED = 10
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def show_game_over_screen(screen):
    font = pygame.font.Font(None, 64)
    text = font.render("¡Game Over!", True, (255, 0, 0))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))

    font_small = pygame.font.Font(None, 36)
    play_again_text = font_small.render("Presiona 'R' para jugar de nuevo", True, (0, 0, 255))
    play_again_rect = play_again_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))

    quit_text = font_small.render("Presiona 'Q' para salir", True, (0, 0, 255))
    quit_rect = quit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))

    screen.blit(text, text_rect)
    screen.blit(play_again_text, play_again_rect)
    screen.blit(quit_text, quit_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake Game')

    snake = [(5, 5)]
    snake_direction = RIGHT

    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    clock = pygame.time.Clock()

    score = 0

    key_mapping = {
        pygame.K_UP: UP,
        pygame.K_DOWN: DOWN,
        pygame.K_LEFT: LEFT,
        pygame.K_RIGHT: RIGHT,
        pygame.K_w: UP,
        pygame.K_s: DOWN,
        pygame.K_a: LEFT,
        pygame.K_d: RIGHT,
    }

    font = pygame.font.Font(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in key_mapping:
                    new_direction = key_mapping[event.key]
                    if (
                        new_direction[0] != -snake_direction[0] or
                        new_direction[1] != -snake_direction[1]
                    ):
                        snake_direction = new_direction

        head = snake[0]
        new_head = (head[0] + snake_direction[0], head[1] + snake_direction[1])
        snake.insert(0, new_head)

        if snake[0] == food:
            score += 1
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        else:
            snake.pop()

        if (
            snake[0][0] < 0
            or snake[0][0] >= GRID_WIDTH
            or snake[0][1] < 0
            or snake[0][1] >= GRID_HEIGHT
        ):
            if show_game_over_screen(screen):
                snake = [(5, 5)]
                snake_direction = RIGHT
                food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
                score = 0
            else:
                pygame.quit()
                sys.exit()

        if snake[0] in snake[1:]:
            if show_game_over_screen(screen):
                snake = [(5, 5)]
                snake_direction = RIGHT
                food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
                score = 0
            else:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        for segment in snake:
            pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        pygame.draw.rect(screen, GREEN, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        draw_text(f"Puntuación: {score}", font, (0, 0, 255), screen, WIDTH // 2, 20)

        pygame.display.update()

        clock.tick(SNAKE_SPEED)

if __name__ == "__main__":
    main()