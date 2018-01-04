# -*- coding: utf-8 -*-

from utils.patterns import SingletonDecorator

__author__ = "mertsalik"
__copyright__ = "Copyright 2018"
__credits__ = ["mertsalik", ""]
__license__ = "Private"
__email__ = ""


class EnvironmentObject(object):
    pass


class Field(EnvironmentObject):
    matrix = [[]]


class Game(EnvironmentObject):
    round = 0
    field = None


class Player(EnvironmentObject):
    bombs = 0
    snippets = 0


@SingletonDecorator
class Environment(object):
    game = Game()
    player0 = Player()
    player1 = Player()

    def _update_game(self, key, value):
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
