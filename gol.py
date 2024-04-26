import pygame
import random

def get_next_gen(board):
    def get_live_neighbors(i, j, board):
        num_lives = 0
        numrows = len(board)
        numcols = len(board[0])
        nrow = (i-1)>=0
        prow = (i+1)<numrows
        ncol = (j-1)>=0
        pcol = (j+1)<numcols
        # print(i, j, numrows, numcols, nrow, ncol, prow, pcol)
        if nrow and ncol: num_lives += board[i-1][j-1]
        if nrow :         num_lives += board[i-1][j]
        if nrow and pcol: num_lives += board[i-1][j+1]
        # if i==3 and j==1:
        #     print(num_lives, nrow, ncol, prow, pcol, board[i-1][j-1], board[i-1][j], board[i-1][j+1])
        if ncol:          num_lives += board[i][j-1]
        if pcol:          num_lives += board[i][j+1]
        if prow and ncol: num_lives += board[i+1][j-1]
        if prow:          num_lives += board[i+1][j]
        if prow and pcol: num_lives += board[i+1][j+1]
        return num_lives

    changes = []
    for i, rows in enumerate(board):
        for j, col in enumerate(rows):
            num_lives = get_live_neighbors(i, j, board)
            if num_lives<2: changes.append([i, j, 0])
            if num_lives>3: changes.append([i, j, 0])
            if num_lives==3: changes.append([i, j, 1])
            # print(i, j, num_lives)
    for chg in changes:
        i, j, val = chg
        board[i][j] = val
    return board

def init_board(GRID_SIZE):
    grid = [[random.randint(0, 1) for _ in range(GRID_SIZE[1])] for _ in range(GRID_SIZE[0])]
    return grid

def main():
    pygame.init()

    WINDOW_SIZE = (500, 500)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Game of Life")

    GRID_SIZE = (500, 500)

    CELL_SIZE = (WINDOW_SIZE[0] // GRID_SIZE[0], WINDOW_SIZE[1] // GRID_SIZE[1])

    grid = init_board(GRID_SIZE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        for x in range(GRID_SIZE[0]):
            for y in range(GRID_SIZE[1]):
                if grid[x][y] == 1:
                    color = (0, 0, 0)  # Black
                else:
                    color = (255, 255, 255)  # White
                pygame.draw.rect(screen, color, (x * CELL_SIZE[0], y * CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1]))

        pygame.display.flip()
        # pygame.time.delay(100)
        grid = get_next_gen(grid)


    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()