
class Validator (object):
    """
    Class for validating the input data
    """
    def check_coordinates_is_int(list_of_coordinates):
        """
        Checks if the coordinates are integers
        :param list_of_coordinates: list of coordinates
        :return: True if the coordinates are int, False otherwise
        """
        for coordinate in list_of_coordinates:
            for value in coordinate:
                if not isinstance(value, int):
                    raise ValueError("Coordinates must be integers")
        return True

    def check_coordinates_length(list_of_coordinates):
        """
        Checks if there are 3 coordinates for each point
        :param list_of_coordinates: list of coordinates
        :return: True if there are 3 coordinates for each point, False otherwise
        """
        for coordinate in list_of_coordinates:
            if len(coordinate) != 3:
                raise ValueError("There must be 3 coordinates for each point")
        return True
    
    def check_coordinates_is_list(list_of_coordinates):
        """
        Checks if the coordinates are in a list
        :param list_of_coordinates: list of coordinates
        :return: True if the coordinates are in a list, False otherwise
        """
        if not isinstance(list_of_coordinates, list):
            raise ValueError("Coordinates must be in a list")
        return True
    
    def check_coordinates_is_not_empty(list_of_coordinates):
        """
        Checks if the coordinates are not empty
        :param list_of_coordinates: list of coordinates
        :return: True if the coordinates are not empty, False otherwise
        """
        if not list_of_coordinates:
            raise ValueError("Coordinates must not be empty")
        return True
    
    def check_coordinates_range(list_of_coordinates):
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
    
    def test_coordinates(list_of_coordinates):
        """
        Test the coordinates
        :param list_of_coordinates: list of coordinates
        :return: True if the coordinates are valid, False otherwise
        """
        if Validator.check_coordinates_is_list(list_of_coordinates) == False:
            raise ValueError("Coordinates must be in a list")
        if Validator.check_coordinates_is_not_empty(list_of_coordinates) == False:
            raise ValueError("Coordinates must not be empty")
        if Validator.check_coordinates_length(list_of_coordinates) == False:
            raise ValueError("There must be 3 coordinates for each point")
        if Validator.check_coordinates_is_int(list_of_coordinates) == False:
            raise ValueError("Coordinates must be integers")
        if Validator.check_coordinates_range(list_of_coordinates) == False:
            raise ValueError("Coordinates must be in the range of the board")
        print("Coordinates are valid - all tests passed")
        return True
    

