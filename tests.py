# Project 4
# Name: Eeshan Mishra
# Instructor: S. Einakian
# Section: 05


import unittest
from func_calcudoku import *

first_grid = [[3, 3, 2, 1, 4], [5, 1, 3, 4, 2], [2, 4, 1, 5, 3], [1, 2, 4, 3, 5], [4, 3, 5, 2, 1]]
second_grid = [[1, 2, 3, 4, 5], [3, 1, 4, 5, 2], [2, 5, 1, 3, 4], [5, 4, 2, 1, 3], [4, 3, 5, 2, 1]]
third_grid = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

first_row = [[3, 3, 2, 1, 4], [5, 1, 3, 4, 2], [2, 4, 1, 5, 3], [1, 2, 4, 3, 5], [4, 3, 5, 2, 1], [3, 5, 2, 1, 4], [3, 1, 4, 2, 3], [2, 3, 1, 4, 5], [1, 4, 5, 3, 2], [4, 2, 3, 5, 1]]
second_row = [[], [], [], [], [], [], [], [], [], []]
third_row = [[], [], [], [], [], [], [], [], [], []]




class TestCalcudoku(unittest.TestCase):
    def test_validate_rows(self):
        self.assertEqual(validate_rows("Eeshan"), "Rrfuna")
        self.assertEqual(validate_rows("Daring"), "Qnevat")
        self.assertEqual(validate_rows("computer"), "pbzchgre")

    def test_validate_cols(self):
        self.assertEqual(validate_cols("eeshan"), "xxshan")
        self.assertEqual(validate_cols("tuple"), "tuple")
        self.assertEqual(validate_cols("polynomial"), "pylynymial")

    def test_validate_cages(self):
        self.assertEqual(validate_cages("eeshan"), "xxshan")
        self.assertEqual(validate_cages("tuple"), "tuple")
        self.assertEqual(validate_cages("polynomial"), "pylynymial")

    def test_validate_all(self):
        self.assertEqual(validate_all("eeshan"), "xxshan")
        self.assertEqual(validate_all("tuple"), "tuple")
        self.assertEqual(validate_all("polynomial"), "pylynymial")


if __name__ == '__main__':
    unittest.main()
