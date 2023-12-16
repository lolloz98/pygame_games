import constants
import effects
from movable_sprite import MovableSprite


def normalTile(position, filename=constants.normal_tile):
    return MovableSprite(position, filename=filename)


def movingAsCharOnX(position, filename=constants.move_x_tile):
    return MovableSprite(position, effects.MoveXEffect(), filename=filename)


def movingTileXY(position, filename=constants.move_xy_tile, stop=(100, 100), vel=constants.moving_tile_vel):
    return MovableSprite(position, effects.MoveBackAndForth(vel, stop=stop), filename=filename)


def jumpingTile(position, filename=constants.jump_tile):
    return MovableSprite(position, effects.JumpHighEffect(), filename=filename)


def disappearingTile(position, filename=constants.disappearing_tile):
    return MovableSprite(position, effects.DisappearingObj(), filename=filename)

