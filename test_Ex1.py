import os
from unittest import TestCase
import sys

from Ex1 import main

combinations = [(1, "a"), (2, "a"), (3, "a"), (3, "b"), (3, "c"), (3, "d"), (4, "a"),
                (4, "b"), (4, "c"), (4, "d"), (5, "a"), (5, "b"), (5, "c"), (5, "d")]


class Test(TestCase):
    def test_main(self):
        flag = True
        try:
            for build, case in combinations:
                building = f"B{build}.json"
                case_str = f"Calls_{case}.csv"
                out = f"Ex1_Calls_case_{build}_{case}.csv"
                os.system(f"python Ex1.py {building} {case_str} {out}")
        except Exception as e:
            flag = False

        self.assertTrue(flag, "Main test")

