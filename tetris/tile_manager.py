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
            self.grid[x][y] = b

    def detectAndDeleteCompleteRows(self):
        rowToDel = []
        for r in reversed(self.grid):
            if None not in r:
                rowToDel.append(r)

        n = len(rowToDel)

        for r in rowToDel:
            self.group.remove(r)
            self.grid.remove(r)

        for i in range(n):
            self.grid.append([None for w in range(self.grid_size[0] // self.block_size[0])])
        return n

    def draw(self, screen):
        self.group.draw(screen)

