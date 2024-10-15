#import the necessary libraries
import pygame
from pygame import mixer
import random

#initializes the game and declares values of X and Y
pygame.init()
X = 1200
Y = 800

#creates the screen, and sets the width to X and the height to Y
scrn = pygame.display.set_mode((X, Y))

#sets the default font values
font = pygame.font.Font('freesansbold.ttf', 40)
font2 = pygame.font.Font('freesansbold.ttf', 20)

#values that determine the current stage of the game
DICE = True
DOUBLES = False
GAME = False
START = True
SELEC = False
P1 = True
P2 = True
P3 = True
P4 = True
player = 1

#sets the values of both dices the player will roll
num1 = random.randint(1,6)
num2 = random.randint(1,6)

#declares Player Class, that contains info of each of the 4 players
class Players:

	#creates a Player and gives it values
	def __init__(self, num):
		self.num = num
		self.wood = 300
		self.brick = 200
		self.metal = 100
		self.name = "Placeholder"
		self.img = "Placeholder"
		self.set_name(num)
		self.set_img(num)
		self.loc_x = 0
		self.loc_y = 0
		self.color = 0,0,0
		self.set_color(num)

	#returns the name of the player
	def get_name(self):
		return self.name

	#sets the name of the player depending on what icon they chose
	def set_name(self, num):
		if num == 1:
			self.name = "Nog Ops"
		if num == 2:
			self.name = "Jonesy"
		if num == 3:
			self.name = "John Wick"
		if num == 4:
			self.name = "Raven"

	def set_color(self, num):
		if num == 1:
			self.color = 89, 211, 227
		if num == 2:
			self.color = 219, 31, 62
		if num == 3:
			self.color = 82, 82, 82
		if num == 4:
			self.color = 137, 42, 156

	def get_color(self):
		return self.color

	#returns the image directory
	def get_img(self):
		return self.img

	#sets the image of the player depending on what icon they chose
	def set_img(self, num):
		if num == 1:
			self.img = "C:\\Users\\vinny\\Downloads\\nog_ops.jpg"
		if num == 2:
			self.img = "C:\\Users\\vinny\\Downloads\\jonesy.jpg"
		if num == 3:
			self.img = "C:\\Users\\vinny\\Downloads\\John_wick.jpg"
		if num == 4:
			self.img = "C:\\Users\\vinny\\Downloads\\Raven.jpg"

	def set_loc_x(self, num):
		self.loc_x = num

	def get_loc_x(self):
		return self.loc_x

	def set_loc_y(self, num):
		self.loc_y = num

	def get_loc_y(self):
		return self.loc_y



#prints the images that make the starting screen
def print_start():

	#fills the screen to blue
	scrn.fill((27, 144, 221))

	# sets imp to the image of the board, and declares its size
	start_but = pygame.image.load("C:\\Users\\vinny\\Downloads\\start_button.jpg")
	start_but = pygame.transform.scale(start_but, (300, 120))
	scrn.blit(start_but, (450, 450))

	#sets imp to the image of the board, and declares its size and location
	title = pygame.image.load("C:\\Users\\vinny\\Downloads\\Title_text.png")
	title = pygame.transform.scale(title, (900, 200))
	scrn.blit(title, (150, 150))

