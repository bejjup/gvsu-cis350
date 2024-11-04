from print_screens import print_board


def start_button(vals):
    if (450 < vals.mx < 750) and (450 < vals.my < 570):
        # TEST FOR WHEN THE START BUTTON HAS BEEN PRESSED
        print("You clicked start")
        vals.START = False
        vals.SELEC = True

def icon_nog_ops(vals, Players, file):
    if (100 < vals.mx < 400) and (100 < vals.my < 400) and vals.P1:
        # declares that P1 can no longer be used and increases whose turn it is to choose by 1
        vals.P1 = False
        p_1 = Players(1, vals.player, file)
        p_1.set_start_val()
        vals.p_1 = p_1
        vals.player += 1
        vals.plays.append(p_1)

def icon_jonesy(vals, Players, file):
    if (800 < vals.mx < 1100) and (100 < vals.my < 400) and vals.P2:
        # declares that P2 can no longer be used and increases whose turn it is to choose by 1
        vals.P2 = False
        p_2 = Players(2, vals.player, file)
        p_2.set_start_val()
        vals.p_2 = p_2
        vals.player += 1
        vals.plays.append(p_2)

def icon_raven(vals, Players, file):
    if (100 < vals.mx < 400) and (450 < vals.my < 750) and vals.P3:
        # declares that P3 can no longer be used and increases whose turn it is to choose by 1
        vals.P3 = False
        p_3 = Players(3, vals.player, file)
        p_3.set_start_val()
        vals.p_3 = p_3
        vals.player += 1
        vals.plays.append(p_3)

def icon_john_wick(vals, Players, file):
    if (800 < vals.mx < 1100) and (450 < vals.my < 750) and vals.P4:
        # declares that P4 can no longer be used and increases whose turn it is to choose by 1
        vals.P4 = False
        p_4 = Players(4, vals.player, file)
        p_4.set_start_val()
        vals.p_4 = p_4
        vals.player += 1
        vals.plays.append(p_4)

def icons(vals, Players, file):
    icon_nog_ops(vals, Players, file)
    # if P2 icon is clicked while it is still available
    icon_jonesy(vals, Players, file)
    # if P3 icon is clicked while it is still available
    icon_raven(vals, Players, file)
    # if P4 icon is clicked while it is still available
    icon_john_wick(vals, Players, file)

def continue_button(vals):
    if (510 < vals.mx < 690) and (480 < vals.my < 510) and vals.player == 5:
        # TEST FOR WHEN THE CONTINUE BUTTON HAS BEEN CLICKED
        print("You clicked start Again")
        vals.SELEC = False
        vals.GAME = True
        vals.player = 1
        vals.P1 = True
        vals.P2 = True
        vals.P3 = True
        vals.P4 = True

def return_to_game(scrn, pygame, file, vals, board):
    if (50 < vals.mx < 352) and (715 < vals.my < 750):
        vals.INFO = False
        vals.SETTINGS = False
        vals.GAME = True
        print_board(scrn, pygame, file, vals, board)

def settings_button(vals):
    if (8 < vals.mx < 91) and (20 < vals.my < 36):
        vals.GAME = False
        vals.SETTINGS = True

def volume_button(vals, mixer):
    if (360 < vals.mx < 380) and (280 < vals.my < 315):
        mixer.music.set_volume(0)
    elif (450 < vals.mx < 490) and (280 < vals.my < 315):
        mixer.music.set_volume(.2)
    elif (547 < vals.mx < 593) and (280 < vals.my < 315):
        mixer.music.set_volume(.4)
    elif (648 < vals.mx < 693) and (280 < vals.my < 315):
        mixer.music.set_volume(.6)
    elif (748 < vals.mx < 793) and (280 < vals.my < 315):
        mixer.music.set_volume(.8)
    elif (838 < vals.mx < 905) and (280 < vals.my < 315):
        mixer.music.set_volume(1)

def resize_screen(vals, pygame):
    if (528 < vals.mx < 674) and (187 < vals.my < 211):
        pygame.display.set_mode((1200, 800))
        vals.full_screen = False
    elif (729 < vals.mx < 872) and (187 < vals.my < 211):
        pygame.display.set_mode((1800, 900))
        vals.full_screen = True

def screen_mode(vals):
    if (495 < vals.mx < 708) and (382 < vals.my < 411):
        vals.current = vals.blue
    elif (797 < vals.mx < 1006) and (382 < vals.my < 411):
        vals.current = vals.black


def info_button(vals):
    if (32 < vals.mx < 68) and (51 < vals.my < 66):
        vals.GAME = False
        vals.INFO = True

