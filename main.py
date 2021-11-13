import FileReader
import sys
import os
from Elevator import Elevator
from Simulator import Simulator
from Call import Call

BUILDING_DIR_PATH = "data/Ex1_input/Ex1_Buildings"
CALL_DIR_PATH = "data/Ex1_input/Ex1_Calls"

building_path = os.path.join(BUILDING_DIR_PATH, sys.argv[1])
call_path = os.path.join(CALL_DIR_PATH, sys.argv[2])

building_dir = FileReader.read_file(building_path)
calls_list = FileReader.read_file(call_path)

simulator = Simulator(building_dir, calls_list)

c = Call(calls_list[0])

print(c)

