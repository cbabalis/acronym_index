#!/usr/bin/env python3


import json
import pdb


def process_key(components):
    key = "\"" + components[0] + "\""
    components[0] = key


def process_value(components):
    if len(components) < 2:
        pdb.set_trace()
    val = "\"" + components[1] + "\""
    components[1] = val


def join_line(components, json_contents):
    json_contents[components[0]] = components[1]


def main():
    a_file = 'tele_defs.txt'
    json_file = 'json_file.json'
    json_contents = {}
    with open(a_file, 'r') as f:
        lines = f.read().splitlines()
        for l in lines:
            # split ONLY the first element to the others!
            l = l.replace("\t", " ")
            components = l.split(" ", 1)
            #process_key(components)
            #process_value(components)
            join_line(components, json_contents)
    print("json_contents are ")
    print(json_contents)
    with open(json_file, 'w') as f:
        json.dump(json_contents, f)


if __name__ == '__main__':
    main()
