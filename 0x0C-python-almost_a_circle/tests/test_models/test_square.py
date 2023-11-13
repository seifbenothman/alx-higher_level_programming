#!/usr/bin/python3
'''Module for Square unit tests.'''
import unittest
from models.base import Base
from models.square import Square
from random import randrange
from contextlib import redirect_stdout
import io

class TestSquare(unittest.TestCase):

    def test_square_id_increment(self):
        square1 = Square(2)
        square2 = Square(3)
        self.assertEqual(square1.id, 1)
        self.assertEqual(square2.id, 2)

    def test_square_size(self):
        square = Square(5)
        self.assertEqual(square.size, 5)

    def test_square_x_y(self):
        square = Square(5, 2, 3)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_square_area(self):
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_square_str_representation(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), '[Square] (1) 2/3 - 5')

    def test_square_update_no_keyword_args(self):
        square = Square(5)
        square.update(10, 2, 3, 4)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_square_update_with_keyword_args(self):
        square = Square(5)
        square.update(id=10, size=2, x=3, y=4)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_square_to_dictionary(self):
        square = Square(5, 2, 3, 1)
        square_dict = square.to_dictionary()
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square_dict, expected_dict)

    def test_square_display(self):
        # This test only checks if the display method runs without errors
        square = Square(3)
        square.display()

if __name__ == '__main__':
    unittest.main()