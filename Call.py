"""
Created on Fri Nov 12 17:36:28 2021

@author: fedora
"""


class Call:
    def __init__(self, x: str):
        self._time = float(x.split(",")[1])
        self._src = int(x.split(",")[2])
        self._dst = int(x.split(",")[3])
        self._state = int(x.split(",")[4])
        self._assigned = int(x.split(",")[5])
        self._next_pos = self._src
        self._direction = 1 if self._dst > self._src else -1

    def __gt__(self, other):
        """
        Overload the ">" operator
        :param other: The other call to compare with
        :return: True if this call's next_pos bigger then the other call's
        """

        return other.get_next_pos() < self._next_pos

    def __ge__(self, other):
        """
        Overload the ">=" operator
        :param other: The other call to compare with
        :return: True if this call's next_pos bigger then the other call's
        """

        return other.get_next_pos() <= self._next_pos

    def __eq__(self, other):
        """
        Overload the "==" operator
        :param other: The other call to compare with
        :return: True if this call's next_pos bigger then the other call's
        """

        return other.get_next_pos() == self._next_pos

    def get_time(self):
        """
        Get the time when the call was made
        :return: a float representing the time when the call was made
        """
        return self._time

    def get_src(self):
        """
        Get the source of the call
        :return: An int representing the source of the call
        """
        return self._src

    def get_dst(self):
        """
        Get the destination of the call
        :return: An int representing the destination of the call
        """

    def get_next_pos(self):
        """
        Get the next floor to which the elevator needs to go according to its state
        if state is 0 or 1, this function will return the source of the call
        if state is 2, this function will return the destination of the call
        :return: The next floor to go to for this call to be done
        """

        if self._state == 0 or self._state == 1:
            return self._src
        else:
            return self._dst

    def get_direction(self):
        """
        Get the direction of the call
        :return: An int representing the direction of the call (1 for up, -1 for down)
        """

        return self._direction

    #
    # def call_time(self, e: Elevator):
    #     way = abs(self._dest - self._src)
    #     time = e._openTime + e._closeTime + e._startTime + (way / e._speed)
    #     + e._stopTime + e._openTime + e._stopTime
    #     return time
    #
    # def time_to_src(self, e: Elevator):
    #     return abs(e._currentPos - self._src) / e._speed

    def __repr__(self):
        return f"Time:{self._time}, Source:{self._src}, Destination:{self._dst}\n"