import pygame
from enum import Enum


def sum2(one, two):
    return one[0] + two[0], one[1] + two[1]


class Dir(Enum):
    LEFT = -1
    RIGHT = 1


def cube(center, size_of_block):
    xs, ys = size_of_block
    positions = [[(-xs, -ys), (0, -ys), (-xs, 0), (0, 0)]]
    blocks = [SingleBlock(size=size_of_block) for i in range(4)]
    return Piece(center, size_of_block, blocks, positions)


def lPiece(center, size_of_block):
    xs, ys = size_of_block
    positions = [
        [(-2 * xs, -ys), (-xs, -ys), (0, -ys), (0, 0)],
        [(-xs, ys), (-xs, 0), (-xs, -ys), (0, -ys)],
        [(xs, 0), (0, 0), (-xs, 0), (-xs, -ys)],
        [(0, -2 * ys), (0, -ys), (0, 0), (-xs, 0)],
    ]
    blocks = [SingleBlock(size=size_of_block) for i in range(4)]
    return Piece(center, size_of_block, blocks, positions)


class Piece:
    def __init__(self, center, size_of_block, blocks, positions):
        self.blocks = blocks
        self.positions = positions
        self.group = pygame.sprite.Group()
        self.group.add(self.blocks)
        self.current_pos = 0
        self.size_of_block = size_of_block
        self.center = center
        self.setBlocksPos()

    def setBlocksPos(self):
        for i, b in enumerate(self.blocks):
            b.rect.x = self.positions[self.current_pos][i][0] + self.center[0]
            b.rect.y = self.positions[self.current_pos][i][1] + self.center[1]

    def rotate(self):
        self.current_pos = (self.current_pos + 1) % len(self.positions)
        self.setBlocksPos()
        self.moveBackIfOutOfScreen()

    def moveBackIfOutOfScreen(self):
        while self.isOutOfScreenL():
            self.updateCenter((self.size_of_block[0], 0))
        while self.isOutOfScreenR():
            self.updateCenter((-self.size_of_block[0], 0))

    def move(self, direction: Dir):
        self.updateCenter((self.size_of_block[0] * direction.value, 0))
        self.moveBackIfOutOfScreen()

    def updateCenter(self, mov):
        self.center = sum2(self.center, mov)
        print("center: ", self.center)
        self.setBlocksPos()

    def down(self):
        self.updateCenter((0, self.size_of_block[1]))

    def isCollided(self, groupOfPieces, ground=0):
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


class SingleBlock(pygame.sprite.Sprite):
    def __init__(self, color='Red', size=(30, 30)):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(bottomleft=(0, 0))