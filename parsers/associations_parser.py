from . import Parser
import pandas as pd
import numpy as np
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
        cols = ['Name', 'Individual voxel z-score', 'Individual voxel Posterior prob', 'Seed-based network Func conn. (r)', 'Seed-based network Meta-analytic coact. (r)']
        
        for assoc in associations:
            df['Name'].append(assoc[0])

            if len(assoc) != len(cols):
                raise IndexError('Association length does not match column length')
            
            # Iterate through each numeric value in the association
            for i in range(1, len(assoc)):
                curr_val = assoc[i]
                try: 
                    df[cols[i]].append(float(curr_val))
                except ValueError:
                    # Set as nan if not a float
                    df[cols[i]].append(np.nan)
            
        return pd.DataFrame(df)