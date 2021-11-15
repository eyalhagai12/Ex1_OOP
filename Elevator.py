import math

from Call import Call


def calculate_time(call, prev_call):
    """
    Given 2 calls, calculate the time it takes to execute "call" after finishing a stage in "prev_call"
    (stage can be going to source or going to destination)

    :param call: The call to which we want to find the stage execution time
    :param prev_call: The call before call2 in the list
    :return: A float representing the time
    """

    # first we need to understand the previous call's state and status
    if call.get_direction() == 1 and prev_call.get_direction() == 1:  # if both are going up
        pass


def calculate_route_time(calls, elevator):
    """
    Calculate the time it takes to execute these calls by some elevator
    The calls list is for one direction, meaning that we assume that each of the next destinations are in same direction
    as the elevator is going

    :param calls: The list of calls
    :param elevator: The elevator
    :return: A float representing the time it should take the elevator to execute the calls
    """

    first_call, last_call = calls[0], calls[-1]
    time = 0

    # handle first call first
    dist = abs(elevator.get_current_position() - first_call.get_next_pos())
    time += (dist / elevator.get_speed())
    time += elevator.get_stop_time() + elevator.get_open_time() + elevator.get_close_time() + elevator.get_start_time()

    for i in range(1, len(calls)):
        # calculate the time for a call after an interaction with the call before it
        dist = abs(calls[i].get_next_pos() - calls[i - 1].get_next_pos())
        time += dist / elevator.get_speed()
        time += elevator.get_stop_time() + elevator.get_open_time() + elevator.get_close_time() + elevator.get_start_time()

    # we add this once at the end where we don't need, so we subtract it from the time
    time -= elevator.get_start_time()

    return time


