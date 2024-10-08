import pygame as pg
import pygame_gui as GUI
class GUI:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode((1280, 480), pg.SCALED)
        pg.display.set_caption("Minesweeper")

        # Create The Background
        self.background = pg.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((170, 155, 187))
        
    def __run_game__(self):
        going = True
        clock = pg.time.Clock()
        while going:
            clock.tick(60)

            # Handle Input Events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    going = False
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    going = False
            
            # Draw to screen
            self.screen.blit(self.background, (0, 0))
            pg.display.flip()

def main():
    g = GUI()
    g.__run_game__()
    
if __name__ == '__main__':
    main()