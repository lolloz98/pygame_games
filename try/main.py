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

snake_rect = snake_surface.get_rect(topleft=(snake_pos_x, snake_pos_y))
snake_vel_x = snake_piece_w

text_surface = test_font.render('Prova', False, '#FFFFFF')

food_piece_w = 20
food_piece_h = 20
food_surface = pygame.Surface((food_piece_w, food_piece_h))
food_surface.fill('#FF0000')
food_rect = food_surface.get_rect(topleft=(100, 100))

while True:
    # draw our elements and update everything
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print('up')
            if event.key == pygame.K_d:
                print('right')

    screen.fill('#000000')

    snake_pos_x += snake_vel_x
    if snake_pos_x > width + snake_piece_w:
        snake_pos_x = 0
    snake_rect.x = snake_pos_x

    if snake_rect.colliderect(food_rect) == 1:
        print("Collision")
    screen.blit(snake_surface, snake_rect)

    screen.blit(food_surface, food_rect)
    screen.blit(text_surface, (700, 30))

    pygame.display.update()
    # this function says that the loop will not run
    # at more than 60 times per second.
    # this set the maximum frame rate
    # (however we are not doing anything for the minimum frame rate)
    clock.tick(30)

