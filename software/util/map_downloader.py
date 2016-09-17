import requests
import os


class MapDownloader:
    """
    Helper class to download a small hybrid Google map, with markers
    at the specified lat-long coordinates. The file is then saved to a
    specified {filename}

    Created 07 September 2016
    By Marcel van Workum

    Modified 13 September 2016
    By Marcel van Workum
    """

    API_ROOT = "https://maps.googleapis.com/maps/api/staticmap?"
    API_ID = "google_maps_api_key"
    API_SEPARATOR = "&"
    SIZE = "size=700x700"
    ZOOM = "zoom=16"
    MAP_TYPE = "maptype=hybrid"
    TARGET_MARKER = "markers=color:red%7Clabel:R%7C"
    CURRENT_MARKER = "markers=color:green%7Clabel:C%7C"

    def __init__(self, target_location, current_location, filename):
        """
        Initialises the MapDownloader taking in a target and current location, which should be a
        (lat, long) tuple, and a filename.

        Example use:

        ` MapDownloader((-41.2880647, 174.7617035), (-41.288712, 174.761792), "example") `
        """
        # initialize the target_location and current_location, setting a mark at the both locations
        self.target_location = target_location
        self.current_location = current_location
        self.markers = self.TARGET_MARKER + self.parse_location(target_location) + "&" \
                       + self.CURRENT_MARKER + self.parse_location(current_location)

        # filename to save the resulting image map to
        self.filename = filename

        # create the request session, used to download the map
        self.session = requests.Session()

        # read the api key from the os' exports
        self.api_key = os.environ[self.API_ID]

    def parse_location(self, location_tuple):
        return str(location_tuple[0]) + "," + str(location_tuple[1])

    def download_map(self):
        """
        Constructs the map download url and then uses the session to download the image data, saving
         it to the specified file
        """
        # construct the request url
        request = self.API_ROOT + self.ZOOM + "&" + self.SIZE + \
                    "&" + self.MAP_TYPE + "&" + self.markers + \
                    "&" + self.api_key

        # get the map from Google API
        response = self.session.get(request)

        # open a new file with the specified filename and write the image to that file
        f = open(self.filename, 'wb')
        f.write(response.content)

        # finally close the file
        f.close()
