import pygame

W = 500
H = 1000
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

def init():
    size = (W, H)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Tetris")
    return screen

def draw_board(tetris, screen):
    screen.fill(WHITE)
    W_BOX = W / tetris.HOR_BOXES
    H_BOX = H / tetris.VER_BOXES
    for i in range(tetris.VER_BOXES):
        for j in range(tetris.HOR_BOXES):
            x = j * W_BOX
            y = i * H_BOX
            if tetris.board[i][j] == 1:
                color = COLORS[tetris.tetromino]
                pygame.draw.rect(screen, color, [x, y, W_BOX, H_BOX])
                pygame.draw.rect(screen, BLACK, [x, y, W_BOX, H_BOX], 5)
            elif tetris.board[i][j] != 0:
                color = COLORS[tetris.board[i][j]]
                pygame.draw.rect(screen, color, [x, y, W_BOX, H_BOX])
                pygame.draw.rect(screen, BLACK, [x, y, W_BOX, H_BOX], 5)
