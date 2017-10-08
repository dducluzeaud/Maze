from map import Maze
from McGyver import McGyver
from items import Item
from constants import WINDOW

import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((600, 600))

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

    # Create and place the object on the map
    tube = Item("T")
    maze.random_coordinates(tube)
    ether = Item("E")
    maze.random_coordinates(ether)
    needle = Item("N")
    maze.random_coordinates(needle)

    # Read and generate the coordinates of the maze
    maze.generate_maze()

    # Display the maze
    maze.display_maze(window)

    pygame.display.flip()

    while not maze.game_over(mac):

        for event in pygame.event.get():

            #Si l'utilisateur quitte, on met la variable qui continue le jeu
            #ET la variable générale à 0 pour fermer la fenêtre
            if event.type == QUIT:
                maze.game_over = True

            elif event.type == KEYDOWN:
                #Si l'utilisateur presse Echap ici, on revient seulement au menu
                if event.key == K_ESCAPE:
                    maze.game_over = True

                #Touches de déplacement de Donkey Kong
                elif event.key == K_RIGHT:
                    mac.move(maze, 'right')
                elif event.key == K_LEFT:
                    mac.move(maze, 'left')
                elif event.key == K_UP:
                    mac.move(maze, 'up')
                elif event.key == K_DOWN:
                    mac.move(maze, 'down')

        maze.display_maze(window)
        pygame.display.flip()
    running = False
    print("fuck you")


    pygame.display.flip()
