from pygame import Vector2
from tile import *
from enemy import *


def level1(p: Vector2):
    return [
        normalTile(p.elementwise() + Vector2(150, 550)),
        movingTileXY(p.elementwise() + Vector2(150, 400)),
        movingAsCharOnX(p.elementwise() + Vector2(150, 200)),
        jumpingTile(p.elementwise() + Vector2(150, 50)),
        normalTile(p.elementwise() + Vector2(150, -20)),
    ]


def level2(p: Vector2):
    return [
        normalTile(p.elementwise() + Vector2(150, 550)),
        basicEnemy(p.elementwise() + Vector2(250, 430)),
        basicEnemy(p.elementwise() + Vector2(150, 300)),
        basicEnemy(p.elementwise() + Vector2(300, 260)),
        basicEnemy(p.elementwise() + Vector2(150, -20)),
    ]
