import json
import csv

"""
Description:
-----------

This file has functions to read files and parse them to different data structures

"""


def read_file(path):
    """
    Read file given its path and parse depending on its type

    :param path: The path to the file
    :returns: The parsed file
    """

    with open(path) as f:
        if ".json" in path:
            file = json.load(f)

        elif ".csv" in path:
            file = f.read().split("\n")
        else:
            raise FileNotFoundError("The file format is not supported")

        return file

