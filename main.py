from map import Maze
from McGyver import McGyver
from items import Item

# Create McGyver and the maze
mac = McGyver()
maze = Maze()

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
        mac.backpack = "pipe"
        print("You got the pipe")
    elif mac.x == gum.x_random and mac.y == gum.y_random:
        mac.backpack = "gum"
        print("You got the gum")
    elif mac.x == needle.x_random and mac.y == needle.y_random:
        mac.backpack = needle
        print("You got the needle")
    maze.display_maze()
    print(mac.backpack)
