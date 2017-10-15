from map import Maze
from McGyver import McGyver
from items import Item
from constants import *

import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

window_width = 600
window_height = 600

# Set the dimension the window
window = pygame.display.set_mode((window_width, window_height))

white = [255, 255, 255]
window.fill(white)
pygame.display.set_caption("Maze")
pygame.display.flip()

# initialize font
font = pygame.font.SysFont("monospace", 40)


def text_objects(text, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace=0):
    textSurf, textRect = text_objects(msg, color)
    textRect.center = (WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2) + y_displace
    window.blit(textSurf, textRect)


# Main loop
def main_loop():

    game_exit = False

    while not game_exit:

        # Slow down the loop
        pygame.time.Clock().tick(30)

        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                game_exit = True

        # Create McGyver and the maze
        mac = McGyver()
        maze = Maze()

        # Display the maze
        maze.display_maze(window)

        # Refresh the screen
        pygame.display.flip()

        game_over = False
        # While McGyver have not find the guardian, the game is not over
        while not game_over:

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
                    pygame.display.flip()
                    game_over = maze.game_over(mac)

        while game_over:

            winner = maze.winner(mac)

            mcgyver_win = pygame.image.load(MCGYVER_WIN).convert()
            murdoc_win = pygame.image.load(MURDOC_WIN).convert()

            if winner == "McGyver":
                window.blit(mcgyver_win, (0, 0))
                message_to_screen("You win", WHITE, -75)
                pygame.display.update()
            elif winner == "Murdoc":
                window.blit(murdoc_win, (0, 0))
                message_to_screen("You loose", WHITE, -75)
                pygame.display.update()
            message_to_screen("Press C to play or Q to quit", WHITE)
            pygame.display.flip()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
                    game_exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == K_c:
                        main_loop()
                        game_over = False
                        game_exit = True
                    elif event.key == K_q:
                        game_over = False
                        game_exit = True


main_loop()
