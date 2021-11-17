import math

from Elevator import Elevator


class Building:
    """
    This class is for simulating the building
    """

    def __init__(self, json_dict: dict):
        """
        Create a building from a given dictionary

        :param json_dict: A dictionary that represents the building
        """

        self._minFloor = json_dict['_minFloor']
        self._maxFloor = json_dict['_maxFloor']
        self._elevators = [Elevator(elev) for elev in json_dict["_elevators"]]
        self._speed_distribution = []
        self._groups = []
        self._dist_distribution = []
        self.initiate_groups()

    def get_elevators(self):
        """
        Get the list of elevators in this building

        :return: A list of elevator objects
        """
        return self._elevators

    def initiate_groups(self):
        """
        Create a distribution of elevator speeds an then create groups of elevators

        """

        # create distribution by speed
        for elev in self._elevators:
            speed = int(elev.get_speed())

            if speed not in self._speed_distribution:
                self._speed_distribution.append(speed)

        self._speed_distribution.sort()

        # create the groups
        self._groups = [list() for speed in self._speed_distribution]

        for elev in self._elevators:
            speed = int(elev.get_speed())
            index = self._speed_distribution.index(speed)
            self._groups[index].append(elev)

        # create the distance distribution
        unit = int((self._maxFloor - self._minFloor) / len(self._speed_distribution))

        for i in range(len(self._speed_distribution)):
            rng = (i * unit, (i + 1) * unit)
            self._dist_distribution.append(rng)

    def get_call_group(self, call):
        """
        Given a call return the elevators that answer such calls

        :param call: A call object, the call that we want to find the group for
        :return: A list of elevators
        """
        # get the distance of this call
        call_dist = abs(call.get_src() - call.get_dst())
        index = -1

        for idx, dist in enumerate(self._dist_distribution):
            if dist[0] <= call_dist < dist[1]:
                index = idx
                break

        return index, self._groups[index]

    def get_best_elev_for_call(self, call):
        """
        Return the index of the best elevator for his call

        :param call: The call to which to find the best elevator
        :return: An integer representing hte index of the best elevator
        """

        best_time = math.inf
        best_index = -1
        for idx, elevator in enumerate(self._elevators):
            time = elevator.calculate_execution_time(call)

            if time < best_time:
                best_index = idx
                best_time = time

        return best_index

    def __repr__(self):
        """
        Return a representation of this building
        """
        return f"minFloor: {self._minFloor}, maxFloor: {self._maxFloor}, elevators: {self._elevators}\n"
