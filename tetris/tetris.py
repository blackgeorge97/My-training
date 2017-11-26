import pygame
from model import Game
from render import Renderer

SPEED = 16
INPUT = {pygame.K_UP: 'up', pygame.K_DOWN: 'down', pygame.K_RIGHT: 'right', pygame.K_LEFT: 'left'}

done = False
clock = pygame.time.Clock()
direction = 'none'
frame = 1
tetris = Game()
drawer = Renderer()
while not done:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if tetris.game_over:
                if event.key == pygame.K_SPACE:
                    tetris.__init__() 
                    tetris.game_over = False
            else:
                try:
                    direction = INPUT[event.key]
                except:
                    pass
        elif event.type == pygame.KEYUP:
            direction = 'none' 
    if frame % 8 == 0:
        tetris.integrate()
        frame = 1
    if direction == 'up':
        direction = 'none'
        tetris.rotate()
    elif direction != 'none':
        tetris.move(direction)
    frame += 1
    drawer.draw_board(tetris)
    pygame.display.flip()
    clock.tick(SPEED)
pygame.quit()
