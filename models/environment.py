# -*- coding: utf-8 -*-

from utils.patterns import SingletonDecorator
from parsers.fieldparser import FieldParser

__author__ = "mertsalik"
__copyright__ = "Copyright 2018"
__credits__ = ["mertsalik", ""]
__license__ = "Private"
__email__ = ""


class EnvironmentObject(object):
    pass


class Cell(EnvironmentObject):
    x = 0
    y = 0
    __bug_count = 0
    __snippet_count = 0
    __is_wall = False
    __is_gate = False

    def __init__(self, x, y, is_wall=False, is_gate=False, bugs=[],
                 snippets=[]):
        self.__is_wall = is_wall
        self.__bug_count = len(bugs)
        self.__snippet_count = len(snippets)
        self.__is_gate = is_gate


class Field(EnvironmentObject):
    matrix = [[]]

    def from_string(self, field_string):
        self.matrix = FieldParser(input_string=field_string).get_matrix()
        return self.matrix


class Game(EnvironmentObject):
    round = 0
    field = Field()


class Player(EnvironmentObject):
    bombs = 0
    snippets = 0


@SingletonDecorator
class Environment(object):
    game = Game()
    player0 = Player()
    player1 = Player()

    def _update_game(self, key, value):
        if key == "round":
            self.game.round = int(value)
        elif key == "field":
            self.field.from_string(value)
        else:
            pass

    def _update_player(self, key, value):
        env_key, env_value = value
        if key.endswith("0"):
            self.player0.__setattr__(env_key, env_value)
        elif key.endswith("1"):
            self.player1.__setattr__(env_key, env_value)

    def update(self, key, value):
        if key == "game":
            self._update_game(key, value)
        elif key.startswith == "player":
            self._update_player(key, value)
        else:
            pass
