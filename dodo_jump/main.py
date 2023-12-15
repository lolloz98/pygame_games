import pygame
from sys import exit
import constants
import tile
import player
import time

pygame.init()

screen = pygame.display.set_mode(constants.screen_size)
pygame.display.set_caption('Dodo Game')
# To control the max frame rate:
clock = pygame.time.Clock()

test_font = pygame.font.Font(None, 20)
die_font = pygame.font.Font(None, 50)

score: int = 0
started: bool = False
died: bool = False
difficulty: int = 0
next_score_for_inc: int = 0


tile_manager = tile.TileManager()
dodo = player.Player()


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

# We make this project to be fps independent
last_time = time.time()
while True:
    tmp = time.time()
    dt = tmp - last_time
    last_time = tmp

    if dt > 3 / constants.max_fps:
        # if dt gets too large the steps of character becomes too large and we might get
        # weird behaviour
        continue

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

    dodo.moveY(dt, tile_manager.group)

    tile_manager.draw(screen)
    dodo.draw(screen)
    screen.blit(text_surface, (int(constants.screen_size[0] * 0.70), int(constants.screen_size[1] * 0.03)))

    pygame.display.update()
    clock.tick(constants.max_fps)
