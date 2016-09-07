import requests
import os

"""
Helper class to download a small hybrid Google map, with a marker
at at a specified lat-long coordinate. The file is then saved to a
specified {filename}.png

Created 07 September 2016
By Marcel van Workum

Modified 07 September 2016
By Marcel van Workum
"""
class MapDownloader:
    API_ROOT = "https://maps.googleapis.com/maps/api/staticmap?"
    API_ID = "google_maps_api_key"
    API_SEPARATOR = "&"
    SIZE = "size=400x400"
    ZOOM = "zoom=16"
    MAP_TYPE = "hybrid"
    MARKER_TEMPLATE = "markers=color:red%7Clabel:R%7C"

    def __init__(self, location, filename):
        # initialize the location and center of map, setting a mark at the location
        self.location = location
        self.center = "center=" + location
        self.marker = self.MARKER_TEMPLATE + location

        # filename to save the resulting png map to
        self.filename = filename

        # create the request session, used to download the map
        self.session = requests.Session()

        # read the api key from the os' exports
        self.api_key = os.environ[self.API_ID]

    def download_map(self):
        # construct the request url
        request = self.API_ROOT + self.center + self.API_SEPARATOR + self.ZOOM + \
                  self.API_SEPARATOR + self.SIZE + self.API_SEPARATOR + \
                  self.MAP_TYPE + self.API_SEPARATOR + self.marker + \
                  self.API_SEPARATOR + self.api_key

        # get the map from Google API
        response = self.session.get(request)

        # open a new file with the specified filename and write the image to that file
        f = open(self.filename + ".png", 'wb')
        f.write(response.content)

        # finally close the file
        f.close()

