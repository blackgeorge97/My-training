import pygame

W = 500
H = 1000
BLACK = (0, 0, 0)
GREY = (150, 150, 150)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (128, 0, 128)
COLORS = {'I' : CYAN, 'O' : YELLOW, 'T' : PURPLE, 'S': GREEN, 'Z' : RED, 'J' : BLUE, 'L' : ORANGE}

pygame.init()

game_over_font = pygame.font.SysFont(None, int(W / 8))
score_font = pygame.font.SysFont(None, int(W / 12))

class Renderer:
    
    size = (W, H)
    
    def __init__(self):
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Tetris")

    def draw_board(self, tetris):
        self.screen.fill(GREY)
        if tetris.game_over:
            if tetris.START:
                text = game_over_font.render("WELCOME", True, RED)
            else:
                if tetris.beat_highscore:
                    text = game_over_font.render("New Highscore!", True, RED)
                else:
                    text = game_over_font.render("Game Over", True, RED)
                score_display = score_font.render("Score:" + str(tetris.score) + " Highscore:" + str(tetris.highscore), True, BLACK)
                score_display_width = score_display.get_width()
                self.screen.blit(score_display, [int(W / 2 - score_display_width / 2), int(2 * H / 5)])
            text_width = text.get_width()
            self.screen.blit(text, [int(W / 2 - text_width / 2), int(H / 4)])
            begin = score_font.render("Press space to play!", True, BLACK)
            begin_width = begin.get_width()
            self.screen.blit(begin, [int(W / 2 - begin_width / 2), int(3 * H / 5)])    
        else:
            W_BOX = W / tetris.HOR_BOXES
            H_BOX = H / tetris.VER_BOXES
            for i in range(tetris.VER_BOXES):
                for j in range(tetris.HOR_BOXES):
                    x = j * W_BOX
                    y = i * H_BOX
                    if tetris.board[i][j] == 1:
                        color = COLORS[tetris.tetromino]
                        pygame.draw.rect(self.screen, color, [x, y, W_BOX, H_BOX])
                        pygame.draw.rect(self.screen, BLACK, [x, y, W_BOX, H_BOX], 5)
                    elif tetris.board[i][j] != 0:
                        color = COLORS[tetris.board[i][j]]
                        pygame.draw.rect(self.screen, color, [x, y, W_BOX, H_BOX])
                        pygame.draw.rect(self.screen, BLACK, [x, y, W_BOX, H_BOX], 5)
