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

        self.home_image = pg.image.load('./images/homescreen.png')
        self.home_image = pg.transform.scale(self.home_image, self.screen.get_size())  # Scale the image to fit the screen size

    def run_home_screen(self):
        showing = True
        while showing:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                elif event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN:
                    showing = False  # Exit the home screen when a key is pressed
            
            # Draw the home screen image
            self.screen.blit(self.home_image, (0, 0))
            
            
            font = pg.font.Font(None, 50)
            text = font.render("Press any key to start the game", True, (255, 255, 255))
            text_rect = text.get_rect(center=self.screen.get_rect().center)
            self.screen.blit(text, text_rect)
            
            # Update the display
            pg.display.flip()

    def run_game(self):
        self.run_home_screen()

        going = True
        while going:

            # Handle Input Events
            for event in pg.event.get():
                if event.type == pg.KEYDOWN and event.key == pg.K_LSHIFT:
                    self.run_win()
                if event.type == pg.QUIT:
                    going = False
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.run_pause()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    # TODO check each button to see if it was clicked
                    x, y = self.tile_at(pos)
                    if 0 <= x < self.size() and 0 <= y < self.size():
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
                        self.run_reset(full_reset = True)
                        going = False # TODO: change to full reset, for now this lets us test easily.
        
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
        print("You Win!")
        going = True
        while going:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    exit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    if self.win_btn.button[1].collidepoint(pos):
                        going = False
                        # TODO: change to shop screen
            self.background = pg.transform.scale(self.background, self.screen.get_size())
            self.screen.blit(self.background, (0, 0))
            self.__draw_board__()
            self.__draw_layout__()
            self.win_bg = pg.transform.scale(self.win_bg, self.screen.get_size())
            pg.draw.rect(self.win_bg, (50, 200, 50, 127), self.win_bg.get_rect())
            self.screen.blit(self.win_bg, (0, 0))
            self.win_text.update()
            self.win_btn.update()
            pg.display.flip()
        self.run_reset()
        
    def run_reset(self, full_reset = False):
        if full_reset:
            self.level = 0
        else:
            self.level += 1
        self.model = Model(self.levels[self.level]['size'], self.levels[self.level]['mines'])
            
        
if __name__ == '__main__':
    GUI.load_images()
    levels = Levels()
    levels.run_game()
    
