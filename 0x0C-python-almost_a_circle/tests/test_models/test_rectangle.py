#!/usr/bin/python3
'''Module for Rectangle unit tests.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from random import randrange
from contextlib import redirect_stdout
import io

class TestRectangle(unittest.TestCase):

    def test_rectangle_id_increment(self):
        rect1 = Rectangle(1, 2)
        rect2 = Rectangle(2, 3)
        self.assertEqual(rect1.id, 1)
        self.assertEqual(rect2.id, 2)

    def test_rectangle_width_height(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)

    def test_rectangle_x_y(self):
        rect = Rectangle(5, 10, 2, 3)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_rectangle_area(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_rectangle_str_representation(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(str(rect), '[Rectangle] (1) 2/3 - 5/10')

    def test_rectangle_update_no_keyword_args(self):
        rect = Rectangle(5, 10)
        rect.update(10, 2, 3, 4, 5)
        self.assertEqual(rect.id, 10)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 5)

    def test_rectangle_update_with_keyword_args(self):
        rect = Rectangle(5, 10)
        rect.update(id=10, width=2, height=3, x=4, y=5)
        self.assertEqual(rect.id, 10)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 5)

    def test_rectangle_to_dictionary(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        rect_dict = rect.to_dictionary()
        expected_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        self.assertEqual(rect_dict, expected_dict)

    def test_rectangle_display(self):
        # This test only checks if the display method runs without errors
        rect = Rectangle(3, 2)
        rect.display()

if __name__ == '__main__':
    unittest.main()