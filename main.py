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
OUTPUT_PATH = "out"

combinations = [("B1", "a"), ("B2", "a"), ("B3", "a"), ("B3", "b"), ("B3", "c"), ("B3", "d"), ("B4", "a"),
                ("B4", "b"), ("B4", "c"), ("B4", "d"), ("B5", "a"), ("B5", "b"), ("B5", "c"), ("B5", "d")]


def make_outputs():
    for comb in combinations:
        sys.argv[1] = f"{comb[0]}.json"
        sys.argv[2] = f"Calls_{comb[1]}.csv"
        sys.argv[3] = f"Ex1_{comb[0]}_case_{comb[1]}.csv"
        main()


def score(case):
    test = combinations[case]
    out_file = f"Ex1_{test[0]}_case_{test[1]}.csv"
    building = f"{test[0]}.json"
    sys.argv[1] = f"{test[0]}.json"
    sys.argv[2] = f"Calls_{test[1]}.csv"
    sys.argv[3] = f"Ex1_{test[0]}_case_{test[1]}.csv"
    main()

    command = f"java -jar ~/Documents/'test ex1'/Ex1/libs/Ex1_checker_V1.2_obf.jar 1111,2222,3333 {os.path.join(BUILDING_DIR_PATH, building)} {os.path.join(OUTPUT_PATH, out_file)} out/Ex1_{test[0]}_case_{test[1]}.log"
    os.system(command)


def create_output(record: list, calls: list, file_name: str):
    """
    This function updates the given output file output file

    :param record: The record of the simulation
    :param calls: The calls of this case
    :param file_name: The name of the output file
    """

    path = os.path.join(OUTPUT_PATH, file_name)

    with open(path, "w") as out_file:
        calls_str = ""

        for call, elevator_index in zip(calls, record):
            call_string = str(call)
            call_string = call_string.split(",")
            call_string[-1] = str(elevator_index)
            call_string = ",".join(call_string)
            calls_str += call_string + "\n"

        out_file.write(calls_str)


def main():
    building_path = os.path.join(BUILDING_DIR_PATH, sys.argv[1])
    call_path = os.path.join(CALL_DIR_PATH, sys.argv[2])

    building_dict = FileReader.read_file(building_path)
    calls_list = FileReader.read_file(call_path)

    calls = [Call(c) for c in calls_list]
    building = Building(building_dict)

    sim = Simulator(building, calls)

    sim.run_sim()

    record = sim.get_records()

    create_output(record, calls, sys.argv[3])


if __name__ == '__main__':
    make_outputs()
