import random
from players import Players


class Values:
    def __init__(self, pygame, file):

        self._DICE = True
        self._DOUBLES = False
        self._GAME = False
        self._START = True
        self._SELEC = False
        self._INFO = False
        self._P1 = True
        self._P2 = True
        self._P3 = True
        self._P4 = True
        self._player = 1
        self._num1 = random.randint(1,6)
        self._num2 = random.randint(1,6)
        self._font1 = pygame.font.Font('freesansbold.ttf', 40)
        self._font2 = pygame.font.Font('freesansbold.ttf', 20)
        self._font3 = pygame.font.Font('freesansbold.ttf', 30)
        self._font4 = pygame.font.Font('freesansbold.ttf', 10)
        self._plays = []
        self._mus_time = 0
        self._clicking = False
        self._p_1 = Players
        self._p_2 = Players
        self._p_3 = Players
        self._p_4 = Players
        self._dice1 = pygame.image.load(file.dice)
        self._dice1 = pygame.transform.scale(self._dice1, (50, 50))
        # sets dice2 to the image of the dice, and declares its size and location
        self._dice2 = pygame.image.load(file.dice)
        self._dice2 = pygame.transform.scale(self._dice2, (50, 50))
        self._mx = 0
        self._my = 0

    @property
    def DICE(self):
        return self._DICE

    @DICE.setter
    def DICE(self, value):
        self._DICE = value

    @property
    def DOUBLES(self):
        return self._DOUBLES

    @DOUBLES.setter
    def DOUBLES(self, value):
        self._DOUBLES = value

    @property
    def GAME(self):
        return self._GAME

    @GAME.setter
    def GAME(self, value):
        self._GAME = value

    @property
    def START(self):
        return self._START

    @START.setter
    def START(self, value):
        self._START = value

    @property
    def SELEC(self):
        return self._SELEC

    @SELEC.setter
    def SELEC(self, value):
        self._SELEC = value

    @property
    def INFO(self):
        return self._INFO

    @INFO.setter
    def INFO(self, value):
        self._INFO = value

    @property
    def P1(self):
        return self._P1

    @P1.setter
    def P1(self, value):
        self._P1 = value

    @property
    def P2(self):
        return self._P2

    @P2.setter
    def P2(self, value):
        self._P2 = value

    @property
    def P3(self):
        return self._P3

    @P3.setter
    def P3(self, value):
        self._P3 = value

    @property
    def P4(self):
        return self._P4

    @P4.setter
    def P4(self, value):
        self._P4 = value

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, value):
        self._player = value

    @property
    def num1(self):
        return self._num1

    @num1.setter
    def num1(self, value):
        self._num1 = value

    @property
    def num2(self):
        return self._num2

    @num2.setter
    def num2(self, value):
        self._num2 = value

    @property
    def font1(self):
        return self._font1

    @font1.setter
    def font1(self, value):
        self._font1 = value

    @property
    def font2(self):
        return self._font2

    @font2.setter
    def font2(self, value):
        self._font2 = value

    @property
    def font3(self):
        return self._font3

    @font3.setter
    def font3(self, value):
        self._font3 = value

    @property
    def font4(self):
        return self._font4

    @font4.setter
    def font4(self, value):
        self._font4 = value

    @property
    def plays(self):
        return self._plays

    @plays.setter
    def plays(self, value):
        self._plays = value

    @property
    def clicking(self):
        return self._clicking

    @clicking.setter
    def clicking(self, value):
        self._clicking = value

    @property
    def p_1(self):
        return self._p_1

    @p_1.setter
    def p_1(self, value):
        self._p_1 = value

    @property
    def p_2(self):
        return self._p_2

    @p_2.setter
    def p_2(self, value):
        self._p_2 = value

    @property
    def p_3(self):
        return self._p_3

    @p_3.setter
    def p_3(self, value):
        self._p_3 = value

    @property
    def p_4(self):
        return self._p_4

    @p_4.setter
    def p_4(self, value):
        self._p_4 = value

    @property
    def dice1(self):
        return self._dice1

    @property
    def dice2(self):
        return self._dice2

    @property
    def mx(self):
        return self._mx

    @mx.setter
    def mx(self, value):
        self._mx = value

    @property
    def my(self):
        return self._my

    @my.setter
    def my(self, value):
        self._my = value


