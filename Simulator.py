import math


class Simulator:
    """
    This class is for simulating the scenarios we encounter and calculate the best way of assigning the elevators
    This class has the algorithm within it, meaning this class is like an algorithm and and a simulator
    The idea is that when we get calls we try to simulate the best outcome and record our actions and then output he results
    """

    def __init__(self, building, calls):
        self._building = building
        self._calls = calls
        self._elevators = self._building.getElvators()

    def run_sim(self):
        """
        The main simulation loop
        This function runs the simulation...
        """

        # the time of the simulation
        simulation_time = self._calls[-1].get_time() + 120

        call_index = 0
        for second in range(simulation_time):
            current_calls = []

            # get current calls
            while second <= self._calls[call_index].get_time() < second + 1:
                current_calls.append(self._calls[call_index])
                call_index += 1

            # assign calls, main work
            best_indices = [-1 for c in current_calls]  # each cell contains the best elevator for this call
            best_times = [math.inf for c in current_calls]

            for idx, call in enumerate(current_calls):
                best_time = math.inf
                for elev_idx, elevator in self._building.getElvators():
                    # calculate time
                    elev_time = elevator.calculate_execution_time(call)

                    # save the best result
                    if best_time > elev_time:
                        best_times[idx] = elev_time
                        best_indices[idx] = elev_idx

            # append to the elevators
            for idx, call in enumerate(current_calls):
                # get the right elevator
                elev = self._elevators[best_indices[idx]]

                # add the call to it
                elev.add_call(call)


