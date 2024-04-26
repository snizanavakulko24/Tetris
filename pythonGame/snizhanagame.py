import pygame
import random

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
CELL_SIZE = 30
GRID_WIDTH = SCREEN_WIDTH // CELL_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // CELL_SIZE
FPS = 10  # Lower FPS for slower speed
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# Tetromino shapes (S, Z, I, O, T, L, J)
SHAPES = [
    [[1, 1, 0],
     [0, 1, 1]],

    [[0, 1, 1],
     [1, 1, 0]],

    [[1, 1, 1, 1]],

    [[1, 1],
     [1, 1]],

    [[0, 1, 0],
     [1, 1, 1]],

    [[1, 0],
     [1, 0],
     [1, 1]],

    [[0, 1],
     [0, 1],
     [1, 1]]
]

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Clock to control the game speed
clock = pygame.time.Clock()

# Helper function to create a grid
def create_grid():
    return [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]

# Helper function to draw the grid
def draw_grid(grid):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[y][x] != 0:
                color = GRAY
            else:
                color = BLACK
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Helper function to create a new tetromino
def new_tetromino():
    shape = random.choice(SHAPES)
    tetromino = {
        'shape': shape,
        'x': GRID_WIDTH // 2 - len(shape[0]) // 2,
        'y': 0
    }
    return tetromino

# Helper function to draw a tetromino on the grid
def draw_tetromino(tetromino):
    shape = tetromino['shape']
    x = tetromino['x']
    y = tetromino['y']
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col] == 1:
                pygame.draw.rect(screen, WHITE, ((x + col) * CELL_SIZE, (y + row) * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Helper function to check if a tetromino can move down
def can_move_down(tetromino, grid):
    shape = tetromino['shape']
    x = tetromino['x']
    y = tetromino['y']
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col] == 1:
                if y + row + 1 >= GRID_HEIGHT or grid[y + row + 1][x + col] != 0:
                    return False
    return True

# Main game loop
def main():
    grid = create_grid()
    tetromino = new_tetromino()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if tetromino['x'] > 0:
                        tetromino['x'] -= 1
                elif event.key == pygame.K_RIGHT:
                    if tetromino['x'] + len(tetromino['shape'][0]) < GRID_WIDTH:
                        tetromino['x'] += 1
                elif event.key == pygame.K_DOWN:
                    if can_move_down(tetromino, grid):
                        tetromino['y'] += 1

        # Move tetromino down automatically
        if can_move_down(tetromino, grid):
            tetromino['y'] += 1
        else:
            # Place tetromino on the grid
            shape = tetromino['shape']
            x = tetromino['x']
            y = tetromino['y']
            for row in range(len(shape)):
                for col in range(len(shape[row])):
                    if shape[row][col] == 1:
                        grid[y + row][x + col] = 1
            # Create a new tetromino
            tetromino = new_tetromino()

        # Clear the screen
        screen.fill(BLACK)

        # Draw the grid and tetromino
        draw_grid(grid)
        draw_tetromino(tetromino)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
