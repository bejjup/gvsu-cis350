import pygame as pg
import pygame_gui as GUI
import copy
from enum import Enum
# from main import Game
import random
import time
import pygame.freetype as ft
from model import Model


class tiles(Enum):
    tile = 0
    tile_empty = 1
    tile_flag = 2
    tile_mine = 5
    tile_clicked_mine = 6
    tile_1 = 8
    tile_2 = 9
    tile_3 = 10
    tile_4 = 11
    tile_5 = 12
    tile_6 = 13
    tile_7 = 14
    tile_8 = 15

class GUI:
    

    def __init__(self) -> None:
        
        self.model = Model(8, 10)
        self.model.generate_numbers()
        self.printed = 0
        pg.init()
        self.screen = pg.display.set_mode((960, 540), pg.RESIZABLE)
        pg.display.set_caption("RogueSweeper")

        # Create The Background
        
        self.background = pg.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((170, 155, 187))
        self.IMAGE_SIZE = lambda: self.screen.get_height() // 12
        self.getXmargin = lambda: self.screen.get_width() - self.IMAGE_SIZE() * 10 # where grid starts
        self.getYmargin = lambda: self.IMAGE_SIZE() * 3
        
        # set pause screen
        self.pause_bg = pg.Surface(self.screen.get_size(), pg.SRCALPHA)
        # init pause font
        self.pause_font = ft.SysFont('Comic Sans MS', 30)
        
                
    @classmethod
    def load_images(cls):
        def load_image(count):
            SS = pg.image.load('./images/MS_Sprites.png')
            width = 17
            height = 16
            surf = pg.Surface((width, height), pg.SRCALPHA)
            surf.blit(SS, (0, 0), pg.rect.Rect(width * (count % 8), height * (count // 8), width, height))
            return surf

        cls.sprites = {}
        for st in range(16): # change to spritetype
            cls.sprites[st] = load_image(st) 

    def tile_at(self, pos):
        grid_x = (pos[0] - self.getXmargin()) // self.IMAGE_SIZE()
        grid_y = (pos[1] - self.getYmargin()) // self.IMAGE_SIZE()
        return grid_x, grid_y

    def run_pause(self):
        paused = True
        clock = pg.time.Clock()
        start = time.time()

        while paused:
            clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                        paused = False
                        return
                if event.type == pg.KEYDOWN and event.key == pg.K_UP:
                    print(time.time())
            
            # draw transparent background
            self.background = pg.transform.scale(self.background, self.screen.get_size())
            self.screen.blit(self.background, (0, 0))
            self.__draw_board__()
            pg.draw.rect(self.pause_bg, (255, 0, 255, 127), self.pause_bg.get_rect())
            self.screen.blit(self.pause_bg, (0, 0))
            pg.display.flip()
            pause_text, rect = self.pause_font.render("Hello World!", True, (0, 0, 0))
            self.screen.blit(pause_text, (40, 250))
                
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
                    self.run_pause()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    x, y = self.tile_at(pg.mouse.get_pos())
                    self.model.board[x][y].status = 1

            
            # Draw to screen
            self.background = pg.transform.scale(self.background, self.screen.get_size())
            self.screen.blit(self.background, (0, 0))
            self.__draw_board__()
            pg.display.flip()
            
    def __draw_board__(self):
        for x in range(8):
            for y in range(8):
                selected = self.model.board[x][y]
                
                # get current sprite
                if selected.status == -1:
                    sprite = tiles.tile_flag.value
                elif selected.status == 1:
                    # for bottom sprites
                    if selected.tile_type == 0:
                        sprite = tiles.tile_empty.value
                    else:
                        sprite = selected.tile_type + 7
                else:
                    sprite = tiles.tile.value
                
                # pg.draw.rect(self.screen, (255, 255, 255), pg.rect.Rect(x * self.IMAGE_SIZE(), y * self.IMAGE_SIZE(), self.IMAGE_SIZE(), self.IMAGE_SIZE()))
                scaled_sprite = pg.transform.scale(copy.deepcopy(GUI.sprites[sprite]), (self.IMAGE_SIZE(), self.IMAGE_SIZE()))
                self.screen.blit(scaled_sprite, (x * self.IMAGE_SIZE() + self.getXmargin(), y * self.IMAGE_SIZE() + self.getYmargin()))


def main():
    GUI.load_images()
    g = GUI()
    g.__run_game__()
    
if __name__ == '__main__':
    main()