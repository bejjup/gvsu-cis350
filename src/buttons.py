def start_button(mx, my, vals):
    if (450 < mx < 750) and (450 < my < 570):
        # TEST FOR WHEN THE START BUTTON HAS BEEN PRESSED
        print("You clicked start")
        vals.START = False
        vals.SELEC = True

def icon_nog_ops(mx, my, vals, Players):
    if (100 < mx < 400) and (100 < my < 400) and vals.P1:
        # declares that P1 can no longer be used and increases whose turn it is to choose by 1
        vals.P1 = False
        p_1 = Players(1, vals.player)
        p_1.set_start_val()
        vals.p_1 = p_1
        vals.player += 1
        vals.plays.append(p_1)

def icon_jonesy(mx, my, vals, Players):
    if (800 < mx < 1100) and (100 < my < 400) and vals.P2:
        # declares that P2 can no longer be used and increases whose turn it is to choose by 1
        vals.P2 = False
        p_2 = Players(2, vals.player)
        p_2.set_start_val()
        vals.p_2 = p_2
        vals.player += 1
        vals.plays.append(p_2)

def icon_raven(mx, my, vals, Players):
    if (100 < mx < 400) and (450 < my < 750) and vals.P3:
        # declares that P3 can no longer be used and increases whose turn it is to choose by 1
        vals.P3 = False
        p_3 = Players(3, vals.player)
        p_3.set_start_val()
        vals.p_3 = p_3
        vals.player += 1
        vals.plays.append(p_3)

def icon_john_wick(mx, my, vals, Players):
    if (800 < mx < 1100) and (450 < my < 750) and vals.P4:
        # declares that P4 can no longer be used and increases whose turn it is to choose by 1
        vals.P4 = False
        p_4 = Players(4, vals.player)
        p_4.set_start_val()
        vals.p_4 = p_4
        vals.player += 1
        vals.plays.append(p_4)
def icons(mx, my, vals, Players):
    icon_nog_ops(mx, my, vals, Players)
    # if P2 icon is clicked while it is still available
    icon_jonesy(mx, my, vals, Players)
    # if P3 icon is clicked while it is still available
    icon_raven(mx, my, vals, Players)
    # if P4 icon is clicked while it is still available
    icon_john_wick(mx, my, vals, Players)

def continue_button(mx, my, vals):
    if (510 < mx < 690) and (480 < my < 510) and vals.player == 5:
        # TEST FOR WHEN THE CONTINUE BUTTON HAS BEEN CLICKED
        print("You clicked start Again")
        vals.SELEC = False
        vals.GAME = True
        vals.player = 1

def return_to_game(mx, my, vals):
    if (50 < mx < 352) and (715 < my < 750):
        vals.INFO = False
        vals.GAME = True

def info_button(mx, my, vals):
    if (20 < mx < 80) and (15 < my < 40):
        vals.GAME = False
        vals.INFO = True

def roll_dice(mx, my, vals, mixer, file, pygame, board, random):
    if (875 < mx < 1175) and (50 < my < 750) and vals.DICE:
        # declares that the player just rolled
        vals.DICE = False
        vals.DOUBLES = False
        vals.ROLLING = True
        mixer.music.load(file.roll_effect)
        pygame.mixer.music.queue(file.music)
        mixer.music.play()
        current_player = vals.plays[vals.player - 1]
        vals.plays[vals.player - 1].space += vals.num1 + vals.num2
        print(f'{current_player.name} on space: {board[current_player.space].name}')
        if current_player.num == 1:
            current_player.loc_x = board[current_player.space].loc1_x
            current_player.loc_y = board[current_player.space].loc1_y
        elif current_player.num == 2:
            current_player.loc_x = board[current_player.space].loc2_x
            current_player.loc_y = board[current_player.space].loc2_y
        elif current_player.num == 3:
            current_player.loc_x = board[current_player.space].loc3_x
            current_player.loc_y = board[current_player.space].loc3_y
        elif current_player.num == 4:
            current_player.loc_x = board[current_player.space].loc4_x
            current_player.loc_y = board[current_player.space].loc4_y
        current_player.wood -= board[current_player.space].price
        if board[current_player.space].name == "Launchpad":
            print('Jump')
            current_player.space += random.randint(1, 6)
            print('You jumped!')

def check_doubles(mx, my, vals):
    if (875 < mx < 1175) and (50 < my < 750) and vals.num1 == vals.num2:
        # declares that the player has doubles
        vals.DOUBLES = True
        vals.DICE = False
        vals.ROLLING = False
    elif (875 < mx < 1175) and (50 < my < 750) and vals.DOUBLES:
        vals.DOUBLES = False
        vals.DICE = True
        vals.ROLLING = False

def next_turn(mx, my, vals, random):
    if (920 < mx < 1130) and (5 < my < 45) and not vals.DICE and not vals.DOUBLES:
        vals.DICE = True
        vals.DOUBLES = False
        vals.num1 = random.randint(1, 6)
        vals.num2 = random.randint(1, 6)
        vals.player += 1
        if vals.player == 5:
            vals.player = 1

def roll_again(mx, my, vals, random):
    if (920 < mx < 1130) and (5 < my < 45):
        # resets the rolling values to allow the next turn
        vals.DICE = True
        vals.DOUBLES = False
        vals.num1 = random.randint(1, 6)
        vals.num2 = random.randint(1, 6)
