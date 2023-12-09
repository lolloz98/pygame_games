import pygame
from sys import exit

width = 800
height = 400

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')
# To control the frame rate:
clock = pygame.time.Clock()

test_font = pygame.font.Font(None, 30)

snake_piece_w = 20
snake_piece_h = 20
snake_surface = pygame.Surface((snake_piece_w, snake_piece_h))
snake_surface.fill('#00FF00')

snake_pos_x = 200
snake_pos_y = 100

snake_vel_x = snake_piece_w

text_surface = test_font.render('Prova', False, '#FFFFFF')

while True:
    # draw our elements and update everything
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill('#000000')

    snake_pos_x += snake_vel_x
    if snake_pos_x > width + snake_piece_w:
        snake_pos_x = 0
    screen.blit(snake_surface, (snake_pos_x, snake_pos_y))

    screen.blit(text_surface, (700, 30))

    pygame.display.update()
    # this function says that the loop will not run
    # at more than 60 times per second.
    # this set the maximum frame rate
    # (however we are not doing anything for the minimum frame rate)
    clock.tick(60)

