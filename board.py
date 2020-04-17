import random
from cell import Cell

DIE = 5
GROW = 7


def chance(percent):
    x = random.randint(0, 100)
    if x <= percent:
        return True
    return False


class Board:
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.max_x = size_x - 1
        self.max_y = size_y - 1
        self.board = [[Cell(x, y) for x in range(size_x)] for y in range(size_y)]
        # self.board = []
        # for x in range(size_x):
        #     for y in range(size_y):
        #         self.board.append(Cell(x, y))

    def print(self, deb=False):
        for row in self.board:
            for cell in row:
                if deb:
                    print(f"({cell.x},{cell.y},{cell.live})", end="")
                else:
                    if cell.live:
                        print("X", end="")
                    else:
                        print("0", end="")
            print("")

    def get(self, x, y):
        return self.board[y][x].live

    def get_fate(self, x, y):
        return self.board[y][x].fate

    def set_fate(self, x, y, fate):
        self.board[y][x].fate = fate

    def set_life(self, x, y, life):
        self.board[y][x].live = life

    def random_populate(self):
        for row in self.board:
            for cell in row:
                if chance(35):
                    cell.live = True

    def populate(self, x, y):
        self.board[x - 1][y - 1].live = True

    def check_neighbours(self, x, y):
        neighbours = 0
        # check left sides
        if x > 0:
            # check left
            if self.get(x - 1, y) is True:
                neighbours += 1
            # check upper left
            if y > 0:
                if self.get(x - 1, y - 1) is True:
                    neighbours += 1
            # check lower left
            if y < self.size_y - 1:
                if self.get(x - 1, y + 1) is True:
                    neighbours += 1

        # check right sides
        if x < self.max_x:
            # check right
            if self.get(x + 1, y) is True:
                neighbours += 1
            # check upper right
            if y > 0:
                if self.get(x + 1, y - 1) is True:
                    neighbours += 1
            # check lower right
            if y < self.max_y:
                if self.get(x + 1, y + 1) is True:
                    neighbours += 1

        # check up and down
        if y > 0:
            if self.get(x, y - 1) is True:
                neighbours += 1
        if y < self.max_y:
            if self.get(x, y + 1) is True:
                neighbours += 1
        return neighbours

    def check_fate(self):
        for y in range(self.size_y):
            for x in range(self.size_x):
                n = self.check_neighbours(x, y)
                if n in [0, 1]:
                    if self.get(x, y):
                        self.set_fate(x, y, DIE)
                        print(f"cell at {x},{y} will die!")
                if n > 4:
                    self.set_fate(x, y, DIE)
                    print(f"cell at {x},{y} will die due to overpopulation!")
                if n == 3:
                    self.set_fate(x, y, GROW)
                    print(f"cell at {x},{y} will grow!")

    def apply_fate(self):
        for y in range(self.size_y):
            for x in range(self.size_x):
                fate = self.get_fate(x, y)
                if fate == DIE:
                    print(f"cell at {x},{y} died!")
                    self.set_life(x, y, False)
                    self.set_fate(x, y, None)
                if fate == GROW:
                    print(f"cell at {x},{y} was born!")
                    self.set_life(x, y, True)
                    self.set_fate(x, y, None)

    def generation(self):
        self.check_fate()
        self.apply_fate()

    def check_at(self, x, y):
        print(self.board[x - 1][y - 1].live)
