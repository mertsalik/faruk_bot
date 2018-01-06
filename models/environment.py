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
    """
    CellType	Description
    .	        A cell (coordinate) with nothing on it.

    x	        An inaccessible cell.

    Pi	ID i (Integer)
                Contains a player, where i is a player's id.

    Si	Number i (Integer)
                Represents a bug spawn point, where i is the amount of
                rounds before a bug spawns. Can just be S is
                no bugs are spawning.

    Gs	String s (String: l, r)
                Represents a gate, where s is the direction the bot needs to
                move when standing on the gate to move through it.

    Ei	Number i (Integer)
                    Contains a bug, where i specifies the bug's AI type.

    Bi	Number i (Integer)
                Contains a laser-mine, where i is the amount of rounds before
                the mine explodes.
                Will just be B if the laser-mine can be picked up.

    C	A cell that contains a code snippet.
    """
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
