import unittest
from random import random
from model import Tile, Model

class modeltest(unittest.TestCase):

    # ensures correct initialization for the default tile state
    def tile_test(self):
        tile = Tile()
        self.assertEqual(tile.tile_type, 0)
        self.assertEqual(tile.status, 0)

    # ensures that the assigning a custom tile value is being passed correctly
    def tile_custom(self):
        tile = Tile(1)
        self.assertEqual(tile.tile_type, 1)
        self.assertEqual(tile.status, 0)
    
    # ensures that the tile is being represented correctly in string format
    def test_str(self):
        tile = Tile(1)
        self.assertIsInstance(tile.tile_type, int)
        self.assertEqual(str(tile), '1')

        tile.tile_type = 2
        self.assertIsInstance(tile.tile_type, int)
        self.assertEqual(str(tile), '2')

    # testing for correct board/mine placement depending on number of mines
    def test_board(self, size=10, mines=5):
        board = Model(size, mines)
        self.assertIsInstance(size, int)
        self.assertIsInstance(mines, int)
        self.assertEqual(size, 10)
        self.assertEqual(mines, 5)

        self.assertEqual(len(board.board), size)
        for row in board.board:
            self.assertEqual(len(row), size)
            for square in board.board:
                self.assertIsInstance(square, size)
    
    # ensures that a -1 will be placed where there is a mine
    def test_gen_mines(self):
        board = Model(size=5, mines=3)
        mine_placements = [(1, 1) (2, 2) (3, 3)]
        for row, col in mine_placements:
            self.assertEqual(board.board[row][col].tile_type, -1)
    
    # ensures that the numbers will be placed correctly based upon the number of mines around an area
    def test_gen_nums(self):
        board = Model(size=5, mines=4)
        board.board[1][1].tile_type = -1
        board.board[1][2].tile_type = -1
        board.board[1][3].tile_type = -1
        board.board[2][1].tile_type = -1

        board.generate_numbers()

        nums = {
            (4, 4): 0, (0, 0): 1, (0, 1): 2, (0, 2): 3, (2, 2): 4
        }

        for (row, col), num in nums.items():
            correct_count = board.board[row][col].tile_type
            self.assertEqual(correct_count, num)

    
if __name__ == '__main__':
    unittest.main()

