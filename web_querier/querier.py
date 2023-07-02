import requests


class Querier(object):
    """Class for querying Neurosynth API.
    Attributes:
        url (str): url to query.
    """

    def __init__(self, url: str):
        """Initialize Querier object with url to query.
        Args:
            url (str): url to query.
            """
        # Verify url is valid.
        if not url.startswith("https://neurosynth.org/api/locations/"):
            raise ValueError("Invalid url: {}".format(url))
        # Verify url has room for x, y, z coordinates, with 1 radius.
        if not "{}_{}_{}_1" in url:
            raise ValueError("Url must contain room for x, y, z coordinates.")

        self.url = url

    def query(self, x: int , y: int, z: int):
        """Query Neurosynth API.
        Args:

            x (int): x coordinate.
            y (int): y coordinate.
            z (int): z coordinate.
        Returns:
            json: json object containing query results.
            """
        return requests.get(self.url.format(x,y,z)).json()
    
