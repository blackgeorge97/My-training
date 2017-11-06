import pygame
from datetime import datetime
import math

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

pygame.init()

size = (700, 500)
center = [350, 200]
radius = 200
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Analog Clock")
dig_clock_font = pygame.font.SysFont(None, 100)
analog_clock_font = pygame.font.SysFont(None, 35)
done = False
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop 
    # --- Game logic should go here
    real_time = str(datetime.now().time())
    int_time = real_time.split('.')
    time = int_time[0]
    digital_clock = dig_clock_font.render(time, True, BLACK)
    separated_time = time.split(':')
    x_hour = center[0] + (radius - 120) * math.sin(int(separated_time[0]) % 12 * math.pi / 6)
    y_hour = center[1] - (radius - 120) * math.cos(int(separated_time[0]) % 12 * math.pi / 6)
    x_minutes = center[0] + (radius - 20) * math.sin(int(separated_time[1]) * math.pi / 30)
    y_minutes = center[1] - (radius - 20) * math.cos(int(separated_time[1]) * math.pi / 30)
    x_seconds = center[0] + (radius - 20) * math.sin(int(separated_time[2]) * math.pi / 30)
    y_seconds = center[1] - (radius - 20) * math.cos(int(separated_time[2]) * math.pi / 30)
    # --- Drawing code should go here
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, center, radius, 5)
    pygame.draw.circle(screen, BLACK, center, 5, 5)
    for i in range(1, 13):
        x = center[0] + (radius - 20)  * math.sin(i * math.pi / 6)
        y = center[1] - (radius - 20)  * math.cos(i * math.pi / 6)
        analog_hours = analog_clock_font.render(str(i), True, BLACK) 
        screen.blit(analog_hours, [x - 10, y - 10])
    for i in range(60):
        if i % 5 != 0:
            x = center[0] + (radius - 10)  * math.sin(i * math.pi / 30)
            y = center[1] - (radius - 10)  * math.cos(i * math.pi / 30)
            pygame.draw.circle(screen, BLACK, [int(x), int(y)], 5, 5)
    pygame.draw.line(screen, BLACK, center ,[x_hour, y_hour], 10)
    pygame.draw.line(screen, BLACK, center ,[x_minutes, y_minutes], 5)
    pygame.draw.line(screen, RED, center ,[x_seconds, y_seconds], 5)
    screen.blit(digital_clock, [200, 425])   
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
