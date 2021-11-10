import json
from Elevator import Elevator
class Building:
    """
    This class is for simulating the building
    """
    def __init__(self, json_dict:dict):
        """
        Description
        -----------
        Constructs all the fields of this class
        
        Parameters
        ----------
        json_dict : dict

        Returns
        -------
        None.
        """
        self._minFloor = json_dict['_minFloor']
        self._maxFloor = json_dict['_maxFloor']
        self._elevators = Building.elev_list(json_dict)
        
    def from_json(path:str):
        """
        Description
        -----------
        Converts JSON file into a Dict and returns it
        
        Parameters
        ----------
        path : str

        Returns
        -------
        JSON file in dict format
        """
        with open(file=path) as fp:
            return json.load(fp)
        
    def elev_list(json_dict:dict):
        """
        Description
        -----------
        Creates a list of elevators and returns it
        
        Parameters
        ----------
        json_dict : dict

        Returns
        -------
        temp2 : list
        """
        temp1 = json_dict['_elevators']
        temp2 = []
        for i in range(len(temp1)):
            temp2.append(Elevator(temp1[i]))
        return temp2
    
    def __repr__(self):
        """
        Description
        -----------
        Returns a string representation of the building
        
        Returns
        -------
        str
        """
        return f"minFloor: {self._minFloor}, maxFloor: {self._maxFloor}, elevators: {self._elevators}\n"
    