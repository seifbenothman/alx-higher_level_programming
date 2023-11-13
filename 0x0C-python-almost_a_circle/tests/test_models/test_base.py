#!/usr/bin/python3
'''Module for Base unit tests.'''
import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):

    def test_base_id_increment(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_base_custom_id(self):
        base_custom_id = Base(100)
        self.assertEqual(base_custom_id.id, 100)

    def test_base_to_json_string(self):
        base1 = Base(1)
        base2 = Base(2)
        json_string = Base.to_json_string([base1.to_dictionary(), base2.to_dictionary()])
        expected_json = '[{"id": 1}, {"id": 2}]'
        self.assertEqual(json_string, expected_json)

    def test_base_from_json_string(self):
        json_string = '[{"id": 1}, {"id": 2}]'
        base_list = Base.from_json_string(json_string)
        expected_list = [{"id": 1}, {"id": 2}]
        self.assertEqual(base_list, expected_list)

    def test_base_save_and_load_from_file(self):
        base1 = Base(1)
        base2 = Base(2)
        Base.save_to_file([base1, base2])
        loaded_bases = Base.load_from_file()
        self.assertEqual(len(loaded_bases), 2)
        self.assertEqual(loaded_bases[0].id, 1)
        self.assertEqual(loaded_bases[1].id, 2)

    def test_base_save_and_load_from_file_csv(self):
        base1 = Base(1)
        base2 = Base(2)
        Base.save_to_file_csv([base1, base2])
        loaded_bases = Base.load_from_file_csv()
        self.assertEqual(len(loaded_bases), 2)
        self.assertEqual(loaded_bases[0].id, 1)
        self.assertEqual(loaded_bases[1].id, 2)

    def test_base_create(self):
        base_dict = {'id': 5}
        base_instance = Base.create(**base_dict)
        self.assertEqual(base_instance.id, 5)

    def test_base_draw(self):
        rect = Rectangle(10, 5, 0, 0)
        square = Square(5, 2, 2)
        Base.draw([rect, square], [])
        # This test only checks if the draw method runs without errors

if __name__ == '__main__':
    unittest.main()