def print_selec():

	#fills the screen to blue
	scrn.fill((27, 144, 221))

	#creates the selection screen text
	title = pygame.image.load("C:\\Users\\vinny\\Downloads\\Title_text.png")
	title = pygame.transform.scale(title, (400, 100))
	scrn.blit(title, (750, 5))

	#tells the user whose turn it is to choose a player
	if player <5:
		text = font.render(f'Player {player} Choose:', True, (245, 245, 245))
		textRect = text.get_rect()
		textRect.center = (200, 50)
		scrn.blit(text, textRect)

	#the user is told to continue when all players are selected
	else:
		text = font.render(f'Please Continue!', True, (245, 245, 245))
		textRect = text.get_rect()
		textRect.center = (200, 50)
		scrn.blit(text, textRect)

		text = font.render(f'Continue', True, (245, 245, 245))
		textRect = text.get_rect()
		textRect.center = (600, 500)
		scrn.blit(text, textRect)

	#only shows the icons when they have not been selected yet
	def display_selec_icons():
		if P1:
			nog_ops = pygame.image.load("C:\\Users\\vinny\\Downloads\\nog_ops.jpg")
			nog_ops = pygame.transform.scale(nog_ops, (300, 300))
			scrn.blit(nog_ops, (100, 100))

		if P2:
			jonesy = pygame.image.load("C:\\Users\\vinny\\Downloads\\jonesy.jpg")
			jonesy = pygame.transform.scale(jonesy, (300, 300))
			scrn.blit(jonesy, (800, 100))

		if P3:
			j_wick = pygame.image.load("C:\\Users\\vinny\\Downloads\\John_wick.jpg")
			j_wick = pygame.transform.scale(j_wick, (300, 300))
			scrn.blit(j_wick, (800, 450))

		if P4:
			raven = pygame.image.load("C:\\Users\\vinny\\Downloads\\Raven.jpg")
			raven = pygame.transform.scale(raven, (300, 300))
			scrn.blit(raven, (100, 450))
	display_selec_icons()

