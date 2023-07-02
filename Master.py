import numpy as np
from verifier import Verifier
from query import Query
from parser import Parser
import pandas as pd

class Master:
    """Synchronizes the query process for a given set of coordinates.

    The Master class accepts a numpy array of X Y Z coordinates (N x 3) as input.
    It iterates through each set of coordinates in the array and performs the following steps:
    
    1. Calls the Verifier class to verify the coordinates (ensure they are valid).
    2. If the coordinates are invalid, it prints an error message and moves on to the next set of coordinates.
    3. If the coordinates are valid, it calls the Query class to query the coordinates.
    4. The output of the query is JSON data, which is the input for the Parser class.
    5. The Parser class parses the JSON data and returns a pandas dataframe.
    6. Each output of the query is the input for the Parser class, which parses the output and returns a dataframe.
    7. It then unites all the pandas dataframes into one dataframe and returns it as output.

    Attributes:
        verifier (Verifier): Instance of the Verifier class for coordinate verification.
        query (Query): Instance of the Query class for querying the coordinates.
        parser (Parser): Instance of the Parser class for parsing the JSON data.

    Methods:
        process_coordinates(coordinates): Processes the coordinates and returns a merged dataframe.
    """

    def __init__(self):
        self.verifier = Verifier()
        self.query = Query()
        self.parser = Parser()
    
    def process_coordinates(self, coordinates):
        """Process the array of coordinates and return a merged dataframe.

        Args:
            coordinates (ndarray): Numpy array of X Y Z coordinates (N x 3).

        Returns:
            DataFrame: Merged pandas dataframe containing the parsed data.
                Returns None if no valid dataframes are obtained.
        """
        dataframes = []
        
        for coord in coordinates:
            if self.verifier.verify_coordinates(coord):
                query_result = self.query.query_coordinates(coord)
                parsed_data = self.parser.parse_data(query_result)
                dataframes.append(parsed_data)
            else:
                print(f"Invalid coordinates: {coord}. Skipping...")
        
        if dataframes:
            merged_dataframe = pd.concat(dataframes)
            return merged_dataframe
        else:
            return None
