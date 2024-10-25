def print_start(scrn, pygame, file, vals):
    if vals.START:
        #fills the screen to blue
        scrn.fill((27, 144, 221))

        # sets imp to the image of the board, and declares its size
        start_but = pygame.image.load(file.start)
        start_but = pygame.transform.scale(start_but, (300, 120))
        scrn.blit(start_but, (450, 450))

        #sets imp to the image of the board, and declares its size and location
        title = pygame.image.load(file.title)
        title = pygame.transform.scale(title, (900, 200))
        scrn.blit(title, (150, 150))

def print_selec(scrn, pygame, file, vals):

    #fills the screen to blue
    scrn.fill((27, 144, 221))

    #creates the selection screen text
    title = pygame.image.load(file.title)
    title = pygame.transform.scale(title, (400, 100))
    scrn.blit(title, (750, 5))

    #tells the user whose turn it is to choose a player
    if vals.player <5:
        text = vals.font1.render(f'Player {vals.player} Choose:', True, (245, 245, 245))
        textRect = text.get_rect()
        textRect.center = (200, 50)
        scrn.blit(text, textRect)

    #the user is told to continue when all players are selected
    else:
        text = vals.font1.render(f'Please Continue!', True, (245, 245, 245))
        textRect = text.get_rect()
        textRect.center = (200, 50)
        scrn.blit(text, textRect)

        text = vals.font1.render(f'Continue', True, (245, 245, 245))
        textRect = text.get_rect()
        textRect.center = (600, 500)
        scrn.blit(text, textRect)

    #only shows the icons when they have not been selected yet
    def display_selec_icons():
        if vals.P1:
            nog_ops = pygame.image.load(file.nog_ops)
            nog_ops = pygame.transform.scale(nog_ops, (300, 300))
            scrn.blit(nog_ops, (100, 100))

        if vals.P2:
            jonesy = pygame.image.load(file.jonesy)
            jonesy = pygame.transform.scale(jonesy, (300, 300))
            scrn.blit(jonesy, (800, 100))

        if vals.P3:
            raven = pygame.image.load(file.raven)
            raven = pygame.transform.scale(raven, (300, 300))
            scrn.blit(raven, (100, 450))

        if vals.P4:
            j_wick = pygame.image.load(file.john_wick)
            j_wick = pygame.transform.scale(j_wick, (300, 300))
            scrn.blit(j_wick, (800, 450))
    display_selec_icons()

def print_info(scrn, pygame, file, vals):
    scrn.fill((27, 144, 221))
    title = pygame.image.load(file.title)
    title = pygame.transform.scale(title, (500, 100))
    scrn.blit(title, (650, 5))
    pygame.draw.rect(scrn, (0, 0, 0), pygame.Rect(97, 97, 86, 121))
    pygame.draw.rect(scrn, (0, 0, 0), pygame.Rect(97, 247, 86, 121))

    imp = pygame.image.load(file.map)
    imp = pygame.transform.scale(imp, (800, 800))
    subsurface = imp.subsurface((525, 685, 80, 115))
    scrn.blit(subsurface, (100, 100))
    subsurface2 = imp.subsurface((198, 685, 80, 115))
    scrn.blit(subsurface2, (100, 250))

    text = vals.font2.render(f'When you land on a launchpad tile, you will move 1-6 additional spaces!', True, (245, 245, 245))
    textRect = text.get_rect()
    textRect.center = (575, 157)
    scrn.blit(text, textRect)

    text = vals.font2.render(f'When you land on a chest tile,  you will gain materials!', True, (245, 245, 245))
    textRect = text.get_rect()
    textRect.center = (495, 307)
    scrn.blit(text, textRect)

    text = vals.font1.render(f'Rules: ', True, (245, 245, 245))
    textRect = text.get_rect()
    textRect.center = (163, 50)
    scrn.blit(text, textRect)

    text = vals.font1.render(f'Return to Game', True, (245, 245, 245))
    textRect = text.get_rect()
    textRect.center = (200, 735)
    scrn.blit(text, textRect)

def print_dice(pygame, scrn, vals):
    if vals.GAME:
        if vals.DICE:
            pygame.draw.rect(scrn, (27, 144, 221), pygame.Rect(865, 50, 335, 800))
            pygame.draw.rect(scrn, (0, 0, 0), pygame.Rect(875, 50, 300, 700))
            if (890 < vals.mx < 1175) and (73 < vals.my < 750):
                scrn.blit(vals.dice1, (vals.mx - 25, vals.my - 25))
                scrn.blit(vals.dice2, (vals.mx + 25, vals.my + 25))

            # moves dice to default spot if the mouse is not within the roll box
            else:
                scrn.blit(vals.dice1, (1060, 675))
                scrn.blit(vals.dice2, (1110, 675))

                # sets the text size and location, and prints the Dice label
                text = vals.font1.render('Dice:', True, (245, 245, 245), (0, 0, 0))
                textRect = text.get_rect()
                textRect.center = (960, 700)
                scrn.blit(text, textRect)

        elif vals.DOUBLES:
            pygame.draw.rect(scrn, (27, 144, 221), pygame.Rect(865, 50, 335, 800))
            pygame.draw.rect(scrn, (0, 0, 0), pygame.Rect(875, 50, 300, 700))
            if (890 < vals.mx < 1175) and (73 < vals.my < 750):
                scrn.blit(vals.dice1, (vals.mx - 25, vals.my - 25))
                scrn.blit(vals.dice2, (vals.mx + 25, vals.my + 25))

            else:
                # moves dice to default spot if the mouse is not within the roll box
                scrn.blit(vals.dice1, (1060, 675))
                scrn.blit(vals.dice2, (1110, 675))
                text = vals.font1.render('Dice:', True, (245, 245, 245), (0, 0, 0))
                textRect = text.get_rect()
                textRect.center = (960, 700)
                scrn.blit(text, textRect)

