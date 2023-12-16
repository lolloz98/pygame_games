from pygame import Vector2
from tile import *
from enemy import *


def level1(lastY):
    return [
        normalTile(Vector2(150, lastY - 20)),
        movingTileXY(Vector2(150, lastY - 100)),
        movingAsCharOnX(Vector2(150, lastY - 180)),
        jumpingTile(Vector2(150, lastY - 300)),
        normalTile(Vector2(150, lastY - 450)),
    ]


def level2(lastY):
    return [
        normalTile(Vector2(150, lastY - 80)),
        disappearingTile(Vector2(250, lastY - 160)),
        basicEnemy(Vector2(150, lastY - 300)),
        basicEnemy(Vector2(300, lastY - 400)),
        basicEnemy(Vector2(150, lastY - 500)),
    ]


def appendLevel(objs, group_collider):
    if len(objs) == 0:
        lev = level1(550)
    else:
        lev = level2(objs[-1].rect.midbottom[1])
    objs += lev
    group_collider.add(lev)
