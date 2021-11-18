#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Building import Building
from Call import Call
import FileReader

"""
Created on Thu Nov 11 22:06:35 2021

@author: fedora
"""


class Algo:
    def __init__(self, building: Building, path: str):
        self._building = building
        self._elevators = building.get_elevators()
        self._calls = Algo.callList(FileReader.read_file(path))
        self._division = Algo.set_elevators_division(self)

    def callList(l: list):
        calls = []
        for i in range(len(l)):
            calls.append(Call(l[i]))
        return calls

    def set_elevators_division(self):
        maxLen = max([abs(x.get_src() - x.get_dst()) for x in self._calls])
        division = maxLen / len(self._elevators)
        return division

    def allocateAnElevator(self):
        sorted_elevs = self._elevators
        sorted_elevs.sort(key=lambda e: e.getPenalty())
        for call in self._calls:
            dist = abs(call.get_dst() - call.get_src())
            ind = int(dist / self._division)
            if ind >= len(self._elevators):
                call.set_assigned(sorted_elevs[ind - 1].get_id())
                sorted_elevs[ind - 1]._calls.append(call)
            else:
                call.set_assigned(sorted_elevs[ind].get_id())
                sorted_elevs[ind]._calls.append(call)

    def get_calls(self):
        return self._calls

    def __repr__(self):
        return f"Building: {self._building}, Calls: {self._calls}"
