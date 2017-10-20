import pygame
from constants import *
from items import Item
from McGyver import McGyver


class Maze:

    def __init__(self):
        self.file = "map.txt"
        self.coord = {}

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

        self.mac = McGyver()

        # load all images needed to display the maze
        self.wall = self.path_to_img(WALL_PICTURE)
        self.background = self.path_to_img(BACKGROUND_PICTURE)
        self.mcgyver = self.path_to_img_alpha(MCGYVER)
        self.guardian = self.path_to_img_alpha(GUARDIAN)

        self.items = {'E': ETHER, 'N': NEEDLE, 'T': TUBE}

        # Create the object on the maze
        for obj in self.items.keys():
            Item(obj, self)
        # Change the constants in the dictionnary in image
        for char, item in self.items.items():
            item = self.path_to_img_alpha(item)
            self.items[char] = item

    # convert the constant into image without transparency
    def path_to_img(self, img):
        return pygame.image.load(img).convert()

    # convert the constant into image with transparency
    def path_to_img_alpha(self, img):
        return pygame.image.load(img).convert_alpha()

    def display_maze(self, window):
        for coord, value in self.coord.items():
            x = coord[1] * SIZE_SPRITE
            y = coord[0] * SIZE_SPRITE
            if value == '#':
                window.blit(self.wall, (x, y))
            else:
                window.blit(self.background, (x, y))
                if value == 'G':
                    window.blit(self.guardian, (x, y))
                elif value == 'M':
                    window.blit(self.mcgyver, (x, y))
            # Display the items
            for char, img in self.items.items():
                if value == char:
                    window.blit(img, (x, y))

    def game_over(self):

        if self.coord[(self.mac.x, self.mac.y)] == self.coord[(1, 14)]:
            return True
        else:
            return False

    def winner(self):

        winner = ""

        if self.game_over() == True:
            if len(self.mac.backpack) == len(self.items):
                winner = "McGyver"
            else:
                winner = "Murdoc"

        return winner
