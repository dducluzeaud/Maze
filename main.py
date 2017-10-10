from map import Maze
from McGyver import McGyver
from items import Item
from constants import WINDOW

import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

# Set the dimension the window
window = pygame.display.set_mode((600, 640))

white = [255, 255, 255]
window.fill(white)
pygame.display.set_caption("Maze")
pygame.display.flip()

# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont("monospace", 15)

# Main loop
running = True
while running:

    #Slow down the loop
    pygame.time.Clock().tick(30)

    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Create McGyver and the maze
    mac = McGyver()
    maze = Maze()

    # Read and generate the coordinates of the maze
    maze.generate_maze()

    # Create and place the object on the map
    tube = Item("T")
    maze.random_coordinates(tube)
    ether = Item("E")
    maze.random_coordinates(ether)
    needle = Item("N")
    maze.random_coordinates(needle)

    # Display the maze
    maze.display_maze(window)

    # Refresh the screen
    pygame.display.flip()

    # While McGyver have not find the guardian, the game is not over
    while not maze.game_over(mac):

        for event in pygame.event.get():

            if event.type == QUIT:
                maze.game_over = True

            elif event.type == KEYDOWN:
                # Escape to quit
                if event.key == K_ESCAPE:
                    maze.game_over = True

                #Arrow keys to move McGyver
                elif event.key == K_RIGHT:
                    mac.move(maze, 'right')
                elif event.key == K_LEFT:
                    mac.move(maze, 'left')
                elif event.key == K_UP:
                    mac.move(maze, 'up')
                elif event.key == K_DOWN:
                    mac.move(maze, 'down')

                print(mac.x, mac.y)
                if mac.x == tube.x_random and mac.y == tube.y_random:
                    mac.backpack += 1
                    tube.x_random = 0
                    tube.y_random = 0
                    label = myfont.render("Some text!", 1, (255,255,0))
                    window.blit(label, (600, 640))
                elif mac.x == ether.x_random and mac.y == ether.y_random:
                    mac.backpack += 1
                    ether.x_random = 0
                    ether.y_random = 0
                    print("You got the ether")
                elif mac.x == needle.x_random and mac.y == needle.y_random:
                    mac.backpack += 1
                    needle.x_random = 0
                    needle.y_random = 0
                    print("You got the needle")
                print(mac.backpack)
                maze.display_maze(window)
                pygame.display.flip()
    running = False
