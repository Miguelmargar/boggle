#file needs to start with test_     - this is to do tdd
import unittest    #unittest comes with python
from boggle import * # * makes sure that all functions are taking into consideration
from string import ascii_uppercase # this is a string with the alphabet in uppercase - ascii_lowercase exists

class TestBoggle(unittest.TestCase):     # this class is to get the unittest functionality with TestCase - this line has to be put in to use unittest
    def test_is_this_thing_on(self):     # the def needs to beging with test_
        self.assertEqual(check(), True)  # this is a python function
        
    def test_empty_grid(self):
        grid = make_grid(2, 2)
        self.assertEqual(len(grid), 4)
        
    def test_grid_has_upper_case_letters(self):
        grid = make_grid(2, 2)
        for c in grid.values(): # here c is the key in the dictionary
            self.assertIn(c, ascii_uppercase)
        
    def test_neighbours_of_cell(self):
        neighbours = get_neighbours((3, 4))
        expected = [
            (2,3),
            (3,3),
            (4,3),
            (4,4),
            (4,5),
            (3,5),
            (2,5),
            (2,4)
            ]
        self.assertEqual(neighbours, expected)
        
    # def test_all_grid_neighbours(self):
    #     actual = all_grid_neighbours(make_grid(2, 2))
    #     expected = {
    #         (0, 0): [(1, 0), (0, 1), (1, 1)],
    #         (1, 0): [(0, 0), (0, 1), (1, 1)],
    #         (0, 1): [(0, 0), (1, 0), (1, 1)],
    #         (1, 1): [(0, 0), (1, 0), (0, 1)]
    #     }
    #     self.assertDictEqual(actual, expected)
    
    def test_path_to_word(self):
        grid = {
            (0, 0): "C", (1, 0): "O",
            (0, 1): "D", (1, 1): "E",
        }
        path = [(0,0), (1,0), (0,1)]
        self.assertEqual(path_to_word(grid, path), "COD")