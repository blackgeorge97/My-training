import pygame
from random import randint

BLACK = (0, 0, 0)
GREY = (70, 70, 70)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
W = 800
H = 800
HOR_BOXES = 50
VER_BOXES = 50
W_BOX = W / HOR_BOXES
H_BOX = H / VER_BOXES
SPEED = 10
STARTING_LENGTH = 5
MOVES = {'up' : [0, -1], 'down' : [0, 1], 'right' : [1, 0], 'left' : [-1, 0]}


def create_apple(snake):
    while True:
        x_apple = randint(0, HOR_BOXES - 1)
        y_apple = randint(0, VER_BOXES - 1)
        if [x_apple, y_apple] not in snake:
            break
    apple = [x_apple, y_apple]
    return apple

def draw_snake(snake):
    for box in snake:
        x = box[0] * W_BOX
        y = box[1] * H_BOX
        pygame.draw.rect(screen, GREEN, [x, y, W_BOX, H_BOX])

pygame.init()

size = (W, H)
screen = pygame.display.set_mode(size)
with open('highscore.txt', 'r') as f:
    highscore = int(f.read())
pygame.display.set_caption("Snake Game")
apple = [0.0]
done = False
clock = pygame.time.Clock()
game_over = True
start = True
snake = []
game_over_font = pygame.font.SysFont(None, int(W / 8))
score_font = pygame.font.SysFont(None, int(W / 12))
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if game_over:
                game_over = False
                start = False
                beat_highscore = False
                snake.clear()
                head_dir = 'none'
                head_x = randint(0, HOR_BOXES - 1)
                head_y = randint(0, VER_BOXES - 1)
                snake.append([head_x, head_y])
                remaining_starting_boxes = STARTING_LENGTH - 1
                apple = create_apple(snake)
            else:
                if event.key == pygame.K_UP and head_dir != 'down':
                    head_dir = 'up'
                elif event.key == pygame.K_DOWN and head_dir != 'up':
                    head_dir = 'down'
                elif event.key == pygame.K_RIGHT and head_dir != 'left':
                    head_dir = 'right'
                elif event.key == pygame.K_LEFT and head_dir != 'right':
                    head_dir = 'left' 
    if not game_over:
        if head_dir != 'none':
            snake.insert(0, [snake[0][0] + MOVES[head_dir][0], snake[0][1] + MOVES[head_dir][1]])
        if len(snake) > 1: 
            if snake[0] in snake[1:]:
                game_over = True
        if (snake[0][0] > HOR_BOXES - 1 or snake[0][0] < 0 or 
            snake[0][1] > VER_BOXES - 1 or snake[0][1] < 0):
            game_over = True
        if head_dir != 'none':
            if snake[0] != apple and remaining_starting_boxes > 0:
                remaining_starting_boxes -= 1
            elif snake[0] == apple:
                apple = create_apple(snake)
            else:
                snake.pop(len(snake) - 1)    
    if game_over:
        score = len(snake) - STARTING_LENGTH
        if score < 0:
            score = 0
        if score > highscore:
                beat_highscore = True
                highscore = score

    screen.fill(GREY)
    if not game_over:
        draw_snake(snake)
        x_apple = apple[0] * W_BOX
        y_apple = apple[1] * H_BOX
        pygame.draw.ellipse(screen, RED, [x_apple, y_apple, W_BOX, H_BOX])
    else:
        if start:
            text = game_over_font.render("WELCOME", True, RED)
        else:
            if beat_highscore:
                text = game_over_font.render("New Highscore!", True, RED)
            else:
                text = game_over_font.render("Game Over", True, RED)
            score_display = score_font.render("Score:" + str(score) + " Highscore:" + str(highscore), True, BLACK)
            score_display_width = score_display.get_width()
            screen.blit(score_display, [int(W / 2 - score_display_width / 2), int(2 * H / 5)])
        text_width = text.get_width()
        screen.blit(text, [int(W / 2 - text_width / 2), int(H / 4)])
        begin = score_font.render("Press any key to play!", True, BLACK)
        begin_width = begin.get_width()
        screen.blit(begin, [int(W / 2 - begin_width / 2), int(3 * H / 5)])
    pygame.display.flip()
    clock.tick(SPEED)
with open('highscore.txt', 'w') as f:
    f.write(str(highscore))
pygame.quit()
