import pygame
import random
import time

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
SECS_MOVE = 0.1
STARTING_LENGTH = 5
 
def create_apple(snake):
    x_apple = random.randint(0, 49)
    y_apple = random.randint(0, 49)
    while [x_apple, y_apple] in snake:
        x_apple = random.randint(0, 49)
        y_apple = random.randint(0, 49)
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
 
pygame.display.set_caption("Snake Game")
apple = [0.0]
done = False
clock = pygame.time.Clock()
game_over = True
start = True
snake = []
highscore = 0
game_over_font = pygame.font.SysFont(None, int(W / 8))
score_font = pygame.font.SysFont(None, int(W / 12))
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if game_over == True:
                game_over = False
                start = False
                beat_highscore = False
                snake.clear()
                head_dir = 'none'
                head_x = random.randint(0, 49)
                head_y = random.randint(0, 49)
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
    if game_over == False:
        if head_dir == 'up':
            snake.insert(0, [snake[0][0], snake[0][1] - 1])
        elif head_dir == 'down':
            snake.insert(0, [snake[0][0], snake[0][1] + 1])
        elif head_dir == 'right':
            snake.insert(0, [snake[0][0] + 1, snake[0][1]])
        elif head_dir == 'left':
            snake.insert(0, [snake[0][0] - 1, snake[0][1]])
        if len(snake) > 1: 
            if snake[0] in snake[1:]:
                game_over = True
        if (snake[0][0] > 49 or snake[0][0] < 0 or 
            snake[0][1] > 49 or snake[0][1] < 0):
            game_over = True
        if head_dir != 'none':
            if snake[0] != apple and remaining_starting_boxes > 0:
                remaining_starting_boxes -= 1
            elif snake[0] == apple:
                apple = create_apple(snake)
            else:
                snake.pop(len(snake) - 1)    
    if game_over == True:
        score = len(snake) - STARTING_LENGTH
        if score > highscore:
                beat_highscore = True
                highscore = score

    screen.fill(GREY)
    if game_over == False:
        draw_snake(snake)
        x_apple = apple[0] * W_BOX
        y_apple = apple[1] * H_BOX
        pygame.draw.ellipse(screen, RED, [x_apple, y_apple, W_BOX, H_BOX])
    else:
        if start:
            text = game_over_font.render("WELCOME", True, RED)
            screen.blit(text, [int(W / 4), int(H / 4)])
        else:
            if beat_highscore:
                text = game_over_font.render("New Highscore!", True, RED)
                screen.blit(text, [int(W / 5), int(H / 5)])
            else:
                text = game_over_font.render("Game Over", True, RED)
                screen.blit(text, [int(W / 4), int(H / 4)])
            score_display = score_font.render("Score:" + str(score) + " Highscore:" + str(highscore), True, BLACK)
            screen.blit(score_display, [int(W / 4.5), int(2 * H / 5)])
        begin = score_font.render("Press an key to play!", True, BLACK)
        screen.blit(begin, [int(W / 5), int(3 * H / 5)])
    pygame.display.flip()
    time.sleep(SECS_MOVE)
    clock.tick(60)
    
pygame.quit()
