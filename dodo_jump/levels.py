from pygame import Vector2
from tile import *
from enemy import *


def level1(lastY):
    distOfTileFromPrev = [
        -80,
        -80,
        -140,
        -100,
        -100
    ]
    absY = getAbsPos(lastY, distOfTileFromPrev)
    return [
        normalTile(Vector2(150, absY[0])),
        movingTileXY(Vector2(150, absY[1])),
        movingAsCharOnX(Vector2(150, absY[2])),
        jumpingTile(Vector2(150, absY[3])),
        normalTile(Vector2(150, absY[4])),
    ]


def level2(lastY):
    distOfTileFromPrev = [
        -80,
        -80,
        -140,
        -100,
        -100
    ]
    absY = getAbsPos(lastY, distOfTileFromPrev)
    return [
        normalTile(Vector2(150, absY[0])),
        disappearingTile(Vector2(250, absY[1])),
        basicEnemy(Vector2(150, absY[2])),
        basicEnemy(Vector2(300, absY[3])),
        basicEnemy(Vector2(150, absY[4])),
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
