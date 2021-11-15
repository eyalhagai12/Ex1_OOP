import FileReader
import sys
import os
from Elevator import Elevator
from Elevator import calculate_route_time
from Call import Call
from Simulator import Simulator
from Building import Building

BUILDING_DIR_PATH = "data/Ex1_input/Ex1_Buildings"
CALL_DIR_PATH = "data/Ex1_input/Ex1_Calls"


def main():
    building_path = os.path.join(BUILDING_DIR_PATH, sys.argv[1])
    call_path = os.path.join(CALL_DIR_PATH, sys.argv[2])

    building_dict = FileReader.read_file(building_path)
    calls_list = FileReader.read_file(call_path)

    calls = [Call(c) for c in calls_list]
    building = Building(building_dict)

    sim = Simulator(building, calls)

    sim.run_sim()


if __name__ == '__main__':
    main()
