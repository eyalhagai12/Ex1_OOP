import FileReader
import sys
import os
from Building import Building
from Algo import Algo
"""
Created on Mon Nov 15 20:40:00 2021

@author: fedora
"""

def main():
    BUILDING_DIR_PATH = "data/Ex1_input/Ex1_Buildings"
    CALL_DIR_PATH = "data/Ex1_input/Ex1_Calls"

    building_path = os.path.join(BUILDING_DIR_PATH, sys.argv[1])
    call_path = os.path.join(CALL_DIR_PATH, sys.argv[2])
    outfile = sys.argv[3]

    b = Building(Building.from_json(building_path))
    a = Algo(b,call_path)
    a.allocateAnElevator()
    
    string = ""
    for call in a._calls:
        string+="Elevator call,"+str(call.getTime())+","+str(call.getSrc())+","+str(call.getDest())+","+str(call.getState())+","+str(call.getAssigned())+"\n"
    print(string)
    
    if(os.path.exists(outfile)):
        with open(outfile,'w') as file:
            file.write(string)
        print(outfile+" has been modified.\n")
    else:
        with open(outfile,'x') as file:
            file.write(string)
        print(outfile+" has been created.\n")
    
if __name__ == "__main__":
    main()