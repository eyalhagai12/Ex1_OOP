import json


class FileReader:
    """
    Read files from csv and json formats
    """

    def __init__(self, path):
        """
        Create a file reader object with the path (with the file name and extension)

        :param path: The path to the file
        """

        with open(path) as f:
            if ".json" in path:
                self.file = json.load(f)

            elif ".csv" in path:
                print("Got csv file will handle later")

            else:
                raise FileNotFoundError("The file format is not supported")

    def get_file(self):
        """
        Return the parsed file stored in this FileReader object

        :return: The parsed file
        """
        return self.file

