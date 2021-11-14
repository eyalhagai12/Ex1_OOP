from Elevator import Elevator
import FileReader


class Building:
    """
    This class is for simulating the building
    """

    def __init__(self, json_dict: dict):
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

<<<<<<< HEAD
    def from_json(path: str):
=======
    @classmethod
    def from_json(cls, path: str):
>>>>>>> c182d9bb33fd7f96268766683c1e630df4102f26
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

        return FileReader.read_file(path)

<<<<<<< HEAD
    def elev_list(json_dict: dict):
=======
    @classmethod
    def elev_list(cls, json_dict: dict):
>>>>>>> c182d9bb33fd7f96268766683c1e630df4102f26
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

<<<<<<< HEAD
    def getElvators(self):
        return self._elevators

=======
>>>>>>> c182d9bb33fd7f96268766683c1e630df4102f26
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
