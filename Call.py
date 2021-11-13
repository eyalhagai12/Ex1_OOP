class Call:
    """
    This class is saving a call
    """

    def __init__(self, call: str):
        """
        Construct the call from a string representing the call
        :param call:
        """

        attr = call.split(",")
        self.init_time = float(attr[1])
        self.src = int(attr[2])
        self.dst = int(attr[3])
        self.state = int(attr[4])
        self.elevator = int(attr[5])

    def __repr__(self):
        """
        Call {
            time:
            src:
            dst:
            state:
            elevator:
        }

        :return: A string representation for the call
        """

        return "Call {\n\tcall_time: " + str(self.init_time) + "\n\tsrc: " + str(self.src) + "\n\tdst: " + str(self.dst) + \
               "\n\tstate: " + str(self.state) + "\n\televator: " + str(self.elevator) + "\n}"
