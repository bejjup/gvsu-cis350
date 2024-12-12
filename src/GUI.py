import pygame as pg
import copy
from enum import Enum
import shop
import pygame.freetype as ft
from model import Model
from typing import Tuple
import shop

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
    def __init__(self, screen: pg.Surface, rect: pg.Rect, image: pg.Surface):
        self.screen = screen
        self.image = image
        self.rect = rect
        self.pos_ratio = (self.rect.centerx / self.screen.get_width(), self.rect.centery / self.screen.get_height())
        self.size_ratio = (self.rect.width / self.screen.get_width(), self.rect.height / self.screen.get_height())
        print(self.pos_ratio, self.size_ratio)
    def update(self, gui=False, shop_x = False):
        self.rect.center = (self.pos_ratio[0] * self.screen.get_width(), self.pos_ratio[1] * self.screen.get_height())
        self.rect.size = (self.size_ratio[0] * self.screen.get_width(), self.size_ratio[1] * self.screen.get_height())
        if shop_x and gui:
            shop_width = gui.getXmargin() - gui.IMAGE_SIZE()
            self.rect.centerx = shop_width * shop_x
        ratio = self.rect.width / self.image.get_width()
        self.cpy_image = pg.transform.scale(self.image, (ratio * self.image.width, ratio * self.image.height)) 
        self.screen.blit(self.cpy_image, self.rect.topleft)
class Button:
    def __init__(self, screen: pg.Surface, pos: Tuple[float, float], text: str, color: Tuple, font: pg.font.Font, text_color: Tuple=(0, 0, 0)):
        self.screen = screen
        self.pos = pos
        self.text = text
        self.color = color
        self.button = font.render(text, text_color)
        self.interactive = True
        self.__text_color__ = text_color
        self.__font__ = font
        
    def update(self, gui=None, shop_x=None):
        center = self.button[1]
        self.bg = center.copy()
        self.bg.width = self.bg.width + 10
        center.center = self.bg.center = (self.screen.get_width() * self.pos[0], self.screen.get_height() * self.pos[1])
        if shop_x and gui:
            shop_width = gui.getXmargin() - gui.IMAGE_SIZE()
            center.centerx = shop_width * shop_x
        if center.collidepoint(pg.mouse.get_pos()) and self.interactive:
            self.bg = self.bg.scale_by(1.05, 1.05)
            tmp_clr = tuple(map(lambda i, j: i + j, self.color, (10, 10, 25)))
        else: tmp_clr = self.color
        self.bg = self.bg.scale_by(1.2, 1.2)
        self.bg.center = center.center
        pg.draw.rect(self.screen, tmp_clr, self.bg, border_radius=10)
        self.screen.blit(self.button[0], center) 
        
    def change_text_color(self, text):
        self.button = self.__font__.render(text, self.__text_color__)


