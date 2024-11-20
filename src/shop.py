from abc import ABC, abstractmethod
from model import Model

class Item(ABC):
    """
    Parent class for all buyable items

    """
    def __init__(self):
        """
        Initializes a new game of chess

        Variables
        ---------
        self.obtained
            - Status of player ownership

        """
        self.obtained = False

    @abstractmethod
    def buy_item(self):
        pass

    @abstractmethod
    def use_item(self):
        pass

class Fireball(Item):
    """
    Class for the fireball item

    """
    def __init__(self):
        """
        Initializes the fireball item

        Variables
        ---------
        self.level
            - sets the level of the item

        """         
        self.level = 1
    
    def buy_item(self, coins):
        """
        Changes obtained variable if player has sufficient funds

        Parameters
        ----------
        coins
            - the amount of coins the player has

        Returns
        -------
        The amount of coins remaining

        """
        if coins < 50:
            return coins
        else:
            coins -= 50
            self.obtained is True
            return coins
    
    def upgrade_item(self, coins):
        """
        Upgrades the fireball if the plater has sufficient funds

        Parameters
        ----------
        coins
            - the amount of coins the player has

        Returns
        -------
        The amount of coins remaining

        """
        if self.obtained is False:
            return coins
        elif self.level == 1:
            if coins < 100:
                return coins
            else:
                coins -= 100
                self.level +=1
                return coins
        elif self.level == 2:
            if coins < 200:
                return coins
            else:
                coins -= 200
                self.level +=1
        return coins
        
    def use_item(self, model, x: int, y: int):
        """
        Uses the fireball item

        Parameters
        ----------
        model
            - the board class to be fireballed
        x
            - the x coordinate
        y
            - the y coordinate
        """
        model.board[x][y].status = 1

"""
b = Model(8, 10)
f = Fireball()

f.use_item(b, 0, 1)


printmodel = []
for row in range(len(b.board)):
    row_placeholder = []
    for column in range(len(b.board[row])):
        row_placeholder.append(b.board[row][column].status)
    printmodel.append(row_placeholder)

print(printmodel)
"""

