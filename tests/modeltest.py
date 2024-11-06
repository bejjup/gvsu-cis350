import unittest
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
