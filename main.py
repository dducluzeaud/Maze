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

    # Display the maze
    maze.display_maze(window)

    # Refresh the screen
    pygame.display.flip()

    # While McGyver have not find the guardian, the game is not over
    while not maze.game_over(mac):
        label = myfont.render("Some text!", 1, (255,255,0))
        for event in pygame.event.get():

            if event.type == QUIT:
                maze.game_over = True

            elif event.type == KEYDOWN:
                # Escape to quit
                if event.key == K_ESCAPE:
                    maze.game_over = True

                # Arrow keys to move McGyver
                elif event.key == K_RIGHT:
                    mac.move(maze, 'right')
                elif event.key == K_LEFT:
                    mac.move(maze, 'left')
                elif event.key == K_UP:
                    mac.move(maze, 'up')
                elif event.key == K_DOWN:
                    mac.move(maze, 'down')

                maze.display_maze(window)
                label = myfont.render("Some text!", 1, (255,255,0))
                window.blit(label, (610, 620))
                pygame.display.flip()
    running = False
