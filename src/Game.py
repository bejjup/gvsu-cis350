#import the necessary libraries
import pygame
from pygame import mixer, MOUSEBUTTONDOWN
import random

#initializes the game and declares values of X and Y
pygame.init()
X = 1200
Y = 800

#creates the screen, and sets the width to X and the height to Y
scrn = pygame.display.set_mode((X, Y))

#sets the default font values
font = pygame.font.Font('freesansbold.ttf', 40)

#sets the DICE value to true, DICE will be used to determine if the player has rolled yet
DICE = True

#sets the values of both dices the player will roll
num1 = random.randint(1,6)
num2 = random.randint(1,6)

#declares the function print_board, that will print all images for board
def print_board(DICE, num1, num2):
	#fills the screen to blue
	scrn.fill((27, 144, 221))

	#draws various rectangles that will hold information for each player
	pygame.draw.rect(scrn, (0,0,0), pygame.Rect(145, 145, 510, 510))
	pygame.draw.rect(scrn, (0,0,0), pygame.Rect(875, 50, 300, 700))
	pygame.draw.rect(scrn, (0,0,0), pygame.Rect(145, 675, 510, 100))
	pygame.draw.rect(scrn, (0,0,0), pygame.Rect(25, 145, 100, 510))
	pygame.draw.rect(scrn, (0,0,0), pygame.Rect(675, 145, 100, 510))
	pygame.draw.rect(scrn, (0,0,0), pygame.Rect(145, 25, 510, 100))

	#sets imp to the image of the board, and declares its size and location
	imp = pygame.image.load("C:\\Users\\vinny\\Downloads\\Mappy .jpg").convert()
	imp = pygame.transform.scale(imp, (500, 500))
	scrn.blit(imp, (150, 150))

	#gets values of mouse movements
	mx, my = pygame.mouse.get_pos()

	#sets dice1 to the image of the dice, and declares its size and location
	dice1 = pygame.image.load("C:\\Users\\vinny\\Downloads\\dice.png").convert()
	dice1 = pygame.transform.scale(dice1, (50, 50))

	#sets dice2 to the image of the dice, and declares its size and location
	dice2 = pygame.image.load("C:\\Users\\vinny\\Downloads\\dice.png").convert()
	dice2 = pygame.transform.scale(dice2, (50, 50))

	#whether or not the player has rolled yet
	if DICE:

		#if the mouse is within the large roll box
		if (875 < mx < 1175) and (50 < my < 750):

			#moves both dice to mouse value
			scrn.blit(dice1, (mx - 25, my - 25))
			scrn.blit(dice2, (mx + 25, my + 25))

		#if the mouse is not within the dice box
		else:

			#moves both dice to the defualt spot
			scrn.blit(dice1, (1060, 675))
			scrn.blit(dice2, (1110, 675))

		#sets the text size and location, and prints the Dice label
		text = font.render('Dice:', True, (245, 245, 245), (0, 0, 0))
		textRect = text.get_rect()
		textRect.center = (960, 700)
		scrn.blit(text, textRect)

	#if the dice has already been rolled
	else:
		#replaces the Dice label with the number the player has rolled
		text = font.render(f'You Rolled {num1 + num2}!', True, (245, 245, 245), (0, 0, 0))
		textRect = text.get_rect()
		textRect.center = (1025, 700)
		scrn.blit(text, textRect)




#sets the window name
pygame.display.set_caption('Fortnite Monopoly')

#starts the mixer, loads the Fortnite theme song, sets the volume, and plays the theme
mixer.init()
mixer.music.load("C:\\Users\\vinny\\Downloads\\01. Battle Royal (Guitar Theme).mp3")
mixer.music.set_volume(0.7)
mixer.music.play()


#paint screen one time
pygame.display.flip()

#loop for running the game until the window is closed
status = True
while (status):

	#iterate over the list of Event objects that was returned by pygame.event.get() method.
	for i in pygame.event.get():

		#prints the board
		print_board(DICE, num1, num2)

		#checks if the player has pressed, which means rolled dice
		if pygame.mouse.get_pressed()[0]:
			DICE = False

		#updates the screen
		pygame.display.update()

		#if window is closed, the program ends
		if i.type == pygame.QUIT:
			status = False

#deactivates pygame library
pygame.quit()
