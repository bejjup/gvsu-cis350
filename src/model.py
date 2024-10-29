class model():
    def __init__(self, size, mines):
        self.mines = mines
        self.board = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(0)
            self.board.append(row)
        self.board = [[0,0,0,"x",0],[0,"x",0,0,0],[0,0,"x",0,0],[0,0,0,0,0],[0,0,0,0,0]]

    def generate_numbers(self):
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                if self.board[row][column] == "x":
                    self.__generate_numbers_helper(self.board, row, column, len(self.board))

    def __generate_numbers_helper(self, board, row, column, size):
        if row - 1 >= 0:
            if isinstance(board[row - 1][column], int) is True:
                board[row - 1][column] += 1
                if column - 1 >= 0:
                    if isinstance(board[row - 1][column - 1], int) is True:
                        board[row - 1][column - 1] += 1
                if column + 1 < size:
                    if isinstance(board[row - 1][column + 1], int) is True:
                        board[row - 1][column + 1] += 1
        if row + 1 < size:
            if isinstance(board[row + 1][column], int) is True:
                self.board[row + 1][column] += 1
                if column - 1 >= 0:
                    if isinstance(board[row + 1][column - 1], int) is True:
                        board[row + 1][column - 1] += 1
                if column + 1 < size:
                    if isinstance(board[row + 1][column + 1], int) is True:
                        board[row + 1][column + 1] += 1
        if column - 1 >= 0:
            if isinstance(board[row][column - 1], int) is True:
                board[row][column - 1] += 1
        if column + 1 < size:
            if isinstance(board[row][column + 1], int) is True:
                board[row][column + 1] += 1
