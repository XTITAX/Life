# life.py
import numpy as np

class GameOfLife:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=int)

    def set_cell(self, x, y, state):
        self.grid[y, x] = state

    def update(self):
        new_grid = self.grid.copy()
        for y in range(self.height):
            for x in range(self.width):
                alive = self.grid[y, x] == 1
                neighbors = self.count_neighbors(x, y)

                if alive and (neighbors < 2 or neighbors > 3):
                    new_grid[y, x] = 0  # Умирает
                elif not alive and neighbors == 3:
                    new_grid[y, x] = 1  # Возрождается

        self.grid = new_grid

    def count_neighbors(self, x, y):
        total = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i == 0 and j == 0) or not (0 <= x + i < self.width) or not (0 <= y + j < self.height):
                    continue
                total += self.grid[y + j, x + i]
        return total

    def reset(self):
        self.grid.fill(0)
