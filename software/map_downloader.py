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
    TARGET_MARKER = "markers=color:red%7Clabel:R%7C"
    CURRENT_MARKER = "markers=color:green%7Clabel:C%7C"

    """
    initialises the MapDownloader taking in a target_location and current_location,
    which should both be a comma separated "lat, long" strings, and a filename.

    Example use:

     ` MapDownloader("-41.2880647,174.7617035", "-41.288712, 174.761792", "example") `

    """
    def __init__(self, target_location, current_location, filename):
        # initialize the target_location and current_location, setting a mark at the both locations
        self.target_location = target_location
        self.current_location = current_location
        self.markers = self.TARGET_MARKER + target_location + "&" + self.CURRENT_MARKER + current_location

        # filename to save the resulting png map to
        self.filename = filename

        # create the request session, used to download the map
        self.session = requests.Session()

        # read the api key from the os' exports
        self.api_key = os.environ[self.API_ID]

    def download_map(self):
        # construct the request url
        request = self.API_ROOT + self.ZOOM + "&" + self.SIZE + \
                    "&" + self.MAP_TYPE + "&" + self.markers + \
                    "&" + self.api_key

        print(request)

        # get the map from Google API
        response = self.session.get(request)

        # open a new file with the specified filename and write the image to that file
        f = open(self.filename + ".png", 'wb')
        f.write(response.content)

        # finally close the file
        f.close()

