import pygame as pg
import copy
from enum import Enum
# from main import Game
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

class Button:
    def __init__(self, screen, pos, text, color, font, text_color=(0, 0, 0)):
        self.screen = screen
        self.pos = pos
        self.text = text
        self.color = color
        self.cont_button = font.render(text, text_color)
        
    def update(self):
        rect = self.cont_button[1]
        self.bg = rect.copy()
        self.bg.width = self.screen.get_width() * .15
        rect.center = self.bg.center = (self.screen.get_width() * self.pos[0], self.screen.get_height() * self.pos[1])
        if rect.collidepoint(pg.mouse.get_pos()):
            self.bg = self.bg.scale_by(1.05, 1.05)
            tmp_clr = tuple(map(lambda i, j: i + j, self.color, (10, 10, 25)))
        else: tmp_clr = self.color
        self.bg = self.bg.scale_by(1.2, 1.2)
        self.bg.center = rect.center
        pg.draw.rect(self.screen, tmp_clr, self.bg, border_radius=10)
        self.screen.blit(self.cont_button[0], rect) 


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
        
        # set pause screen
        self.pause_bg = pg.Surface(self.screen.get_size(), pg.SRCALPHA)
        # init pause font
        font = ft.SysFont('Comic Sans MS', 30)
        self.pause_text = Button(self.screen, (.5, .2), 'Paused', (55, 55, 55), font, (225, 225, 225))
        #init buttons
        self.cont_btn = Button(self.screen, (.5, .4), 'Continue', self.btn_clr, font)
        self.exit_btn = Button(self.screen, (.5, .6), 'Exit', self.btn_clr, font)
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
                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    if self.cont_btn.cont_button[1].collidepoint(pos):
                        paused = False
                    elif self.exit_btn.cont_button[1].collidepoint(pos):
                        exit()

            # draw transparent background
            self.background = pg.transform.scale(self.background, self.screen.get_size())
            self.screen.blit(self.background, (0, 0))
            self.__draw_board__()
            self.__draw_layout__()
            pg.draw.rect(self.pause_bg, (100, 100, 100, 127), self.pause_bg.get_rect())
            self.pause_bg = pg.transform.scale(self.pause_bg, self.screen.get_size())
            self.screen.blit(self.pause_bg, (0, 0))
            # draw text
            self.pause_text.update()
            # draw buttons
            self.cont_btn.update()
            self.exit_btn.update()
            pg.display.flip()
                
                
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
                    pos = pg.mouse.get_pos()
                    # TODO check each button to see if it was clicked
                    x, y = self.tile_at(pos)
                    if 0 <= x <= 7 and 0 <= y <= 7:
                        if event.button == 3: # right click
                            selected = self.model.board[y][x]
                            if selected.status == 0:
                                selected.status = -1 # set to flag
                            elif selected.status == -1:
                                selected.status = 0 # remove flag
                                     
                        elif event.button == 1: # left click
                            # if we haven't called generate_mines yet, we need to call it
                            if not self.model.generated:
                                self.model.generate_mines(x, y)
                            self.reveal_tiles(x, y)                    

            
            # Draw to screen
            self.background = pg.transform.scale(self.background, self.screen.get_size())
            self.screen.blit(self.background, (0, 0))
            self.__draw_layout__()
            self.__draw_board__()
            pg.display.flip()
            
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


def main():
    GUI.load_images()
    g = GUI()
    g.__run_game__()
    
if __name__ == '__main__':
    main()
    
