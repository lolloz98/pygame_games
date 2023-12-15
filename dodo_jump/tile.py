import pygame
import constants
import effects
from movable_sprite import MovableSprite


def normalTile(position):
    return Tile(position)


def movingAsCharOnX(position, color='Blue'):
    return Tile(position, effects.MoveXEffect(), color=color)


def movingTileXY(position, color='Red', stop=(100, 100), vel=constants.moving_tile_vel):
    return Tile(position, effects.MoveBackAndForth(vel, stop=stop), color=color)


def jumpingTile(position, color='Grey'):
    return Tile(position, effects.JumpHighEffect(), color=color)


class Tile(MovableSprite):
    def __init__(
            self,
            position,
            effect=effects.Effect(),
            dimensions=constants.tile_basic_size,
            color=constants.tile_basic_color
    ):
        super().__init__(position, effect, dimensions, color)
        effect.init_pos = pygame.Vector2(position)




