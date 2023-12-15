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


tile_manager: tile.TileManager = None
dodo: player.Player = None


def reset():
    global score
    score = 0
    global started
    started = True
    global died
    died = False
    global difficulty
    difficulty = 5
    global tile_manager
    tile_manager = tile.TileManager()
    global dodo
    dodo = player.Player()


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
            elif not started:
                started = True
            else:
                if event.key == pygame.K_a:
                    dodo.changeInDir(player.Dir.LEFT, pygame.KEYDOWN)
                if event.key == pygame.K_s:
                    pass
                if event.key == pygame.K_d:
                    dodo.changeInDir(player.Dir.RIGHT, pygame.KEYDOWN)
                if event.key == pygame.K_f:
                    pass
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                dodo.changeInDir(player.Dir.LEFT, pygame.KEYUP)
            if event.key == pygame.K_d:
                dodo.changeInDir(player.Dir.RIGHT, pygame.KEYUP)

    screen.fill('#000000')
    text_surface = test_font.render('Score: ' + str(score), False, '#FFFFFF')

    if dodo.isDead():
        died = True
        died_surface = die_font.render('You Died!', False, '#FFFFFF')
        die_rect = died_surface.get_rect(midbottom=(int(constants.screen_size[0] * 0.5), int(constants.screen_size[1] * 0.5)))
        screen.blit(died_surface, die_rect)
        big_score_surface = die_font.render('Score: ' + str(score), False, '#FFFFFF')
        big_score_ret = big_score_surface.get_rect(midtop=(int(constants.screen_size[0] * 0.5), int(constants.screen_size[1] * 0.5)))
        screen.blit(big_score_surface, big_score_ret)
        pygame.display.update()
        clock.tick(constants.max_fps)
        continue

    tile_manager.apply_effects_on_tiles(dt)
    dodo.moveX(dt)
    dodo.moveY(dt, tile_manager.group)
    if dodo.rect.midbottom[1] < constants.lift_screen_height:
        diff = constants.lift_screen_height - dodo.rect.midbottom[1]
        dodo.rect.midbottom = (dodo.rect.midbottom[0], constants.lift_screen_height)
        tile_manager.push_down_tiles(diff)
        score += diff

    tile_manager.draw(screen)
    dodo.draw(screen)
    screen.blit(
        text_surface,
        text_surface.get_rect(topright=(int(constants.screen_size[0] * 0.9), int(constants.screen_size[1] * 0.03)))
    )

    pygame.display.update()
    clock.tick(constants.max_fps)
