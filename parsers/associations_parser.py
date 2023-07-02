from . import Parser
import pandas as pd
import json


class AssociationsParser(Parser):
    """
    Parses the JSON data returned by the query to a pandas dataframe.
    """

    def parse(self, data: str) -> pd.DataFrame:
        """Parse json to pandas DF row
        
        Args:
            json (str): json to parse
        Returns:
            pd.DataFrame: pandas DF row"""
        
        associations = json.loads(data)['data']

        df = {'Name': [], 'Individual voxel z-score': [], 'Individual voxel Posterior prob': [], 'Seed-based network Func conn. (r)': [], 'Seed-based network Meta-analytic coact. (r)':[]}
        
        for assoc in associations:
            df['Name'].append(assoc[0])
            df['Individual voxel z-score'].append(float(assoc[1]))
            df['Individual voxel Posterior prob'].append(float(assoc[2]))
            df['Seed-based network Func conn. (r)'].append(float(assoc[3]))
            df['Seed-based network Meta-analytic coact. (r)'].append(float(assoc[4]))
        
        return pd.DataFrame(df)