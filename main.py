from map import Maze
from McGyver import McGyver

"""Open and read the file containing the maze. Each char in the file will get
   coordinates with a dictionnary
"""
mac = McGyver()
maze = Maze(mac)
maze.generate_maze()
maze.display_maze()

maze.place_random_object(3)
maze.display_maze()
