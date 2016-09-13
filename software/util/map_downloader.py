import requests
import os


class MapDownloader:
    """
    Helper class to download a small hybrid Google map, with a marker
    at at a specified lat-long coordinate. The file is then saved to a
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
    MARKER_TEMPLATE = "markers=color:red%7Clabel:R%7C"

    def __init__(self, location, filename):
        """
        Initialises the MapDownloader taking in a location, which should be a comma separated
        "lat, long" string, and a filename.

        Example use:

         ` MapDownloader("-41.2880647,174.7617035", "example") `

        """
        # initialize the location and center of map, setting a mark at the location
        self.location = location
        self.center = "center=" + location
        self.marker = self.MARKER_TEMPLATE + location

        # filename to save the resulting image map to
        self.filename = filename

        # create the request session, used to download the map
        self.session = requests.Session()

        # read the api key from the os' exports
        self.api_key = os.environ[self.API_ID]

    def download_map(self):
        """
        Constructs the map download url and then uses the session to download the image data, saving
         it to the specified file
        """
        # construct the request url
        request = self.API_ROOT + self.center + "&" + self.ZOOM + \
                  "&" + self.SIZE + "&" + self.MAP_TYPE + \
                  "&" + self.marker + "&" + self.api_key

        # get the map from Google API
        response = self.session.get(request)

        # open a new file with the specified filename and write the image to that file
        f = open(self.filename, 'wb')
        f.write(response.content)

        # finally close the file
        f.close()
