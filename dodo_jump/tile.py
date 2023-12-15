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
    def __init__(self, position, effect=effects.Effect(), dimensions=constants.tile_basic_size,
                 color=constants.tile_basic_color):
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


