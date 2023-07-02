import pytest
from validator import *

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

if __name__ == "__main__":
    tests = ["test_check_coordinates_is_int", "test_check_coordinates_length", "test_check_coordinates_is_list", 
             "test_check_coordinates_is_not_empty", "test_check_coordinates_range"]
    errors = []

    for test in tests:
        try:
            eval(test)()
        except AssertionError as e:
            errors.append(f"Failed when testing 'test_{test}': {e}")
            break

    if errors:
        raise AssertionError(errors)
    else:
        print("All tests passed")


