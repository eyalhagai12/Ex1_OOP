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

    def timeSrcDest(self, e: Elevator):
        way = abs(self._dest - self._src)
        time = e._openTime + e._closeTime + e._startTime + (way / e._speed)
        + e._stopTime + e._openTime + e._stopTime
        return time

    def timeGetToCall(self, e: Elevator):
        return abs(e._currentPos - self._src) / e._speed

    def __repr__(self):
        return f"Time:{self._time}, Source:{self._src}, Destination:{self._dest}\n"
