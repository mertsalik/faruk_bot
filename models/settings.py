# -*- coding: utf-8 -*-

from utils.patterns import SingletonDecorator

__author__ = "mertsalik"
__copyright__ = "Copyright 2018"
__credits__ = ["mertsalik", ""]
__license__ = "Private"
__email__ = ""


@SingletonDecorator
class Settings(object):
    timebank = 0
    time_per_move = 0
    player_names = []
    your_bot = None
    your_bot_id = None
    field_width = 0
    field_height = 0
    max_rounds = 0

    def update(self, key, value):
        if key == "timebank":
            self.timebank = value
        elif key == "time_per_move":
            self.time_per_move = value
        elif key == "player_names":
            self.player_names = value.split(',')
        elif key == "your_bot":
            self.your_bot = value
        elif key == "your_bot_id":
            self.your_bot_id = value
        elif key == "field_width":
            self.field_width = value
        elif key == "field_height":
            self.field_height = value
        elif key == "max_rounds":
            self.max_rounds = value
        else:
            pass
