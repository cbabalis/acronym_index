#!/usr/bin/env python
# -*- encoding: utf-8 -*-

""" This module loads a json file with abbreviation-definition pairs.
It waits a user input, it searches for the abbreviation and if it
exists, it then returns the definition.

:author: Babis Babalis
"""


import json
import sys


def help_me():
    """ Method to print a short help message.."""
    with open('README.md', 'r') as help_file:
        contents = help_file.read()
        print(contents)


def add_abb(abb, abb_def, acro_index, abbs_file='abbs.json'):
    """ Method to add an abbreviation to abbreviations file.

    Args:
        abb (string): The acronym to be added.
        abb_def (string): Definition of the acronym to be added.
        acro_index (dict): Dictionary of already existed acronyms.
        abbs_file (string): The file where the acronyms are being saved.
    """
    abb = abb.lower()
    if abb not in acro_index:
        acro_index[abb] = abb_def
        with open(abbs_file, 'w') as json_file:
            json.dump(acro_index, json_file)
        print("New abbreviation has been added!")
        # load the json file
        acro_index = load_file()
    else:
        print("Abbreviation already exists!")


def load_file(abbs_file='abbs.json'):
    """ Loads a json file containing acronyms to a dictionary."""
    data = {}
    with open(abbs_file, 'r') as json_file:
        data = json.load(json_file)
        # make all keys lowercase, too
        data = {k.lower(): v for k, v in data.items()}
        return data


def find_abb(usr_abb, acro_index):
    """ Method to search for user's abbreviation.

    Args:
        usr_abb (string): User's input arg.
        acro_index (dict): Dictionary of existing acronyms.

    Returns:
        int: 0 if the acronym has been found, -1 else.
    """
    # make user's input case insensitive
    usr_abb = usr_abb.lower()
    # search inside the dictionary for the key (case insensitive)
    # if abbreviation found, then print it
    if usr_abb in acro_index:
        print(acro_index[usr_abb])
        return 0
    for k in acro_index:
        # else search for something near to it (reverse order)
        if k in usr_abb:
            print("Did you mean %s ?" % (k))
            print(acro_index[k])
            return 0
    print("Nothing found!")
    return -1


def process_user_input(usr_input, acro_index):
    """ Method to process user input.

    Args:
        usr_input (str): User's input.
        acro_index (dict): Dictionary of existing acronyms.
    """
    # load the json file
    acro_index = load_file()
    # analyze user's input.
    input_args = usr_input.split(" ")
    if input_args[0] == 'help' or input_args[0] == '-h':
        help_me()
    elif input_args[0] == 'add' or input_args[0] == '-a':
        definition = " ".join(input_args[1:])
        add_abb(input_args[1], definition, acro_index)
    elif input_args[0] == 'quit' or input_args[0] == '-q':
        sys.exit(0)
    else:
        find_abb(input_args[-1], acro_index)


def main():
    """ main function """
    # read user's input
    acro_index = load_file()
    print("%d acronyms are available" % len(acro_index))
    while True:
        # search for the abb
        # return appropriate
        user_input = str(input())
        process_user_input(user_input, acro_index)


if __name__ == '__main__':
    main()
