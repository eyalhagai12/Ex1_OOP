#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Building import Building
from Elevator import Elevator
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
        self._division = Algo.setElevatorsDivision(self)
    
    def callList(l:list):
        calls = []
        for i in range(len(l)):
            calls.append(Call(l[i]))
        return calls
    
    # old version of function, not in use
    def setElevatorsDivision2(self):
        maxSrc = max([x.getSrc() for x in self._calls])
        maxDst = max([x.getDest() for x in self._calls])
        minSrc = min([x.getSrc() for x in self._calls])
        minDst = min([x.getDest() for x in self._calls])
        
        maxFloor = max(maxSrc,maxDst)
        minFloor = min(minSrc,minDst)
        
        division = int(maxFloor-minFloor)/len(self._elevators)
        
        return division
    
    def setElevatorsDivision(self):
        maxLen = max([abs(x.getSrc()-x.getDest()) for x in self._calls])
        division = maxLen/len(self._elevators)
        return division
    
    def allocateAnElevator(self):
        sorted_elevs = self._elevators
        sorted_elevs.sort(key=lambda e : e.getPenalty())
        for call in self._calls:
            dist = abs(call.getDest()-call.getSrc())
            ind = int(dist/self._division)
            if(ind>=len(self._elevators)):
                call.setAssigned(sorted_elevs[ind-1]._id)
                sorted_elevs[ind-1]._calls.append(call)
            else:
                call.setAssigned(sorted_elevs[ind]._id)
                sorted_elevs[ind]._calls.append(call)
    
    #old version of function, not in use
    def allocateAnElevator2(self):
        sorted_elevs = self._elevators
        sorted_elevs.sort(key=lambda e : e._speed)
        for call in self._calls:
            dist = abs(call.getDest()-call.getSrc())
            ind = int(dist/self._division)
            call.setAssigned(sorted_elevs[ind]._id)
            sorted_elevs[ind]._calls.append(call)
    
    
    
    def __repr__(self):
        return f"Building: {self._building}, Calls: {self._calls}"
    
