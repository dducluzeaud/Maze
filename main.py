from map import *

"""Open and read the file containing the maze. Each char in the file will get
   coordinates with a dictionnary
"""

maze = Maze()
maze.generate_maze()
maze.display_maze()
maze.place_random_object()
maze.display_maze()
