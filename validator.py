from typing import List

class Validator():
    """
    Class for validating the input data
    """
    def check_coordinates_is_int(self, list_of_coordinates: List[List[int]]) -> bool:
        """
        Checks if the coordinates are integers
        :param list_of_coordinates: list of coordinates
        :return: True if the coordinates are int, False otherwise
        """
        if not all(isinstance(value, int) for coordinate in list_of_coordinates for value in coordinate):
            raise ValueError("Coordinates must be integers")
        
        return True


    def check_coordinates_length(self, list_of_coordinates: List[List[int]]) -> bool:
        """
        Checks if there are 3 coordinates for each point
        :param list_of_coordinates: list of coordinates
        :return: True if there are 3 coordinates for each point, False otherwise
        """
        if not all(len(coordinate) == 3 for coordinate in list_of_coordinates):
            raise ValueError("There must be 3 coordinates for each point")
        
        return True
    

    def check_coordinates_is_list(self, list_of_coordinates: List[List[int]]) -> bool:
        """
        Checks if the coordinates are in a list
        :param list_of_coordinates: list of coordinates
        :return: True if the coordinates are in a list, False otherwise
        """
        if not isinstance(list_of_coordinates, list):
            raise ValueError("Coordinates must be in a list")
        
        return True
    

    def check_coordinates_is_not_empty(self, list_of_coordinates: List[List[int]]) -> bool:
        """
        Checks if the coordinates are not empty
        :param list_of_coordinates: list of coordinates
        :return: True if the coordinates are not empty, False otherwise
        """
        if not list_of_coordinates:
            raise ValueError("Coordinates must not be empty")
        
        return True
    

    def check_coordinates_range(self,list_of_coordinates: List[List[int]]) -> bool:
        """
        Checks if the coordinates are in the range of the board
        The range:
         -90 to +90 along the x-axis
         -126 to +90 along the y-axis
         -72 to +108 along the z-axis
        :param list_of_coordinates: list of coordinates
        :return: True if the coordinates are in the range of the board, False otherwise
        """
        for coordinate in list_of_coordinates:
            if coordinate[0] < -90 or coordinate[0] > 90:
                raise ValueError("The x-axis must be in the range of -90 to +90")
            if coordinate[1] < -126 or coordinate[1] > 90:
                raise ValueError("The y-axis must be in the range of -126 to +90")
            if coordinate[2] < -72 or coordinate[2] > 108:
                raise ValueError("The z-axis must be in the range of -72 to +108")
        
        return True
    

    def test_coordinates(self, list_of_coordinates: List[List[int]]) -> bool:
        """
        Test the coordinates
        :param list_of_coordinates: list of coordinates
        :return: True if the coordinates are valid, False otherwise
        """
        if not Validator.check_coordinates_is_list(list_of_coordinates):
            raise ValueError("Coordinates must be in a list")
        if not Validator.check_coordinates_is_not_empty(list_of_coordinates):
            raise ValueError("Coordinates must not be empty")
        if not Validator.check_coordinates_length(list_of_coordinates):
            raise ValueError("There must be 3 coordinates for each point")
        if not Validator.check_coordinates_is_int(list_of_coordinates):
            raise ValueError("Coordinates must be integers")
        if not Validator.check_coordinates_range(list_of_coordinates):
            raise ValueError("Coordinates must be in the range of the board")
        print("Coordinates are valid - all tests passed")
        
        return True
    

import pytest

"""
Tests for the Validator class
"""

def test_check_coordinates_is_int(validator):
    assert validator.check_coordinates_is_int([[1, 2, 3], [4, 5, 6]])
    assert not validator.check_coordinates_is_int([[1, 2, 3], [4, 5, 6.5]])

def test_check_coordinates_length(validator):
    assert validator.check_coordinates_length([[1, 2, 3], [4, 5, 6]])
    assert not validator.check_coordinates_length([[1, 2, 3, 4], [4, 5, 6]])

def test_check_coordinates_is_list(validator):
    assert validator.check_coordinates_is_list([[1, 2, 3], [4, 5, 6]])
    assert not validator.check_coordinates_is_list("1, 2, 3")

def test_check_coordinates_is_not_empty(validator):
    assert validator.check_coordinates_is_not_empty([[1, 2, 3], [4, 5, 6]])
    assert not validator.check_coordinates_is_not_empty([])

def test_check_coordinates_range(validator):
    assert validator.check_coordinates_range([[1, 2, 3], [4, 5, 6]])
    assert not validator.check_coordinates_range([[100, 2, 3], [4, 5, 6]])

def test_test_coordinates(validator):
    assert validator.test_coordinates([[1, 2, 3], [4, 5, 6]])
    with pytest.raises(ValueError):
        validator.test_coordinates([[1, 2, 3], [4, 5, 6.5]])
        validator.test_coordinates([[1, 2, 3, 4], [4, 5, 6]])
        validator.test_coordinates("1, 2, 3")
        validator.test_coordinates([])
        validator.test_coordinates([[100, 2, 3], [4, 5, 6]])

