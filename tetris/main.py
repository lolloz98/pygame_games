import pygame
from sys import exit
import pieces
from tile_manager import TileManager

# grid is 10x20
width = 300
height = 600
block_size = (30, 30)

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tetris')
# To control the max frame rate:
clock = pygame.time.Clock()

test_font = pygame.font.Font(None, 20)

piece: pieces.Piece
tile_manager: TileManager
score: int


def reset():
    global piece
    piece = pieces.generateRandomPiece((60, 60), block_size)
    global tile_manager
    tile_manager = TileManager((width, height), block_size)
    global score
    score = 0


reset()

while True:
    # draw our elements and update everything
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                piece.move(pieces.Dir.LEFT, tile_manager.group)
            if event.key == pygame.K_s:
                piece.move(pieces.Dir.RIGHT, tile_manager.group)
            if event.key == pygame.K_d:
                pass
            if event.key == pygame.K_f:
                piece.rotate(tile_manager.group)

    piece.down()
    if piece.collidedBefore():
        if piece.isCollided(tile_manager.group, height):
            piece.up()
            tile_manager.addBlocks(piece.blocks)
            s = tile_manager.detectAndDeleteCompleteRows()
            while s != 0:
                score += s * s
                s = tile_manager.detectAndDeleteCompleteRows()
            piece = pieces.generateRandomPiece((60, 60), block_size)
            if piece.isCollided(tile_manager.group, height):
                # DEATH
                reset()
                pass
        else:
            piece.setHasCollided(False)
    if piece.isCollided(tile_manager.group, height):
        piece.up()
        piece.setHasCollided()

    screen.fill('#000000')
    piece.draw(screen)
    tile_manager.draw(screen)
    text_surface = test_font.render('Score: ' + str(score), False, '#FFFFFF')

    screen.blit(text_surface, (int(width * 0.70), int(height * 0.03)))
    pygame.display.update()
    clock.tick(5)
