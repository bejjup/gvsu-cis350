import pygame as pg

class GUI:
    def __init__(self) -> None:
        pg.init()
        # self.__model = MineModel()
        self._screen = pg.display.set_mode((800, 600))
        pg.display.set_caption("Minesweeper Roguelike")
        self._screen.fill((255, 255, 255))
        
def main():
    g = GUI()
    
    
if __name__ == '__main__':
    main()