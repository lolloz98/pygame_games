import effects
from movable_sprite import MovableSprite
import constants


def basicEnemy(position, dimensions=constants.basic_enemy_dims, color='Red'):
    return MovableSprite(position, effects.BasicEnemy(), dimensions, color)

