# -*- coding: utf-8 -*-

__author__ = "mertsalik"
__copyright__ = "Copyright 2018"
__credits__ = ["mertsalik", ""]
__license__ = "Private"
__email__ = ""


class IOParser(object):
    """
    Import settings from engine to bot
    """

    @staticmethod
    def parse(input_string):
        _, key, value = input_string.split()
        return {key: value}

    def command_loop(self):
        pass
