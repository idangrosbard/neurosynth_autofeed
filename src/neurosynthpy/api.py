from .master import Master
from .parsers import AssociationsParser, StudiesParser
from .web_querier import Querier
from .validator import Validator
import pandas as pd
from . import consts
from typing import Dict


class API(object):
    def __init__(self, masters: Dict[str, Master]):
        self.masters = masters
    
    def get(self, coords: pd.DataFrame, master_name: str):
        return self.masters[master_name].process_coordinates(coords)
    

def get(coords: pd.DataFrame, data_type: str) -> pd.DataFrame:
    studies_master = Master(Querier(consts.STUDIES_URL), StudiesParser(), Validator())
    associations_master = Master(Querier(consts.ASSOCIATIONS_URL), AssociationsParser(), Validator())

    if data_type == 'studies':
        return studies_master.process_coordinates(coords)
    elif data_type == 'associations':
        return associations_master.process_coordinates(coords)
    else:
        raise ValueError("Unavailable name: {}".format(data_type))