#declares the function print_board, that will print all images for board
def print_board(DOUBLES, DICE, num1, num2):

	#fills the screen to blue
	scrn.fill((27, 144, 221))

	#draws the rectangles
	def recs():
		pygame.draw.rect(scrn, (0,0,0), pygame.Rect(145, 145, 510, 510))
		pygame.draw.rect(scrn, (0,0,0), pygame.Rect(875, 50, 300, 700))
		pygame.draw.rect(scrn, (0,0,0), pygame.Rect(145, 675, 510, 100))
		pygame.draw.rect(scrn, (0,0,0), pygame.Rect(25, 145, 100, 510))
		pygame.draw.rect(scrn, (0,0,0), pygame.Rect(675, 145, 100, 510))
		pygame.draw.rect(scrn, (0,0,0), pygame.Rect(145, 25, 510, 100))
	recs()

	#sets imp to the image of the board, and declares its size and location
	def map():
		imp = pygame.image.load("C:\\Users\\vinny\\Downloads\\Mappy .jpg").convert()
		imp = pygame.transform.scale(imp, (500, 500))
		scrn.blit(imp, (150, 150))
	map()

	#gets values of mouse movements
	mx, my = pygame.mouse.get_pos()

	#sets dice1 to the image of the dice, and declares its size and location
	dice1 = pygame.image.load("C:\\Users\\vinny\\Downloads\\dice.png")
	dice1 = pygame.transform.scale(dice1, (50, 50))

	#sets dice2 to the image of the dice, and declares its size and location
	dice2 = pygame.image.load("C:\\Users\\vinny\\Downloads\\dice.png")
	dice2 = pygame.transform.scale(dice2, (50, 50))

	#displays player 1's information
	def p1_out():
		text = font2.render(f'{p_1.name}', True, (245, 245, 245))
		textRect = text.get_rect()
		textRect.center = (195, 787)
		scrn.blit(text, textRect)
		img_1 = pygame.image.load(p_1.get_img())
		img_1 = pygame.transform.scale(img_1, (100, 100))
		scrn.blit(img_1, (145, 675))
		pygame.draw.circle(scrn, (p_1.get_color()),[p_1.get_loc_x(), p_1.get_loc_y()], 10, 0)
	p1_out()

	# displays player 2's information
	def p2_out():
		text = font2.render(f'{p_2.name}', True, (245, 245, 245))
		textRect = text.get_rect()
		textRect.center = (75, 130)
		scrn.blit(text, textRect)
		img_2 = pygame.image.load(p_2.get_img())
		img_2 = pygame.transform.scale(img_2, (100, 100))
		scrn.blit(img_2, (25, 145))
		pygame.draw.circle(scrn, (p_2.get_color()), [p_2.get_loc_x(), p_2.get_loc_y()], 10, 0)
	p2_out()

	# displays player 3's information
	def p3_out():
		text = font2.render(f'{p_3.name}', True, (245, 245, 245))
		textRect = text.get_rect()
		textRect.center = (195, 13)
		scrn.blit(text, textRect)
		img_3 = pygame.image.load(p_3.get_img())
		img_3 = pygame.transform.scale(img_3, (100, 100))
		scrn.blit(img_3, (145, 25))
		pygame.draw.circle(scrn, (p_3.get_color()), [p_3.get_loc_x(), p_3.get_loc_y()], 10, 0)
	p3_out()

	# displays player 4's information
	def p4_out():
		text = font2.render(f'{p_4.name}', True, (245, 245, 245))
		textRect = text.get_rect()
		textRect.center = (725, 130)
		scrn.blit(text, textRect)
		img_4 = pygame.image.load(p_4.get_img())
		img_4 = pygame.transform.scale(img_4, (100, 100))
		scrn.blit(img_4, (675, 145))
		pygame.draw.circle(scrn, (p_4.get_color()), [p_4.get_loc_x(), p_4.get_loc_y()], 10, 0)
	p4_out()

	#whether or not the player has rolled yet
	if DICE:

		#moves the dice to follow the mouse if the mouse is within the roll box
		if (875 < mx < 1175) and (50 < my < 750):
			scrn.blit(dice1, (mx - 25, my - 25))
			scrn.blit(dice2, (mx + 25, my + 25))

		#moves dice to default spot if the mouse is not within the roll box
		else:
			scrn.blit(dice1, (1060, 675))
			scrn.blit(dice2, (1110, 675))

			#sets the text size and location, and prints the Dice label
			text = font.render('Dice:', True, (245, 245, 245), (0, 0, 0))
			textRect = text.get_rect()
			textRect.center = (960, 700)
			scrn.blit(text, textRect)

		#displays the Next Turn button if the player can roll
		text = font.render('Next Turn:', True, (245, 245, 245))
		textRect = text.get_rect()
		textRect.center = (1025, 25)
		scrn.blit(text, textRect)


	#if the previous dice were doubles
	elif DOUBLES:
		# moves the dice to follow the mouse if the mouse is within the roll box
		if (875 < mx < 1175) and (50 < my < 750):
			scrn.blit(dice1, (mx - 25, my - 25))
			scrn.blit(dice2, (mx + 25, my + 25))

		else:
			# moves dice to default spot if the mouse is not within the roll box
			scrn.blit(dice1, (1060, 675))
			scrn.blit(dice2, (1110, 675))

		#Displays the sum of the numbers rolled as well as that they were doubles
		text = font.render(f'Doubles {num1 + num2}!', True, (245, 245, 245))
		textRect = text.get_rect()
		textRect.center = (1000, 630)
		scrn.blit(text, textRect)

		# sets the text size and location, and prints the Dice label
		text = font.render('Dice:', True, (245, 245, 245))
		textRect = text.get_rect()
		textRect.center = (960, 700)
		scrn.blit(text, textRect)

		# displays the Roll Again button if the player can roll after had rolling doubles
		text = font.render('Roll Again:', True, (245, 245, 245))
		textRect = text.get_rect()
		textRect.center = (1025, 25)
		scrn.blit(text, textRect)


	else:
		# Displays the sum of the numbers rolled
		text = font.render(f'You Rolled {num1 + num2}!', True, (245, 245, 245))
		textRect = text.get_rect()
		textRect.center = (1025, 700)
		scrn.blit(text, textRect)

		# displays the Next Turn button if the player can roll
		text = font.render('Next Turn:', True, (245, 245, 245))
		textRect = text.get_rect()
		textRect.center = (1025, 25)
		scrn.blit(text, textRect)


#sets the window name
pygame.display.set_caption('Fortnite Monopoly')

#starts the mixer, loads the Fortnite theme song, sets the volume, and plays the theme
def music():
	mixer.init()
	mixer.music.load("C:\\Users\\vinny\\Downloads\\01. Battle Royal (Guitar Theme).mp3")
	mixer.music.set_volume(0.7)
	mixer.music.play()
