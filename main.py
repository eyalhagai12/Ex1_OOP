from Building import Building
from Simulator import Simulator
from Elevator import Elevator
from FileReader import FileReader


fr = FileReader("data/Ex1_input/Ex1_Buildings/B2.json")

building_dict = fr.get_file()

for key in building_dict:
    print("{}: {}".format(key, building_dict[key]))



