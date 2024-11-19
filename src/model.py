import random

class Tile:
    def __init__(self, type = 0):
        self.tile_type = type
        self.status = 0

    def __str__(self):
        return str(self.tile_type)

class Model:
    def __init__(self, size: int, mines: int):
        """
        Initializes the minesweeper board

        Variables
        ---------
        self.mines
            - The total number of mines to be placed on the board
        self.board
            - minesweeper board

        """
        self.mines = mines

        self.board = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(Tile())
            self.board.append(row)
    
        self.generate_mines()

    def generate_mines(self):
        """
        Randomly places mines (tile_type = -1) on the board
        and ensures that the number of mines equals self.mines
        """
        mines_place = 0
        size = len(self.board)
        while mines_place < self.mines:
            row = random.randint(0, size - 1)
            column = random.randint(0, size - 1)
            # Check if there is not already a mine at the randomly selected position
            if self.board[row][column].tile_type != -1:
                self.board[row][column].tile_type = -1
                mines_place += 1

    def generate_numbers(self):
        """
        Traverses through board to find mines and sends to helper function to increment adjacent spaces

        """
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                if self.board[row][column].tile_type == -1:
                    self.__generate_numbers_helper(row, column)

    def __generate_numbers_helper(self, row, column):
        """
        Helper function for generate numbers and increments adjacent space based in an input bomb coordinate

        Parameters
        ----------
        board
            - The current board being incremented
        row
            - the row coordinate of the current bomb
        column
            - the column coordinate of current bomb
        
        """
        # Increments spaces above the mine
        if row - 1 >= 0:
            if self.board[row - 1][column].tile_type >= 0:
                self.board[row - 1][column].tile_type += 1
            if column - 1 >= 0:
                if self.board[row - 1][column - 1].tile_type >= 0:
                    self.board[row - 1][column - 1].tile_type += 1
            if column + 1 < len(self.board[row]):
                if self.board[row - 1][column + 1].tile_type >= 0:
                    self.board[row - 1][column + 1].tile_type += 1

        # Increments spaces below the mine
        if row + 1 < len(self.board):
            if self.board[row + 1][column].tile_type >= 0:
                self.board[row + 1][column].tile_type += 1
            if column - 1 >= 0:
                if self.board[row + 1][column - 1].tile_type >= 0:
                    self.board[row + 1][column - 1].tile_type += 1
            if column + 1 < len(self.board[row]):
                if self.board[row + 1][column + 1].tile_type >= 0:
                    self.board[row + 1][column + 1].tile_type += 1

        # Increments the space to the left of the mine
        if column - 1 >= 0:
            if self.board[row][column - 1].tile_type >= 0:
                self.board[row][column - 1].tile_type += 1

        # Increments the space to the right of the mine
        if column + 1 < len(self.board[row]):
            if self.board[row][column + 1].tile_type >= 0:
                self.board[row][column + 1].tile_type += 1

    def is_complete(self):
        """
        Traverses through the board to determine if the board is complete

        Returns
        -------
        True
            - if all numbers on the board are revealed
        False
            - if a number is still yet to be revealed
        """
        for row in self.board:
            for column in self.board[row]:
                if self.board[row][column].type > 0 and self.board[row][column].status == 0:
                    return False
        return True

    def __str__(self):
        printmodel = []
        for row in range(len(self.board)):
            row_placeholder = []
            for column in range(len(self.board[row])):
                row_placeholder.append(int(str(self.board[row][column])))
            printmodel.append(row_placeholder)
        return str(printmodel)
            