from levels import *
import pygame


class MovableObjectsManager:
    def __init__(self):
        # self.tiles = [normalTile((150, 550)), movingTileXY((150, 350)), jumpingTile((150, 150))]
        self.tiles = level1(pygame.Vector2(0, 0))
        self.tiles_type = [MovableSprite]
        self.tile_group = pygame.sprite.Group()
        self.tile_group.add(self.tiles)

    def addTile(self, offset=10, type_of_tile=0):
        # todo
        pass

    def draw(self, screen):
        self.tile_group.draw(screen)

    def push_down_tiles(self, diff):
        torem = 0
        for t in self.tiles:
            ny = t.rect.midtop[1] + diff
            t.rect.midtop = (t.rect.midtop[0], ny)
            if ny > constants.screen_size[1] + constants.tile_offset_to_die:
                torem += 1

        for i in range(torem):
            self.tiles.pop(0)

    def apply_effects_on_tiles(self, dt):
        for tile in self.tiles:
            tile.effect.applyEffectToTile(tile, dt)
