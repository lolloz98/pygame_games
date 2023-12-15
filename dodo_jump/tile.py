import pygame
import constants
import effects


def normalTile(position):
    return Tile(position)


def movingAsCharOnX(position, color='Blue'):
    return Tile(position, effects.MoveXEffect(), color=color)


def movingTileXY(position, color='Red', stop=(100, 100), vel=constants.moving_tile_vel):
    return Tile(position, effects.MoveBackAndForth(vel, stop=stop), color=color)


def jumpingTile(position, color='Grey'):
    return Tile(position, effects.JumpHighEffect(), color=color)


class Tile(pygame.sprite.Sprite):
    def __init__(self, position, effect=effects.Effect(), dimensions=constants.tile_basic_size, color=constants.tile_basic_color):
        super().__init__()
        effect.init_pos = pygame.Vector2(position)
        self.position = position
        self.image = pygame.Surface(dimensions)
        self.image.fill(color)
        self.rect = self.image.get_rect(midtop=position)
        self.effect = effect

    def move(self, direction, dt=1):
        # For sure there is a better way to handle movement...
        # For now it's good enough :)
        self.rect.midbottom = (
            self.rect.midbottom[0] + direction[0] * dt,
            self.rect.midbottom[1] + direction[1] * dt
        )


class TileManager:
    def __init__(self):
        self.tiles = [normalTile((150, 550)), movingTileXY((150, 350)), jumpingTile((150, 150))]
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
            if ny > constants.screen_size[1] + constants.tile_offset_to_die:
                torem = True

        if torem:
            self.tiles.pop(0)

    def apply_effects_on_tiles(self, dt):
        for tile in self.tiles:
            tile.effect.applyEffectToTile(tile, dt)
