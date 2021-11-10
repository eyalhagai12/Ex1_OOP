import json
import csv

"""
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
            file = read_csv(f)
        else:
            raise FileNotFoundError("The file format is not supported")

        return file


def read_csv(file):
    """
    A custom csv file reader that turns the calls to a list of dictionaries
    :param file: The file of the
    :return: A list of dictionaries that represent the calls
    """

    calls = file.read().split("\n")

    return calls



