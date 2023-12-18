from pygame import Vector2
from tile import *
from enemy import *
from powerup import *
import random


def level1(lastY):
    distOfTileFromPrev = [
        -80,
        -80,
        -75,
        -100,
        -80
    ]
    absY = getAbsPos(lastY, distOfTileFromPrev)
    return [
        normalTile(Vector2(150, absY[0])),
        normalTile(Vector2(250, absY[1])),
        normalTile(Vector2(50, absY[2])),
        normalTile(Vector2(170, absY[3])),
        flyPowerup(Vector2(175, absY[4])),
    ]


def level2(lastY):
    distOfTileFromPrev = [
        -80,
        -90,
        0,
        -140,
        -100,
        -100,
        -120
    ]
    absY = getAbsPos(lastY, distOfTileFromPrev)
    return [
        normalTile(Vector2(150, absY[0])),
        normalTile(Vector2(50, absY[1])),
        normalTile(Vector2(constants.screen_size[0] - 50, absY[2])),
        normalTile(Vector2(150, absY[3])),
        normalTile(Vector2(40, absY[4])),
        normalTile(Vector2(230, absY[5])),
        normalTile(Vector2(60, absY[6])),
    ]


def level3(lastY):
    distOfTileFromPrev = [
        -80,
        -100,
        -140,
        -100,
        -100,
        -120
    ]
    absY = getAbsPos(lastY, distOfTileFromPrev)
    return [
        normalTile(Vector2(150, absY[0])),
        movingAsCharOnX(Vector2(50, absY[1])),
        normalTile(Vector2(150, absY[2])),
        disappearingTile(Vector2(40, absY[3])),
        normalTile(Vector2(230, absY[4])),
        normalTile(Vector2(60, absY[5])),
    ]


def level4(lastY):
    stopy = 60
    distOfTileFromPrev = [
        -80,
        -80 - stopy,
        0,
        -180,
        -100,
        -100,
        -120
    ]
    absY = getAbsPos(lastY, distOfTileFromPrev)
    return [
        normalTile(Vector2(150, absY[0])),
        movingTileXY(Vector2(50, absY[1]), stop=(0, stopy), vel=(0, constants.moving_tile_vel[1])),
        movingTileXY(Vector2(constants.screen_size[0] - 50, absY[2]), stop=(0, stopy), vel=(0, constants.moving_tile_vel[1])),
        normalTile(Vector2(150, absY[3])),
        normalTile(Vector2(40, absY[4])),
        normalTile(Vector2(230, absY[5])),
        normalTile(Vector2(60, absY[6])),
    ]


def level5(lastY):
    distOfTileFromPrev = [
        -80,
        -80,
        -440,
        -440,
        -440,
        -100,
        -120
    ]
    absY = getAbsPos(lastY, distOfTileFromPrev)
    return [
        normalTile(Vector2(150, absY[0])),
        jumpingTile(Vector2(50, absY[1])),
        jumpingTile(Vector2(constants.screen_size[0] - 50, absY[2])),
        jumpingTile(Vector2(50, absY[3])),
        normalTile(Vector2(constants.screen_size[0] - 50, absY[4])),
        disappearingTile(Vector2(230, absY[5])),
        disappearingTile(Vector2(60, absY[6])),
    ]


def level6(lastY):
    stopy = 60
    distOfTileFromPrev = [
        -80,
        -80 - stopy,
        0,
        -155,
        -100,
        -100,
        -120
    ]
    absY = getAbsPos(lastY, distOfTileFromPrev)
    return [
        normalTile(Vector2(150, absY[0])),
        movingTileXY(Vector2(50, absY[1]), stop=(0, stopy), vel=(0, constants.moving_tile_vel[1])),
        movingTileXY(Vector2(constants.screen_size[0] - 50, absY[2]), stop=(0, stopy), vel=(0, constants.moving_tile_vel[1])),
        basicEnemy(Vector2(150, absY[3])),
        normalTile(Vector2(40, absY[4])),
        basicEnemy(Vector2(230, absY[5])),
        normalTile(Vector2(60, absY[6])),
    ]


def getAbsPos(start, distOfTileFromPrev):
    ans = []
    for i in range(len(distOfTileFromPrev)):
        if i == 0:
            ans.append(start + distOfTileFromPrev[i])
        else:
            ans.append(distOfTileFromPrev[i] + ans[i - 1])
    return ans


levelTypes = [
    level1,
    level2,
    level3,
    level4,
    level5,
    level6
]


def appendLevel(objs, group_collider, score, pos=None):
    # todo use score to select difficulty of level based on score
    if pos is None:
        pos = objs[-1].rect.midbottom[1] if len(objs) > 0 else 630

    if len(objs) == 0:
        # lev = random.choice(levelTypes)(630)
        lev = level1(pos)
    else:
        lev = random.choice(levelTypes)(pos)
    objs += lev
    group_collider.add(lev)
