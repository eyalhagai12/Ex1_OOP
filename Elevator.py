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
        self._calls = []
        self._penalty = (self._openTime + self._closeTime + self._startTime + self._stopTime) - self._speed

        # as i understood the elevator starts at level 0
        self._currentPos = 0

    
    def getCalls(self):
        return self._calls
    
    def getPenalty(self):
        return self._penalty

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
