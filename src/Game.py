# importing required library
import pygame
from pygame import mixer, MOUSEBUTTONDOWN
import random
# activate the pygame library .
pygame.init()
X = 1200
Y = 800

# create the display surface object
# of specific dimension..e(X, Y).
scrn = pygame.display.set_mode((X, Y))
font = pygame.font.Font('freesansbold.ttf', 40)
DICE = True
num1 = random.randint(1,6)
num2 = random.randint(1,6)
def print_board(DICE, num1, num2):
	scrn.fill((27, 144, 221))
	pygame.draw.rect(scrn, (0,0,0), pygame.Rect(145, 145, 510, 510))
	pygame.draw.rect(scrn, (0,0,0), pygame.Rect(875, 50, 300, 700))
	pygame.draw.rect(scrn, (0,0,0), pygame.Rect(145, 675, 510, 100))
	pygame.draw.rect(scrn, (0,0,0), pygame.Rect(25, 145, 100, 510))
	pygame.draw.rect(scrn, (0,0,0), pygame.Rect(675, 145, 100, 510))
	pygame.draw.rect(scrn, (0,0,0), pygame.Rect(145, 25, 510, 100))
	imp = pygame.image.load("C:\\Users\\vinny\\Downloads\\Mappy .jpg").convert()
	imp = pygame.transform.scale(imp, (500, 500))
	scrn.blit(imp, (150, 150))
	mx, my = pygame.mouse.get_pos()
	dice1 = pygame.image.load("C:\\Users\\vinny\\Downloads\\dice.png").convert()
	dice1 = pygame.transform.scale(dice1, (50, 50))
	dice2 = pygame.image.load("C:\\Users\\vinny\\Downloads\\dice.png").convert()
	dice2 = pygame.transform.scale(dice2, (50, 50))
	if DICE:
		if (875 < mx < 1175) and (50 < my < 750):
			scrn.blit(dice1, (mx - 25, my - 25))
			scrn.blit(dice2, (mx + 25, my + 25))
		else:
			scrn.blit(dice1, (1060, 675))
			scrn.blit(dice2, (1110, 675))
		text = font.render('Dice:', True, (245, 245, 245), (0, 0, 0))
		textRect = text.get_rect()
		textRect.center = (960, 700)
		scrn.blit(text, textRect)
	else:
		text = font.render(f'You Rolled {num1 + num2}!', True, (245, 245, 245), (0, 0, 0))
		textRect = text.get_rect()
		textRect.center = (1025, 700)
		scrn.blit(text, textRect)





pygame.display.set_caption('Fortnite Monopoly')

# create a surface object, image is drawn on it.


# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load("C:\\Users\\vinny\\Downloads\\01. Battle Royal (Guitar Theme).mp3")

# Setting the volume
mixer.music.set_volume(0.7)

# Start playing the song
mixer.music.play()


# paint screen one time
pygame.display.flip()
status = True
while (status):

# iterate over the list of Event objects
# that was returned by pygame.event.get() method.
	for i in pygame.event.get():
		print_board(DICE, num1, num2)
		if pygame.mouse.get_pressed()[0]:
			DICE = False
		pygame.display.update()
		if i.type == pygame.QUIT:
			status = False

# deactivates the pygame library
pygame.quit()
