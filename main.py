import FileReader
import sys
import os
from Elevator import Elevator
from Elevator import calculate_route_time
from Call import Call

BUILDING_DIR_PATH = "data/Ex1_input/Ex1_Buildings"
CALL_DIR_PATH = "data/Ex1_input/Ex1_Calls"

building_path = os.path.join(BUILDING_DIR_PATH, sys.argv[1])
call_path = os.path.join(CALL_DIR_PATH, sys.argv[2])

building_dir = FileReader.read_file(building_path)
calls_list = FileReader.read_file(call_path)

elevators = building_dir["_elevators"]

elevators = [Elevator(x) for x in elevators]

calls = [Call(calls_list[c]) for c in range(0, len(calls_list), 10)]

for idx, elevator in enumerate(elevators):
    print("Elevator ", idx, ": ", elevator.calculate_execution_time(calls[0]))