def roll_dice(vals, mixer, file, pygame, board, random):
    if (875 < vals.mx < 1175) and (50 < vals.my < 750) and vals.DICE:
        # declares that the player just rolled
        vals.DICE = False
        vals.DOUBLES = False
        vals.ROLLING = True

        mixer.music.load(file.roll_effect)
        pygame.mixer.music.queue(file.music)
        mixer.music.play()

        current_player = vals.plays[vals.player - 1]
        current_player.space += vals.num1 + vals.num2

        print(f'{current_player.name} on space: {board[current_player.space].name}')
        if board[current_player.space].name == "Launchpad":
            current_player.space += random.randint(1, 6)
            print(f'You jumped! to {board[current_player.space].name}')

        if board[current_player.space].name == "Go To Jail":
            current_player.space = 8
            current_player.jail = True
            print("You go to jail now!")

        if board[current_player.space].name == "Chest":
            current_player.money -= board[current_player.space].price
            print(f'You gained {-board[current_player.space].price} materials!')

        for p in range(0,3):
            owner = vals.plays[p]
            if board[current_player.space] in owner.inventory and owner != current_player:
                print(f'{owner.name} owns this space.')
                if current_player.money - board[current_player.space].price >= 0:
                    owner.money += board[current_player.space].price
                    current_player.money -= board[current_player.space].price
                    print(f'{current_player.name} paid {owner.name} {board[current_player.space].price}')
                else:
                    current_player.health -= 50
                    if current_player.health <= 0:
                        if current_player == vals.plays[0]:
                            vals.P1 = False
                        elif current_player == vals.plays[1]:
                            vals.P2 = False
                        elif current_player == vals.plays[2]:
                            vals.P3 = False
                        elif current_player == vals.plays[3]:
                            vals.P4 = False
                        for stuff in current_player.inventory:
                            owner.add_to_inventory(stuff)
                            stuff.owner = owner
                        current_player.inventory = []
                        mixer.music.load(file.death)
                        pygame.mixer.music.queue(file.music)
                        mixer.music.play()
                        print(f'{current_player.name} died :(')
                    print(f'{current_player.name} took 50 damage')
        def check_for_win():
            if vals.P1 and not vals.P2 and not vals.P3 and not vals.P4:
                print()
                print(f'{vals.plays[0].name} WON!')
                print()
                vals.winner = vals.plays[0]
                vals.WIN = True
                vals.GAME = False
                mixer.music.load(file.death)
                pygame.mixer.music.queue(file.music)
                mixer.music.play()
            elif not vals.P1 and vals.P2 and not vals.P3 and not vals.P4:
                print()
                print(f'{vals.plays[1].name} WON!')
                print()
                vals.winner = vals.plays[1]
                vals.WIN = True
                vals.GAME = False
            elif not vals.P1 and not vals.P2 and vals.P3 and not vals.P4:
                print()
                print(f'{vals.plays[2].name} WON!')
                print()
                vals.winner = vals.plays[2]
                vals.WIN = True
                vals.GAME = False
            elif not vals.P1 and not vals.P2 and not vals.P3 and vals.P4:
                print()
                print(f'{vals.plays[3].name} WON!')
                print()
                vals.winner = vals.plays[3]
                vals.WIN = True
                vals.GAME = False
        check_for_win()

        current_player.get_icon_location(board)

def check_doubles(vals):
    if (875 < vals.mx < 1175) and (50 < vals.my < 750) and vals.num1 == vals.num2:
        # declares that the player has doubles
        vals.plays[vals.player-1].doubles_count += 1
        vals.DOUBLES = True
        vals.DICE = False
        vals.ROLLING = False

    elif (875 < vals.mx < 1175) and (50 < vals.my < 750) and vals.DOUBLES:
        vals.DOUBLES = False
        vals.DICE = True
        vals.ROLLING = False

def next_turn(vals, random):
    if (920 < vals.mx < 1130) and (5 < vals.my < 45) and not vals.DICE and not vals.DOUBLES:
        vals.plays[vals.player - 1].doubles_count = 0
        vals.DICE = True
        vals.DOUBLES = False
        vals.num1 = random.randint(1, 6)
        vals.num2 = random.randint(1, 6)
        vals.player += 1
        if vals.player > 4:
            vals.player -= 4
        if not vals.P1 and vals.player == 1:
            vals.player = 2
        if not vals.P2 and vals.player == 2:
            vals.player = 3
        if not vals.P3 and vals.player == 3:
            vals.player = 4
        if not vals.P4 and vals.player == 4:
            vals.player = 1
        if not vals.P1 and vals.player == 1:
            vals.player = 2


def roll_again(vals, random):
    if (920 < vals.mx < 1130) and (5 < vals.my < 45):
        # resets the rolling values to allow the next turn
        vals.DICE = True
        vals.DOUBLES = False
        vals.num1 = random.randint(1, 6)
        vals.num2 = random.randint(1, 6)

def purchase(vals, board):
    if board[vals.plays[vals.player - 1].space].buyable and board[vals.plays[vals.player - 1].space] not in vals.plays[vals.player - 1].inventory:
        if vals.plays[vals.player - 1].money > board[vals.plays[vals.player - 1].space].price:
            if (669 < vals.mx < 852) and (700 < vals.my < 740):
                vals.plays[vals.player - 1].add_to_inventory(board[vals.plays[vals.player - 1].space])
                board[vals.plays[vals.player - 1].space].buyable = False
                vals.plays[vals.player - 1].money -= board[vals.plays[vals.player - 1].space].price
                board[vals.plays[vals.player - 1].space].owner = vals.plays[vals.player - 1]
                print(f'{vals.plays[vals.player - 1].name} bought {board[vals.plays[vals.player - 1].space].name} for {board[vals.plays[vals.player - 1].space].price}')

def pay(vals, board):
    if board[vals.plays[vals.player - 1].space].name == 'Jail' and vals.plays[vals.player - 1].jail:
            if (669 < vals.mx < 852) and (700 < vals.my < 740) and vals.plays[vals.player - 1].money >= 50:
                current_player = vals.plays[vals.player - 1]
                current_player.jail = False
                current_player.money -= 50
                current_player.get_icon_location(board)
                print(f'{current_player.name} paid to get out of jail')
