import re

class McGyver:

    """McGyver have to collect 3 items to get out of the maze, if he don't he
    die."""


    def __init__(self):
        self.x = 1
        self.y = 1
        self.count_items = 0

    def teleport(self, maze):
        """McGyver has the ability to go anywhere in the map"""

        teleport = False

        while not teleport:
            line = int(input())
            column = int(input())
            if re.search(r"(^[(\s)GIEO]$)", maze.coord[(line, column)]):
                # delete the position of McGyver
                maze.coord[(self.x, self.y)] = " "
                # McGyver teleport himself in the new position
                maze.coord[line, column] = 'M'
                self.x, self.y = line, column
                teleport = True
            else:
                print("McGyver can't teleport here, try again !")

    def move(self, direction, maze):
        direction = {
            z: "top",
            s: "bottom",
            q: "left",
            d: "right",
        }
