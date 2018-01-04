# -*- coding: utf-8 -*-
from collections import defaultdict

__author__ = "mertsalik"
__copyright__ = "Copyright 2018"
__credits__ = ["mertsalik", ""]
__license__ = "Private"
__email__ = ""


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, source, destination, distance):
        self.edges[source].append(destination)
        self.edges[destination].append(source)
        self.distances[(source, destination)] = distance

    def from_matrix(self, matrix):
        raise NotImplementedError
