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
    def __init__(self, building:Building, path:str):
        self._building = building;
        self._elevators = building._elevators
        self._calls = Algo.callList(FileReader.read_file(path))
        self._elevTime = []
        for i in range(len(self._elevators)):
            self._elevTime.append(0)
        
    
    def callList(l:list):
        calls = []
        for i in range(len(l)):
            calls.append(Call(l[i]))
        return calls
    
    
    def allocateAnElevator(self, call:Call):
        pass
    
    def cmdElevator():
        pass
    
    def __repr__(self):
        return f"Building: {self._building}, Calls: {self._calls}"
    