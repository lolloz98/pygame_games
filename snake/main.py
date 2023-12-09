import pygame
from sys import exit
from snake import Snake

width = 800
height = 400

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')
# To control the frame rate:
clock = pygame.time.Clock()

test_font = pygame.font.Font(None, 30)

snake = Snake()

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
                snake.changeMotionToUp()
            if event.key == pygame.K_d:
                snake.changeMotionToRight()
            if event.key == pygame.K_s:
                snake.changeMotionToDown()
            if event.key == pygame.K_a:
                snake.changeMotionToLeft()

    screen.fill('#000000')

    snake.draw(screen)

    if food_rect.colliderect(snake.parts[0].rect):
        snake.setNeedToAdd()

    snake.applyMotion(width, height)
    snake.applyAdd()

    screen.blit(food_surface, food_rect)
    screen.blit(text_surface, (700, 30))

    pygame.display.update()
    # this function says that the loop will not run
    # at more than 60 times per second.
    # this set the maximum frame rate
    # (however we are not doing anything for the minimum frame rate)
    clock.tick(15)
