import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (150, 150, 150)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
COLORS = {0: RED, 1: ORANGE, 2: YELLOW, 3: GREEN, 4: BLUE, 5: PURPLE}

pygame.init()

class Renderer:
    def __init__(self, game):
        self.size = (game.W, game.H)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Breakout')
        self.game_over_font = pygame.font.SysFont(None, int(game.W / 8))
        self.begin_font = pygame.font.SysFont(None, int(game.W / 12))
       

    def draw_game(self, game):
        if game.game_over:
            self.screen.fill(WHITE)
            if game.start:
                text = self.game_over_font.render("WELCOME", True, BLUE)
            else:
                if game.win:
                    text = self.game_over_font.render("Victory!", True, GREEN)
                else:
                    text = self.game_over_font.render("Game Over", True, RED)
            text_width = text.get_width()
            self.screen.blit(text, [int(game.W / 2 - text_width / 2), int(game.H / 4)])
            begin = self.begin_font.render("Press space to play!", True, BLACK)
            begin_width = begin.get_width()
            self.screen.blit(begin, [int(game.W / 2 - begin_width / 2), int(3 * game.H / 5)])      
            return
        self.screen.fill(BLACK)
        pygame.draw.circle(self.screen, WHITE, [game.ball_x, game.ball_y], game.BALL_R) 
        pygame.draw.rect(self.screen, GREY, [game.paddle_x, game.PADDLE_Y, game.PADDLE_W, game.PADDLE_H])
        for peace in game.peace_places:
            pygame.draw.rect(self.screen, COLORS[peace[1] % 6], [peace[0] * game.RECT_W, peace[1] * game.RECT_H, game.RECT_W, game.RECT_H])
            pygame.draw.rect(self.screen, BLACK, [peace[0] * game.RECT_W, peace[1] * game.RECT_H, game.RECT_W, game.RECT_H], 5) 
