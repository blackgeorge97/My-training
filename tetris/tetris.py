import pygame
from random import choice

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (128, 0, 128)
HOR_BOXES = 10
VER_BOXES = 20
W = 500
H = 1000
W_BOX = W / HOR_BOXES
H_BOX = H / VER_BOXES
SPEED = 5
I = [[HOR_BOXES / 2 - 2, 0], [HOR_BOXES / 2 - 1, 0], [HOR_BOXES / 2, 0], [HOR_BOXES / 2 + 1, 0]]
O = [[HOR_BOXES / 2 - 1, 0], [HOR_BOXES / 2 - 1, 1], [HOR_BOXES / 2, 0], [HOR_BOXES / 2, 1]]
T = [[HOR_BOXES / 2 - 2, 0], [HOR_BOXES / 2 - 1, 0], [HOR_BOXES / 2 - 1, 1], [HOR_BOXES / 2, 0]]
S = [[HOR_BOXES / 2 - 2, 1], [HOR_BOXES / 2 - 1, 1], [HOR_BOXES / 2 - 1, 0], [HOR_BOXES / 2, 0]]
Z = [[HOR_BOXES / 2 - 2, 0], [HOR_BOXES / 2 - 1, 0], [HOR_BOXES / 2 - 1, 1], [HOR_BOXES / 2, 1]]
J = [[HOR_BOXES / 2 - 2, 0], [HOR_BOXES / 2 - 1, 0], [HOR_BOXES / 2, 0], [HOR_BOXES / 2, 1]]
L = [[HOR_BOXES / 2 - 2, 1], [HOR_BOXES / 2 - 2, 0], [HOR_BOXES / 2 - 1, 0], [HOR_BOXES / 2, 0]]
TETRIMINOES = ['I', 'O', 'T', 'S', 'Z', 'J' ,'L']
PIECES = {'I' : I, 'O': O,'T' : T, 'S': S, 'Z' : Z, 'J' : J, 'L' : L}
COLORS = {'I' : CYAN, 'O' : YELLOW, 'T' : PURPLE, 'S': GREEN, 'Z' : RED, 'J' : BLUE, 'L' : ORANGE}
INPUT = {pygame.K_UP : 'up', pygame.K_DOWN : 'down', pygame.K_RIGHT : 'right', pygame.K_LEFT : 'left'}
MOVES = {'up' : [0, -1], 'down' : [0, 1], 'right' : [1, 0], 'left' : [-1, 0]}

def move_piece(move_dir, piece):
    if move_dir == 'none':
        return piece
    new_piece = []
    for box in piece:
        new_box = [box[0] + MOVES[move_dir][0], box[1] + MOVES[move_dir][1]]
        new_piece.append(new_box)
        if new_box[0] not in range(HOR_BOXES) or new_box[1] not in range(VER_BOXES):
            new_piece = piece
            break
    return new_piece

def draw_piece(piece, color):
    for box in piece:
        x = box[0] * W_BOX
        y = box[1] * H_BOX
        pygame.draw.rect(screen, color, [x, y, W_BOX, H_BOX])
        pygame.draw.rect(screen, BLACK, [x, y, W_BOX, H_BOX], 5)
pygame.init()

size = (W, H)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tetris")
done = False
clock = pygame.time.Clock()
move_dir = 'none'
tetrimino = choice(TETRIMINOES)
piece = PIECES[tetrimino]
color = COLORS[tetrimino]
while not done:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            try:
                move_dir = INPUT[event.key]
            except:
                pass
        elif event.type == pygame.KEYUP:
            move_dir = 'none'    
    piece = move_piece(move_dir, piece)        
    screen.fill(WHITE)
    draw_piece(piece, color)
    pygame.display.flip()
    clock.tick(SPEED)
pygame.quit()
