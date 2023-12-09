import pygame
from sys import exit
from snake import Snake
from tile_manager import TileManager
from food import Food

width = 800
height = 400
grid_w = 20
grid_h = 20
snake_init_x = 100
snake_init_y = 100
food_init_x = 200
food_init_y = 100

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')
# To control the frame rate:
clock = pygame.time.Clock()

test_font = pygame.font.Font(None, 30)

snake = Snake(snake_init_x, snake_init_y, grid_w, grid_h)
tile_manager = TileManager(width, height, grid_w, grid_h, snake_init_x, snake_init_y)

food = Food(grid_w, grid_h, food_init_x, food_init_y)

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
    screen.blit(food.image, food.rect)

    if snake.isDead():
        food = Food(grid_w, grid_h, food_init_x, food_init_y)
        snake = Snake(snake_init_x, snake_init_y, grid_w, grid_h)
        tile_manager = TileManager(width, height, grid_w, grid_h, snake_init_x, snake_init_y)

    snake.draw(screen)

    # we just move the food, no need to recreate it
    if pygame.sprite.spritecollide(food, snake.head, False):
        snake.setNeedToAdd()
        # update food
        try:
            food = Food(grid_w, grid_h, *tile_manager.getRandomFreeTile())
        except IndexError:
            print("No more empty tiles :)")

    snake.applyMotion(width, height)
    snake.applyAdd()
    tile_manager.update(len(snake), snake.headPos(), snake.tailPos())

    text_surface = test_font.render('Score: ' + str(len(snake)), False, '#FFFFFF')

    screen.blit(text_surface, (700, 30))
    pygame.display.update()
    # this function says that the loop will not run
    # at more than 60 times per second.
    # this set the maximum frame rate
    # (however we are not doing anything for the minimum frame rate)
    clock.tick(15)
