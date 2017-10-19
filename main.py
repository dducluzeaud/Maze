from maze import Maze
from items import Item
from constants import *

import pygame
from pygame.locals import *


class Main():

    def __init__(self):

        # Initialize pygame
        pygame.init()
        pygame.font.init()

        # initialize font
        self.font = pygame.font.SysFont("monospace", 40)
        self.smallfont = pygame.font.SysFont("monospace", 25)

        # Set the dimension the window
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Maze")
        pygame.display.flip()

        self.game_over = False
        self.game_exit = False

        # Create and generatethe Maze
        self.maze = Maze()

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

    def show_items_collected(self):

        show = True
        tube = pygame.image.load(TUBE).convert_alpha()
        ether = pygame.image.load(ETHER).convert_alpha()
        needle = pygame.image.load(NEEDLE).convert_alpha()
        line = 320
        nb_items_left = 3 - len(self.maze.mac.backpack)

        while show:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.game_over = True

                elif event.type == KEYDOWN:
                    # Escape to quit
                    if event.key == K_TAB:
                        show = False

            self.window.fill(WHITE)
            self.message_to_screen("You picked up:", BLACK)

            for item in self.maze.mac.backpack:
                if item == 'T':
                    self.window.blit(tube, (280, line))
                elif item == 'N':
                    self.window.blit(needle, (320, line))
                elif item == 'E':
                    self.window.blit(ether, (240, line))
            if len(self.maze.mac.backpack) == 3:
                self.message_to_screen("You can put the guardian to sleep now",GREEN, 80, size = "small")
            else:
                self.message_to_screen("You still have {} items to collect".format(nb_items_left), RED, 80, size = "small")
            pygame.display.flip()

    def screen_game_over(self):

        display_screen = True

        while display_screen:

            winner = self.maze.winner()

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
            self.message_to_screen("Press P to play agin or Q to quit", WHITE)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = False
                    self.game_exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == K_p:
                        self.game_over = False
                        self.game_exit = False
                        # Reset the object
                        self.maze.__init__()
                        self.maze.mac.__init__()
                        display_screen = False
                    elif event.key == K_q:
                        self.game_over = False
                        self.game_exit = True
                        display_screen = False

    def event_in_pygame(self):

        move = True

        while move:
            for event in pygame.event.get():

                # check for closing window
                if event.type == pygame.QUIT:
                    self.game_exit = True
                    self.game_over = False
                    move = False
                elif event.type == KEYDOWN:
                # Escape to quit
                    if event.key == K_ESCAPE:
                        self.game_exit = True
                        self.game_over = False
                        move = False

                    # Arrow keys to move McGyver
                    elif event.key == K_RIGHT:
                        self.maze.mac.move(self.maze, 'right')
                    elif event.key == K_LEFT:
                        self.maze.mac.move(self.maze, 'left')
                    elif event.key == K_UP:
                        self.maze.mac.move(self.maze, 'up')
                    elif event.key == K_DOWN:
                        self.maze.mac.move(self.maze, 'down')
                    # Show the items colectted
                    elif event.key == K_TAB:
                        self.show_items_collected()
                    elif event.key == K_ESCAPE:
                        self.game_over = False
                        self.game_exit = True
                    

                    self.maze.display_maze(self.window)
                    pygame.display.flip()
                    self.game_over = self.maze.game_over()
            
            if self.game_over == True:
                move = False

    # Main loop
    def main_loop(self):

        pygame.display.flip()
                        
        while not self.game_exit:

            # Slow down the loop
            pygame.time.Clock().tick(30)

            # Display the maze
            self.maze.display_maze(self.window)

            # Refresh the screen
            pygame.display.flip()

            # While McGyver have not find the guardian, he can move around the map
            if not self.game_over:

                self.event_in_pygame()

            # Show a screen where you can quit or play again
            else:

                self.screen_game_over()

        self.game_exit = True

if __name__ == '__main__':
    main = Main()
    main.main_loop()
