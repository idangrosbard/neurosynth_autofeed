import pandas as pd


class Parser(object):
    """ An interface class for parsing json answers to pandas DF rows"""
    def parse(self, data: str) -> pd.DataFrame:
        """Parse json to pandas DF row
        
        Args:
            data (str): json to parse
        Returns:
            pd.DataFrame: pandas DF row"""
        raise NotImplementedError
