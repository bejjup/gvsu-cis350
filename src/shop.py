from abc import ABC, abstractmethod
from model import Model

class Item(ABC):
    """
    Parent class for all buyable items

    """ 
    def __init__(self, level):
        """
        Initializes the item

        Variables
        ---------
        self.count
            - Status of player ownership
        self.level
            - sets the level of the item

        """
        self.count = 0
        self.cost = 5
        self.level = level
        self.upgrades = [20, 50, 'Max']

    @abstractmethod
    def buy_item(self):
        pass

    @abstractmethod
    def use_item(self):
        pass
    
    def get_upgrade_cost(self):
        return self.upgrades[self.level]

class Fireball(Item):
    def __init__(self, level):
        super().__init__(level)
    """
    Class for the fireball item

    """
    def buy_item(self, coins):
        """
        Changes count variable if player has sufficient funds

        Parameters
        ----------
        coins
            - the amount of coins the player has

        Returns
        -------
        The amount of coins remaining

        """
        if coins < self.cost:
            return coins
        else:
            coins -= self.cost
            self.count += 1
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
        if self.get_upgrade_cost() < coins and len(self.upgrades) > self.level:
                coins -= self.get_upgrade_cost()
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
        if self.level >= 0:
            model.board[x][y].status = 1
        if self.level >= 1:
            if x - 1 >= 0:
                model.board[x - 1][y].status = 1
            if x + 1 <= len(model.board) - 1:
                model.board[x + 1][y].status = 1
            if y - 1 >= 0:
                model.board[x][y - 1].status = 1
            if y + 1 <= len(model.board[x]) - 1:
                model.board[x][y + 1].status = 1
        if self.level >= 2:
            if x - 1 >= 0:
                if y - 1 >= 0:
                    model.board[x - 1][y - 1].status = 1
                if y + 1 <= len(model.board[x]) - 1:
                    model.board[x - 1][y + 1].status = 1
            if x + 1 <= len(model.board) - 1:
                if y - 1 >= 0:
                    model.board[x + 1][y - 1].status = 1
                if y + 1 <= len(model.board[x]) - 1:
                    model.board[x + 1][y + 1].status = 1
        self.count -= 1

class Lazer(Item):
    coins = 20
    def __init__(self, level):
        super().__init__(level)
    """
    Class for the lazer item

    """
    def buy_item(self, coins):
        """
        Changes count variable if player has sufficient funds

        Parameters
        ----------
        coins
            - the amount of coins the player has

        Returns
        -------
        The amount of coins remaining

        """
        if coins < self.cost:
            return coins
        else:
            coins -= self.cost
            self.count += 1
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
        if self.get_upgrade_cost() < coins and len(self.upgrades) > self.level:
                coins -= self.get_upgrade_cost()
                self.level +=1
        return coins
        
    def use_item(self, model, x: int, y: int):
        """
        Uses the lazer item

        Parameters
        ----------
        model
            - the board class to be fireballed
        x
            - the x coordinate
        y
            - the y coordinate

        """
        if self.level >= 0:
            model.board[x][y].status = 1
            if x - 1 >= 0:
                model.board[x - 1][y].status = 1
            if x + 1 <= len(model.board) - 1:
                model.board[x + 1][y].status = 1
        if self.level >= 1:
            if x - 2 >= 0:
                model.board[x - 2][y].status = 1
            if x + 2 <= len(model.board) - 1:
                model.board[x + 2][y].status = 1
        if self.level >= 2:
            if x - 3 >= 0:
                model.board[x - 3][y].status = 1
            if x + 3 <= len(model.board) - 1:
                model.board[x + 3][y].status = 1
        self.count -= 1

"""
b = Model(8, 10)
f = Fireball()
print(f.buy_item(500))
print(f.level)
print(f.upgrade_item(450))
print(f.level)
print(f.upgrade_item(350))
print(f.level)
f.use_item(b, 0, 0)


printmodel = []
for row in range(len(b.board)):
    row_placeholder = []
    for column in range(len(b.board[row])):
        row_placeholder.append(b.board[row][column].status)
    printmodel.append(row_placeholder)

print(printmodel)


b = Model(8, 10)
l = Lazer()
print(l.buy_item(500))
print(l.level)
print(l.upgrade_item(450))
print(l.level)
print(l.upgrade_item(350))
print(l.level)
l.use_item(b, 4, 4)


printmodel = []
for row in range(len(b.board)):
    row_placeholder = []
    for column in range(len(b.board[row])):
        row_placeholder.append(b.board[row][column].status)
    printmodel.append(row_placeholder)

print(printmodel)
"""
