import requests
import os


class MapURLGenerator:
    """
    Helper class to generate the api url for a small hybrid Google map, with markers
    at the specified lat-long coordinates.

    Created 09 October 2016
    By Marcel van Workum

    Created 09 October 2016
    By Marcel van Workum
    """

    API_ROOT = "https://maps.googleapis.com/maps/api/staticmap?"
    API_ID = "google_maps_api_key"
    API_SEPARATOR = "&"
    SIZE = "size=400x400"
    MAP_TYPE = "maptype=hybrid"
    TARGET_MARKER = "markers=color:red%7Clabel:R%7C"
    CURRENT_MARKER = "markers=color:green%7Clabel:C%7C"
    PATH = "path="

    def __init__(self, target_location, current_location):
        """
        Initialises the MapDownloader taking in a target and current location, which should be a
        (lat, long) tuple.

        Example use:

        ` MapDownloader((-41.2880647, 174.7617035), (-41.288712, 174.761792)) `
        """
        # initialize the target_location and current_location, setting a mark at the both locations
        self.target_location = target_location
        self.current_location = current_location
        self.markers = self.TARGET_MARKER + self.parse_location(target_location) + "&" \
                       + self.CURRENT_MARKER + self.parse_location(current_location)
        self.path = self.PATH + self.parse_location(target_location) + "|" + self.parse_location(current_location)

        # read the api key from the os' exports
        self.api_key = os.environ[self.API_ID]

    def parse_location(self, location_tuple):
        """
        Helper method to split the location tuple.
        """
        return str(location_tuple[0]) + "," + str(location_tuple[1])

    def generate_url(self):
        """
        Constructs the map download url and then uses the session to download the image data, saving
         it to the specified file
        """
        # construct the request url
        request = self.API_ROOT + self.SIZE + \
                    "&" + self.MAP_TYPE + "&" + self.markers + \
                    "&" + self.path + "&" + self.api_key

        return request
