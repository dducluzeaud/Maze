from map import Maze
from McGyver import McGyver
from items import Item

"""Open and read the file containing the maze. Each char in the file will get
   coordinates with a dictionnary
"""
mac = McGyver()
maze = Maze()
maze.generate_maze()
pipe = Item(maze, "|")
gum = Item(maze, "O")
needle = Item(maze, "E")

maze.display_maze()

while not maze.game_over(mac):
    mac.teleport(maze)
    maze.display_maze()
