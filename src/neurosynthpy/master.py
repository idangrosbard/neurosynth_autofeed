import numpy as np
from src.neurosynthpy.web_querier import Querier
from src.neurosynthpy.parsers import Parser
from src.neurosynthpy.validator import Validator
import pandas as pd


class Master:
    """Synchronizes the query process for a given set of coordinates.

    The Master class accepts a numpy array of X Y Z coordinates (N x 3) as input.
    It iterates through each set of coordinates in the array and performs the following steps:
    
    1. Calls the Verifier class to verify the coordinates (ensure they are valid).
    2. If the coordinates are valid, it calls the Query class to query the coordinates.
    3. The output of the query is JSON data, which is the input for the Parser class.
    4. The Parser class parses the JSON data and returns a pandas dataframe.
    5. Each output of the query is the input for the Parser class, which parses the output and returns a dataframe.
    6. It then unites all the pandas dataframes into one dataframe and returns it as output.

    Attributes:
        verifier (Verifier): Instance of the Verifier class for coordinate verification.
        query (Query): Instance of the Query class for querying the coordinates.
        parser (Parser): Instance of the Parser class for parsing the JSON data.

    Methods:
        process_coordinates(coordinates): Processes the coordinates and returns a merged dataframe.
    """

    def __init__(self, query: Querier, parser: Parser, validator: Validator):
        self.query = query
        self.parser = parser
        self.validator = validator
    
    def process_coordinates(self, coordinates: np.ndarray) -> pd.DataFrame:
        """Process the array of coordinates and return a merged dataframe.

        Args:
            coordinates (ndarray): Numpy array of X Y Z coordinates (N x 3).

        Returns:
            DataFrame: Merged pandas dataframe containing the parsed data.
                Returns None if no valid dataframes are obtained.
        """
        dataframes = []

        if self.validator.test_coordinates(coordinates):
            for coord in coordinates:
                query_result = self.query.query(coord[0], coord[1], coord[2])
                parsed_data = self.parser.parse(query_result)
                
                parsed_data['x'] = coord[0]
                parsed_data['y'] = coord[1]
                parsed_data['z'] = coord[2]
                parsed_data['x, y, z'] = f'{coord[0]}, {coord[1]}, {coord[2]}'
                
                dataframes.append(parsed_data)
            
            if dataframes:
                merged_dataframe = pd.concat(dataframes)
                return merged_dataframe
            else:
                return None
        else:
            raise ValueError('Invalid coordinates.')
