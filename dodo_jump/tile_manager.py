from levels import *


class TileManager:
    def __init__(self):
        # self.tiles = [normalTile((150, 550)), movingTileXY((150, 350)), jumpingTile((150, 150))]
        self.tiles = level1(pygame.Vector2(0, 0))
        self.tiles_type = [Tile]
        self.group = pygame.sprite.Group()
        self.group.add(self.tiles)

    def addTile(self, offset=10, type_of_tile=0):
        # todo
        pass

    def draw(self, screen):
        self.group.draw(screen)

    def push_down_tiles(self, diff):
        torem = False
        for t in self.tiles:
            ny = t.rect.midtop[1] + diff
            t.rect.midtop = (t.rect.midtop[0], ny)
            if ny > constants.screen_size[1] + constants.tile_offset_to_die:
                torem = True

        if torem:
            self.tiles.pop(0)

    def apply_effects_on_tiles(self, dt):
        for tile in self.tiles:
            tile.effect.applyEffectToTile(tile, dt)
