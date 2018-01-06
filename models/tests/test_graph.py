# -*- coding: utf-8 -*-

import unittest
from models.graph import Graph

__author__ = "mertsalik"
__copyright__ = "Copyright 2018"
__credits__ = ["mertsalik", ""]
__license__ = "Private"
__email__ = ""


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.sample_matrix_1 = [
            ['x', '.', 'x'],
            ['.', '.', '.'],
            ['x', '.', 'x']
        ]
        self.sample_graph_1_edges = {
            '0-1': ['1-1'],
            '1-0': ['1-1'],
            '1-1': ['0-1', '1-0', '1-2', '2-1'],
            '1-2': ['1-1'],
            '2-1': ['1-1']
        }
        self.sample_graph_1_nodes = {
            '0-1', '1-0', '1-1', '1-2', '2-1'
        }

        self.sample_matrix_2 = [
            ['.', 'x', '.', 'x'],
            ['.', 'x', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', 'x', '.']
        ]
        self.sample_graph_2_nodes = {
            '0-0', '0-2',
            '1-0', '1-2', '1-3',
            '2-0', '2-1', '2-2', '2-3',
            '3-0', '3-1', '3-3'
        }
        self.sample_graph_2_edges = {
            '0-0': ['1-0'],
            '0-2': ['1-2'],
            '1-0': ['0-0', '2-0'],
            '1-2': ['0-2', '1-3', '2-2'],
            '1-3': ['1-2', '2-3'],
            '2-0': ['1-0', '2-1', '3-0'],
            '2-1': ['2-0', '2-2', '3-1'],
            '2-2': ['1-2', '2-1', '2-3'],
            '2-3': ['1-3', '2-2', '3-3'],
            '3-0': ['2-0', '3-1'],
            '3-1': ['2-1', '3-0'],
            '3-3': ['2-3']
        }

    def tearDown(self):
        pass

    def test_from_matrix(self):
        graph1 = Graph.from_matrix(self.sample_matrix_1, 3, 3)
        self.assertIsNotNone(graph1)
        self.assertTrue(graph1.nodes.issubset(self.sample_graph_1_nodes))
        self.assertTrue(self.sample_graph_1_nodes.issubset(graph1.nodes))

        for node in graph1.nodes:
            self.assertListEqual(sorted(graph1.edges[node]),
                                 sorted(self.sample_graph_1_edges[node]))

        graph2 = Graph.from_matrix(self.sample_matrix_2, 4, 4)
        self.assertIsNotNone(graph2)
        self.assertTrue(graph2.nodes.issubset(self.sample_graph_2_nodes))
        self.assertTrue(self.sample_graph_2_nodes.issubset(graph2.nodes))

        for node in graph2.nodes:
            self.assertListEqual(sorted(graph2.edges[node]),
                                 sorted(self.sample_graph_2_edges[node]))
