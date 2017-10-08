import random
import pygame
from constants import *

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

        # load all images needed to display the maze2
        wall = pygame.image.load(WALL_PICTURE).convert()
        background = pygame.image.load(BACKGROUND_PICTURE).convert()
        mcgyver = pygame.image.load(MCGYVER).convert()
        guardian = pygame.image.load(GUARDIAN).convert()
        tube = pygame.image.load(TUBE).convert()
        ether = pygame.image.load(ETHER).convert()
        needle = pygame.image.load(NEEDLE).convert()

        for coord, value in self.coord.items():
            x = coord[1] * SIZE_SPRITE
            y = coord[0] * SIZE_SPRITE
            if value == '#':
                window.blit(wall, (x, y))
            elif value == ' ':
                window.blit(background, (x, y))
            elif value == 'G':
                window.blit(guardian, (x, y))
            elif value == 'M':
                window.blit(mcgyver, (x, y))
            elif value =='N':
                window.blit(needle, (x,y))
            elif value == 'T':
                window.blit(tube, (x, y))
            elif value == 'E':
                window.blit(ether, (x, y))


    def random_coordinates(self, item):

        item_placed = False

        while not item_placed:
            if self.coord[(item.x_random, item.y_random)] == " ":
                self.coord[(item.x_random, item.y_random)] = item.img
                item_placed = True
            else:
                item.x_random = random.randrange(1,13)
                item.y_random = random.randrange(1,13)

    def game_over(self, mac):
        if self.coord[(mac.x, mac.y)] == self.coord[(1, 14)]:

            if mac.backpack == 3:
                print("You won")
            else:
                print("You loose")
            return True
