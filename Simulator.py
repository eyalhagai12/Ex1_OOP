import math
from Building import Building


class Simulator:
    """
    This class is for simulating the scenarios we encounter and calculate the best way of assigning the elevators
    This class has the algorithm within it, meaning this class is like an algorithm and a simulator
    The idea is that when we get calls we try to simulate the best outcome and record our actions and then output the results
    """

    def __init__(self, building: Building, calls):
        """
        Create a simulator object
        Simulate the movements of the elevators in a given building

        :param building: The building
        :param calls: The calls
        """
        self._building = building
        self._calls = calls
        self._elevators = self._building.get_elevators()
        self._record = []

    def run_sim(self):
        """
        The main simulation loop
        This function runs the simulation [add more doc here]
        """

        # the time of the simulation
        simulation_time = int(self._calls[-1].get_time() + 120) + 1

        call_index = 0
        for second in range(simulation_time):
            current_calls = []

            # get current calls
            while call_index < len(self._calls) and second <= self._calls[call_index].get_time() < second + 1:
                current_calls.append(self._calls[call_index])
                call_index += 1

            # assign calls, main work
            best_indexes = [-1 for c in current_calls]  # each cell contains index of the best elevator for this call
            # best_times = [math.inf for c in current_calls]

            for idx, call in enumerate(current_calls):
                # create function get best for call
                index = self._building.get_best_elev_for_call(call)
                best_indexes[idx] = index

            # append to the elevators
            for idx, call in enumerate(current_calls):
                # add the best elevator index to the record
                self._record.append(best_indexes[idx])

                # get the right elevator
                elev = self._elevators[best_indexes[idx]]

                # add the call to it
                elev.add_call(call)

            # move and update elevators
            for elevator in self._elevators:
                elevator.update()

    def get_records(self):
        """
        After simulation get the records of the simulation to output to a file

        :return: A list containing the indexes of the elevators for eah call in the call list
        """
        if len(self._record) <= 0:
            print("Please run the simulation first!")
            return None

        return self._record
