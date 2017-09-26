import random

class Maze:

    def __init__(self):
        self.file = "map.txt"
        self.coord = {}

    def generate_maze(self):
        """Open and read the file containing the maze. Each char in the file will get
           coordinates with a dictionnary
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
            print(value, end='')

    def place_random_object(self):
        object_placed = False
        random_object = '@'

        while not object_placed:
            x_random = random.randint(0, 14)
            y_random = random.randint(0, 14)
            if self.coord[(x_random, y_random)] == " ":
                self.coord[(x_random, y_random)] = random_object
                object_placed = True
