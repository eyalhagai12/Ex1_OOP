from Elevator import Elevator

"""
Created on Fri Nov 12 17:36:28 2021

@author: fedora
"""


class Call:
    def __init__(self, x: str):
        self._time = float(x.split(",")[1])
        self._src = int(x.split(",")[2])
        self._dest = int(x.split(",")[3])
        self._state = int(x.split(",")[4])
        self._assigned = int(x.split(",")[5])

    def getTime(self):
        return self._time
    
    def getSrc(self):
        return self._src
    
    def getDest(self):
        return self._dest
    
    def getState(self):
        return self._state

    def getAssigned(self):
        return self._assigned
    
    def setAssigned(self, x:int):
        self._assigned=x
        

    def __repr__(self):
        return f"Time:{self._time}, Source:{self._src}, Destination:{self._dest}, Assigned:{self._assigned}\n"
