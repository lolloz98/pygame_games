from pygame import Vector2
from tile import *


def level1(p: Vector2):
    return [
        normalTile(p.elementwise() + Vector2(150, 550)),
        movingTileXY(p.elementwise() + Vector2(150, 400)),
        normalTile(p.elementwise() + Vector2(150, 200)),
        normalTile(p.elementwise() + Vector2(150, 50)),
        normalTile(p.elementwise() + Vector2(150, -20)),
    ]

