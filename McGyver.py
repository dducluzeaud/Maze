import re


class McGyver:
    """McGyver have to collect 3 items to get out of the maze, if he don't he
    die."""

    def __init__(self):
        """At the start of the game McGyver is at the position 1, 1. He have a backpack to be able to count the items he collet"""
        self._x = 1
        self._y = 1
        self._backpack = 0

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def backpack(self):
        return self._backpack

    @backpack.setter
    def backpack(self, item):
        print("You collect {}".format(item))
        self._backpack += 1

    def teleport(self, maze):
        """McGyver has the ability to go anywhere in the map"""

        teleport = False

        while not teleport:
            try:
                line = int(input("Line: "))
                column = int(input("Column: "))
                if re.search(r"(^[(\s)GPLN]$)", maze.coord[(line, column)]):
                    # delete the position of McGyver
                    maze.coord[(self._x, self._y)] = " "
                    # McGyver teleport himself in the new position
                    maze.coord[line, column] = 'M'
                    self._x, self._y = line, column
                    teleport = True
                else:
                    print("McGyver can't teleport here, try again !")
            except KeyError:
                print("You try to teleport out of the boundaries!")
            except ValueError:
                print("You must use integer!")