music()

#paint screen one time
pygame.display.flip()

#loop for running the game until the window is closed
status = True
while (status):

	#iterate over the list of Event objects that was returned by pygame.event.get() method.
	for i in pygame.event.get():
		#stores the x and y values of the mouse
		mx, my = pygame.mouse.get_pos()

		#TEST TO RETURN THE MOUSE VALUES WHEN CLICKED
		if pygame.mouse.get_pressed()[0]:
			print(f'{mx} {my}')

		#displays start screen if START is true
		if START:
			print_start()

		#if the start button is pressed, enters the select screen
		if (450 < mx < 750) and (450 < my < 570) and pygame.mouse.get_pressed()[0] and START:
			#TEST FOR WHEN THE START BUTTON HAS BEEN PRESSED
			print("You clicked start")
			START = False
			SELEC = True

		#display the select screen
		if SELEC:
			print_selec()

		#if P1 icon is clicked while it is still available
		if (100 < mx < 400) and (100 < my < 400) and pygame.mouse.get_pressed()[0] and SELEC and P1:
			#declares that P1 can no longer be used and increases whose turn it is to choose by 1
			P1 = False
			p_1 = Players(player)
			p_1.set_loc_x(605)
			p_1.set_loc_y(605)
			player += 1

		#if P2 icon is clicked while it is still available
		if (800 < mx < 1100) and (100 < my < 400) and pygame.mouse.get_pressed()[0] and SELEC and P2:
			#declares that P2 can no longer be used and increases whose turn it is to choose by 1
			P2 = False
			p_2 = Players(player)
			p_2.set_loc_x(625)
			p_2.set_loc_y(605)
			player += 1

		#if P3 icon is clicked while it is still available
		if (800 < mx < 1100) and (450 < my < 750) and pygame.mouse.get_pressed()[0] and SELEC and P3:
			#declares that P3 can no longer be used and increases whose turn it is to choose by 1
			P3 = False
			p_3 = Players(player)
			p_3.set_loc_x(605)
			p_3.set_loc_y(625)
			player += 1

		#if P4 icon is clicked while it is still available
		if (100 < mx < 400) and (450 < my < 750) and pygame.mouse.get_pressed()[0] and SELEC and P4:
			#declares that P4 can no longer be used and increases whose turn it is to choose by 1
			P4 = False
			p_4 = Players(player)
			p_4.set_loc_x(625)
			p_4.set_loc_y(625)
			player += 1

		#if the continue button is clicked, enters the game screen
		if (510 < mx < 690) and (480 < my < 510) and pygame.mouse.get_pressed()[0] and SELEC and player == 5:
			#TEST FOR WHEN THE CONTINUE BUTTON HAS BEEN CLICKED
			print("You clicked start Again")
			SELEC = False
			GAME = True

		#displays the game screen
		if GAME:
			print_board(DOUBLES, DICE, num1, num2)


		#checks if the player has pressed within the dice box, which will 'roll dice'
		if (875 < mx < 1175) and (50 < my < 750) and pygame.mouse.get_pressed()[0] and GAME:
			#declares that the player just rolled
			DICE = False
			DOUBLES = False

		#checks if the player has pressed within the dice box while they have doubles
		if (875 < mx < 1175) and (50 < my < 750) and pygame.mouse.get_pressed()[0] and GAME and num1 == num2:
			#declares that the player has doubles
			DOUBLES = True
			DICE = False

		#checks if the player has pressed within the reset box
		if (920 < mx < 1130) and (5 < my < 45) and pygame.mouse.get_pressed()[0] and GAME:
			#resets the rolling values to allow the next turn
			DICE = True
			DOUBLES = False
			num1 = random.randint(1,6)
			num2 = random.randint(1,6)



		#updates the screen
		pygame.display.update()

		#if window is closed, the program ends
		if i.type == pygame.QUIT:
			status = False

#deactivates pygame library
pygame.quit()
