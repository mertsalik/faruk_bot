# -*- coding: utf-8 -*-
import os, sys
import unittest
from parsers.fieldparser import FieldParser

__author__ = "mertsalik"
__copyright__ = "Copyright 2018"
__credits__ = ["mertsalik", ""]
__license__ = "Private"
__email__ = ""


class TestFieldParser(unittest.TestCase):
    def setUp(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(dir_path,
                               "field_input_sample1.txt")) as field_input_file:
            self.engine_start_input = field_input_file.read()

        self.sample_input_1 = "S,.,.,.,.,.,.,.,.,.,.,.,.,.,S"
        self.expected_sample_matrix = [
            ['S', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', 'S']
        ]
        self.field_sample1_width = 19
        self.field_sample1_height = 15

    def tearDown(self):
        pass

    def test_fieldparser(self):
        fp = FieldParser(input_string=self.sample_input_1, width=5)
        self.assertEqual(fp.get_matrix(), self.expected_sample_matrix)

    def test_fieldparser_spawn_points(self):
        fp = FieldParser(input_string=self.engine_start_input,
                         width=self.field_sample1_width)
        field_matrix = fp.get_matrix()
        self.assertEqual('S', field_matrix[0][0])
        self.assertEqual('S', field_matrix[0][self.field_sample1_width - 1])
        self.assertEqual('S', field_matrix[self.field_sample1_height - 1][0])
        self.assertEqual('S', field_matrix[self.field_sample1_height - 1][
            self.field_sample1_width - 1])
