# -*- coding: utf-8 -*-

__author__ = "mertsalik"
__copyright__ = "Copyright 2018"
__credits__ = ["mertsalik", ""]
__license__ = "Private"
__email__ = ""


def save_setting(key, value):
    pass


def do_action(action_type):
    pass


def update_environment(obj_name, *args):
    pass


def process_next_command():
    input_string = input()
    command_type, command_key, *command_values = input_string.split()

    if command_type == "settings":
        save_setting(key=command_key, value=command_values.fi)

    elif command_type == "action":
        do_action(command_key)

    elif command_type == "update":
        update_environment(command_key, command_values)
    else:
        pass


if __name__ == "__main__":

    while True:
        process_next_command()
    pass
