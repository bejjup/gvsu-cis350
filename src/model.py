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
                row.append(0)
            self.board.append(row)

    def generate_numbers(self):
        """
        Traverses through board to find mines and sends to helper function to increment adjacent spaces

        """
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                if self.board[row][column] == "x":
                    self.__generate_numbers_helper(self.board, row, column)

    def __generate_numbers_helper(self, board, row, column):
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
            if isinstance(board[row - 1][column], int) is True:
                board[row - 1][column] += 1
                if column - 1 >= 0:
                    if isinstance(board[row - 1][column - 1], int) is True:
                        board[row - 1][column - 1] += 1
                if column + 1 < len(board[row]):
                    if isinstance(board[row - 1][column + 1], int) is True:
                        board[row - 1][column + 1] += 1

        # Increments spaces below the mine
        if row + 1 < len(board):
            if isinstance(board[row + 1][column], int) is True:
                self.board[row + 1][column] += 1
                if column - 1 >= 0:
                    if isinstance(board[row + 1][column - 1], int) is True:
                        board[row + 1][column - 1] += 1
                if column + 1 < len(board[row]):
                    if isinstance(board[row + 1][column + 1], int) is True:
                        board[row + 1][column + 1] += 1

        # Increments the space to the left of the mine
        if column - 1 >= 0:
            if isinstance(board[row][column - 1], int) is True:
                board[row][column - 1] += 1

        # Increments the space to the right of the mine
        if column + 1 < len(board[row]):
            if isinstance(board[row][column + 1], int) is True:
                board[row][column + 1] += 1
