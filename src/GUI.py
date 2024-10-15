import pygame as pg
import pygame_gui as GUI
import copy
from enum import Enum
# from main import Game
import random

IMAGE_SIZE = 52

class tiles(Enum):
    tile_1 = 1
    tile_2 = 2
    tile_3 = 3
    tile_4 = 4
    tile_5 = 5
    tile_6 = 6
    tile_7 = 7
    tile_8 = 8
    tile_empty = 9
    tile_tile = 10
    tile_flag = 11

class GUI:

    def __init__(self) -> None:
        self.printed = 0
        pg.init()
        self.screen = pg.display.set_mode((1280, 480), pg.SCALED)
        pg.display.set_caption("RogueSweeper")

        # Create The Background
        self.background = pg.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((170, 155, 187))
     
    @classmethod
    def load_images(cls):
        def load_image(count):
            SS = pg.image.load('./images/MS_Sprites.png')
            width = 17
            height = 16
            surf = pg.Surface((width, height), pg.SRCALPHA)
            surf.blit(SS, (0, 0), pg.rect.Rect(width * (count % 8), height * (count // 8), width, height))
            surf_scaled = pg.transform.scale(surf, (IMAGE_SIZE, IMAGE_SIZE)) # Change to image size
            return surf_scaled

        cls.sprites = {}
        for st in range(16): # change to spritetype
            cls.sprites[st] = load_image(st) 
            print(GUI.sprites)

        
    def __run_game__(self):
        print('running')
        going = True
        clock = pg.time.Clock()
        while going:

            # Handle Input Events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    going = False
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    going = False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    self.printed = (self.printed + 1) % 16

            
            # Draw to screen
            self.screen.blit(self.background, (0, 0))
            self.__draw_board__()
            pg.display.flip()
            
    def __draw_board__(self):
        for x in range(8):
            for y in range(8):
                # selected = Game.tile_at(x, y)
                selected = self.printed
                pg.draw.rect(self.screen, (255, 255, 255), pg.rect.Rect(x * IMAGE_SIZE, y * IMAGE_SIZE, IMAGE_SIZE, IMAGE_SIZE))
                self.screen.blit(copy.deepcopy(GUI.sprites[selected]), (x * IMAGE_SIZE, y * IMAGE_SIZE))


def main():
    GUI.load_images()
    g = GUI()
    g.__run_game__()
    
if __name__ == '__main__':
    main()