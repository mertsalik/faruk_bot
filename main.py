# -*- coding: utf-8 -*-

from models.environment import Environment
from models.settings import Settings
from models.moves import Moves

__author__ = "mertsalik"
__copyright__ = "Copyright 2018"
__credits__ = ["mertsalik", ""]
__license__ = "Private"
__email__ = ""


def process_next_move():
    print(Moves.noop)


def save_setting(key, value):
    Settings().update(key=key, value=value)


def do_action(action_type):
    if action_type == "character":
        print("bixie")
    elif action_type == "move":
        process_next_move()


def update_environment(obj_name, *args):
    Environment().update(obj_name, *args)


def process_next_command():
    input_string = input()
    try:
        command_type, command_key, *command_values = input_string.split()
    except ValueError:
        return

    if command_type == "settings":
        save_setting(key=command_key, value=command_values.pop())

    elif command_type == "action":
        do_action(command_key)

    elif command_type == "update":
        update_environment(command_key, command_values)
    else:
        pass


if __name__ == "__main__":

    while True:
        process_next_command()
