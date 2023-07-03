import numpy as np
from typing import List

class Validator():
    """
    Class for validating the input data
    """

    def validate_integers(self, coordinates: np.array) -> bool:
        """
        Checks if the coordinates are integers
        Args:
            coordinates: NumPy array of coordinates
        Returns:
            True if the coordinates are int, False otherwise
        """
        if not np.issubdtype(coordinates.dtype, np.integer):
            raise ValueError("Coordinates must be integers")

        return True


    def validate_length(self, coordinates: np.array) -> bool:
        """
        Checks if there are 3 coordinates for each point
        Args:
            coordinates: NumPy array of coordinates
        Returns:
            True if there are 3 coordinates for each point, False otherwise
        """
        if not coordinates.shape[1] == 3:
            raise ValueError("There must be 3 coordinates for each point")

        return True
    

    def validate_type(self, coordinates: np.array) -> bool:
        """
        Checks if the coordinates are in a NumPy array
        Args:
            coordinates: NumPy array of coordinates
        Returns:
            True if the coordinates are in a NumPy array, False otherwise
        """
        if not isinstance(coordinates, np.ndarray):
            raise ValueError("Coordinates must be in a NumPy array")

        return True
    

    def validate_not_empty(self, coordinates: np.array) -> bool:
        """
        Checks if the coordinates are not empty
        Args:
            coordinates: NumPy array of coordinates
        Returns:
            True if the coordinates are not empty, False otherwise
        """
        if coordinates.size == 0:
            raise ValueError("Coordinates must not be empty")

        return True
    

    def validate_range(self, coordinates: np.array) -> bool:
        """
        Checks if the coordinates are in the range of the board
        The range:
         -90 to +90 along the x-axis
         -126 to +90 along the y-axis
         -72 to +108 along the z-axis
        Args:
            coordinates: NumPy array of coordinates
        Returns:
            True if the coordinates are in the range of the board, False otherwise
        """
        x_range = np.logical_and(coordinates[:, 0] >= -90, coordinates[:, 0] <= 90)
        y_range = np.logical_and(coordinates[:, 1] >= -126, coordinates[:, 1] <= 90)
        z_range = np.logical_and(coordinates[:, 2] >= -72, coordinates[:, 2] <= 108)

        if not np.all(np.logical_and(x_range, np.logical_and(y_range, z_range))):
            raise ValueError("Coordinates must be in the range of the board")

        return True
    

    def test_coordinates(self, coordinates: np.array) -> bool:
        """
        Test the coordinates
        Args:
            coordinates: NumPy array of coordinates
        Returns:
            True if the coordinates are valid, False otherwise
        """
        if not self.validate_type(coordinates):
            raise ValueError("Coordinates must be in a NumPy array")
        if not self.validate_not_empty(coordinates):
            raise ValueError("Coordinates must not be empty")
        if not self.validate_integers(coordinates):
            raise ValueError("There must be 3 coordinates for each point")
        if not self.validate_integers(coordinates):
            raise ValueError("Coordinates must be integers")
        if not self.validate_range(coordinates):
            raise ValueError("Coordinates must be in the range of the board")
        print("Coordinates are valid - all tests passed")

        return True