class Elevator:
    """
    This class is used to simulate an elevator \n

    Attributes:\n----\n
    _id: int \n\t The id number of this elevator \n
    _speed: double \n\t The speed of the elevator \n
    _minFloor: int \n\t The lowest floor where this elevator is operating (our case mostly the lowest floor in the building) \n
    _maxFloor: int \n\t The highest floor where this elevator is operating (also the highest floor in the building) \n
    _closeTime: double \n\t The time it takes this elevator to close its doors \n\n\n\n
    _openTime: double \n\t The time it takes this elevator to open its door \n\n\n\n
    _startTime: double \n\t The time it takes this elevator to reach "full speed" (basically a wait time for this elevator
    to start moving after he stopped at a floor) \n
    _stopTime: double \n\t The time it takes this elevator to get to a "full stop" (again a wait time before actually
    stopping and opening doors) \n
    """

    def __init__(self, elevator_dict: dict):
        """
        Constructs all the fields of this class using the "elevator_dict" argument

        :param elevator_dict: A dictionary representing the elevator
        """

        self._id = elevator_dict["_id"]
        self._speed = elevator_dict["_speed"]
        self._minFloor = elevator_dict["_minFloor"]
        self._maxFloor = elevator_dict["_maxFloor"]
        self._closeTime = elevator_dict["_closeTime"]
        self._openTime = elevator_dict["_openTime"]
        self._startTime = elevator_dict["_startTime"]
        self._stopTime = elevator_dict["_stopTime"]
        self._direction = 0
        self._state = 0
        self._up_calls = []
        self._down_calls = []
        self._currentPos = 0
        self.counter = -1
        self.delay = self._stopTime + self._startTime + self._openTime + self._closeTime

    def add_call(self, call):
        """
        Add a new call to the elevators queues

        :param call: The call to add
        """

        # if elevator is going up
        if call.get_next_pos() >= self._currentPos:
            # add the call in the correct position
            self._up_calls.append(call)
            self._up_calls.sort()

        # if elevator is going down
        elif call.get_next_pos() < self._currentPos:
            # add the call in the correct position
            self._down_calls.append(call)
            self._down_calls.sort(reverse=True)

    def calculate_execution_time(self, call):
        """
        Calculate the time for this elevator to do the call with the new call added to its call list

        :return: A float representing the calculated time
        """

        # if elevator is going up
        if self._direction == 1 and call.get_next_pos() >= self._currentPos:
            # copy the up calls
            up_calls = self._up_calls.copy()

            # add the call in the correct position
            up_calls.append(call)
            up_calls.sort()

            # calculate the time it takes to complete all these calls
            time = calculate_route_time(up_calls, self)

            return time

        # if elevator goes down
        elif self._direction == -1 and call.get_next_pos() <= self._currentPos:
            # copy the down calls
            down_calls = self._down_calls.copy()

            # add the call in the correct position
            down_calls.append(call)
            down_calls.sort(reverse=True)

            # calculate the time it takes to complete all these calls
            time = calculate_route_time(down_calls, self)

            return time

        # if elevator is not in any direction
        else:
            if call.get_next_pos() >= self._currentPos:
                # copy the up calls
                up_calls = self._up_calls.copy()

                # add and sort the calls
                up_calls.append(call)
                up_calls.sort()

                # calculate time
                time = calculate_route_time(up_calls, self)

                return time

            else:
                # copy the down calls
                down_calls = self._down_calls.copy()

                # add and sort the calls
                down_calls.append(call)
                down_calls.sort()

                # calculate time
                time = calculate_route_time(down_calls, self)

                return time

    def update(self):
        """
        This function moves the elevator in the simulator
        """

        # if elevator is moving
        if self._state == 1:
            # elevator is going up
            if self._direction == 1:
                # get the next floor step of the elevator
                next_jump = self._currentPos + self._speed

                # get the current call next floor
                call = self._up_calls[0].get_next_pos()

                if next_jump > self._maxFloor:
                    self._currentPos = self._maxFloor
                elif call <= next_jump:
                    self._currentPos = call
                    self._state = 0
                else:
                    self._currentPos = next_jump

            # elevator is going down
            if self._direction == -1:
                # get the next floor step of the elevator
                next_jump = self._currentPos - self._speed

                # get the current call next floor
                call = self._down_calls[0].get_next_pos()

                if next_jump < self._minFloor:
                    self._currentPos = self._minFloor
                elif call >= next_jump:
                    self._currentPos = call
                    self._state = 0
                else:
                    self._currentPos = next_jump

        # if elevator is not moving
        else:
            self.counter += 1

            # when we are done waiting, move
            if self.delay <= self.counter:
                self._state = 1
                self.counter = -1

                # update calls --------- make a function for that
                # update elevator direction ----------- make a function for that as well

                # if elevator is at direction 0
                if self._direction == 0:
                    if len(self._up_calls) < len(self._down_calls):
                        self._direction = -1
                    else:
                        self._direction = 1
                # if elevator is at some direction
                else:
                    # if elevator is going up
                    if self._direction == 1:
                        if len(self._up_calls) <= 0:
                            self._direction = 0
                    # if elevator is going down
                    elif self._direction == -1:
                        if len(self._down_calls) <= 0:
                            self._direction = 0

    def get_direction(self):
        """
        Get the direction the elevator is currently going

        :return: An int representing the direction in which the elevator is going
        """
        return self._direction

    def get_current_position(self):
        """
        Get the current position of the elevator

        :return: An int representing the current position of the elevator
        """
        return self._currentPos

    def get_speed(self):
        """
        Get the speed of the elevator

        :return: A float representing the speed of the elevator
        """
        return self._speed

    def get_open_time(self):
        """
        Get the open time for this elevator

        :return: A float representing the open time of this elevator
        """
        return self._openTime

    def get_close_time(self):
        """
        Get the close time for this elevator

        :return: A float representing the close time of this elevator
        """
        return self._closeTime

    def get_start_time(self):
        """
        Get the start time for this elevator, the time it takes for this elevator to reach its full speed

        :return: A float representing the start time of this elevator
        """
        return self._startTime

    def get_stop_time(self):
        """
        Get the stop time for this elevator, the time that it takes for this elevator to reach full stop

        :return: A float representing the stop time of this elevator
        """
        return self._stopTime

    def get_state(self):
        """
        Get the current state of the elevator (moving or not moving)

        :return: An int representing the state of this elevator
        """
        return self._state

    def __repr__(self):
        """
        Elevator {id} {
            current position: {pos}
            speed: {speed}
        }

        :return: A representation of the elevator
        """

        # why did you do this ?
        o = '{'
        c = '}'
        return f"\n{o}\n\tElevator ID: {self._id}\n\tPosition: {self._currentPos}\n\tSpeed: {self._speed}\n{c}"
