import pandas as pd


class Parser(object):
    """ An interface class for parsing json answers to pandas DF rows"""
    def parse(self, json: str) -> pd.DataFrame:
        """Parse json to pandas DF row
        
        Args:
            json (str): json to parse
        Returns:
            pd.DataFrame: pandas DF row"""
        raise NotImplementedError
