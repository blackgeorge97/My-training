import pygame
from model import Game
from render import Renderer

INPUT = {pygame.K_UP: 'up', pygame.K_RIGHT: 'right', pygame.K_LEFT: 'left', pygame.K_SPACE: 'space'}
FPS = 60

done = False
clock = pygame.time.Clock()
game = Game()
drawer = Renderer(game)
direction = 'none'
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            try:
                input = INPUT[event.key]
            except:
                pass
        elif event.type == pygame.KEYUP:
            input = 'none'
    game.read_input(input)
    game.integrate()
    drawer.draw_game(game)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
