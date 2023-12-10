import pygame


class TileManager:
    def __init__(self, grid_size, block_size):
        self.block_size = block_size
        self.grid_size = grid_size
        self.grid = [[None for w in range(grid_size[0] // block_size[0])] for h in range(grid_size[1] // block_size[1])]
        self.group = pygame.sprite.Group()

    def addBlocks(self, blocks):
        self.group.add(blocks)
        for b in blocks:
            x = b.rect.x // self.block_size[0]
            y = b.rect.y // self.block_size[1]
            # print(x, y, len(self.grid), len(self.grid[0]))
            self.grid[y][x] = b

    def moveDownBlocksIfRowDel(self, rowToDel):
        rowToDel.insert(0, (0, []))
        move = 1
        for i in range(len(rowToDel) - 1, 0, -1):
            for j in range(rowToDel[i - 1][0] + 1, rowToDel[i][0]):
                for block in self.grid[j]:
                    if block is not None:
                        block.rect.y += move * self.block_size[1]
            move += 1
        rowToDel.pop(0)

    def detectAndDeleteCompleteRows(self):
        rowToDel = []
        for (i, r) in enumerate(self.grid):
            if None not in r:
                rowToDel.append((i, r))
                print(i, end="")

        n = len(rowToDel)

        self.moveDownBlocksIfRowDel(rowToDel)

        for ir in reversed(rowToDel):
            self.group.remove(ir[1])
            self.grid.pop(ir[0])

        for i in range(n):
            self.grid.insert(0, [None for w in range(self.grid_size[0] // self.block_size[0])])
        return n

    def draw(self, screen):
        self.group.draw(screen)

