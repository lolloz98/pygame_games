import pygame
from sys import exit
import time

# grid is 10x20
width = 300
height = 600
block_size = (30, 30)
spawn_point = ((width // (block_size[0] * 2)) * block_size[0], int(0.05 * height // block_size[1]) * block_size[1])

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tetris')
# To control the max frame rate:
clock = pygame.time.Clock()

test_font = pygame.font.Font(None, 20)
die_font = pygame.font.Font(None, 50)

score: int = 0
started: bool = False
died: bool = False
difficulty: int = 0
next_score_for_inc: int = 0


def reset():
    global score
    score = 0
    global started
    started = False
    global died
    died = False
    global difficulty
    difficulty = 5
    global next_score_for_inc
    next_score_for_inc = 10


reset()

while True:
    # draw our elements and update everything
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if died:
                reset()
            else:
                started = True
            if event.key == pygame.K_a:
                pass
            if event.key == pygame.K_s:
                pass
            if event.key == pygame.K_d:
                pass
            if event.key == pygame.K_f:
                pass

    screen.fill('#000000')
    text_surface = test_font.render('Score: ' + str(score), False, '#FFFFFF')

    screen.blit(text_surface, (int(width * 0.70), int(height * 0.03)))

    pygame.display.update()
    clock.tick(5)
