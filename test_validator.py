import pytest
import numpy as np
from validator import Validator


"""
Tests for the Validator class
"""


@pytest.fixture
def validator():
    return Validator()


def test_validate_integers(validator):
    assert validator.validate_integers(np.array([[1, 2, 3], [4, 5, 6]]))
    with pytest.raises(ValueError):
        validator.validate_integers(np.array([[1, 2, 3], [4, 5, 6.5]]))


def test_validate_length(validator):
    assert validator.validate_length(np.array([[1, 2, 3], [4, 5, 6]]))
    with pytest.raises(ValueError):
        validator.validate_length(np.array([[1, 2, 3, 4], [4, 5, 6]]))


def test_validate_type(validator):
    assert validator.validate_type(np.array([[1, 2, 3], [4, 5, 6]]))
    with pytest.raises(ValueError):
        validator.validate_type("1, 2, 3")


def test_validate_not_empty(validator):
    assert validator.validate_not_empty(np.array([[1, 2, 3], [4, 5, 6]]))
    with pytest.raises(ValueError):
        validator.validate_not_empty(np.array([]))


def test_validate_range(validator):
    assert validator.validate_range(np.array([[1, 2, 3], [4, 5, 6]]))
    with pytest.raises(ValueError):
        validator.validate_range(np.array([[100, 2, 3], [4, 5, 6]]))


if __name__ == "__main__":
    pytest.main()
