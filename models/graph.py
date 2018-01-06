# -*- coding: utf-8 -*-
from collections import defaultdict

__author__ = "mertsalik"
__copyright__ = "Copyright 2018"
__credits__ = ["mertsalik", ""]
__license__ = "Private"
__email__ = ""


class CellTypes(object):
    pass


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, source, destination, distance=1):
        self.edges[source].append(destination)
        self.edges[destination].append(source)
        self.distances[(source, destination)] = distance

    @staticmethod
    def from_matrix(matrix, r, c):
        """
        :param matrix: 2x2 dim array of cells
        :param r: row count
        :param c: col count
        :return: Graph
        """
        g = Graph()
        for j in range(c - 1):
            for i in range(r - 1):
                if matrix[j][i] == "x":
                    continue
                g.add_node("%s-%s" % (j, i))
                if matrix[j][i + 1] != "x":
                    g.add_edge(source="%s-%s" % (j, i),
                               destination="%s-%s" % (j, i + 1))
                if matrix[j + 1][i] != "x":
                    g.add_edge(source="%s-%s" % (j, i),
                               destination="%s-%s" % (j + 1, i))
        # bind right-most nodes
        for j in range(c - 1):
            if matrix[j][r - 1] == "x": continue
            g.add_node("%s-%s" % (j, r - 1))
            if matrix[j + 1][r - 1] != "x":
                g.add_edge("%s-%s" % (j, r - 1), "%s-%s" % (j + 1, r - 1))
        # bind bottom-side nodes
        for i in range(r - 1):
            if matrix[c - 1][i] == "x": continue
            g.add_node("%s-%s" % (c - 1, i))
            if matrix[c - 1][i + 1] != "x":
                g.add_edge("%s-%s" % (c - 1, i), "%s-%s" % (c - 1, i + 1))

        if matrix[c - 1][r - 1] != "x":
            g.add_node("%s-%s" % (c - 1, r - 1))
        return g
