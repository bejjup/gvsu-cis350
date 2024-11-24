import pygame as pg
import copy
from enum import Enum
import random
import time
import pygame.freetype as ft
from model import Model
from typing import Tuple

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
    
class Image:
    def __init__(self, screen, rect, image):
        self.screen = screen
        self.rect = rect
        self.image = image
    
    def update(self):
        self.image = pg.transform.scale(self.image, self.rect.size)
        self.screen.blit(self.image, self.rect) 

class Button:
    def __init__(self, screen, pos, text, color, font, text_color=(0, 0, 0)):
        self.screen = screen
        self.pos = pos
        self.text = text
        self.color = color
        self.button = font.render(text, text_color)
        self.interactive = True
        
    def update(self):
        rect = self.button[1]
        self.bg = rect.copy()
        self.bg.width = self.screen.get_width() * .15
        rect.center = self.bg.center = (self.screen.get_width() * self.pos[0], self.screen.get_height() * self.pos[1])
        if rect.collidepoint(pg.mouse.get_pos()) and self.interactive:
            self.bg = self.bg.scale_by(1.05, 1.05)
            tmp_clr = tuple(map(lambda i, j: i + j, self.color, (10, 10, 25)))
        else: tmp_clr = self.color
        self.bg = self.bg.scale_by(1.2, 1.2)
        self.bg.center = rect.center
        pg.draw.rect(self.screen, tmp_clr, self.bg, border_radius=10)
        self.screen.blit(self.button[0], rect) 


class GUI:
    

    def __init__(self) -> None:
        
        self.model = Model(8, 10)
        self.printed = 0
        pg.init()
        self.btn_clr = (170, 155, 187)
        self.screen = pg.display.set_mode((960, 630), pg.RESIZABLE)
        # self.ui_manager = GUI.UIManager(self.screen.get_size())
        pg.display.set_caption("RogueSweeper")
        # Create The Background
        
        self.background = pg.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((170, 155, 187))
        self.IMAGE_SIZE = lambda: self.screen.get_height() // 12
        self.getXmargin = lambda: self.screen.get_width() - self.IMAGE_SIZE() * 9 # where grid starts
        self.getYmargin = lambda: self.IMAGE_SIZE() * 3
        font = ft.SysFont('Comic Sans MS', 30)
        
        # set pause screen and buttons
        self.pause_bg = pg.Surface(self.screen.get_size(), pg.SRCALPHA)
        self.pause_text = Button(self.screen, (.5, .2), 'Paused', (55, 55, 55), font, (225, 225, 225))
        self.pause_text.interactive = False
        self.cont_btn = Button(self.screen, (.5, .4), 'Continue', self.btn_clr, font)
        self.exit_btn = Button(self.screen, (.5, .6), 'Exit', self.btn_clr, font)
        # set lose screen and button
        self.lose_bg = pg.Surface(self.screen.get_size(), pg.SRCALPHA)
        self.lose_text = Button(self.screen, (.5, .2), 'Game Over', (55, 55, 55), font, (225, 225, 225))
        self.lose_text.interactive = False
        r = pg.Rect(0, 0, self.IMAGE_SIZE() * 3, self.IMAGE_SIZE() * 3)
        r.center = self.screen.get_rect().center
        self.img_mine = Image(self.screen, r, self.sprites[tiles.tile_clicked_mine.value])
        self.restart_btn = Button(self.screen, (.5, .8), 'Restart', self.btn_clr, font)
    # class method that is ran before game to load sprites                
    @classmethod
    def load_images(cls):
        # helper function ran for each individual sprite
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
        # returns minesweeper grid pos for a mouse click
        grid_x = (pos[0] - self.getXmargin()) // self.IMAGE_SIZE()
        grid_y = (pos[1] - self.getYmargin()) // self.IMAGE_SIZE()
        return grid_x, grid_y
    
    def reveal_tiles(self, x: int, y: int):
        # recursive function to reveal empty spaces
        if (x < 0 or x > 7) or (y < 0 or y > 7):
            return
        b = self.model.board
        if b[y][x].status != 1: # Not Revealed
            b[y][x].status = 1
            if b[y][x].tile_type == -1:
                for i in range(8):
                    for j in range(8):
                        b[i][j].status = 1
                       
            elif b[y][x].tile_type == 0: # empty
                l = [-1, 0, 1]
                for i in l:
                    for j in l:
                        self.reveal_tiles(x + i, y + j)   
            
    def __draw_board__(self):
        for x in range(8):
            for y in range(8):
                selected = self.model.board[y][x]
                
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

    def __draw_layout__(self):
        pg.draw.line(self.screen, (0, 0, 0), (self.getXmargin() - self.IMAGE_SIZE(), self.getYmargin() - self.IMAGE_SIZE()), (self.screen.get_width(), self.getYmargin() - self.IMAGE_SIZE()), 3)
        pg.draw.line(self.screen, (0, 0, 0), (self.getXmargin() - self.IMAGE_SIZE(), 0), (self.getXmargin() - self.IMAGE_SIZE(), self.screen.get_height()), 3)
