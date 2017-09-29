class Maze:


    def __init__(self):
        self.file = "map.txt"
        self.coord = {}

    def generate_maze(self):
        """Open and read the file containing the maze. Each char in the file
        will get coordinates with a dictionnary
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

    def place_random_object(self, n):
        object_placed = 0
        nb_objet = n
        random_object = '@'

        while object_placed != nb_objet:
            x_random = random.randint(1, 13)
            y_random = random.randint(1, 13)
            if self.coord[(x_random, y_random)] == " ":
                self.coord[(x_random, y_random)] = random_object
                object_placed += 1

    def game_over(self, mac):
        if self.coord[(mac.x, mac.y)] == self.coord[(1, 13)]:
            print("You won")
            return True
