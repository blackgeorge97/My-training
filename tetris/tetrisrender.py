import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (128, 0, 128)
COLORS = {'I' : CYAN, 'O' : YELLOW, 'T' : PURPLE, 'S': GREEN, 'Z' : RED, 'J' : BLUE, 'L' : ORANGE}

def draw_board(screen, board, W, H, W_BOX, H_BOX, tetrimino):
    screen.fill(WHITE)
    for i in range(H):
        for j in range(W):
            if board[i][j] == 1:
                x = j * W_BOX
                y = i * H_BOX
                color = COLORS[tetrimino]
                pygame.draw.rect(screen, color, [x, y, W_BOX, H_BOX])
                pygame.draw.rect(screen, BLACK, [x, y, W_BOX, H_BOX], 5)
