from web_querier import Querier
import pytest


class TestQuerier(object):
    """Test Querier class."""

    def test_valid_url(self):
        """Test that valid url is accepted."""
        q = Querier("https://neurosynth.org/api/locations/{}_{}_{}_1/compare/")
        assert q.url == "https://neurosynth.org/api/locations/{}_{}_{}_1/compare/"


    def test_no_room_for_coordinates(self):
        """Test that url has room for coordinates."""
        with pytest.raises(ValueError):
            Querier("https://neurosynth.org/api/locations/compare/")


    def test_invalid_url(self):
        """Test that invalid url is rejected."""
        with pytest.raises(ValueError):
            Querier("https://google.com")