def print_board(scrn, pygame, file, vals, board):
    #fills the screen to blue
    scrn.fill((27, 144, 221))

    #draws the rectangles
    def recs():
        pygame.draw.rect(scrn, (0,0,0), pygame.Rect(145, 145, 510, 510))
        pygame.draw.rect(scrn, (0,0,0), pygame.Rect(875, 50, 300, 700))
        pygame.draw.rect(scrn, (0,0,0), pygame.Rect(265, 675, 390, 100))
        pygame.draw.rect(scrn, (0,0,0), pygame.Rect(25, 265, 100, 390))
        pygame.draw.rect(scrn, (0,0,0), pygame.Rect(675, 265, 100, 390))
        pygame.draw.rect(scrn, (0,0,0), pygame.Rect(265, 25, 390, 100))
    recs()

    text = vals.font3.render(f'Info', True, (245, 245, 245))
    textRect = text.get_rect()
    textRect.center = (50, 30)
    scrn.blit(text, textRect)

    #sets imp to the image of the board, and declares its size and location
    def map():
        imp = pygame.image.load(file.map)
        imp = pygame.transform.scale(imp, (500, 500))
        scrn.blit(imp, (150, 150))
    map()

    #displays player 1's information
    def process(p):
        for i in range(4):
            num = p.num
            if num == 1:
                p.p1_out(vals, scrn, pygame)
            elif num == 2:
                p.p2_out(vals, scrn, pygame)
            elif num == 3:
                p.p3_out(vals, scrn, pygame)
            elif num == 4:
                p.p4_out(vals, scrn, pygame)

    process(vals.p_1)
    process(vals.p_2)
    process(vals.p_3)
    process(vals.p_4)

    text = vals.font3.render(f'{vals.plays[vals.player-1].name}\'s turn', True, (245, 245, 245), vals.plays[vals.player-1].color)
    textRect = text.get_rect()
    textRect.center = (775, 25)
    scrn.blit(text, textRect)
    vals.plays[0].render_circle(scrn, pygame)
    vals.plays[1].render_circle(scrn, pygame)
    vals.plays[2].render_circle(scrn, pygame)
    vals.plays[3].render_circle(scrn, pygame)

    if vals.DICE:
        pass

    # if the previous dice were doubles
    elif vals.DOUBLES:

        # Displays the sum of the numbers rolled as well as that they were doubles
        text = vals.font1.render(f'Doubles {vals.num1 + vals.num2}!', True, (245, 245, 245))
        textRect = text.get_rect()
        textRect.center = (1000, 630)
        scrn.blit(text, textRect)

        # sets the text size and location, and prints the Dice label
        text = vals.font1.render('Dice:', True, (245, 245, 245))
        textRect = text.get_rect()
        textRect.center = (960, 700)
        scrn.blit(text, textRect)

        # displays the Roll Again button if the player can roll after had rolling doubles
        text = vals.font1.render('Roll Again:', True, (245, 245, 245))
        textRect = text.get_rect()
        textRect.center = (1025, 25)
        scrn.blit(text, textRect)

    else:
        # Displays the sum of the numbers rolled
        text = vals.font1.render(f'You Rolled {vals.num1 + vals.num2}!', True, (245, 245, 245))
        textRect = text.get_rect()
        textRect.center = (1025, 700)
        scrn.blit(text, textRect)

        # displays the Next Turn button if the player can roll
        text = vals.font1.render('Next Turn:', True, (245, 245, 245))
        textRect = text.get_rect()
        textRect.center = (1025, 25)
        scrn.blit(text, textRect)

    if board[vals.plays[vals.player-1].space].buyable and board[vals.plays[vals.player-1].space] not in vals.plays[vals.player-1].inventory:
        text = vals.font1.render(f'Purchase', True, (245, 245, 245), (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (760, 720)
        scrn.blit(text, textRect)
    mat_img = pygame.image.load(file.materials)
    mat_img = pygame.transform.scale(mat_img, (50, 30))
    scrn.blit(mat_img, (260, 695))
    scrn.blit(mat_img, (20, 265))
    scrn.blit(mat_img, (260, 45))
    scrn.blit(mat_img, (670, 265))
