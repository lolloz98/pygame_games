import pygame
from sys import exit

# grid is 10x20
width = 300
height = 600
grid_w = 30
grid_h = 30

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')
# To control the max frame rate:
clock = pygame.time.Clock()

test_font = pygame.font.Font(None, 20)

while True:
    # draw our elements and update everything
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print('left')
            if event.key == pygame.K_s:
                print('right')
            if event.key == pygame.K_d:
                print('down')
            if event.key == pygame.K_f:
                print('rotate')

    screen.fill('#000000')

    text_surface = test_font.render('Score: ', False, '#FFFFFF')

    screen.blit(text_surface, (int(width * 0.70), int(height * 0.03)))
    pygame.display.update()
    clock.tick(15)
