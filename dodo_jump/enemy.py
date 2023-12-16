import effects
from movable_sprite import MovableSprite
import constants


def basicEnemy(position, filename=constants.wind):
    return MovableSprite(position, effects.BasicEnemy(), filename)

