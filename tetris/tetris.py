import pygame
from model import Game
from render import init, draw_board

SPEED = 8
INPUT = {pygame.K_UP: 'up', pygame.K_DOWN: 'down', pygame.K_RIGHT: 'right', pygame.K_LEFT: 'left'}

screen = init()
done = False
clock = pygame.time.Clock()
direction = 'none'
start = True
move = False
while not done:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            try:
                direction = INPUT[event.key]
            except:
                pass
        elif event.type == pygame.KEYUP:
            direction = 'none' 
    if start:
        start = False
        tetris = Game() 
    else:
        if move:
            tetris.integrate()
            move = False
        else:
            move = True
        tetris.move(direction)
    draw_board(tetris, screen)
    pygame.display.flip()
    clock.tick(SPEED)
pygame.quit()
