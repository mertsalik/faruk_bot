# -*- coding: utf-8 -*-

__author__ = "mertsalik"
__copyright__ = "Copyright 2018"
__credits__ = ["mertsalik", ""]
__license__ = "Private"
__email__ = ""


class FieldParser(object):
    matrix = []

    def __init__(self, input_string, width, height):
        cells = input_string.split(',')
        self.matrix = [cells[x:x + width] for x in
                       range(0, len(cells), width)]

    def get_matrix(self):
        return self.matrix
