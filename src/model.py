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

    def generate_numbers(self):
        """
        Traverses through board to find mines and sends to helper function to increment adjacent spaces

        """
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                if self.board[row][column].tile_type == -1:
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
        print("going to helper")
        # Increments spaces above the mine
        if row - 1 >= 0:
            if board[row - 1][column].tile_type >= 0:
                board[row - 1][column].tile_type += 1
                if column - 1 >= 0:
                    if board[row - 1][column - 1].tile_type >= 0:
                        board[row - 1][column - 1].tile_type += 1
                if column + 1 < len(board[row]):
                    if board[row - 1][column + 1].tile_type >= 0:
                        board[row - 1][column + 1].tile_type += 1

        # Increments spaces below the mine
        if row + 1 < len(board):
            if board[row + 1][column].tile_type >= 0:
                self.board[row + 1][column].tile_type += 1
                if column - 1 >= 0:
                    if board[row + 1][column - 1].tile_type >= 0:
                        board[row + 1][column - 1].tile_type += 1
                if column + 1 < len(board[row]):
                    if board[row + 1][column + 1].tile_type >= 0:
                        board[row + 1][column + 1].tile_type += 1

        # Increments the space to the left of the mine
        if column - 1 >= 0:
            if board[row][column - 1].tile_type >= 0:
                board[row][column - 1].tile_type += 1

        # Increments the space to the right of the mine
        if column + 1 < len(board[row]):
            if board[row][column + 1].tile_type >= 0:
                board[row][column + 1].tile_type += 1

    def __str__(self):
        printmodel = []
        for row in range(len(self.board)):
            row_placeholder = []
            for column in range(len(self.board[row])):
                row_placeholder.append(int(str(self.board[row][column])))
            printmodel.append(row_placeholder)
        return str(printmodel)
            