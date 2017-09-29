import random

class Maze:


    def __init__(self):
        self.file = "map.txt"
        self.coord = {}

    def generate_maze(self):
        """Open and read the file containing the maze. Each char in the file
        will get the coordinates in a dictionnary
        """
        with open(self.file, "r") as map_file:
            id_line = 0
            for line in map_file:
                id_column = 0
                for char in line:
                    self.coord[(id_line, id_column)] = char
                    id_column += 1
                id_line += 1

    def display_maze(self):
        for value in self.coord.values():
            print(value, end="")

    def random_coordinates(self, item):

        item_placed = False
        item.x_random = random.randrange(1,13)
        item.y_random = random.randrange(1,13)

        while not item_placed:
            if self.coord[(item.x_random, item.y_random)] == " ":
                self.coord[(item.x_random, item.y_random)] = item.img
                item_placed = True
            else:
                item.x_random = random.randrange(1,13)
                item.y_random = random.randrange(1,13)

    def game_over(self, mac):
        if self.coord[(mac.x, mac.y)] == self.coord[(1, 13)]:
            print("You won")
            return True
