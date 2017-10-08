import random


class Item:
    """Items are mandatory to win the game. McGyver have to collect them."""

    def __init__(self, img):
        """An item is placed randomly in the map."""
        self._img = img
        self._x_random = random.randrange(1, 14)
        self._y_random = random.randrange(1, 14)

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
