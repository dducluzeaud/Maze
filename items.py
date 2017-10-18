import random


class Item:
    """Items are mandatory to win the game. McGyver have to collect them."""

    def __init__(self, img, maze):
        """An item is placed randomly in the map."""
        self._img = img
        self._x_random = random.randrange(1, 13)
        self._y_random = random.randrange(1, 13)

        item_placed = False

        while not item_placed:
            self.x_random = random.randrange(1,13)
            self.y_random = random.randrange(1,13)
            if maze.coord[(self._x_random, self._y_random)] == " ":
                maze.coord[(self._x_random, self._y_random)] = self._img
                item_placed = True

    @property
    def x_random(self):
        return self._x_random

    @property
    def y_random(self):
        return self._y_random

    @x_random.setter
    def x_random(self, value):
        self._x_random = value

    @y_random.setter
    def y_random(self, value):
        self._y_random = value

    @property
    def img(self):
        return self._img

    @img.setter
    def img(self, value):
        self._img = value
