import pygame
import constants


class Tile(pygame.sprite.Sprite):
    def __init__(self, position, dimensions=constants.tile_basic_size, color=constants.tile_basic_color):
        super().__init__()
        self.position = position
        self.image = pygame.Surface(dimensions)
        self.image.fill(color)
        self.rect = self.image.get_rect(midtop=position)


class TileManager:
    def __init__(self):
        self.tiles = [Tile((150, 550)), Tile((150, 450)), Tile((150, 350))]
        self.tiles_type = [Tile]
        self.group = pygame.sprite.Group()
        self.group.add(self.tiles)

    def addTile(self, offset=10, type_of_tile=0):
        self.tiles.append(self.tiles_type[type_of_tile](self.tiles[-1].position))
        self.group.add(self.tiles[-1])

    def draw(self, screen):
        self.group.draw(screen)

    def push_down_tiles(self, diff):
        torem = False
        for t in self.tiles:
            ny = t.rect.midtop[1] + diff
            t.rect.midtop = (t.rect.midtop[0], ny)
            if ny > constants.screen_size[1]:
                torem = True

        if torem:
            self.tiles.pop(0)