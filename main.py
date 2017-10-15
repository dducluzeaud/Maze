from map import Maze
from McGyver import McGyver
from items import Item
from constants import *

import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

# initialize font
font = pygame.font.SysFont("monospace", 40)
smallfont = pygame.font.SysFont("monospace", 25)

# Set the dimension the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Maze")
pygame.display.flip()




def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace=0, size = "medium"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2) + y_displace
    window.blit(textSurf, textRect)

def show_items_collected(mac):

    show = True
    tube = pygame.image.load(TUBE).convert_alpha()
    ether = pygame.image.load(ETHER).convert_alpha()
    needle = pygame.image.load(NEEDLE).convert_alpha()
    line = 320

    while show:
        for event in pygame.event.get():
            if event.type == QUIT:
                maze.game_over = True

            elif event.type == KEYDOWN:
                # Escape to quit
                if event.key == K_TAB:
                    show = False

        window.fill(WHITE)
        message_to_screen("You picked up:", BLACK)

        for item in mac.backpack:
            if item == 'T':
                window.blit(tube, (280, line))
            elif item == 'N':
                window.blit(needle, (320, line))
            elif item == 'E':
                window.blit(ether, (240, line))
        if len(mac.backpack) == 3:
            message_to_screen("You can put the guardian to sleep now",GREEN, 80, size = "small")
        else:
            message_to_screen("You have to collect more items", RED, 80, size = "small")
        pygame.display.flip()


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
                    game_exit = True

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
                    # Show the items colectted
                    elif event.key == K_TAB:
                        show_items_collected(mac)

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
