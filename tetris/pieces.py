import pygame
from enum import Enum
import random


def generateRandomPiece(center, size_of_block):
    # pieces = [cube, lPiece, tetris, zigL, zigR, tPiece]
    pieces = [cube, tPiece]
    return random.choice(pieces)(center, size_of_block)


def sum2(one, two):
    return one[0] + two[0], one[1] + two[1]


def sub2(one, two):
    return one[0] - two[0], one[1] - two[1]


class Dir(Enum):
    LEFT = -1
    RIGHT = 1


def _buildPiece(center, size_of_block, positions, color='Red', offsets=None):
    return Piece(center, size_of_block, [SingleBlock(color, size_of_block) for i in positions[0]], positions, offsets)


def cube(center, size_of_block, color='#FFFF00'):
    xs, ys = size_of_block
    positions = [[(-xs, -ys), (0, -ys), (-xs, 0), (0, 0)]]
    return _buildPiece(center, size_of_block, positions, color)


def lPiece(center, size_of_block, color='#FFA500'):
    xs, ys = size_of_block
    positions = [
        [(-2 * xs, -ys), (-xs, -ys), (0, -ys), (0, 0)],
        [(-xs, ys), (-xs, 0), (-xs, -ys), (0, -ys)],
        [(xs, 0), (0, 0), (-xs, 0), (-xs, -ys)],
        [(0, -2 * ys), (0, -ys), (0, 0), (-xs, 0)],
    ]
    return _buildPiece(center, size_of_block, positions, color)


def tetris(center, size_of_block, color='#ADD8E6'):
    xs, ys = size_of_block
    positions = [
        [(-2 * xs, 0), (-xs, 0), (0, 0), (xs, 0)],
        [(0, 2 * ys), (0, ys), (0, 0), (0, -ys)],
    ]
    return _buildPiece(center, size_of_block, positions, color)


def zigL(center, size_of_block, color='#FFA500'):
    xs, ys = size_of_block
    positions = [
        [(-2 * xs, 0), (-xs, 0), (-xs, -ys), (0, -ys)],
        [(-xs, -ys), (-xs, 0), (0, 0), (0, ys)],
    ]
    return _buildPiece(center, size_of_block, positions, color)


def zigR(center, size_of_block, color='#FF0000'):
    xs, ys = size_of_block
    positions = [
        [(-2 * xs, -ys), (-xs, 0), (-xs, -ys), (0, 0)],
        [(0, -2 * ys), (-xs, -ys), (0, -ys), (-xs, 0)],
    ]
    return _buildPiece(center, size_of_block, positions, color)


def tPiece(center, size_of_block, color='#A020F0'):
    xs, ys = size_of_block
    positions = [
        [(-xs, -ys), (0, -ys), (xs, -ys), (0, 0)],
        [(0, 0), (0, -ys), (0, -2 * ys), (-xs, -ys)],
        [(-xs, 0), (0, 0), (xs, 0), (0, -ys)],
        [(-xs, ys), (-xs, 0), (-xs, -ys), (0, 0)],
    ]
    offsets = [(0, 0), (0, 0), (0, 0), (0, -ys)]
    return _buildPiece(center, size_of_block, positions, color, offsets)


class Piece:
    def __init__(self, center, size_of_block, blocks, positions, offsets=None):
        if offsets is None:
            offsets = [(0, 0) for i in positions]
        self.blocks = blocks
        self.positions = positions
        self.offsets = offsets
        self.group = pygame.sprite.Group()
        self.group.add(self.blocks)
        self.current_pos = 0
        self.size_of_block = size_of_block
        self.center = center
        self.setBlocksPos()
        self.hasCollided = False

    def setBlocksPos(self):
        for i, b in enumerate(self.blocks):
            b.rect.x = self.positions[self.current_pos][i][0] + self.center[0]
            b.rect.y = self.positions[self.current_pos][i][1] + self.center[1]

    def _change_pos_to_back(self):
        self.current_pos = (self.current_pos - 1)
        if self.current_pos < 0:
            self.current_pos = len(self.positions) - 1

    def _change_pos_to_forward(self):
        self.current_pos = (self.current_pos + 1) % len(self.positions)

    def rotate(self, collider_group):
        self.center = sub2(self.center, self.offsets[self.current_pos])
        self._change_pos_to_forward()
        self.center = sum2(self.center, self.offsets[self.current_pos])
        self.setBlocksPos()
        if pygame.sprite.groupcollide(self.blocks, collider_group, False, False):
            # revert rotation
            self.center = sub2(self.center, self.offsets[self.current_pos])
            self._change_pos_to_back()
            self.center = sum2(self.center, self.offsets[self.current_pos])
            self.setBlocksPos()
        self.moveBackIfOutOfScreen()

    def moveBackIfOutOfScreen(self):
        while self.isOutOfScreenL():
            self.updateCenter((self.size_of_block[0], 0))
        while self.isOutOfScreenR():
            self.updateCenter((-self.size_of_block[0], 0))

    def _move(self, direction: Dir):
        self.updateCenter((self.size_of_block[0] * direction.value, 0))
        self.moveBackIfOutOfScreen()

    def move(self, direction: Dir, collider_group):
        self._move(direction)
        if pygame.sprite.groupcollide(self.blocks, collider_group, False, False):
            self._move(Dir.LEFT if direction == Dir.RIGHT else Dir.RIGHT)

    def updateCenter(self, mov):
        self.center = sum2(self.center, mov)
        self.setBlocksPos()

    def down(self):
        self.updateCenter((0, self.size_of_block[1]))

    def up(self):
        self.updateCenter((0, -self.size_of_block[1]))

    def isCollided(self, groupOfPieces, ground):
        if pygame.sprite.groupcollide(self.group, groupOfPieces, False, False):
            return True
        for b in self.blocks:
            if b.rect.y == ground:
                return True
        return False

    def isOutOfScreenL(self, left=0):
        for b in self.blocks:
            if b.rect.x < left:
                return True
        return False

    def isOutOfScreenR(self, right=300):
        for b in self.blocks:
            if b.rect.x + self.size_of_block[0] > right:
                return True
        return False

    def draw(self, screen):
        self.group.draw(screen)

    def setHasCollided(self, val=True):
        self.hasCollided = val

    def collidedBefore(self):
        return self.hasCollided


class SingleBlock(pygame.sprite.Sprite):
    def __init__(self, color='Red', size=(30, 30)):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(bottomleft=(0, 0))
