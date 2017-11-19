import pygame
from tetrismodel import tetris, new_game
from tetrisrender import draw_board

HOR_BOXES = 10
VER_BOXES = 20
W = 500
H = 1000
W_BOX = W / HOR_BOXES
H_BOX = H / VER_BOXES
SPEED = 7
INPUT = {pygame.K_UP: 'up', pygame.K_DOWN: 'down', pygame.K_RIGHT: 'right', pygame.K_LEFT: 'left'}

size = (W, H)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tetris")
done = False
clock = pygame.time.Clock()
move_dir = 'none'
game_over = True
board = []
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
    if game_over:
        game_over = False
        board, tetrimino, place = new_game(HOR_BOXES, VER_BOXES)
    board, place = tetris(board, HOR_BOXES, VER_BOXES, move_dir, place) 
    draw_board(screen, board, HOR_BOXES, VER_BOXES, W_BOX, H_BOX, tetrimino)
    pygame.display.flip()
    clock.tick(SPEED)
pygame.quit()
