from map import Maze
from McGyver import McGyver
from items import Item
from constants import WINDOW

import pygame
from pygame.locals import *

pygame.init()

# Create McGyver and the maze
mac = McGyver()
maze = Maze()

window = pygame.display.set_mode((WINDOW, WINDOW))

# Read and generate the coordinates of the maze
maze.generate_maze()

# Create and place the object on the map
pipe = Item("P")
maze.random_coordinates(pipe)
lamp = Item("L")
maze.random_coordinates(lamp)
needle = Item("N")
maze.random_coordinates(needle)

# Display the maze
maze.display_maze()

# While McGyver have not find the guardian, the game is not over
while not maze.game_over(mac):
    mac.teleport(maze)
    if mac.x == pipe.x_random and mac.y == pipe.y_random:
        mac.backpack += 1
        print("You got the pipe")
    elif mac.x == lamp.x_random and mac.y == lamp.y_random:
        mac.backpack += 1
        print("You got the gum")
    elif mac.x == needle.x_random and mac.y == needle.y_random:
        mac.backpack += 1
        print("You got the needle")
    maze.display_maze()
    print(mac.backpack)
