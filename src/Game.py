#import the necessary libraries
import pygame
from pygame import mixer, MOUSEBUTTONUP, MOUSEBUTTONDOWN
import random
from buttons import *
from values import Values
from files import File
from spaces import make_board
from print_screens import *
from players import *

#initializes the game and declares values of X and Y
pygame.init()
X = 1200
Y = 800
scrn = pygame.display.set_mode((X, Y))

#values that determine the current stage of the game
file = File()
vals = Values(pygame, file)
board = []
make_board(board)

#sets the window name
pygame.display.set_caption('Fortnite Monopoly')

#starts the mixer, loads the Fortnite theme song, sets the volume, and plays the theme
mixer.init()
mixer.music.load(file.music)
mixer.music.set_volume(0.7)
mixer.music.play()

#paint screen one time
pygame.display.flip()

#loop for running the game until the window is closed
status = True
while status:

    #iterate over the list of Event objects that was returned by pygame.event.get() method.
    for i in pygame.event.get():
        #stores the x and y values of the mouse
        mx, my = pygame.mouse.get_pos()
        #displays start screen if START is true

        if i.type == MOUSEBUTTONDOWN and i.button == 1:
            vals.clicking = True
            if vals.START:
                start_button(mx, my, vals)

            if vals.SELEC:
                # if P1 icon is clicked while it is still available
                icon_nog_ops(mx, my, vals, Players)
                # if P2 icon is clicked while it is still available
                icon_jonesy(mx, my, vals, Players)
                # if P3 icon is clicked while it is still available
                icon_raven(mx, my, vals, Players)
                # if P4 icon is clicked while it is still available
                icon_john_wick(mx, my, vals, Players)

        # if the continue button is clicked, enters the game screen
                continue_button(mx, my, vals)

            if vals.INFO:
                return_to_game(mx, my, vals)
            if vals.GAME:
                info_button(mx, my, vals)

                #Next Turn
                roll_dice(mx, my, vals, mixer, file, pygame, board, random)

                #Checks if the player rolls doubles
                check_doubles(mx, my, vals)

                #player rolls again after double

                #Player presses next turn
                next_turn(mx, my, vals, random)

                #Player presses roll again
                roll_again(mx, my, vals, random)
            print(f'{mx} {my}')
        elif i.type == MOUSEBUTTONUP and i.button == 1:
            vals.clicking = False

        if vals.START:
            print_start(scrn, pygame)

        elif vals.SELEC:
            print_selec(scrn, pygame, vals)

        elif vals.INFO:
            print_info(scrn, pygame, file, vals)

        elif vals.GAME:
            print_board(scrn, pygame, file, vals, vals.p_1, vals.p_2, vals.p_3, vals.p_4, mx, my, vals.dice1, vals.dice2)

        pygame.display.update()

        #if window is closed, the program ends
        if i.type == pygame.QUIT:
            status = False

#deactivates pygame library
pygame.quit()
