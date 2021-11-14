class Simulator:
    """
    This class is for simulating the scenarios we encounter and calculate the best way of assigning the elevators
    """

    def __init__(self, building, calls):
        self._building = building
        self._calls = calls

    def run_sim(self):
        """
        The main simulation loop
        This function runs the simulation...
        """

        # the time of the simulation
        simulation_time = self._calls[-1].getTime() + 120

        call_index = 0
        for second in range(simulation_time):
            current_calls = []

            # get current calls
            while second <= self._calls[call_index].getTime() < second + 1:
                current_calls.append(self._calls[call_index])
                call_index += 1

            # assign calls main work
            for idx, call in enumerate(current_calls):
                for elevator in self._building.getElvators():
                    # calculate min time (overall or to execute call)
