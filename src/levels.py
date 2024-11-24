import pygame as pg
from GUI import GUI
from model import Model


class Levels(GUI):
    def __init__(self):
        GUI.__init__(self)
        self.level = 0
        self.levels = [
            {
                "name": "Easy",
                "mines": 10,
                "size": 8
            },
            {
                "name": "Medium",
                "mines": 15,
                "size": 10
            },
            {
                "name": "Hard",
                "mines": 25,
                "size": 12
            },
            {
                "name": "Insane",
                "mines": 35,
                "size": 14
            }
        ]
    
    def run_game(self):
        going = True
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
                        selected = self.model.board[y][x]
                        if event.button == 3: # right click
                            if selected.status == 0:
                                selected.status = -1 # set to flag
                            elif selected.status == -1:
                                selected.status = 0 # remove flag
                                     
                        elif event.button == 1: # left click
                            # if we haven't called generate_mines yet, we need to call it
                            if not self.model.generated:
                                self.model.generate_mines(x, y)
                            if selected.status == 0:
                                self.reveal_tiles(x, y)
                            if selected.tile_type == -1:
                                self.run_lose()
                                             
            if self.model.is_complete():
                self.run_win()

            
            # Draw to screen
            self.background = pg.transform.scale(self.background, self.screen.get_size())
            self.screen.blit(self.background, (0, 0))
            self.__draw_layout__()
            self.__draw_board__()
            pg.display.flip()
        
    def run_pause(self):
        paused = True
        while paused:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                        paused = False
                        return
                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    if self.cont_btn.button[1].collidepoint(pos):
                        paused = False
                    elif self.exit_btn.button[1].collidepoint(pos):
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
        
    def run_lose(self):
        going = True
        while going:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    exit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    if self.restart_btn.button[1].collidepoint(pos):
                        going = False
        
            # draw transparent background
            self.background = pg.transform.scale(self.background, self.screen.get_size())
            self.screen.blit(self.background, (0, 0))
            self.__draw_board__()
            self.__draw_layout__()
            pg.draw.rect(self.pause_bg, (100, 100, 100, 127), self.pause_bg.get_rect())
            self.lose_bg = pg.transform.scale(self.lose_bg, self.screen.get_size())
            self.screen.blit(self.lose_bg, (0, 0))
            pg.draw.rect(self.screen, (200, 50, 50, 127), self.screen.get_rect())
            self.img_mine.update()
            self.restart_btn.update()
            self.lose_text.update()
            pg.display.flip()
        
    def run_win(self):
        print("win!")
        self.level += 1
        self.model = Model(self.levels[self.level]['size'], self.levels[self.level]['mines'])
        #Temporary pause
        self.run_pause()
        
        
if __name__ == '__main__':
    GUI.load_images()
    levels = Levels()
    levels.run_game()
    
