import random


# Utility class that allows us to know which tiles are not occupied
# by the snake at any given frame
class TileManager:
    def __init__(self, max_x, max_y, w, h, snake_init_x, snake_init_y):
        self.last = (snake_init_x, snake_init_y)
        self.free = set()
        # here we could make it a  set of integers no problem
        for i in range(0, max_x, w):
            for j in range(0, max_y, h):
                self.free.add((i, j))
        self.free.remove(self.last)
        self.snake_size = 1

    def update(self, snake_size, next, last):
        if snake_size > self.snake_size:
            self.snake_size = snake_size
            self.free.add(self.last)
            self.last = last
        if next in self.free:
            self.free.remove(next)

    def getRandomFreeTile(self):
        return random.choice(list(self.free))
