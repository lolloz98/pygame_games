import constants
import effects
from movable_sprite import MovableSprite


def normalTile(position):
    return MovableSprite(position)


def movingAsCharOnX(position, color='Blue'):
    return MovableSprite(position, effects.MoveXEffect(), color=color)


def movingTileXY(position, color='Purple', stop=(100, 100), vel=constants.moving_tile_vel):
    return MovableSprite(position, effects.MoveBackAndForth(vel, stop=stop), color=color)


def jumpingTile(position, color='Grey'):
    return MovableSprite(position, effects.JumpHighEffect(), color=color)


def disappearingTile(position, color='White'):
    return MovableSprite(position, effects.DisappearingObj(), color=color)

