from .parser import Parser
import pandas as pd
import json


def xml_element_to_name(xml_element: str) -> str:
    """Converts XML element to name.

    Args:
        xml_element (str): XML element to convert.

    Returns:
        str: Name of the XML element.
    """
    return xml_element.split('>')[1].split('<')[0]


class StudiesParser(Parser):
    """Parses the JSON data returned by the query to a pandas dataframe.

    Methods:
        parse_data(data): Parses the JSON data and returns a pandas dataframe.
    """

    def __init__(self):
        self.parser = Parser()

    def parse_data(self, data: str) -> pd.DataFrame:
        """Parse the JSON data and return a pandas dataframe.

        Args:
            data (str): JSON data returned by the query.

        Returns:
            DataFrame: Pandas dataframe containing the parsed data.
                Returns None if no valid dataframes are obtained.
        """
        df = {'Study': [], 'Authors': [], 'Journal': []}
        studies = json.loads(data)['data']
        for study in studies:
            df['Study'].append(xml_element_to_name(study[0]))
            df['Authors'].append(study[1])
            df['Journal'].append(study[2])
        
        return pd.DataFrame(df)