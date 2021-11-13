from Call import Call

class Simulator:
    """
    This class is for simulating the scenarios we encounter and calculate the best way of assigning the elevators
    """

    def __init__(self, building, calls):
        """
        Construct a simulator using a building and calls

        :param building:
        :param calls:
        """
        self._building = building
        self._calls = [Call(c) for c in calls]


    def run_simulator(self):
        pass
