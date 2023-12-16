from pygame import Vector2
from tile import *
from enemy import *


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
        normalTile(Vector2(175, absY[4])),
    ]


def level2(lastY):
    distOfTileFromPrev = [
        -80,
        0,
        -140,
        -100,
        -100,
        -120
    ]
    absY = getAbsPos(lastY, distOfTileFromPrev)
    return [
        normalTile(Vector2(50, absY[0])),
        normalTile(Vector2(constants.screen_size[0] - 50, absY[1])),
        normalTile(Vector2(150, absY[2])),
        normalTile(Vector2(40, absY[3])),
        normalTile(Vector2(230, absY[4])),
        normalTile(Vector2(60, absY[5])),
    ]


def getAbsPos(start, distOfTileFromPrev):
    ans = []
    for i in range(len(distOfTileFromPrev)):
        if i == 0:
            ans.append(start + distOfTileFromPrev[i])
        else:
            ans.append(distOfTileFromPrev[i] + ans[i - 1])
    return ans


def appendLevel(objs, group_collider):
    if len(objs) == 0:
        lev = level1(630)
    else:
        lev = level2(objs[-1].rect.midbottom[1])
    objs += lev
    group_collider.add(lev)
