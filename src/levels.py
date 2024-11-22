import pygame as pg




class Levels:
    def __init__(self, gui):
        self.gui = gui
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
        gui = self.gui
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
                    x, y = gui.tile_at(pos)
                    if 0 <= x <= 7 and 0 <= y <= 7:
                        selected = gui.model.board[y][x]
                        if event.button == 3: # right click
                            if selected.status == 0:
                                selected.status = -1 # set to flag
                            elif selected.status == -1:
                                selected.status = 0 # remove flag
                                     
                        elif event.button == 1: # left click
                            # if we haven't called generate_mines yet, we need to call it
                            if not gui.model.generated:
                                gui.model.generate_mines(x, y)
                            if selected.status == 0:
                                gui.reveal_tiles(x, y)
                            if selected.tile_type == -1:
                                self.run_lose()
                                             
            if gui.model.is_complete():
                self.run_win()

            
            # Draw to screen
            gui.background = pg.transform.scale(gui.background, gui.screen.get_size())
            gui.screen.blit(gui.background, (0, 0))
            gui.__draw_layout__()
            gui.__draw_board__()
            pg.display.flip()
        
    def run_pause(self):
        paused = True
        gui = self.gui
        while paused:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                        paused = False
                        return
                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    if gui.cont_btn.cont_button[1].collidepoint(pos):
                        paused = False
                    elif gui.exit_btn.cont_button[1].collidepoint(pos):
                        exit()

            # draw transparent background
            gui.background = pg.transform.scale(gui.background, gui.screen.get_size())
            gui.screen.blit(gui.background, (0, 0))
            gui.__draw_board__()
            gui.__draw_layout__()
            pg.draw.rect(gui.pause_bg, (100, 100, 100, 127), gui.pause_bg.get_rect())
            gui.pause_bg = pg.transform.scale(gui.pause_bg, gui.screen.get_size())
            gui.screen.blit(gui.pause_bg, (0, 0))
            # draw text
            gui.pause_text.update()
            # draw buttons
            gui.cont_btn.update()
            gui.exit_btn.update()
            pg.display.flip()
        
    def run_lose(self):
        print("loss!")
        #Temporary pause
        self.run_pause()
        
    def run_win(self):
        print("win!")
        #Temporary pause
        self.run_pause()