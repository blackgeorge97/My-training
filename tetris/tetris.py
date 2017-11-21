import pygame
from model import Game
from render import init, draw_board

SPEED = 4
INPUT = {pygame.K_UP: 'up', pygame.K_DOWN: 'down', pygame.K_RIGHT: 'right', pygame.K_LEFT: 'left'}

screen = init()
done = False
clock = pygame.time.Clock()
direction = 'none'
start = True
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
        tetris.move(direction)
        tetris.integrate()
    draw_board(tetris, screen)
    pygame.display.flip()
    clock.tick(SPEED)
pygame.quit()
