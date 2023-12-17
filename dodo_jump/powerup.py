import effects
from movable_sprite import MovableSprite
import constants


def flyPowerup(position, filename=constants.wings_inactive):
    return MovableSprite(position, effects.WindPowerup(), filename)