class GUI:
    

    def __init__(self) -> None:
        
        self.model = Model(8, 10)
        self.size = lambda: len(self.model.board)
        pg.init()
        self.btn_clr = (170, 155, 187)
        self.shop_clr = (224, 184, 52)
        self.screen = pg.display.set_mode((1200, 800), pg.RESIZABLE)
        pg.display.set_caption("RogueSweeper")
        self.fb_cls = shop.Fireball(0)
        self.lz_cls = shop.Lazer(0)
        # Create The Background
        self.background = pg.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((64, 110, 153))
        self.IMAGE_SIZE = lambda: self.screen.get_height() // (self.size() + 4)
        self.getXmargin = lambda: self.screen.get_width() - self.IMAGE_SIZE() * (self.size() + 1) # where grid starts
        self.getYmargin = lambda: self.IMAGE_SIZE() * 3 # Where grid starts
        self.font = font = ft.SysFont('Comic Sans MS', 30)
        
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
        
        # set win screen and button
        self.win_bg = pg.Surface(self.screen.get_size(), pg.SRCALPHA)
        self.win_text = Button(self.screen, (.5, .2), 'You Win', (55, 55, 55), font, (225, 225, 225))
        self.win_text.interactive = False
        self.win_btn = Button(self.screen, (.5, .6), 'Shop', self.shop_clr, font)
        
        # set coins and shop screen
        self.coins = 0
        img_rect = pg.Rect(0, self.getYmargin(), (self.getXmargin() - self.IMAGE_SIZE()) / 4, (self.getXmargin() - self.IMAGE_SIZE()) / 4)  
        img_rect.centerx = (self.getXmargin() - self.IMAGE_SIZE()) / 4
        self.fb_img = Image(self.screen, img_rect, pg.image.load('./images/fireball.jpg'))
        self.fb_buy = Button(self.screen, (img_rect.centerx / self.screen.get_width(), 4 / 6), f'Buy: {self.fb_cls.cost}', self.shop_clr, font)
        self.fb_ug = Button(self.screen, (img_rect.centerx / self.screen.get_width(), 5 / 6), f'Upgrade: {self.fb_cls.get_upgrade_cost()}', self.shop_clr, font)
        lz_rect = img_rect.copy()
        lz_rect.centerx *= 3
        self.lz_img = Image(self.screen, lz_rect, pg.image.load('./images/lazer.jpg'))
        self.lz_buy = Button(self.screen, (lz_rect.centerx / self.screen.get_width(), 4 / 6), f'Buy: {self.lz_cls.cost}', self.shop_clr, font)
        self.lz_ug = Button(self.screen, (lz_rect.centerx / self.screen.get_width(), 5 / 6), f'Upgrade: {self.lz_cls.get_upgrade_cost()}', self.shop_clr, font)
        self.ctrl_txt = Button(self.screen, (1 - (self.IMAGE_SIZE() * self.size() / 2) / self.screen.get_width(), self.IMAGE_SIZE() / self.screen.get_height() / 2), f'Use Fireball: Q     Use Lazer: E', (64, 110, 153), font, (255, 255, 255))
        self.cnt_txt = Button(self.screen, (1 - (self.IMAGE_SIZE() * self.size() / 2) / self.screen.get_width(), self.IMAGE_SIZE() / self.screen.get_height() * 1.5), f'Count: {self.fb_cls.count}          Count: {self.lz_cls.count}', (64, 110, 153), font, (255, 255, 255))
        self.ctrl_txt.interactive = False
        self.cnt_txt.interactive = False
        
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

    def tile_at(self, pos: Tuple[int, int]) -> Tuple[int, int]:
        # returns minesweeper grid pos for a mouse click
        grid_x = (pos[0] - self.getXmargin()) // self.IMAGE_SIZE()
        grid_y = (pos[1] - self.getYmargin()) // self.IMAGE_SIZE()
        return grid_x, grid_y
    
    def reveal_tiles(self, x: int, y: int) -> None:
        # recursive function to reveal empty spaces
        if (x < 0 or x >= self.size()) or (y < 0 or y >= self.size()):
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
        for x in range(self.size()):
            for y in range(self.size()):
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
        barrier = self.getXmargin() - self.IMAGE_SIZE()
        pg.draw.line(self.screen, (0, 0, 0), (barrier, self.getYmargin() - self.IMAGE_SIZE()), (self.screen.get_width(), self.getYmargin() - self.IMAGE_SIZE()), 3)
        pg.draw.line(self.screen, (0, 0, 0), (barrier, 0), (self.getXmargin() - self.IMAGE_SIZE(), self.screen.get_height()), 3)
        self.coin_text = Button(self.screen, (barrier / 2 / self.screen.get_width(), .1), f"Coins: {self.coins}", self.shop_clr, self.font)
        self.coin_text.update()
        
    def __draw_shop__(self):
        self.fb_img.update(self, 1/3)
        self.fb_buy.update(self, 1/3)
        self.fb_ug.change_text_color(f'Upgrade: {self.fb_cls.get_upgrade_cost()}')
        if self.fb_cls.get_upgrade_cost() == 'Max':
            self.fb_ug.interactive = False
        self.fb_ug.update(self, 1/3)
        self.lz_img.update(self, 2/3)
        self.lz_buy.update(self, 2/3)
        self.lz_ug.change_text_color(f'Upgrade: {self.lz_cls.get_upgrade_cost()}')
        if self.lz_cls.get_upgrade_cost() == 'Max':
            self.lz_ug.interactive = False
        self.lz_ug.update(self, 2/3)
        self.ctrl_txt.update()
        self.cnt_txt.change_text_color(f'Count: {self.fb_cls.count}          Count: {self.lz_cls.count}')
        self.cnt_txt.update()