from levels import *
import pygame


class MovableObjectsManager:
    def __init__(self):
        # self.tiles = [normalTile((150, 550)), movingTileXY((150, 350)), jumpingTile((150, 150))]
        self.objs = []
        self.group = pygame.sprite.Group()
        self.appendLevels(0)

    def remove(self, movable_obj: MovableSprite):
        self.objs.remove(movable_obj)
        self.group.remove(movable_obj)

    def draw(self, screen):
        self.group.draw(screen)

    def appendLevelUntil(self, pos, score):
        pos += constants.character_max_height
        while self.objs[-1].rect.midtop[1] >= pos:
            appendLevel(self.objs, self.group, score)
        while len(self.objs) > 0 and self.objs[-1].rect.midbottom[1] <= pos:
            self.remove(self.objs[-1])
        appendLevel(self.objs, self.group, score, pos)

    def appendLevels(self, score):
        while len(self.objs) == 0 or self.objs[-1].rect.midtop[1] > 0:
            appendLevel(self.objs, self.group, score)

    def push_down_tiles(self, diff, score):
        torem = []
        for t in self.objs:
            ny = t.rect.midtop[1] + diff
            t.rect.midtop = (t.rect.midtop[0], ny)
            if ny > constants.screen_size[1] + constants.tile_offset_to_die:
                torem.append(t)

        for t in torem:
            self.remove(t)

        self.appendLevels(score)

    def apply_effects_on_tiles(self, dt):
        for tile in self.objs:
            tile.effect.applyEffectToTile(tile, dt)
