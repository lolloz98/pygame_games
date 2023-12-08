import pygame
from sys import exit

width = 800
height = 400

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')
# To control the frame rate:
clock = pygame.time.Clock()

test_surface_w = 100
test_surface_h = 200
test_surface = pygame.Surface((test_surface_w, test_surface_h))
test_surface.fill('#FF0000')

while True:
    # draw our elements and update everything
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface, (200, 100))
    pygame.display.update()
    # this function says that the loop will not run
    # at more than 60 times per second.
    # this set the maximum frame rate
    # (however we are not doing anything for the minimum frame rate)
    clock.tick(60)

