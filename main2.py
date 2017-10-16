from map import Maze
from McGyver import McGyver
from items import Item
from constants import *

import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()


class Main():

    def __init__(self):

        # initialize font
        self.font = pygame.font.SysFont("monospace", 40)
        self.smallfont = pygame.font.SysFont("monospace", 25)

        # Set the dimension the window
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Maze")
        pygame.display.flip()

        self.game_over = False
        self.game_exit = False

    def text_objects(self, text, color, size):
        if size == "small":
            textSurface = self.smallfont.render(text, True, color)
        elif size == "medium":
            textSurface = self.font.render(text, True, color)
        return textSurface, textSurface.get_rect()


    def message_to_screen(self, msg, color, y_displace=0, size = "medium"):
        textSurf, textRect = self.text_objects(msg, color, size)
        textRect.center = (WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2) + y_displace
        self.window.blit(textSurf, textRect)

    def show_items_collected(self, mac):

        show = True
        tube = pygame.image.load(TUBE).convert_alpha()
        ether = pygame.image.load(ETHER).convert_alpha()
        needle = pygame.image.load(NEEDLE).convert_alpha()
        line = 320
        nb_items_left = 3 - len(mac.backpack)

        while show:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.game_over = True

                elif event.type == KEYDOWN:
                    # Escape to quit
                    if event.key == K_TAB:
                        show = False

            self.message_to_screen("You picked up:", BLACK)
            self.window.fill(WHITE)

            for item in mac.backpack:
                if item == 'T':
                    self.window.blit(tube, (280, line))
                elif item == 'N':
                    self.window.blit(needle, (320, line))
                elif item == 'E':
                    self.window.blit(ether, (240, line))
            if len(mac.backpack) == 3:
                self.message_to_screen("You can put the guardian to sleep now",GREEN, 80, size = "small")
            else:
                self.message_to_screen("You still have {} itemsto collect".format(nb_items_left), RED, 80, size = "small")
            pygame.display.flip()

    def screen_game_over(self, mac, maze):

        winner = maze.winner(mac)

        mcgyver_win = pygame.image.load(MCGYVER_WIN).convert()
        murdoc_win = pygame.image.load(MURDOC_WIN).convert()

        if winner == "McGyver":
            self.window.blit(mcgyver_win, (0, 0))
            self.message_to_screen("You win", WHITE, -75)
            pygame.display.update()
        elif winner == "Murdoc":
            self.window.blit(murdoc_win, (0, 0))
            self.message_to_screen("You loose", WHITE, -75)
            pygame.display.update()
        self.message_to_screen("Press C to play or Q to quit", WHITE)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = False
                self.game_exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == K_c:
                    self.main_loop()
                    self.game_over = False
                    self.game_exit = True

                elif event.key == K_q:
                    self.game_over = False
                    self.game_exit = True

    def event_in_pygame(self, mac, maze):
        for event in pygame.event.get():

            if event.type == QUIT:
                self.game_exit = True

            elif event.type == KEYDOWN:
                # Escape to quit
                if event.key == K_ESCAPE:
                    self.game_exit = True

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
                    self.show_items_collected(mac)

                maze.display_maze(self.window)
                pygame.display.flip()
                self.game_over = maze.game_over(mac)


    # Main loop
    def main_loop(self):

        # Create McGyver and the maze
        mac = McGyver()
        maze = Maze()

        pygame.display.flip()

        while not self.game_exit:

            # Slow down the loop
            pygame.time.Clock().tick(30)

            # Process input (events)
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    self.game_exit = True
                    pygame.exit()

            # Display the maze
            maze.display_maze(self.window)

            # Refresh the screen
            pygame.display.flip()

            # While McGyver have not find the guardian, he can move around the map
            while not self.game_over:

                self.event_in_pygame(mac, maze)

            # Show a screen where you can quit or play again
            while self.game_over:

                self.screen_game_over(mac, maze)

        self.game_exit = True

play = Main()
play.main_loop()
