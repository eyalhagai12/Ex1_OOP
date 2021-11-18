import math

from Call import Call


def calculate_route_time(calls, elevator):
    """
    Calculate the time it takes to execute these calls by some elevator
    The calls list is for one direction, meaning that we assume that each of the next destinations are in same direction
    as the elevator is going

    :param calls: The list of calls
    :param elevator: The elevator
    :return: A float representing the time it should take the elevator to execute the calls
    """

    time = 0
    if len(calls) > 0:
        first_call = calls[0]
        # time += elevator.get_extra_time()

        # handle first call first
        dist = abs(elevator.get_current_position() - first_call.get_next_pos())
        time += (dist / elevator.get_speed())
        time += elevator.get_stop_time() + elevator.get_open_time() + elevator.get_close_time() + elevator.get_start_time()

    for i in range(1, len(calls)):
        # calculate the time for a call after an interaction with the call before it
        dist = abs(calls[i].get_next_pos() - calls[i - 1].get_next_pos())
        time += dist / elevator.get_speed()
        time += elevator.get_stop_time() + elevator.get_open_time() + elevator.get_close_time() + elevator.get_start_time()

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
        self._extra_time = 0

    def add_call(self, call):
        """
        Add a new call to the elevators queues

        :param call: The call to add
        """

        # if elevator is going up
        if call.get_next_pos() is not None and call.get_next_pos() >= self._currentPos:
            # add the call in the correct position
            self._up_calls.append(call)
            self._up_calls.sort()

            # if the elevator is not pointed to a direction, set its direction to this call
            if self._direction == 0:
                self._direction = 1
                self._state = 1
                self.counter = -1

        # if elevator is going down
        elif call.get_next_pos() is not None and call.get_next_pos() < self._currentPos:
            # add the call in the correct position
            self._down_calls.append(call)
            self._down_calls.sort(reverse=True)

            # if the elevator is not pointed to a direction, set its direction to this call
            if self._direction == 0:
                self._direction = -1
                self._state = 1
                self.counter = -1

    def calculate_execution_time(self, call):
        """
        Calculate the time for this elevator to do the call with the new call added to its call list

        :return: A float representing the calculated time
        """

        # speed / distance must be close to 1 as much as possible
        call_dist = abs(call.get_src() - call.get_dst())

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
                # copy the up calls and down calls
                up_calls = self._up_calls.copy()
                down_calls = self._down_calls.copy()

                # add and sort the calls
                up_calls.append(call)
                up_calls.sort()

                # calculate time
                time = calculate_route_time(up_calls, self) + calculate_route_time(down_calls, self)

                return time

            else:
                # copy the down calls and up calls
                down_calls = self._down_calls.copy()
                up_calls = self._up_calls.copy()

                # add and sort the calls
                down_calls.append(call)
                down_calls.sort(reverse=True)

                # calculate time
                time = calculate_route_time(down_calls, self) + calculate_route_time(up_calls, self)

                return time

    def update(self):
        """
        This function moves the elevator in the simulator
        """

        # if elevator is moving
        if self._state == 1:
            # move the elevator
            self.move()

        # if elevator is not moving
        else:
            self.counter += 1

            # when we are done waiting, move
            if self.delay <= self.counter:
                self._state = 1
                self.counter = -1

                # update calls
                self.update_calls()

                # update the direction of the elevator
                self.update_direction()

    def update_direction(self):
        """
        This function is for updating the direction of the elevator in the simulation
        """

        # if the direction is 0, set some direction
        if self._direction == 0:
            if len(self._up_calls) > len(self._down_calls):
                self._direction = 1
            else:
                self._direction = -1

        # else if the direction is up look if the next call is below
        elif len(self._up_calls) > 0 and self._direction == 1 and self._up_calls[0].get_next_pos() < self._currentPos:
            self._direction = -1

        # else if direction is down, look if the next call is above
        elif len(self._down_calls) > 0 and self._direction == -1 and self._down_calls[
            0].get_next_pos() > self._currentPos:
            self._direction = 1

        if len(self._up_calls) <= 0 and len(self._down_calls) > 0:
            self._direction = -1

        if len(self._down_calls) <= 0 and len(self._up_calls) > 0:
            self._direction = 1

        if len(self._down_calls) <= 0 and len(self._up_calls) <= 0:
            self._direction = 0
            self._state = 0

    def update_calls(self):
        """
        Update the calls of this elevator
        """

        # check if elevator is going up
        if self._direction == 1:
            call = self._up_calls[0]
            del self._up_calls[0]

            # if the call is at "to source" state
            if call.get_state() == 0 or call.get_state() == 1:
                call.set_state(2)  # set to destination
                self.add_call(call)  # add the call back to the elevator calls

        # check if elevator is going up
        if len(self._down_calls) > 0 and self._direction == -1:
            call = self._down_calls[0]
            del self._down_calls[0]

            # if the call is at "to source" state
            if call.get_state() == 0 or call.get_state() == 1:
                call.set_state(2)  # set to destination
                self.add_call(call)  # add the call back to the elevator calls

    def move(self):
        """
        Move the elevator in the simulation
        """
        # elevator is going up
        if len(self._up_calls) > 0 and self._direction == 1:
            # get the next floor step of the elevator
            next_jump = self._currentPos + self._speed

            # get the current call's next floor
            call_pos = self._up_calls[0].get_next_pos()

            # make the next step
            if next_jump > self._maxFloor:
                self._currentPos = self._maxFloor
            if call_pos <= next_jump:
                self._extra_time += abs(self._currentPos - call_pos) / self._speed
                self._currentPos = call_pos
                self._state = 0
            else:
                self._currentPos = next_jump

        # elevator is going down
        if len(self._down_calls) > 0 and self._direction == -1:
            # get the next floor step of the elevator
            next_jump = self._currentPos - self._speed

            # get the current call next floor
            call_pos = self._down_calls[0].get_next_pos()

            # make the next step
            if next_jump < self._minFloor:
                self._currentPos = self._minFloor
            if call_pos >= next_jump:
                self._extra_time += abs(self._currentPos - call_pos) / self._speed
                self._currentPos = call_pos
                self._state = 0
            else:
                self._currentPos = next_jump

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

    def get_extra_time(self):
        """
        Get the extra time of this elevator
        extra time is the time that is accumulated over the simulation because in order to keep track
        of the times when they are not integers but the simulator is running on integers

        :return: A float representing the extra time
        """
        return self._extra_time

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
        return f"\n{o}\n\tElevator ID: {self._id}\n\tPosition: {self._currentPos}\n\tSpeed: {self._speed}\n" \
               f"Calls: {len(self._up_calls) + len(self._down_calls)}\nDirection: {self._direction}\nState: {self._state}{c}"
