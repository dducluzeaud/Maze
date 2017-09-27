from map import Maze

class McGyver:

    """McGyver have to collect 3 items to get out of the maze, if he don't he
    die."""

    def __init__(self):
        self.x = 0
        self.y = 0
        self.pipe_collected = False
        self.phial_collected = False
        self.coin_collected = False

    def teleport(self, Maze):
        """McGyver has the ability to go anywhere in the map"""

        teleport = False

        while not teleport:
            line = input()
            column = input()
            if self.coord[(line, column)] == " ":
                # delete the position of McGyver
                del self.coord[(McGyver.x, McGyver.y)]
                # McGyver teleport himself in the new position
                self.coord[line, column] = McGyver
                teleport = True
            else:
                print("McGyver can't teleport here, try again !")
