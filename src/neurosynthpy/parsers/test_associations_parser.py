from . import AssociationsParser
import pandas as pd
import pytest
import numpy as np



class TestAssociationsParser(object):
    def test_single_parse(self):
        """Test the parse method of the AssociationsParser class.
        
        Returns:
            None
        """
        test_json = '{"data": [["test_name", "0.1", "0.2", "0.3", "0.4"]]}'
        test_df = pd.DataFrame({'Name': ['test_name'], 'Individual voxel z-score': [0.1], 'Individual voxel Posterior prob': [0.2], 'Seed-based network Func conn. (r)': [0.3], 'Seed-based network Meta-analytic coact. (r)': [0.4]})
        assert AssociationsParser().parse(test_json).equals(test_df)

    def test_parse_with_int_vals(self):
        """Test the parse method of the AssociationsParser class.
        
        Returns:
            None
        """
        test_json = '{"data": [["test_name", "1", "0.2", "4", "0.4"]]}'
        test_df = pd.DataFrame({'Name': ['test_name'], 'Individual voxel z-score': [float(1)], 'Individual voxel Posterior prob': [0.2], 'Seed-based network Func conn. (r)': [float(4)], 'Seed-based network Meta-analytic coact. (r)': [0.4]})
        assert AssociationsParser().parse(test_json).equals(test_df)

    def test_multiple_parse(self):
        """Test the parse method of the AssociationsParser class.
        
        Returns:
            None
        """
        test_json = '{"data": [["test_name", "0.1", "0.2", "0.3", "0.4"], ["test_name2", "0.5", "0.6", "0.7", "0.8"]]}'
        test_df = pd.DataFrame({'Name': ['test_name', 'test_name2'], 'Individual voxel z-score': [0.1, 0.5], 'Individual voxel Posterior prob': [0.2, 0.6], 'Seed-based network Func conn. (r)': [0.3, 0.7], 'Seed-based network Meta-analytic coact. (r)': [0.4, 0.8]})
        assert AssociationsParser().parse(test_json).equals(test_df)

    def test_parse_with_bad_vals(self):
        test_json = '{"data": [["test_name", "0.1", "0.2", "0.3", "not float"]]}'
        test_df = pd.DataFrame({'Name': ['test_name'], 'Individual voxel z-score': [float(1)], 'Individual voxel Posterior prob': [0.2], 'Seed-based network Func conn. (r)': [float(4)], 'Seed-based network Meta-analytic coact. (r)': [np.nan]})
    
    def test_parse_with_bad_length(self):
        test_json = '{"data": [["test_name", "0.1", "0.2", "0.3"]]}'
        with pytest.raises(IndexError):
            AssociationsParser().parse(test_json)

    def test_no_associations(self):
        test_json = '{"data": []}'
        test_df = pd.DataFrame({'Name': [], 'Individual voxel z-score': [], 'Individual voxel Posterior prob': [], 'Seed-based network Func conn. (r)': [], 'Seed-based network Meta-analytic coact. (r)':[]})
        assert AssociationsParser().parse(test_json).equals(test_df)